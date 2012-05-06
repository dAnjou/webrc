from bottle import Bottle, run, template, redirect, abort
import os
import dbus
import re
import subprocess

app = Bottle()

org_mpris2_re = re.compile('^org\.mpris\.MediaPlayer2\.([^.]+)$')
bus = dbus.SessionBus()

MUSIC = "/home/max/Musik"

@app.route("/browse/")
@app.route("/browse/<d:path>")
def browse(d=""):
    folders = []
    files = []
    current_dir = path(MUSIC, d)
    if not current_dir.startswith(MUSIC):
        abort(403, "You are not allowed here!")
    for item in os.listdir(current_dir):
        p = os.path.join(current_dir, item)
        if os.path.isfile(p):
            files.append((p, item))
        if os.path.isdir(p):
            folders.append((p, item))
    return template('browse', folders=folders, files=files)

@app.route("/play/<f:path>")
def play(f=None):
    # play that shit here
    return f

@app.route("/")
def index():
    players = []
    info = ""
    try:
        players = [ name for name in bus.list_names() if org_mpris2_re.match(name)]
        info = subprocess.check_output(["python", "/home/max/bin/mpris-remote"])
    except:
        pass
    return template('index', players=players, info=info)

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
    run(app, reloader=True, debug=True, host="0.0.0.0", port=31337)
