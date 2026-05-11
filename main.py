# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request, redirect
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r", encoding="utf-8") as f:
        return json.load(f)

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:
db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        result = db[keyword]
    
    else:
        all_jobs = load_jobs()
        result = []
        for job in all_jobs:
            if keyword.lower() in job["title"].lower():
                result.append(job)
        db[keyword] = result

    return render_template("search.html", keyword=keyword, jobs=result)


# /YOUR CODE


# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run()

# /BLUEPRINT
