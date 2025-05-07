from os import abort
from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'super-secret-key'

# hosts meta data for learning modules --> printed in the flask terminal for every page after clicking "next"
learning_metaData = []

modules_data = [
    {
        "id": "1",
        "title": "Lighting and Reflections",
        "example1_pic": "static/pictures/learning_modules/1.1.jpg",
        "example1_description" : "Inconsistent reflections in eyeglasses",
        "example2_pic": "static/pictures/learning_modules/1.2.jpg",
        "example2_description" : "Conflicting shadow directions",
        "what_to_look_for" : ["Shadows pointing in different directions", "Reflections that don't match the environment", "Inconsistent lighting between foreground and background", "Unnatural highlights on skin, eyes, or reflective surfaces"],
        "go_back": "null",
        "next": "q1"  
    },
     {
        "id": "2",
        "title": "Text and Typography Analysis",
        "example1_pic": "static/pictures/learning_modules/2.1.jpg",
        "example1_description" : "Store sign with text that doesn't follow proper perspective",
        "example2_pic": "static/pictures/learning_modules/2.2.jpg",
        "example2_description" : "Mixed or impossible character combinations",
        "what_to_look_for" : ["Gibberish or nonsensical text elements", "Inconsistent letter spacing or alignment", "Mixed or impossible character combinations", "Text that doesn't follow surface perspective"],
        "go_back": "q1",
        "next": "q2"  
    },
     {
        "id": "3",
        "title": "Digital Noise and Compression Patterns",
        "example1_pic": "static/pictures/learning_modules/3.1.jpg",
        "example1_description" : "Unnatural noise pattern transitions between areas",
        "example2_pic": "static/pictures/learning_modules/3.2.jpg",
        "example2_description" : "Unnaturally clean areas in otherwise textured surfaces",
        "what_to_look_for" : ["Inconsistent noise patterns across similar lighting areas", "Unnatural transitions between noisy and clean areas", "Suspicious smoothing in areas that should be textured", "Noise pattern breaks between foreground and background"],
        "go_back": "q2",
        "next": "q3"  
    },
     {
        "id": "4",
        "title": "Perspective and Spatial Coherence",
        "example1_pic": "static/pictures/learning_modules/4.1.jpg",
        "example1_description" : "Objects not following the same perspective rules",
        "example2_pic": "static/pictures/learning_modules/4.2.jpg",
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
        "example1_link" : "https://youtu.be/QMoLt_5tr1g",
        "example2_pic": "",
        "example2_description" : "Objects appearing at physically impossible angles",
        "example2_link" : "https://youtu.be/h4Q_mqgRTzQ",
        "what_to_look_for" : ["Elements that flicker or change subtly between frames", "Objects that don't follow natural physics in movement", "Lighting or shadows that change inconsistently across frames", "Complex elements (hair, water) that don't move naturally"],
        "go_back": "q4",
        "next": "q5"  
    }
]
quiz_data = {
    "1": {
        "image1": "pictures/mod_quiz/1.1.png",
        "image2": "pictures/mod_quiz/1.2.png",
        "correct_answer": "image2",
        "tip": "Look closely at the lighting and reflections in both images. Pay special attention to eyes, glasses, and shiny surfaces.",
        "go_back_module": 1,
        "next_module": 2
    },
    "2": {
        "image1": "pictures/mod_quiz/2.1.jpg",
        "image2": "pictures/mod_quiz/2.2.png",
        "correct_answer": "image1",
        "tip": "Examine the text elements in both images. Look for inconsistent letter spacing, mixed character sets, or text that doesn't follow perspective correctly.",
        "go_back_module": 2,
        "next_module": 3
    },
    "3": {
        "image1": "pictures/mod_quiz/3.1.png",
        "image2": "pictures/mod_quiz/3.2.png",
        "correct_answer": "image1",
        "tip": "Focus on areas with similar lighting and check if the noise patterns are consistent. AI often creates unnaturally clean areas or inconsistent noise distribution.",
        "go_back_module": 3,
        "next_module": 4
    },
    "4": {
        "image1": "pictures/mod_quiz/4.1.png",
        "image2": "pictures/mod_quiz/4.2.png",
        "correct_answer": "image2",
        "tip": "Check if all objects follow the same perspective rules. Look for elements that appear at physically impossible angles or don't match the environment's vanishing points.",
        "go_back_module": 4,
        "next_module": 5
    },
    "5": {
        "image1": "https://www.youtube.com/embed/nyoDX9vPf_E",
        "image2": "https://www.youtube.com/watch?v=PavYAOpVpJI",
        "correct_answer": "video1",
        "tip": "Watch for elements that flicker or change subtly between frames. Pay attention to physics in movement and how complex elements like hair or water flow.",
        "go_back_module": 5,
        "next_module": "big_quiz"
    }
}

