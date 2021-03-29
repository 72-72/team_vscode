from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/Salary")
def Salary():
    return render_template("salary_index.html")

@app.route("/salary_result")
def salary_result():
    x = int(request.args.get("x"))
    y = int(request.args.get("y"))
    z = x * y
    return render_template("salaty_result.html",result=z)

if __name__ == "__main__":
    app.run(debug=True)