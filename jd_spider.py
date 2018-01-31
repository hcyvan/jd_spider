import re
import requests

url = 'https://sclub.jd.com/comment/productPageComments.action'
params = dict(
    callback='fetchJSON_comment98vv47937',
    productId=1242256,
    score=3,
    sortType=6,
    page=0,
    pageSize=10,
    isShadowSku=0,
    fold=1
)

params_good = dict(**params)
params_middle = dict(**params)
params_bad = dict(**params)
params_good['score'] = 3
params_middle['score'] = 2
params_bad['score'] = 1


def get_comments(request_url, url_params):
    r = requests.get(request_url, params=url_params)
    print(r.url)
    pattern = re.compile('.*?\((.*)\);')
    match = pattern.match(r.text)
    if match:
        return match.group(1)
    return 'NA'


def get_good():
    for i in range(100):
        params_good['page'] = i
        print('Getting page {} ...'.format(i))
        content = get_comments(url, params_good)
        with open('./result/good.txt', 'a') as f:
            f.write(content)
            f.write('\n')


def get_middle():
    for i in range(100):
        params_middle['page'] = i
        print('Getting page {} ...'.format(i))
        content = get_comments(url, params_middle)
        with open('./result/middle.txt', 'a') as f:
            f.write(content)
            f.write('\n')


def get_bad():
    for i in range(100):
        params_bad['page'] = i
        print('Getting page {} ...'.format(i))
        content = get_comments(url, params_bad)
        with open('./result/bad.txt', 'a') as f:
            f.write(content)
            f.write('\n')


get_middle()
get_bad()
