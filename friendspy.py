from os import listdir,remove
from random import choice
from subprocess import Popen
from ast import literal_eval
with open('friendssettings.txt') as f: 
    data = f.read()
d = literal_eval(data)
i = 1
while i in range(0,d['num']+1):
	string = d['seriespath']
	str1 = choice(listdir(string))
	string = string + "\\"+str1
	str2 = choice(listdir(string))
	string = string + "\\"+ str2
	if string.endswith(d['video_format']):
		fo = open(d['playlist_path'],"a")
		fo.write("\n"+string)
		fo.close()
		i = i + 1
	del string
p = Popen([d['vlc_path'],d['playlist_path'].replace('\\','\/')])

p.wait()
if(p.returncode == 0):
	remove(d['playlist_path'])
