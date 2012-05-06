<!doctype html>
<title>Browse</title>
<ul>
    %for d in folders:
    <li><a href="/browse/{{ d[0] }}">{{ d[1] }}</a></li>
    %end
</ul>
<ul>
    %for f in files:
    <li><a href="/play/{{ f[0] }}">{{ f[1] }}</a></li>
    %end
</ul>