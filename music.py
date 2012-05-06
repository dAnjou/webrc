from flask import Flask, render_template, redirect
import os
import dbus
import re
import subprocess

app = Flask(__name__)

org_mpris2_re = re.compile('^org\.mpris\.MediaPlayer2\.([^.]+)$')
bus = dbus.SessionBus()

@app.route("/", methods=["GET"])
def index():
    players = []
    info = ""
    try:
        players = [ name for name in bus.list_names() if org_mpris2_re.match(name)]
        info = subprocess.check_output(["python", "/home/max/bin/mpris-remote"])
    except:
        pass
    return render_template('index.html', players=players, info=info)

@app.route("/volume/<x>")
def volume(x):
    try:
        int(x)
        os.system("pactl -- set-sink-volume 0 %s%%" % x)
    except:
        pass
    return redirect("/")

@app.route("/playback/<x>")
def playback(x):
    if x in ["play", "pause", "prev", "next", "stop", "playpause"]:
        os.system("python /home/max/bin/mpris-remote %s" % x)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=31337)
