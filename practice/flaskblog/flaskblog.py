from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"author": "akhil",
     "title": "Blog Post 1",
     "content":"This is book 1 content",
     "date_posted": "28 Apr 2024",
     },
    {"author": "reddy",
     "title": "Blog Post 2",
     "content":"This is book 2 content",
     "date_posted": "28 Apr 2024"}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")


if __name__ == "__main__":
    app.run(debug=True)