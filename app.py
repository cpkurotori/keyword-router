from flask import Flask, render_template
from flask import request, redirect
import yaml

with open("clues.yaml") as file:
    raw_yaml_file = next(yaml.safe_load_all(file))
# print(list(raw_yaml_file))
keyword_map = {item["keyword"]: item["next"] for item in raw_yaml_file}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", invalid=False)

def handle_keyword(keyword):
    if keyword not in keyword_map:
        return render_template("index.html", invalid=True)
    next = keyword_map[keyword]
    if next["type"].lower() == "url":
        return redirect(next["value"])
    if next["type"].lower() == "clue":
        return render_template("clue.html", clue=next["value"])


@app.route("/", methods=["POST"])
def get_keywords():
    keyword = request.form.get("keyword")
    return handle_keyword(keyword)

if __name__ == "__main__":
    app.run()