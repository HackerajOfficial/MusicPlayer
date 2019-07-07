from tkinter import *
#import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
import os

root = Tk() #tk creates window and put in root variable

#Create Menubar
menubar = Menu(root)
root.config(menu=menubar)

#Create sub menu
subMenu = Menu(menubar, tearoff=0)
def browse_file():
    global filename
    filename = filedialog.askopenfilename()

menubar.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Open',command=browse_file)
subMenu.add_command(label='Exit',command=root.destroy)

def About_Us():
    tkinter.messagebox.showinfo('About Music Player','Developer: Hackeraj')

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=subMenu)
subMenu.add_command(label='About Us', command=About_Us)

mixer.init() #initializing the mixer

root.geometry('300x400')
root.title("Music Player")
root.iconbitmap(r'music_player.ico')

text = Label(root,text='Lets Make Some Niose!!!')
text.pack(pady=10)

def play_music():
    try:
        paused
    except NameError:

        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text']= "Playing Music" + '-' + os.path.basename(filename)
        except:
            #tkinter.messagebox.showerror('File Not Found','File Not Found Please import song')
            browse_file()
    else:
        mixer.music.unpause()
def stop_music():
    mixer.music.stop()
    statusbar['text']= "Stopped Music"

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()

def set_volume(volume):
    volume=int(volume) / 100
    mixer.music.set_volume(volume)

def rewind_music():
    play_music()
    statusbar['text']= "Playing Music" + '-' + os.path.basename(filename)

muted = FALSE
def mute_music():
    global muted
    if muted:
        pass
    else:
        pass

    volumebtn.configure(image=mutephoto)

middleframe = Frame(root)
middleframe.pack(padx=30,pady=30)

playphoto = PhotoImage(file='play.png')
#labelphoto = Label(root,image=photo)
#labelphoto.pack()

playbtn = Button(middleframe, image=playphoto , command=play_music)
playbtn.grid(row=0,column=0,padx=10)


stopphoto = PhotoImage(file='stop.png')
stopbtn = Button(middleframe, image=stopphoto, command=stop_music )
stopbtn.grid(row=0,column=1,padx=10)

pausephoto = PhotoImage(file='pause.png')
pausebtn = Button(middleframe, image=pausephoto, command=pause_music )
pausebtn.grid(row=0,column=2,padx=10)

rewindphoto = PhotoImage(file='rewind-button.png')
rewindbtn = Button(middleframe, image=rewindphoto, command=rewind_music )
rewindbtn.grid(row=1,column=0,padx=10,pady=10)

volumephoto = PhotoImage(file='volume.png')
mutephoto = PhotoImage(file='mute.png')
volumebtn = Button(middleframe, image=volumephoto, command=mute_music )
volumebtn.grid(row=1,column=1,padx=10,pady=10)

scale = Scale(root, from_=0,to=100,orient=HORIZONTAL, command=set_volume)
scale.set(0.01)
mixer.music.set_volume(0.01)
scale.pack(pady=15)

statusbar = Label(root, text='Welcome To Music Player', relief=SUNKEN)
statusbar.pack(side='bottom', fill=X)

root.mainloop() #this helps countinously show windows
