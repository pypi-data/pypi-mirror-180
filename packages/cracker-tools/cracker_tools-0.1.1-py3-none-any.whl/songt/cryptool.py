# encoding: utf-8
# Date: 2022/12/12 14:27
# 方法命名规范： base64(content) 和 base64_decode()
__author__ = 'songt'
import hashlib
import base64 as b64
from Crypto.Hash import MD5


def md5(content):
    """
    md5
    :param content:
    :return:
    """
    hash = hashlib.md5()
    hash.update(content.encode('utf-8'))
    return hash.hexdigest()


def base64(content):
    return b64.b64encode(content.encode('utf-8')).decode('utf-8')


def base64_decode(content):
    return b64.b64decode(content.encode('utf-8'))


def aes(content):
    pass


if __name__ == '__main__':
    # 1.md5
    print("md5:", md5('s'))
    # 2.base64 encode
    print("base64:", base64('s'))
    # 3.base64 decode
    print("base64_encode:", base64_decode(base64('s')))
