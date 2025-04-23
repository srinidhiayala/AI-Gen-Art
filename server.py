from os import abort
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import logging

from flask import Flask, render_template, request, redirect, url_for, session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'super-secret-key'  # Required for sessions

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
        "next": "q1"  
    },
     {
        "id": "2",
        "title": "Text and Typography Analysis",
        "example1_pic": "https://i.warbycdn.com/s/c/164957dac184e44592d221ad828fd2c92a8e1ba9.png",
        "example1_description" : "Store sign with text that doesn't follow proper perspective",
        "example2_pic": "https://i.warbycdn.com/s/c/164957dac184e44592d221ad828fd2c92a8e1ba9.png",
        "example2_description" : "Mixed or impossible character combinations",
        "what_to_look_for" : ["Gibberish or nonsensical text elements", "Inconsistent letter spacing or alignment", "Mixed or impossible character combinations", "Text that doesn't follow surface perspective"],
        "go_back": "q1",
        "next": "q2"  
    },
     {
        "id": "3",
        "title": "Digital Noise and Compression Patterns",
        "example1_pic": "https://i.warbycdn.com/s/c/164957dac184e44592d221ad828fd2c92a8e1ba9.png",
        "example1_description" : "Unnatural noise pattern transitions between areas",
        "example2_pic": "https://i.warbycdn.com/s/c/164957dac184e44592d221ad828fd2c92a8e1ba9.png",
        "example2_description" : "Unnaturally clean areas in otherwise textured surfaces",
        "what_to_look_for" : ["Inconsistent noise patterns across similar lighting areas", "Unnatural transitions between noisy and clean areas", "Suspicious smoothing in areas that should be textured", "Noise pattern breaks between foreground and background"],
        "go_back": "q2",
        "next": "q3"  
    },
     {
        "id": "4",
        "title": "Perspective and Spatial Coherence",
        "example1_pic": "https://i.warbycdn.com/s/c/164957dac184e44592d221ad828fd2c92a8e1ba9.png",
        "example1_description" : "Objects not following the same perspective rules",
        "example2_pic": "https://i.warbycdn.com/s/c/164957dac184e44592d221ad828fd2c92a8e1ba9.png",
        "example2_description" : "Objects appearing at physically impossible angles",
        "what_to_look_for" : ["Multiple objects not following the same perspective rules", "Objects appearing at impossible angles", "Size relationships that don't make physical sense", "Reflections with improper perspective matching"],
        "go_back": "q3",
        "next": "q4"  
    },
     {
        "id": "5",
        "title": "Consistency Over Time in Video",
        "example1_pic": "",
        "example1_description" : "Objects not following the same perspective rules",
        "example1_link" : "https://artlist.io/stock-footage/clip/drone-pyrenees-ridge-lake/6415520",
        "example2_pic": "",
        "example2_description" : "Objects appearing at physically impossible angles",
        "example2_link" : "https://www.youtube.com/watch?v=PavYAOpVpJI",
        "what_to_look_for" : ["Elements that flicker or change subtly between frames", "Objects that don't follow natural physics in movement", "Lighting or shadows that change inconsistently across frames", "Complex elements (hair, water) that don't move naturally"],
        "go_back": "q4",
        "next": "q5"  
    }
]

correct_answers = {
    1: "image2",
    2: "image1",
    3: "image2",
    4: "image1",
    5: "image2",
    6: "image1",
    7: "image2"
}

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

@app.route('/big_quiz/<int:step>', methods=['GET', 'POST'])
def big_quiz(step):
    if step < 1 or step > 7:
        return redirect(url_for('big_quiz', step=1))

    if request.method == 'POST':
        answer = request.form.get('answer')
        session[f'answer_{step}'] = answer
        if step < 7:
            return redirect(url_for('big_quiz', step=step + 1))

    score = None
    if step == 7:
        score = sum(
            1 for s, correct in correct_answers.items()
            if session.get(f'answer_{s}') == correct
        )

    return render_template("big_quiz.html", step=step, score=score)

# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True, port=5001)




