from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cards = [
        {"title": "Great Pyramid of Giza", "content": "(Egypt)", "link": "/first", "backgroundImage": "static/1stpyram.jpg"},
        {"title": "Great Wall of China", "content": "(China)", "link": "/second", "backgroundImage": "static/g wall of china.jpg"},
        {"title": "Petra", "content": "(Jordan)", "link": "/third", "backgroundImage": "static/Petra.jpg"},
        {"title": "Christ the Redeemer", "content": "(Brazil)", "link": "/fourth", "backgroundImage": "static/Christ the Redeemer.jpg"},
        {"title": "Machu Picchu", "content": "(Peru)", "link": "/fifth", "backgroundImage": "static/Machu Picchu.jpg"},
        {"title": "Roman Colosseum", "content": "(Italy)", "link": "/sixth", "backgroundImage": "static/Roman Colosseum.jpg"},
        {"title": "Taj Mahal", "content": "(India)", "link": "/seventh", "backgroundImage": "static/Taj Mahal.jpg"},
    ]
    return render_template("index.html", cards=cards)

@app.route("/first")
def first():
    return render_template("first.html")

@app.route("/second")
def second():
    return render_template("second.html")

@app.route("/third")
def third():
    return render_template("third.html")

@app.route("/fourth")
def fourth():
    return render_template("fourth.html")

@app.route("/fifth")
def fifth():
    return render_template("fifth.html")

@app.route("/sixth")
def sixth():
    return render_template("sixth.html")

@app.route("/seventh")
def seventh():
    return render_template("seventh.html")

if __name__ == "__main__":
    app.run(debug=True, port=5023)
