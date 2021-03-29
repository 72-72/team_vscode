from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/Salary")
def Salary():
    return render_template("index.html")

@app.route("/result")
def result():
    x = int(request.args.get("x"))
    y = int(request.args.get("y"))
    z = x * y
    return render_template("result.html",result=z)

if __name__ == "__main__":
    app.run(debug=True)