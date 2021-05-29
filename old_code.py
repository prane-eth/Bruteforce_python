
' This file contains old unused code '

# Detector code
# in class var: last_totals = [394]  # 'abcd'
def is_brute_force(password, ip_addr):
    ' Detect whether the request is brute force or not, using password and IP address '
    
    # check if there are similar attempts
    if len(var.last_totals) > 10:
        var.last_totals.pop(0)  # decrease length of list to 10

    # sum of values of all characters in password
    total = sum(ord(char) for char in password)
    var.last_totals.append(total)  # add last total

    # Find if similar passwords are being attempted
    # difference total-x for last 5 passwords
    diffs = [total-x for x in var.last_totals[-5:]]
    similar_attempts = 0
    for diff in diffs:
        if diff < 5:
            similar_attempts += 1
    if similar_attempts > 2:
        block(ip_addr)
        return True

    # Find how many failed attempts from same IP
    if var.failed_attempts.get(ip_addr, 0) > var.attempts_limit:
        block(ip_addr)
        return True  # yes. it is brute-force
    else:
        return False


# Attack code

def main():
    ' Perform Brute force attack '
    password = '.5_pFO*p6s8Kcj+K'
    password = list(password)
    for attempt in range(15):
        res = try_password(password)
        if res:  # if there is response, stop attack
            print(res)
            break
        if password[-1] == '~':  # last char can't be increased
            password[-1] = '!'
            if password[-2] == '~':
                pass
            else:
                password[-2] = chr(ord(password[-2]) + 1)
        else:
            password[-1] = chr(ord(password[-1]) + 1)  # increase last character
        time.sleep(1)  # wait for 1 second before next attempt

'''
Note:
for x in range(150):
    print(x, chr(x))

Characters which can be in password
33 !  to 126 ~
'''