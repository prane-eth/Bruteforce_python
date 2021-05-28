
' Web app which detects Brute force attacks '

import re
from flask import *

app = Flask(__name__)
app.secret_key = 'my_secret_key_123'


class var:
    ' A class used to store variables '
    attempts_limit = 8
    email = 'test@gmail.com'
    password = '.5_pFO*p6s8Kcj+U'
    last_totals = [394]
    failed_attempts = {}
    blocked_ips = []
    html_code = '''
        <title> Login page </title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <div align="center" class="border"> 
            <div class="header"> 
                <h1 class="word">Login</h1> 
            </div> <br> <br> <br> 
            <h2 class="word"> 
                <form action="/" method="post"> 
                <input id="email" name="email" type="text" placeholder="Enter Your Email" class="textbox" value=""> </br> </br> 
                <input id="password" name="password" type="password" placeholder="Enter Your Password" class="textbox" value=""> </br>
                <input type="submit" class="btn btn-primary" value="Sign In">
                </form> 
                <div class="msg"> {{ msg }} </div> 
            </h2> 
            <p class="bottom">
                Don't have an account? <a class="bottom" href="/">Sign Up here</a>
            </p>
            test@gmail.com <br>
            .5_pFO*p6s8Kcj+U
        </div>
    '''


def block(ip_addr):
    var.blocked_ips.append(ip_addr)


def is_brute_force(password, ip_addr):
    ' Detect whether the request is brute force or not, using password and IP address '
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


def generate_message(request):
    ' Generate response using the request '
    if request is None:
        return

    email = request.form['email']
    password = request.form['password']
    ip_addr = request.remote_addr
    if is_brute_force(password=password, ip_addr=ip_addr):
        msg = " -----> Brute force detected <----- "
    elif email==var.email and password==var.password:
        msg = " -----> Login successful <----- "
    else:
        msg = " -----> Login failed <----- "
        # add failed attempt
        var.failed_attempts[ip_addr] = \
            var.failed_attempts.get(ip_addr, 0) + 1
    return msg


@app.route('/', methods = ['POST', 'GET'])
def home():
    user_agent = request.headers.get('User-Agent')
    # bots_list = '/bot|spider|curl|wget|crawl|slurp|python|java|blowfish|mediapartners/i'
    # isBot = re.search(var.bots_list, user_agent, flags=re.IGNORECASE)
    # if isBot or user_agent=='':
    if not user_agent.startswith('Mozilla'):
        return 'Bot detected. This website is not for bots'

    ip_addr = request.remote_addr
    if ip_addr in var.blocked_ips:
        return 'Your IP is blocked'
    
    if request.method == 'POST':
        msg = generate_message(request)
    else:
        msg = ''  
    return render_template_string(var.html_code, msg=msg)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
