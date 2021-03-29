from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/result")
def result():
    han = int(request.args.get("han"))
    menseki = han * han * 3.14
    ensyu = 2 * han * 3.14
    return render_template("result.html",menseki = menseki,ensyu = ensyu)
    
if __name__ == "__main__":
    app.run(debug=True)