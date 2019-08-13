import os

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("/pics) if isfile(join("/pics", f))]

print onlyfiles
print len(onlyfiles)
contents = ""i
count = 0
for x in onlyfiles:
    x = "./pics/" + x
    contents += "<div><object data=" + repr(x) +  "></object></div>"
    count += 1

f = open('./gallery.html','w')

message = """<html>
<head></head>
<body>

<p>Hello World!</p>
""" + contents + """

<script type="text/javascript">
for (i=1;i<=count;i++)
{
    var id=i;
    document.write("<div id=\"gallery" <img id=\"ts"+id+"\" src=./pics"thumb"+id+".jpg"/></div>");
}
</script>


</body>
</html>"""

f.write(message)
f.close()


