import os
import subprocess

files = os.listdir()

with open('test.txt', 'w') as f:
    for file in files:
        if file[len(file)-4:]=='.mkv' or file[len(file)-4:]=='.avi':            
            process = subprocess.Popen(['ffmpeg', '-i',file,file[:len(file)-4]+'.mp4'], stdout=f)
            process.wait()
