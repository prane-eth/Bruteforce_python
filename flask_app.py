import re
from flask import *

app = Flask(__name__)
app.secret_key = 'my_secret_key'


class var:
    ' A class used to store variables '
    last_pass = ['abcd']
    last_totals = [394]
    failed_attempts = {}
    blocked_ips = []
    bots_list = '/bot|spider|curl|wget|crawl|slurp|python|java|blowfish|mediapartners/i'
    html_code = '''
        <html> 
        <head> 
          <title> Login page </title>
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"-->
        </head> 
        <body>
          <div align="center" class="border"> 
            <div class="header"> 
              <h1 class="word">Login</h1> 
            </div></br></br></br> 
            <h2 class="word"> 
              <form action="/" method="post"> 
              <input id="email" name="email" type="text" placeholder="Enter Your Email" class="textbox" value=""> </br> </br> 
              <input id="password" name="password" type="password" placeholder="Enter Your Password" class="textbox" value=""> </br>
              <input type="submit" class="btn" value="Sign In">
              </form> 
              
              <div class="msg"> {{ msg }} </div> 
            </h2> 
            <p class="bottom">Don't have an account? <a class="bottom" href="/"> Sign Up here</a></p> 
              
        		test@gmail.com <br>
            	~5_pFO*p6s8Kcj+U
          </div> 
          </div> 
        </body> 
        </html> 
    '''


def is_brute_force(password='', ip_addr=''):
    var.last_pass.append(password)  # add last password
    total = sum(ord(char) for char in password)
    var.last_totals.append(total)  # add last

    # Find if similar passwords are being attempted
    diffs = [ total-x for x in var.last_totals[-5:] ]
    diffs.sort()
    diff = sum(diffs[:2])  # sum of 2 least differences
    if (abs(diff) < 5):
        return True

    # Find how many failed attempts from same IP
    if ip_addr in var.failed_attempts:
        if var.failed_attempts[ip_addr] > 5:
            return True
        else:
            var.failed_attempts[ip_addr] += 1
    else:
        var.failed_attempts[ip_addr] = 1
        
    return False


def generate_message(request=None):
    ' Generate response using the request '
    if request is None:
        return

    email = request.form['email']
    password = request.form['password']
    ip_addr = request.remote_addr
    if is_brute_force(password=password, ip_addr=ip_addr):
        msg = " -----> Brute force detected <----- "
        var.blocked_ips.append(ip_addr)
    elif email=='test@gmail.com' and password=='~5_pFO*p6s8Kcj+U':
        msg = " -----> Login successful <----- "
    else:
        msg = " -----> Login failed <----- "
        var.last_pass.append(password)
    return msg



@app.route('/', methods = ['POST', 'GET'])
def home():
    user_agent = request.headers.get('User-Agent')
    output = re.search(var.bots_list, user_agent, flags=re.IGNORECASE)
    if output or not user_agent:
        return 'This website is not for bots'

    ip_addr = request.remote_addr
    if ip_addr in var.blocked_ips:
        return 'Your IP is blocked'
    
    if request.method == 'POST':
        msg = generate_message(request)
    else:
        msg = ''  
    return render_template_string(var.html_code, msg=msg)


@app.route('/last/')
def display_arr():
    ' Temporary function to be removed later '
    return '<br>'.join(var.last_pass)  # list last_pass separated by new line using <br>


if __name__ == "__main__":
    app.run(port=8080)
  
