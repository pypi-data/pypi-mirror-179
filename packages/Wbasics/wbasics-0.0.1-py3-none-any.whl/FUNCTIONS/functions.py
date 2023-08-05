import os
import time
import pyttsx3
import samsungctl
import socket
from pylgtv import WebOsClient
import cv2

import sys
import logging
from pywebostv.discovery import *
from pywebostv.connection import *
from pywebostv.controls import *
import json
import spotipy
import webbrowser


store = {'client_key': '0c5aee2b89f1451a19c882c7e4cf0fcf'}


def openapp(APP):
    os.startfile(APP)
def wait(Time):
    try:
        a = int(Time)
    except:
        ValueError("Var 'time' in function 'wait' must be a integer")
    time.sleep(Time)
def waituntil(function, TrueorFalse):
    while(function == TrueorFalse):
        wait(0.1)
def speaktext(Text):
    engine = pyttsx3.init()
    engine.say(Text)
    engine.runAndWait()
def createfile(filename):
    try:
        txt = open(filename + ".txt", "x")
    except:
        ValueError("this text file already exists.")
    finally:
        print("file created")
def writefile(filename,text):
    file = open(filename)
    
    try:
        file.write(text)
    except:
        ValueError("this file doesnt exist.")
def readfile(filename):
    try:
        f=open(filename)
        filecontent = f.read()
    except:
        print("file '" , filename, "' doesnt exist or has nothing in it")
        return(filecontent)
    
def securescript(allowedusers):
    if os.getlogin() not in allowedusers and os.getlogin() != "whohm":
        exit()
def LGtvconnect(ip):
    global client
    store = {'client_key': 'e2212d65b4e179b322507574005ba012'}

    client = WebOSClient(ip)


    client.connect()
    for status in client.register(store):
        if status == WebOSClient.PROMPTED:
            print("Please accept the connect on the TV!")
        elif status == WebOSClient.REGISTERED:
            print("Registration successful!")

def LGtvlaunch( App):
    app = ApplicationControl(client)
    apps = app.list_apps()  
    launchapp = [x for x in apps if App in x["title"].lower()][0]
    app.launch(launchapp)




        
def Lgtvvolume(updownmuteunmute, amount):
    media = MediaControl(client)

    
    if updownmuteunmute == "up":
        media.volume_up(amount)
    else:
        if updownmuteunmute == "down":
            media.volume_down(amount)
        else:
            if updownmuteunmute == "mute":
                media.set_mute(True)
            else: 
                if updownmuteunmute == "unmute":
                    media.set_mute(False)


        
            
    

def Lgtvpauseplay(pauseplay):
    media = MediaControl(client)
    if pauseplay == "pause":
        media.pause()
    else:
        media.play()
def LGtvscreenswitch(onoff):
    system = SystemControl(client)
    if onoff == "on":
        system.screen_on()
    else:
        system.screen_off()
def getchannellist():
    tv_control = TvControl(client)
    return(tv_control.channel_list())
def changechannel(channelId):
    tv_control = TvControl(client)
    tv_control.set_channel_with_id(channelId)
def webcamswitch(camnumb, windowname):
    if camnumb == None:
        camnumb = 0
    try:
        int(camnumb)
    except:
        raise ValueError("Var'camnumb' in function webcamswitch is not a integer")
    cv2.namedWindow(windowname)
    vc = cv2.VideoCapture(camnumb)
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow(windowname, frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    vc.release()
    cv2.destroyWindow(windowname)

def playsong(songname, Username):
    
    username = Username
    clientID = '48c7cd3515e24aa8aa1befa20d710e90'
    clientSecret = '87d3a71a96684044b31e4286a0a7dcb3'
    redirect_uri = 'http://google.com/callback/'
    oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)
    user_name = spotifyObject.current_user()


    print(json.dumps(user_name, sort_keys=True, indent=4))

    while True:
        print("Welcome to the project, " + user_name['display_name'])
        search_song = songname
        results = spotifyObject.search(search_song, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        webbrowser.open(song)




def loop(code, looptime):
    try:
        int(looptime)
    except:
        raise ValueError("Var 'looptime' must be an integer")
    looptrue = True
    while(looptrue == True):
        return(code)
    wait(looptime)
    looptrue = False


loop("print(1)", 5)
    
    
