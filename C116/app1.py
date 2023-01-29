from flask import Flask, render_template

app1 = Flask(__name__)

@app1.route("/template")
def showTemplate():
    return render_template("index.html")

if __name__ == "__main__":
    app1.run()