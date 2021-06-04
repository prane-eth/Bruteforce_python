
' Web app which detects Brute force attacks '

import re
from flask import *

app = Flask(__name__)
app.secret_key = 'my_secret_key_123'


class var:
    ' A class used to store variables '
    attempts_limit = 4  # maximum incorrect attempts allowed
    email = 'test@gmail.com'  # correct email and password
    password = '.5_pFO*p6s8Kcj+U'
    failed_attempts = {}  # dictionary
    blocked_ips = set()  # empty set
    html_code = '''
        <title> Login page </title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <div align="center" class="border"> 
            <div class="header"> 
                <h1 class="word"> Login </h1> 
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
            ''' + email + ''' <br>
            ''' + password + '''
        </div>
    '''


def block(ip_addr):
    var.blocked_ips.add(ip_addr)
    print("\nBlocked IP: " + ip_addr + "\n")


def is_brute_force(ip_addr):
    ' Detect whether the request is brute force or not '

    # Find how many failed attempts from same IP
    if var.failed_attempts.get(ip_addr, 0) > var.attempts_limit:
        block(ip_addr)
        return True  # yes. it is brute-force
    else:
        return False


def generate_message(request):
    ' Generate response using the request '
    email = request.form['email']
    password = request.form['password']
    ip_addr = request.remote_addr
    if email==var.email and password==var.password:
        return " -----> Login successful <----- "
    else:
        # add failed attempt
        var.failed_attempts[ip_addr] = \
            var.failed_attempts.get(ip_addr, 0) + 1
        if is_brute_force(ip_addr):
            return " -----> Brute force detected <----- "
        else:
            return " -----> Login failed <----- "


@app.route('/', methods = ['POST', 'GET'])
def home():
    ip_address = request.remote_addr
    if ip_address in var.blocked_ips:
        return 'Your IP is blocked'

    user_agent = request.headers.get('User-Agent')
    # bots_list = '/bot|spider|curl|wget|crawl|slurp|python|java|blowfish|mediapartners/i'
    # isBot = re.search(var.bots_list, user_agent, flags=re.IGNORECASE)
    # if isBot or user_agent=='':
    if not user_agent.startswith('Mozilla'):
        return 'Bot detected. This website is not for bots'
    
    if request.method == 'POST':
        msg = generate_message(request)
    else:
        msg = ''
    return render_template_string(var.html_code, msg=msg)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
