from attr import define
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

root=Tk()
root.title('Music Player | NateBrook ')

        
def addsongs():
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    for s in temp_song:
        s=s.replace("C:/Users/%USERNAME%/python-mp3-music-player/","")
        songs_list.insert(END,s)
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])
    
def Play():
    song=songs_list.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()
def Pause():
    mixer.music.pause()
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)
def Resume():
    mixer.music.unpause()
mixer.init()
songs_list=Listbox(root,selectmode=SINGLE,bg="gray",fg="white",font=('arial',15),height=12,width=30,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=9)
defined_font = font.Font(family='Helvetica')
#play button
play_button=Button(root,text="Play",width =7,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)
#stop button
stop_button=Button(root,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=1)
#pause button 
pause_button=Button(root,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=2)
#resume button
Resume_button=Button(root,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)
#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
#add_song_menu.add_command(label="Download songs",command=downloadsong) # coming soon
add_song_menu.add_command(label="Delete song",command=deletesong)
mainloop()