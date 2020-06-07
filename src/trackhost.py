#!/bin/python3

from flask import Flask, render_template, request, jsonify, abort, redirect, url_for

from networkhostinfo.hostinfo import TrackHost, InvalidIPError
from networkhostinfo.inventoryoperations import display_inventory

app = Flask(__name__)

net = {}


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/inventory/display")
def inventory():
    return jsonify(display_inventory())


@app.route("/loaddata")
def loaddata():
    global net
    net = TrackHost()
    data = net.load()
    return render_template("loaddata.html", data=data)


@app.route("/hosts/track", methods=["GET", "POST"])
def trackhosts():

    if request.method == "POST":
        ips = list(map(str.strip, request.form["ips"].split(",")))
        try:
            data = net.track_and_print(
                ips, port_type=request.form["port_type"], export=True
            )
            return render_template("trackhostresult.html", data=data)
        except InvalidIPError:
            abort(422)
    else:
        return render_template("trackhosts.html")


@app.route("/hosts/track/command", methods=["GET", "POST"])
def trackcommand():
    if request.method == "POST":
        try:
            ips = list(map(str.strip, request.form["ips"].split(",")))
            commands = list(map(str.strip, request.form["commands"].split(",")))
            data = net.track_command_print(
                ips, commands, port_type=request.form["port_type"], export=True
            )
            return render_template("trackhostresult.html", data=data)
        except InvalidIPError:
            abort(422)

    else:
        return render_template("trackhostcommand.html")


@app.route("/subnet/track", methods=["GET", "POST"])
def tracksubnet():

    if request.method == "POST":
        subnet = request.form["subnet"]
        eipsstr = request.form["eips"]
        if eipsstr:
            eips = list(map(str.strip, request.form["eips"].split(",")))
        else:
            eips = []
        try:
            data = net.track_subnet(subnet, True, request.form["port_type"], eips)
            return render_template("trackhostresult.html", data=data)
        except (ValueError, InvalidIPError):
            abort(422)

    else:
        return render_template("tracksubnet.html")


@app.route("/inventory/update", methods=["GET", "POST"])
def loadinv():
    if request.method == "POST":
        file = request.files["file"]
        file.save("static/inventory.yml")
        return redirect(url_for("inventory"))
    else:
        return render_template("load_inv.html")
