from flask import Flask, render_template, redirect, url_for, request
import json
import dockercommands
import logging

settings = None
with open("settings.json") as handle:
    settings = json.load(handle)
    print(settings)

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("swarmstacks"))

@app.route("/composestacks")
def composestacks():
    return render_template("composestacks.html", composeStacks=dockercommands.getComposeStacks(settings), errors=dockercommands.getLastStdErr())

@app.route("/composestack")
def composestack():
    stackname = request.args.get("stackname")
    return render_template("composestack.html", stackname=stackname, stack=dockercommands.getComposeStack(settings, stackname), errors=dockercommands.getLastStdErr())

@app.route("/swarmstacks")
def swarmstacks():
    return render_template("swarmstacks.html", swarmStacks=dockercommands.getSwarmStacks(settings), errors=dockercommands.getLastStdErr())

@app.route("/swarmstack")
def swarmstack():
    stackname = request.args.get("stackname")
    return render_template("swarmstack.html", stackname=stackname, stack=dockercommands.getSwarmStack(settings, stackname), errors=dockercommands.getLastStdErr())

if __name__ == "__main__":
    app.run(debug=True)