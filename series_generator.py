import os
import random
import subprocess
import ast

with open('friends_settings.txt') as f:
    data: str = f.read()
d: object = ast.literal_eval(data)
i = 1
while i <= d["number_of_episodes"]:
    string = os.path.normpath(d['series_path'])
    choice1: str = random.choice(os.listdir(string))
    # string: object = string + '\\' + str1
    string = os.path.join(string, choice1)
    choice2 = random.choice(os.listdir(string))
    # string = string + "\\" + choice2
    string = os.path.join(string, choice2)
    if not string.endswith(d['video_format']):
        pass
    else:
        with open(os.path.normpath(d['playlist_path']), "a") as fo:
            fo.write(string + "\n")
            i = i + 1
    del string
# p = subprocess.Popen([d['vlc_path'], d['playlist_path'].replace('\\', '\/')])
p = subprocess.Popen([d['vlc_path'], d['playlist_path']])
p.wait()
if p.returncode == 0:
    os.remove(d['playlist_path'])
