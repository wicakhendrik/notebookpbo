# Dokumentasi OOP KiPyMusicPlayer

<img src="../../img/doc-kivy1.png" align="center" />

## Global Variabel
+ Config.set('graphics', 'fullscreen', '0')

## Class and Method
### 1. Class ChooseFile
Kelas ini berfungsi untuk memilih direktori music yang ada di direktori file untuk dimasukkan ke dalam playlist. Kelas ini inheritance terhadap class **kivy.uix.floatlayout.FloatLayout**.
Di dalam kelas ini terdapat 2 attribut yaitu atribut:
+ **-select** :

Berfungsi untuk memilih direktori music yang dimaksud

+ **-cancel** :

Berfungsi untuk membatalkan perintah

### 2. Class MusicPlayer
Kelas ini berfungsi sebagai kelas utama/root. Kelas ini inheritance terhadap class kivy.uix.widget.Widget.
Di dalam kelas ini terdapat 5 attribut yaitu atribut:
+ **-songs** :

  Atribut ini berbentuk list, karena berfungsi untuk menampung lagu/musik yang akan dijalankan.

+ **-directory** :

  Atribut ini berfungsi untuk mendefinisikan direktori file yang sedang dipilih.

+ **-nowPlaying** :

  Atribut ini berfungsi untuk mendefinisikan musik yang sedang di jalankan saat ini.

+ **-volume** :

  Atribut ini berfungsi untuk mendefinisikan volume musik dengan default 0. 

+ **-maxvolume** :

  Atribut ini berfungsi untuk mendefinisikan maxsimum volume musik.

Di dalam kelas ini terdapat 9 method yaitu method:

+ **+getpath()**      :

  Method ini berfungsi untuk membuat file dat untuk menyimpan playlist lagu/musik yang akan diputar. 
  
+ **+savepath()**     :

  Method ini berfungsi untuk menyimpan playlist lagu/musik ke dalam file dat yang telah dibut di method getpath() tadi.
  
+ **+dismiss_popup()**  :

  Method ini agar tidak muncul popup
  
+ **+fileSelect()**     :

  Method ini berfungsi untuk memilih file directory musik yang akan dimasukkan ke dalam playlist dengan memanggil(inheritance) dari kelas ChooseFile.
  
+ **+select()**         :

  Method ini berfungsi untuk memilih file lagu/musik dari direktory yang sudah dipilih pada method fileSelect tadi.
  
+ **+getSongs()**       :

  Method ini berfungsi untuk memainkan lagu/musik yang sudah dipilih pada method select.
  
+ **+volumectrl()**     :

  Method ini berfungsi untuk mengatur volume lagu/musik
  
+ **+pause()**          :

  Method ini berfungsi untuk pause lagu/musik
  
+ **+play()**           :

  Method ini berfungsi untuk memainkan lagu/musik yang sedang di pause



### 3. Class KiPyMusic

Kelas ini berfungsi untuk menjalankan aplikasi/software. Di dalam kelas ini hanya terdapat 1 method, yaitu method **+build()** untuk menjalankan aplikasi/software KiPyMusic ini dengan memanggil dari class **MusicPlayer**. Kelas ini 
inheritance terhadap class **kivy.app.App**.






# About KiPyMusicPlayer
A music player application written in python-kivy.
#Things to do
* Find a good sound module to handle playing mp3, m4a, ogg
* Make GUI more attractive
source : https://github.com/JasonHinds13/KVMusicPlayer

