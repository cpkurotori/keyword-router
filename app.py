from flask import Flask, render_template
from flask import request, redirect
import yaml
import os

with open("clues.yaml") as file:
    raw_yaml_file = next(yaml.safe_load_all(file))
# print(list(raw_yaml_file))
keyword_map = {item["keyword"]: item["url"] for item in raw_yaml_file}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", invalid=False)

@app.route("/", methods=["POST"])
def get_keywords():
    keyword = request.form.get("keyword")
    if keyword and keyword in keyword_map:
        return redirect(keyword_map[keyword])
    else:
        return render_template("index.html", invalid=True)

if __name__ == "__main__":
    app.run(host=os.getenv("HOST", "0.0.0.0"), port=os.getenv("PORT", "5000"))