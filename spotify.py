def unmutemusic():
      global currentvol
      root.unmuteButton.grid_remove()
      root.muteButton.grid()
      mixer.music.set_volume(currentvol)

def mutemusic():
      global currentvol
      root.muteButton.grid_remove()
      root.unmuteButton.grid()
      currentvol = mixer.music.get_volume()
      mixer.music.set_volume(0)

def resumemusic():
      root.ResumeButton.grid_remove()
      root.PauseButton.grid()
      mixer.music.unpause()
      AudioStatusLabel.configure(text='Playing.....')
      
def stopmusic():
      mixer.music.stop()
      AudioStatusLabel.configure(text='Stopped.....')

def volumedown():
      vol = mixer.music.get_volume()
      mixer.music.set_volume(vol-0.1)

def volumeup():
      vol = mixer.music.get_volume()
      mixer.music.set_volume(vol+0.1)

def pausemusic():
      mixer.music.pause()
      root.PauseButton.grid_remove()
      root.ResumeButton.grid()
      AudioStatusLabel.configure(text='Paused.....')
def playmusic():
      ad = audiotrack.get()
      mixer.music.load(ad)
      mixer.music.play()
      AudioStatusLabel.configure(text='Playing.....')
      
def musicurl():     
    try:

          dd = filedialog.askopenfilename(initialdir='Libraries/Music', title='Select File Audio File',filetype=(('.MP3','.mp3'),('.WAV','.wav')))

    except:
          dd = filedialog.askopenfilename(title='Select File Audio File',filetype=(('.MP3','.mp3'),('.WAV','.wav')))
      
    audiotrack.set(dd)

      
def createwidthes():
      global imbrowse, implay, impause, imvolumeup, imvolumedown, imstop,imresume,immute,imunmute,AudioStatusLabel
       
      ####### Images Register #######

      implay = PhotoImage(file='play.png')
      impause = PhotoImage(file='pause.png')
      imbrowse = PhotoImage(file='browse.png')
      imvolumeup = PhotoImage(file='volumeu.png')
      imvolumedown = PhotoImage(file='volumed.png')
      imstop = PhotoImage(file='stop.png')
      imresume = PhotoImage(file='play.png')
      immute = PhotoImage(file='mute.png')
      imunmute = PhotoImage(file='sound.png')

       ############# Change size of images #########

      imbrowse = imbrowse.subsample(15,15)
      implay = implay.subsample(15,15)
      impause = impause.subsample(15,15)
      imvolumeup = imvolumeup.subsample(15,15)
      imvolumedown = imvolumedown.subsample(15,15)
      imstop = imstop.subsample(15,15)
      imresume = imresume.subsample(15,15)
      immute = immute.subsample(15,15)
      imunmute = imunmute.subsample(15,15)
       
      #### Create Labels ########

      TrackLabel = Label(root,text="Select Audio Track :",bg="lightskyblue",font=('arial',15,'italic bold'))
      TrackLabel.grid(row=0,column=0,padx=20,pady=20)

      AudioStatusLabel = Label(root,text='',bg='lightskyblue',font=('arial',13,'italic bold'),width=20)
      AudioStatusLabel.grid(row=2,column=1)


      #####################################
      TrackLabelEntry = Entry(root,font=('arial',16,'italic bold'),width=35,textvariable=audiotrack)
      TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)

      ###### Buttons ######
      BrowseButton = Button(root,text='Search',bg='deeppink',font=('arial',10,'italic bold'),width=100,bd=3,
      activebackground='purple4',image=imbrowse,compound=RIGHT,command=musicurl)
      BrowseButton.grid(row=0,column=2,padx=20,pady=20)

      PlayButton = Button(root,text='Play',bg='green2',font=('arial',10,'italic bold'),width=100,bd=3,
      activebackground='purple4',image=implay,compound=RIGHT,command=playmusic)
      PlayButton.grid(row=1,column=0,padx=20,pady=20)

      root.PauseButton = Button(root,text='Pause',bg='yellow',font=('arial',10,'italic bold'),width=100,bd=3,
      activebackground='purple4',image=impause,compound=RIGHT,command=pausemusic)
      root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

      root.ResumeButton = Button(root,text='resume',bg='yellow',font=('arial',10,'italic bold'),width=100,bd=3,
      activebackground='purple4',image=imresume,compound=RIGHT,command=resumemusic)
      root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
      root.ResumeButton.grid_remove()

      root.muteButton = Button(root,text='Mute',width=100,font=('arial',10,'italic bold'),bg='yellow',activebackground='purple4',bd=3,
      image=immute,compound=RIGHT,command=mutemusic)
      root.muteButton.grid(row=3,column=2,padx=10,pady=10)

      root.unmuteButton = Button(root,text='Unmute',width=100,font=('arial',10,'italic bold'),bg='yellow',activebackground='purple4',bd=3,
      image=imunmute,compound=RIGHT,command=unmutemusic)
      root.unmuteButton.grid(row=3,column=2,padx=10,pady=10)
      root.unmuteButton.grid_remove()

      VolumeUButton = Button(root,text='VolumeUp',bg='blue',font=('arial',10,'italic bold'),width=150,bd=3,
      activebackground='purple4',image=imvolumeup,compound=RIGHT,command=volumeup)
      VolumeUButton.grid(row=1,column=2,padx=20,pady=20)

      StopButton = Button(root,text='Stop',bg='red',font=('arial',10,'italic bold'),width=100,bd=3,
      activebackground='purple4',image=imstop,compound=RIGHT,command=stopmusic)
      StopButton.grid(row=2,column=0,padx=20,pady=20)

      VolumeDButton = Button(root,text='VolumeDown',bg='blue',font=('arial',10,'italic bold'),width=150,
      bd=3,activebackground='purple4',image=imvolumedown,compound=RIGHT,command=volumedown)
      VolumeDButton.grid(row=2,column=2,padx=20,pady=20)

from tkinter import *
from tkinter import filedialog
from pygame import mixer
root = Tk()
root.geometry("1100x500+200+50")
root.title("Music Player...")
root.iconbitmap('mu.ico')
root.resizable(False,False)
root.configure(bg="lightskyblue")
##### Global Variables ########
audiotrack = StringVar()
currentvol = 0

########## Create Slider #######
ss = 'Developed By Kamal Parekh'
count = 0
text = ''
SliderLabel = Label(root,text=ss,bg='lightskyblue',font=('arial',20,'italic bold'))
SliderLabel.grid(row=4,column=0,pady=20,padx=20,columnspan=3)
def IntroLabelTrick():
      global count,text
      if(count>=len(ss)):
            count = -1
            text = ''
            SliderLabel.configure(text=text)
      else:
            text =text+ss[count]
            SliderLabel.configure(text=text)
      count +=1
      SliderLabel.after(200,IntroLabelTrick)

IntroLabelTrick()
mixer.init()
createwidthes()
root.mainloop()
