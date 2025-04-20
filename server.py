from os import abort
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

modules_data = [
    {
        "id": "1",
        "title": "Lighting and Reflections",
        "example1_pic": "https://i.warbycdn.com/s/c/164957dac184e44592d221ad828fd2c92a8e1ba9.png",
        "example1_description" : "Inconsistent reflections in eyeglasses",
        "example2_pic": "https://i.warbycdn.com/s/c/164957dac184e44592d221ad828fd2c92a8e1ba9.png",
        "example2_description" : "Conflicting shadow directions",
        "what_to_look_for" : ["Shadows pointing in different directions", "Reflections that don't match the environment", "Inconsistent lighting between foreground and background", "Unnatural highlights on skin, eyes, or reflective surfaces"],
        "go_back": "null",
        "next": "2"  
    }
]
# ROUTES

@app.route('/')
def homepage():
   return render_template('welcome.html')   

@app.route('/about')
def about():
   return render_template('about.html')  

@app.route('/learning/<int:id>', methods=['GET', 'POST'])
def learning_modules(id):
    module = next((m for m in modules_data if int(m["id"]) == id), None)

    if module is None:
        abort(404)

    return render_template('modules.html', module=module)

@app.route('/quiz/<int:id>', methods=['GET', 'POST'])
def big_quiz(id):
   return render_template('big_quiz.html')  


# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True, port=5001)




