from flask import Flask, render_template, redirect, url_for
import json
import dockercommands

settings = None
with open("settings.json") as handle:
    settings = json.load(handle)
    print(settings)

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("stacks"))

@app.route("/stacks")
def stacks():
    return render_template("stacks.html", composeStacks=dockercommands.getComposeStacks(settings), swarmStacks=dockercommands.getSwarmStacks(settings))

if __name__ == "__main__":
    app.run(debug=True)
