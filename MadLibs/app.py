from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)

@app.route("/home")
def show_form():
    return render_template("form.html")

@app.route("/story")
def create_story():
    places = request.args["place"]
    nouns = request.args["noun"]
    verbs = request.args["verb"]
    adjectives = request.args["adjective"]
    plural_nouns = request.args["plural_noun"]
    
    ans = {"place": places,"noun": nouns, "verb": verbs, "adjective": adjectives, "plural_noun": plural_nouns}
    
    story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


    return story.generate(ans)