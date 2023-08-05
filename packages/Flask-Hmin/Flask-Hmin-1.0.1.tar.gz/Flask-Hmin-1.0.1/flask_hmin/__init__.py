from functools import wraps
from flask import current_app, request
from htmlmin import minify


class HMin(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
        self._compress_routes = set()

    def init_app(self, app):
        app.config.setdefault('HMIN_COMPRESS_HTML', False)
        if app.config['HMIN_COMPRESS_HTML']:
            app.after_request(self.set_response)

    def set_response(self, response):
        if response.content_type == u'text/html; charset=utf-8':
            endpoint = request.endpoint or ''
            view_func = current_app.view_functions.get(endpoint, None)
            name = (
                '%s.%s' % (view_func.__module__, view_func.__name__)
                if view_func else ''
            )
            content = response.data.decode('utf-8')
            if name in self._compress_routes:
                return response
            compress = minify(content.replace("\n", ""), remove_all_empty_space=True)
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
