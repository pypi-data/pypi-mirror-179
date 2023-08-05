from functools import wraps
from flask import current_app, request
from htmlmin import minify
from flask_hmin.tool import RedisTool
from flask_hmin.tool import str_to_md5


class HMin(object):
    def __init__(self, app=None, redis_config=None):
        self.app = app
        self.redis_tool = RedisTool(
            host=redis_config.get('host') or 'localhost',
            port=redis_config.get('port') or 6379,
            db=redis_config.get('db') or 0,
            password=redis_config.get('password') or ''
        )
        if app is not None:
            self.init_app(app)
        self._compress_routes = set()

    def init_app(self, app):
        app.config.setdefault('HMIN_COMPRESS_HTML', False)
        app.config.setdefault('HTML_LOAD_REDIS', False)
        app.config.setdefault("EXPIRIES_TIME", 86400)
        if app.config['HMIN_COMPRESS_HTML']:
            app.after_request(self.set_response)
        self.app = app

    def set_response(self, response):
        if response.content_type == u'text/html; charset=utf-8':
            endpoint = request.endpoint or ''
            view_func = current_app.view_functions.get(endpoint, None)
            name = (
                '%s.%s' % (view_func.__module__, view_func.__name__)
                if view_func else ''
            )
            content = response.data.decode('utf-8')
            compress = minify(content.replace("\n", ""), remove_all_empty_space=True)
            key = str_to_md5(content=compress)
            if self.app.config.get("HTML_LOAD_REDIS"):
                if self.redis_tool.is_response_key(key):
                    d = self.redis_tool.get_response_redis(key).decode('utf8')
                    response.set_data(d)
                    return response
                else:
                    self.redis_tool.set_response_redis(
                        key=key,
                        value=compress,
                        time=self.app.config.get("EXPIRIES_TIME") or 86400
                    )
            if name in self._compress_routes:
                return response
            response.set_data(compress)
            return response
        return response

    def not_compress(self, func):
        name = '%s.%s' % (func.__module__, func.__name__)

        @wraps(func)
        def __inner(*a, **k):
            return func(*a, **k)

        self._compress_routes.add(name)
        return __inner
