from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# ROUTES

@app.route('/')
def welcome():
   return render_template('welcome.html')   


# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True, port=5001)




