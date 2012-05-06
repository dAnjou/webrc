<!doctype html>
<title>Music</title>
<ul>
    %for p in players:
    <li>{{ p }}</li>
    %end
</ul>
<h1><a href="/volume/+5">Lauter</a></h1>
<h1><a href="/volume/-5">Leiser</a></h1>
<h1><a href="/playback/playpause">PlayPause</a></h1>
<h1><a href="/playback/prev">Prev</a></h1>
<h1><a href="/playback/next">Next</a></h1>
<pre>{{ info }}</pre>