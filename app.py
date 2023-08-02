from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

@app.route('/')
def index():
    render_template("index.html")

@app.route('/result',methods = ["get", "post"])
def result():
    if request.method == "post":
        render_template('result.html')
    else:
        redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)    