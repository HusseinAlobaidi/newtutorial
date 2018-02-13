import time
import webbrowser

print('this project start at :' + time.ctime())
take_break = 0
while take_break < 3:
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    take_break += 1


