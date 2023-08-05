import hashlib
from redis import StrictRedis


def str_to_md5(content):
    """
    字符串转md5字符
    :param content: 字符串的内容
    :return: fe01ce2a7fbac8fafaed7c982a04e229
    """
    if not isinstance(content, bytes):
        content = content.encode('utf-8')
    md5_l = hashlib.md5()
    md5_l.update(content)
    md5_str = md5_l.hexdigest()
    return md5_str


class RedisTool(object):
    def __init__(self, host='localhost', port=6379, db=0, password=''):
        self.redis = StrictRedis(host=host, port=port, db=db, password=password)

    def set_response_redis(self, key, value, time=86400) -> bool:
        return self.redis.setex(name=key, value=value, time=time)

    def get_response_redis(self, key) -> bytes:
        return self.redis.get(key)

    def is_response_key(self, key):
        return True if self.redis.exists(key) == 1 else False
