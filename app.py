from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def renderForm():
    return render_template("questions.html", prompts=story.prompts)
@app.route('/story')
def renderStory():
    return render_template("story.html", story=story.generate(request.args))