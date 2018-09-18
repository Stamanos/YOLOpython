from twitter import *
from tkinter import *

print("user")
user = sys.stdin.readline()

print("screen_name")
screen_name = sys.stdin.readline()

print("text")
text = sys.stdin.readline()


def showTweets(x, num): # display a number of new tweets and usernames
    for i in range(0, num):
        line1 = (x[i][user][screen_name])
        line2 = (x[i][text])
        w = Label(master, text=line1 + "\n" + line2 + "\n\n")
        w.pack()

def getTweets():
    x = t.statuses.home_timeline(screen_name="putscreennamehere")
    return x

consumer_key = "	Tdge4a6konBvh9FEhui3aoYPZ"
consumer_secret = "7owY8wMRFGH71pAKxaauboDNIpJZU0Bzpcb9AiDMvvWef2RpDG"
access_token = "834100303897231360-ezMd7Jm44XMI66WFpf5oUFuRyyxaZcB"
access_token_secret = "xtzaAh6Hr2AbvCgWoCkqhpnNnbat21rA4EbegDVIjNSrn"
auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def tweet():
    global entryWidget
    if entryWidget.get().strip() == "":
        print("Empty")
    else:
        t.statuses.update(status=entryWidget.get().strip())
        entryWidget.delete(0,END)
        print("working")



numberOfTweets = 10



master = Tk()
showTweets(getTweets(), numberOfTweets)

master.title("Tkinter Entry Widget")
master["padx"] = 40
master["pady"] = 20
# Create a text frame to hold the text Label and the Entry widget
textFrame = Frame(master)
#Create a Label in textFrame
entryLabel = Label(textFrame)
entryLabel["text"] = "Make a new Tweet:"
entryLabel.pack(side=LEFT)
# Create an Entry Widget in textFrame
entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack(side=LEFT)
textFrame.pack()
button = Button(master, text="Submit", command=tweet)
button.pack()

master.mainloop()