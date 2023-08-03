from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

@app.route('/')
def index():
        return render_template("index.html")
   

@app.route('/predict',methods = ["GET", "POST"])
def predict():  
    if request.method == "POST":
        weight = int(request.form['weight'])
        height = int(request.form['height'])
        result = weight * height
        return render_template('predict.html', show = result)
    else:
        return redirect(url_for("index"))

@app.route('/result')
def result():
     return render_template("result.html", show = "please enter the correct credentials")

    

if __name__ == "__main__":
    app.run(debug=True)    