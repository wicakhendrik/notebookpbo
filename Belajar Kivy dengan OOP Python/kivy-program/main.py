#If on Windows to avoid fullscreen, use the following two lines of code
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.uix.slider import Slider
from kivy.core.audio import SoundLoader

from os import listdir, path

Builder.load_file("layout.kv")

class ChooseFile(FloatLayout):
    select = ObjectProperty(None)
    cancel = ObjectProperty(None)

class MusicPlayer(Widget):

    songs = [] #List to hold songs from music directory
    directory = '' #location of songs folder
    nowPlaying = '' #Song that is currently playing
    volume = 0
    maxvolume = NumericProperty(1.0)
    
    def getpath(self):
        try:
            f = open("sav.dat","r")
            self.ids.direct.text = str(f.readline())
            f.close()
            self.ids.searchBtn.text = "Scan"
            self.getSongs()
        except:
            self.ids.direct.text = ''
            
    def savepath(self, path):
        f = open("sav.dat","w")
        f.write(path)
        f.close()

    def dismiss_popup(self):
        self._popup.dismiss()

    def fileSelect(self):
        content = ChooseFile(select=self.select,
                             cancel=self.dismiss_popup)
        
        self._popup = Popup(title="Select Folder", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def select(self, path):
        self.directory = path
        self.ids.direct.text = self.directory
        self.ids.searchBtn.text = "Scan"
        self.savepath(self.directory)
        self.getSongs()
        self.dismiss_popup()
                        
    def getSongs(self):

        self.directory = self.ids.direct.text #Directory entered by the user

        if self.directory == '':
            self.fileSelect()

        #To make sure that the directory ends with a '/'
        if not self.directory.endswith('/'):
            self.directory += '/'

        #Check if directory exists
        if not path.exists(self.directory):
            self.ids.status.text = 'Folder Not Found'
            self.ids.status.color = (1,0,0,1)

        else:

            self.ids.status.text = ''

            self.ids.scroll.bind(minimum_height=self.ids.scroll.setter('height'))

            #get mp3 files from directory
            for fil in listdir(self.directory):
                if fil.endswith('.mp3'):
                    self.songs.append(fil)
                if fil.endswith('.ogg'):
                    self.songs.append(fil)
                if fil.endswith('.m4a'):
                    self.songs.append(fil)

            #If there are no mp3 files in the chosen directory
            if self.songs == [] and self.directory != '':
                self.ids.status.text = 'No Music Found'
                self.ids.status.color = (1,0,0,1)
                    
            self.songs.sort()
            
            for song in self.songs:
                if song.endswith('.mp3'):
                    def playSong(bt):
                        try:
                            self.nowPlaying.stop()
                        except:
                            pass
                        finally:
                            self.nowPlaying = SoundLoader.load(self.directory+bt.text+'.mp3')
                            self.nowPlaying.play()
                            self.nowPlaying.volume = self.volume
                            self.ids.nowplay.text = bt.text
                if song.endswith('.ogg'):
                    def playSong(bt):
                        try:
                            self.nowPlaying.stop()
                        except:
                            pass
                        finally:
                            self.nowPlaying = SoundLoader.load(self.directory+bt.text+'.ogg')
                            self.nowPlaying.play()
                            self.nowPlaying.volume = self.volume
                            self.ids.nowplay.text = bt.text
                if song.endswith('.m4a'):
                    def playSong(bt):
                        try:
                            self.nowPlaying.stop()
                        except:
                            pass
                        finally:
                            self.nowPlaying = SoundLoader.load(self.directory+bt.text+'.m4a')
                            self.nowPlaying.play()
                            self.nowPlaying.volume = self.volume
                            self.ids.nowplay.text = bt.text

                btn = Button(text=song[:-4], on_press=playSong)
                icon = Button(size_hint_x=None, width=40, background_down="ico.png", background_normal="ico.png")

                #Color Buttons Alternatively
                if self.songs.index(song)%2 == 0:
                    btn.background_color=(0.78039215686, 0.1725490196, 0.25490196078, 1)
                else:
                    btn.background_color=(0.93333333333, 0.27058823529, 0.25098039215, 1)
                    
                self.ids.scroll.add_widget(icon) #Add icon to layout
                self.ids.scroll.add_widget(btn) #Add btn to layout

    def volumectrl(self, *args):
        self.volume = int(args[1]) / 100
        if self.volume >= int(self.maxvolume):
            self.volume = int(self.maxvolume)
        self.nowPlaying.volume = self.volume
        
    def pause(self):
        if self.ids.pause.state == "down":
            if self.nowPlaying == "":
                pass
            else:
                self.position = self.nowPlaying.get_pos()
                self.nowPlaying.stop()
                
    def play(self):
        if self.ids.play.state == "down":
            if self.nowPlaying == "":
                pass
            if self.nowPlaying.state == "stop":
                self.nowPlaying.play()
                self.nowPlaying.volume = self.volume
                self.nowPlaying.seek(self.position - 1)
            if self.nowPlaying.state =="play":
                pass
            
class KiPyMusicApp(App):
    
    def build(self):
        music = MusicPlayer()
        music.getpath()
        return music
        
if __name__ == "__main__":
    KiPyMusicApp().run()
