from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'banana'

#from AMCowmvg import routes
import routes