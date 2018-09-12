######################################
# PlayList
# Morgan Hill
# 10/17/16
# A PlayList GUI that allows for users
# to enter, edit, and save playlists.
######################################

from tkinter import *
from tkinter import messagebox
from Song import Song
from tkinter import font

class GuiTesting:

    def __init__(self, master):
        self.master = master
        master.title('Gui PlayList Prototype')

        self.customFont = font.Font(family="Courier", size=9)

        self.tLabel = Label(master, text='Title', background='pink', padx=18, font=self.customFont)
        self.tLabel.grid(row=0, column=0, columnspan=1)
        self.text = Text(master, height=1, background='pink')
        self.text.grid(row=0, column=1, columnspan=2)
        self.aLabel = Label(master, text='Artist', background='pink', padx=14, font=self.customFont)
        self.aLabel.grid(row=1, column=0, columnspan=1)
        self.artist = Text(master, height=1, background='pink')
        self.artist.grid(row=1, column=1, columnspan=2)
        self.gLabel = Label(master, text='Genre', background='pink', padx=18, font=self.customFont)
        self.gLabel.grid(row=2, column=0, columnspan=1)
        self.genre = Text(master, height=1, background='pink')
        self.genre.grid(row=2, column=1, columnspan=2)
        self.tiLabel = Label(master, text='Time', background='pink', padx=21, font=self.customFont)
        self.tiLabel.grid(row=3, column=0, columnspan=1)
        self.time = Text(master, height=1, background='pink')
        self.time.grid(row=3, column=1, columnspan=2)

        self.greeter = Button(master, text='Add', command=self.greet, background='palevioletred')
        self.greeter.grid(row=0, column=3, rowspan=2)
        self.update = Button(master, text='Update', command=self.up, background='palevioletred')
        self.update.config(state=DISABLED)
        self.update.grid(row=2, column=3, rowspan=2)

        #self.scroll = Scrollbar(master)
        #self.scroll.pack(side=RIGHT, fill=Y)


        self.sortT = Button(master,text='Sort by Title',command=self.sortTitle, background='palevioletred')
        self.sortT.grid(row=6, column=0)

        self.sortA = Button(master, text='Sort by Artist', command=self.sortArtist, background='palevioletred')
        self.sortA.grid(row=6, column=1, columnspan=2)

        self.sortG = Button(master, text='Sort by Genre', command=self.sortGenre, background='palevioletred')
        self.sortG.grid(row=6, column=2)

        self.label2 = Label(master, text='Your PlayList', background='pink')
        self.label2.grid(row=6, column=0, columnspan=2)

        self.liststuff = Listbox(master,  selectmode=MULTIPLE, background='orchid') #yscrollcommand=self.scroll.set,
        self.liststuff.grid(row=7, column=0, rowspan = 4, columnspan = 4, sticky=N+E+S+W)
        self.liststuff.config(font=self.customFont)
        self.listcount = 0

        self.closerer = Button(master, text='Delete', command=self.deletin, background='palevioletred')
        self.closerer.grid(row=7, column=3)

        self.swapper = Button(master, text='Swap', command=self.swap, background='palevioletred')
        self.swapper.grid(row=8, column=3)

        self.editer = Button(master, text='Edit', command=self.edit, background='palevioletred')
        self.editer.grid(row=9, column=3)

        self.saver = Button(master, text='Save', command=self.save, background='palevioletred')
        self.saver.grid(row=10, column=3)


        self.label3 = Label(master, text='All Songs', background='pink')
        self.label3.grid(row=12, column=0, columnspan=2)

        self.fulllist = Listbox(master, selectmode=MULTIPLE, background='orchid')
        self.fulllist.grid(row=13, column=0, rowspan = 10, columnspan = 4, sticky=N+E+S+W)
        self.fulllist.config(font=self.customFont)
        self.greeter2 = Button(master, text='Add', command=self.greet, background='palevioletred')
        self.greeter2.grid(row=14, column=3, rowspan=4)
        self.filllist()

        #self.scroll.config(command=self.liststuff.yview())

        #notes::::
        #Frame, Toplevel, Canvas, Text, Button, Label, Message, Scrollbar,
        #Checkbutton, Radiobutton, Listbox, Entry, Scale, Menu, Menubutton
        #
        #read only labels: text.config(state=DISABLED) vs. state=NORMAL

        self.text.focus()


    def filllist(self):
        f = open('songData')
        song = None
        stri = f.readline()
        self.fulllistcount = 0
        while stri != '':
            song = Song(stri)
            if stri != '':
                self.fulllist.insert(self.fulllistcount, song)
                self.fulllistcount += 1
            stri = f.readline()
        result = messagebox.askyesno('Would you like to continue on your last playlist')
        if result:
            self.reloadSaved()

    def reloadSaved(self):
        f = open('playlistData')
        song = None
        stri = f.readline()
        self.listcount = 0
        while stri != '':
            print(stri == '')
            song = Song(stri)
            if stri != '':
                self.liststuff.insert(self.listcount, song)
                self.listcount += 1
            stri = f.readline()


    def greet(self):
        notInList = True
        if self.text.get(1.0) != '\n':
            self.fulllist.select_clear(0,END)
            tempSong = Song(self.text.get(1.0,END).split('\n')[0] +','+ self.artist.get(1.0,END).split('\n')[0] +','+ self.genre.get(1.0,END).split('\n')[0] +','+ self.time.get(1.0,END))
            for i in range(0, len(self.liststuff.get(0,END))):
                if (tempSong.__str__().strip() == self.liststuff.get(i).__str__().strip()) | (tempSong.toString().strip() == self.liststuff.get(i).__str__().strip()):
                    notInList = False
            if notInList:
                self.liststuff.insert(self.listcount, tempSong)
                self.fulllist.insert(self.fulllistcount, tempSong)
                self.listcount += 1
                self.fulllistcount += 1
                self.text.delete(1.0, END)
                self.artist.delete(1.0, END)
                self.genre.delete(1.0, END)
                self.time.delete(1.0, END)
            else:
                messagebox.showinfo('Duplicate','You already have this song!')
                self.text.delete(1.0, END)
                self.artist.delete(1.0, END)
                self.genre.delete(1.0, END)
                self.time.delete(1.0, END)
        elif len(self.fulllist.curselection()) != 0:
            for i in range(len(self.fulllist.curselection())-1,-1,-1):
                notInList = True
                tempSong1 = Song(self.fulllist.get(self.fulllist.curselection()[i]))
                for j in range(0, len(self.liststuff.get(0, END))):
                    if (tempSong1.__str__().strip() == self.liststuff.get(j).__str__().strip()) | (tempSong1.toString().strip() == self.liststuff.get(i).__str__().strip()):
                        messagebox.showinfo('Duplicate','{} {}'.format('You already have the song',((Song)(self.liststuff.get(j))).title))
                        notInList = False
                if notInList:
                    self.liststuff.insert(self.listcount, tempSong1)
                    self.listcount += 1
        else:
            messagebox.showinfo('No input detected','Please enter a song in the text box')
        self.fulllist.select_clear(0,END)

    def deletin(self):
        if len(self.liststuff.curselection()) == 0:
            messagebox.showinfo('No selection detected','No song selected. Please select the song(s) you wish to remove')
        else:
            for i in range(len(self.liststuff.curselection())-1,-1,-1):
                self.liststuff.delete(self.liststuff.curselection()[i])
        self.fulllist.select_clear(0, END)

    def swap(self):
        if len(self.liststuff.curselection()) == 0:
            messagebox.showinfo('No song selected','No song selected. Please choose the songs to swap')
        elif len(self.liststuff.curselection()) != 2:
            messagebox.showinfo('{}{} {}'.format('',len(self.liststuff.curselection()),'song(s) chosen'),'Please only choose two songs.')
        else:
            fnum = self.liststuff.curselection()[0]
            first = self.liststuff.get(fnum)
            tnum = self.liststuff.curselection()[1]
            temp = self.liststuff.get(tnum)
            self.liststuff.delete(fnum)
            self.liststuff.insert(fnum,temp)
            self.liststuff.delete(tnum)
            self.liststuff.insert(tnum,first)
        self.fulllist.select_clear(0, END)

    def askquit(self):
        result = messagebox.askyesno('Save?', 'Would you like to save first?')
        if result:
            self.save()
            root.destroy()
        else:
            fil = open('songData', 'w')
            for i in range(0, len(self.fulllist.get(0, END))):
                fil.write(((Song)(self.fulllist.get(i))).toString() + '\n')
            root.destroy() #opening and edit
    def save(self):
        # r = read only, w = write only, a = append,  r+ = read and write
        fi = open('playlistData', 'w')
        for i in range(0, len(self.liststuff.get(0, END))):
            strin = ((Song)(self.liststuff.get(i))).toString() + '\n'
            fi.write(strin)
        fil = open('songData', 'w')
        for i in range(0, len(self.fulllist.get(0,END))):
            stri = ((Song)(self.fulllist.get(i))).toString() + '\n'
            fil.write(stri)

    def sortTitle(self):
        arr = []
        for i in range(0,len(self.liststuff.get(0,END))):
            nextS = (Song)(self.liststuff.get(i))
            arr.append(nextS)
        arr = sorted(arr,key=lambda song: song.title)
        for i in range(0, len(self.liststuff.get(0, END))):
            self.liststuff.delete(i)
            self.liststuff.insert(i,arr[i])

    def sortArtist(self):
        arr = []
        for i in range(0, len(self.liststuff.get(0, END))):
            nextS = (Song)(self.liststuff.get(i))
            arr.append(nextS)
        arr = sorted(arr, key=lambda song: song.artist)
        for i in range(0, len(self.liststuff.get(0, END))):
            self.liststuff.delete(i)
            self.liststuff.insert(i,arr[i])

    def sortGenre(self):
        arr = []
        for i in range(0, len(self.liststuff.get(0, END))):
            nextS = (Song)(self.liststuff.get(i))
            arr.append(nextS)
        arr = sorted(arr, key=lambda song: song.genre)
        for i in range(0, len(self.liststuff.get(0, END))):
            self.liststuff.delete(i)
            self.liststuff.insert(i,arr[i])

    def edit(self):
        if len(self.liststuff.curselection()) == 0:
            messagebox.showwarning('No Song Selected', 'Please select a song to edit')
        else:
            messagebox.showinfo('Song Edit Mode','Edit Song information and click update')
            self.text.insert(0.0,((Song)(self.liststuff.get(self.liststuff.curselection()))).title)
            self.artist.insert(0.0,((Song)(self.liststuff.get(self.liststuff.curselection()))).artist)
            self.genre.insert(0.0,((Song)(self.liststuff.get(self.liststuff.curselection()))).genre)
            self.time.insert(0.0,((Song)(self.liststuff.get(self.liststuff.curselection()))).length)
            self.update.config(state=NORMAL)

    def up(self):
        print('gotcha')
        song = Song(self.text.get(1.0,END).split('\n')[0] +','+ self.artist.get(1.0,END).split('\n')[0] +','+ self.genre.get(1.0,END).split('\n')[0] +','+ self.time.get(1.0,END))
        pos1 = self.liststuff.curselection()
        pos2 = -1
        print(self.liststuff.get(self.liststuff.curselection()))
        for i in range(0, len(self.fulllist.get(0,END))):
            if self.fulllist.get(i).strip() == self.liststuff.get(self.liststuff.curselection()).strip():
                pos2 = i
        self.liststuff.delete(self.liststuff.curselection())
        self.liststuff.insert(pos1,song)
        if pos2 == -1:
            print('we have a problem')
        else:
            self.fulllist.delete(pos2)
            self.fulllist.insert(pos2,song)
        self.update.config(state=DISABLED)
        self.text.delete(1.0,END)
        self.artist.delete(1.0, END)
        self.genre.delete(1.0, END)
        self.time.delete(1.0, END)

root = Tk()
root.config(background='purple')
gui = GuiTesting(root)
root.protocol("WM_DELETE_WINDOW", gui.askquit)
root.mainloop()