import re
from flask import Flask, request, redirect, session, render_template, render_template_string

app = Flask(__name__)
app.secret_key = 'my_secret_key'

class var:
  arr = []
  bots_list = \
    '/bot|spider|curl|wget|crawl|slurp|python|java|blowfish|mediapartners/i'
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


@app.route('/', methods = ['POST', 'GET'])
def home():

    user_agent = request.headers.get('User-Agent')

    output = re.search(var.bots_list, user_agent, flags=re.IGNORECASE)
    
    if output or not user_agent:
        return 'This website is not for bots'

    msg = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email=='test@gmail.com' and password=='~5_pFO*p6s8Kcj+U':
            msg = " -----> Login successful <----- "
        else:
            msg = " -----> Login failed <----- "
            var.arr.append(password)
    return user_agent[:10] + render_template_string(var.html_code, msg=msg)


@app.route('/last/')
def display_arr():
    return '\n'.join(var.arr)


if __name__ == "__main__":
    app.run()
  
