# Author: John Jiang
# Date  : 2016/8/21
from random import randint
import requests
import config

__all__ = ['generate_integers', 'generate_gaussians', 'generate_decimal_fractions', 'generate_strings']

api_url = 'https://api.random.org/json-rpc/1/invoke'


def to_camel(key):
    if not isinstance(key, str):
        return None
    first, *rest = key.split('_')
    if not rest:
        return first
    return first + ''.join(x.capitalize() for x in rest)


def make_api(func):
    def wrapper(**kwargs):
        kwargs = {to_camel(key): value for key, value in kwargs.items()}
        func_name = to_camel(func.__name__)
        func()
        return get_random(func_name, kwargs)

    return wrapper


def get_random(method, params=None, id=None):
    if id is None:
        id = randint(1, 999)
    data = {
        'jsonrpc': '2.0',
        'method': method,
        'params': {
            'apiKey': config.key
        },
        'id': id
    }
    data['params'].update(params)
    try:
        r = requests.post(api_url, json=data)
        j = r.json()
        if 'error' in j or id != j['id']:
            return None
        return j['result']['random']['data']
    except Exception:
        return None


@make_api
def generate_integers(*, min, max, n, replacement=True):
    """第一个参数为没有名字的*, 则所有参数都必须使用keyword形式"""
    pass


@make_api
def generate_decimal_fractions(*, n, decimal_places, replacement=True):
    pass


@make_api
def generate_gaussians(*, n, mean, standard_deviation, significant_digits):
    pass


@make_api
def generate_strings(*, n, length, characters):
    if not (1 < n < 1e4):
        raise AttributeError('n must be within the [1,1e4] range.')
    if not (1 <= length <= 20):
        raise AttributeError('The length of each string must be within the [1,20] range. ')
    if len(characters) > 80:
        raise AttributeError('The maximum number of characters is 80.')


if __name__ == '__main__':
    print(generate_integers(min=1, max=10, n=5))
    # print(generate_decimal_fractions(n=10, decimal_places=10))
    # print(generate_gaussians(n=10, mean=100, standard_deviation=99, significant_digits=5))
