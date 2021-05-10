from flask import Flask, request, redirect, session, render_template, render_template_string

app = Flask(__name__)
app.secret_key = 'my_secret_key'

class var:
  arr = []
  html_code = '''
  <html> 
    <head> 
      <title> Login page </title>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"-->
    </head> 
    <body></br></br></br></br></br> 
      <div align="center"> 
      <div align="center" class="border"> 
        <div class="header"> 
          <h1 class="word">Login</h1> 
        </div></br></br></br> 
        <h2 class="word"> 
          <form action="/login" method="post"> 
          <div class="msg">{{ msg }}</div> 
            <input id="email" name="email" type="text" placeholder="Enter Your Email" class="textbox" value="test@test.com" /></br></br> 
            <input id="password" name="password" type="password" placeholder="Enter Your Password" class="textbox" value="test@test.com" /></br></br></br> 
            <input type="submit" class="btn" value="Sign In"></br></br> 
          </form> 
        </h2> 
        <p class="bottom">Don't have an account? <a class="bottom" href="/register"> Sign Up here</a></p> 
      </div> 
      </div> 
    </body> 
  </html> 
  '''

@app.route('/')
def home():
    return render_template_string(var.html_code)
