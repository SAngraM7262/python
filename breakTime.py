import time
import webbrowser

count = 0
totalCount = 3
print("This program is started on "+time.ctime())
while(totalCount > count):
    time.sleep(5)
    webbrowser.open("file:///D:/web/css-gloing%20text/index.html")
    count = count + 1