big_quiz_data = {
    1: {
        "image1": "https://britannicaeducation.com/wp-content/uploads/2024/02/Frog.jpg",
        "image2": "https://britannicaeducation.com/wp-content/uploads/2024/02/Blue-frog.jpg",
        "image3": "https://britannicaeducation.com/wp-content/uploads/2024/02/3.png",
        "correct_answer": "image2",
    },
    2: {
        "image1": "https://britannicaeducation.com/wp-content/uploads/2024/02/Students-Activity.jpg",
        "image2": "https://britannicaeducation.com/wp-content/uploads/2024/02/Kids-doing-art.jpg",
        "image3": "https://britannicaeducation.com/wp-content/uploads/2024/02/5.png",
        "correct_answer": "image1",
    },
    3: {
        "image1": "https://britannicaeducation.com/wp-content/uploads/2024/02/Mt-Fuji.jpg",
        "image2": "https://britannicaeducation.com/wp-content/uploads/2024/02/Mount-Fuji.jpg",
        "image3": "https://britannicaeducation.com/wp-content/uploads/2024/02/6.png",
        "correct_answer": "image2",
    },
    4: {
        "image1": "https://britannicaeducation.com/wp-content/uploads/2024/02/HK.jpg",
        "image2": "https://britannicaeducation.com/wp-content/uploads/2024/02/Hong-Kong.jpg",
        "image3": "https://britannicaeducation.com/wp-content/uploads/2024/02/8.png",
        "correct_answer": "image1",
    },
    5: {
        "image1": "https://britannicaeducation.com/wp-content/uploads/2024/02/Northern-Lights.jpg",
        "image2": "https://britannicaeducation.com/wp-content/uploads/2024/02/Aurora.jpg",
        "image3": "https://britannicaeducation.com/wp-content/uploads/2024/02/9.png",
        "correct_answer": "image2",
    },
    6: {
        "image1": "https://example.com/quiz6_img1.jpg",
        "correct_answer": "yes",
    },
    7: {
        "image1": "https://example.com/quiz7_img1.jpg",
        "correct_answer": "yes",
    }
}

correct_answers = {
      1: "image1",
      2: "image2",
      3: "image1",
      4: "image1",
      5: "image1",
      6: "yes",
      7: "yes"
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

@app.route("/quiz/<quiz_id>", methods=["GET", "POST"])
def quiz(quiz_id):
    quiz = quiz_data[quiz_id]
    user_answer = None
    correct_answer = quiz["correct_answer"]

    if request.method == "POST":
        user_answer = request.form["answer"]
    
    return render_template(
        "quiz.html",
        quiz=quiz,
        user_answer=user_answer,
        correct_answer=correct_answer
    )

@app.route('/big_quiz/<int:step>', methods=['GET', 'POST'])
def big_quiz(step):
    if step < 1 or step > 7:
        return redirect(url_for('big_quiz', step=1))

    quiz = big_quiz_data[step]

    if step == 1 and request.method == 'GET':
        session.pop('quiz_submitted', None)
        for i in range(1, 8):
            session.pop(f'answer_{i}', None)

    if request.method == 'POST':
        answer = request.form.get('answer')
        session[f'answer_{step}'] = answer

        if step < 7:
            return redirect(url_for('big_quiz', step=step + 1))
        else:
            session['quiz_submitted'] = True
            return redirect(url_for('big_quiz_results'))

    return render_template('big_quiz.html', step=step, quiz=quiz, big_quiz_data=big_quiz_data)

@app.route('/big_quiz_results')
def big_quiz_results():
    if not session.get('quiz_submitted'):
        return redirect(url_for('big_quiz', step=1))

    score = sum(
        1 for s, correct in correct_answers.items()
        if session.get(f'answer_{s}') == correct
    )

    user_id = session.get('user_id', 1) 

    return render_template('big_quiz_results.html', score=score, user_id=user_id)


@app.route('/record_time', methods=['POST'])
def record_time():
    global learning_metaData
    if request.data:
        import json
        data = json.loads(request.data) 
    else:
        data = {}

    module_id = data.get('module_id')
    time_spent = data.get('time_spent')
    
    learning_metaData.append({"module_id":module_id, "seconds_spent":time_spent})
    
    logger.info(learning_metaData)

    return jsonify({'status': 'success'})
@app.route('/begin_quiz')
def begin_quiz():
    return render_template('begin_quiz.html')


@app.route('/record_quiz_time', methods=['POST'])
def record_quiz_time():
    global quiz_metaData
    if request.data:
        import json
        data = json.loads(request.data) 
    else:
        data = {}

    quiz_id = data.get('quiz_id')
    time_spent = data.get('time_spent')
    
    quiz_metaData.append({"quiz_id": quiz_id, "seconds_spent": time_spent})  
    logger.info(quiz_metaData)

    return jsonify({'status': 'success'})


# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True, port=5001)




