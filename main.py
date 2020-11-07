from tkinter import *
import tkinter.messagebox
from pygame import mixer
from tkinter import filedialog
from mutagen.mp3 import MP3
from ttkthemes import themed_tk as tk
from tkinter import ttk
import threading
import time
import os

root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")

showbar=ttk.Label(root,text="welcome to mussica",relief=SUNKEN,anchor=W,font="Times 10 italic")
showbar.pack(side=BOTTOM,fill=X)

menubar = Menu(root)
root.config(menu=menubar)
submenu = Menu(menubar, tearoff=0)


def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    print(filename_path)
    add_to_playlist(filename_path)

playlist1=[]

def add_to_playlist(filename):
    filename=os.path.basename(filename)
    index=0
    playlist.insert(index, filename)
    playlist1.insert(index,filename_path)
    index +=1

menubar.add_cascade(label="choose", menu=submenu)
submenu.add_command(label="open", command=browse_file)
submenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo("About Musica", "This is python base Ui")


submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About us", command=about_us)

mixer.init()  # intilizing the mixer

root.title("Musica")
root.iconbitmap(r'images\musica.ico')

leftframe=Frame(root)
leftframe.pack(side=LEFT,padx=30,pady=30)

playlist = Listbox(leftframe)
playlist.pack()

addBtn=ttk.Button(leftframe,text="+Add",command=browse_file)
addBtn.pack(side=LEFT)

def del_song():
    selected_song = playlist.curselection()
    selected_song = int(selected_song[0])
    playlist.delete(selected_song)
    playlist1.pop(selected_song)

delBtn=ttk.Button(leftframe,text="-Del",command=del_song)
delBtn.pack(side=LEFT)

rightframe=Frame(root)
rightframe.pack(pady=30)

topframe=Frame(rightframe)
topframe.pack()


lengthLabel= ttk.Label(topframe, text="Total Length - __:__")
lengthLabel.pack(pady=10)

currenttimeLabel= ttk.Label(topframe, text="Current Length - __:__",relief=GROOVE)
currenttimeLabel.pack(pady=10)

def show_details(play_song):
    file_data=os.path.splitext(play_song)
    print(file_data)

    if file_data[1] == '.mp3':
        audio =MP3(play_song)
        total_length=audio.info.length

    else:
        a = mixer.sound(play_song)
        total_length = a.get_length()

    mins,secs=divmod(total_length,60)
    mins=round(mins)
    secs=round(secs)
    timeformat="{:02d}:{:02d}".format(mins, secs)
    lengthLabel["text"] = "total_length" + "  " + timeformat
    t1=threading.Thread(target=start_count,args=(total_length,))
    t1.start()

def start_count(t):

    global paused
    #mixer.music.get_busy(): Return false when we pause the stop button (music stop playing)
    
    current_time=0
    while current_time<=t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = "{:02d}:{:02d}".format(mins, secs)
            currenttimeLabel["text"] = "Current Time" + " " + timeformat
            time.sleep(1)
            current_time += 1
    #This code used for to start the current time from back        
    # while t and mixer.music.get_busy():
    # if paused:
    #    continue
    # else:
    #   mins, secs = divmod(t, 60)
    #  mins = round(mins)
    # secs = round(secs)
    # timeformat = "{:02d}:{:02d}".format(mins, secs)
    # currenttimeLabel["text"] = "Current Time" + " " + timeformat
    # time.sleep(1)
    # t -= 1


def play_music():
    global paused
    if paused:
        mixer.music.unpause()
        showbar["text"] = "Resume Music"
        paused=FALSE

    else:
         try:
             stop_music()
             time.sleep(1)
             selected_song=playlist.curselection()
             selected_song=int(selected_song[0])
             play_it=playlist1[selected_song]
             mixer.music.load(play_it)
             mixer.music.play()
             showbar["text"] = "play Music" + "  " + os.path.basename(play_it)
             show_details(play_it)
         except:
             tkinter.messagebox.showerror("File not found", "Mussica does not find your file please select actual file")
             print("Error")


def stop_music():
    mixer.music.stop()
    showbar["text"] = "stop Music"

paused=FALSE

def pause_music():
    global paused
    paused=TRUE
    mixer.music.pause()
    showbar["text"] = "pause Music"



def set_volume(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)
    # set_volume of mixer takes value only from 0 t0 1 example-0,0.1,0.55,0.54,0.99,1

def rewind_music():
    play_music()
    showbar["text"] = "Music Rewind"

muted=FALSE

def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(0.5)
        audioBtn.configure(image=audioPhoto)
        scale.set(50)
        muted=FALSE
    else:
        mixer.music.set_volume(0)
        audioBtn.configure(image=mutePhoto)
        scale.set(0)
        muted=TRUE

middleframe=Frame(rightframe)
middleframe.pack(padx=30,pady=30)

playPhoto = PhotoImage(file="images/play.png")
playBtn = ttk.Button(middleframe, image=playPhoto, command=play_music)
playBtn.grid(row=0,column=0,padx=10)

stopPhoto = PhotoImage(file="images/stop.png")
stopBtn = ttk.Button(middleframe, image=stopPhoto, command=stop_music)
stopBtn.grid(row=0,column=1,padx=10)

pausePhoto = PhotoImage(file="images/pause.png")
pauseBtn = ttk.Button(middleframe, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0,column=2,padx=10)

bottomframe=Frame(rightframe)
bottomframe.pack(padx=10,pady=10)

rewindPhoto=PhotoImage(file="images/rewind.png")
rewindBtn=ttk.Button(bottomframe,image=rewindPhoto,command=rewind_music)
rewindBtn.grid(row=0,column=0)

mutePhoto=PhotoImage(file="images/mute.png")
audioPhoto=PhotoImage(file="images/audio.png")
audioBtn=ttk.Button(bottomframe,image=audioPhoto,command=mute_music)
audioBtn.grid(row=0,column=1,padx=10)

scale = ttk.Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(50)
mixer.music.set_volume(0.5)
scale.grid(row=0,column=2,padx=15,pady=15)

def on_closing():
    stop_music()
    root.destroy()

root.protocol("WM_DELETE_WINDOW",on_closing)
root.mainloop()
