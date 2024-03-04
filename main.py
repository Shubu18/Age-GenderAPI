from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route("/")
def pri():
    return render_template("aa.html")`

@app.route("/a/<name>")
def ess(name):
    api = f"https://api.genderize.io?name={name}"
    gen_responce = requests.get(api)
    g_data = gen_responce.json()
    gender = g_data["gender"]

    api2 = f"https://api.agify.io?name={name}"
    g_res = requests.get(api2)
    g2_data = g_res.json()
    age = g2_data["age"]

    return render_template("aa.html", pname=name, agender=gender, aage=age)


if __name__ == "__main__":
    app.run(debug=True)
