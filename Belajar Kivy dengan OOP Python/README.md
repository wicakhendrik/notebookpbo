# Belajar Kivy dengan OOP Python
<img src="../img/kivy.png" align="right" />

Kivy adalah library Python untuk membuat aplikasi untuk berbagai platform. Kivy bisa dijalankan pada Windows, Linux, OS X, Android, iOS, dan Raspberry Pi.

Untuk memulai belajar Kivy dengan Menggunakan OOP Python, kita harus menginstall library Kivy terlebih dahulu.

## Instalasi Kivy
Untuk menginstall Kivy, kita harus mempersiapkan Python versi 2.7 atau 3.4 keatas, karena Kivy hanya tersedia pada beberapa versi Python tersebut.

### Instalasi pada Windows
- Dengan menggunakan paket manager [pip](https://pip.pypa.io/en/stable/) untuk menginstall Kivy.
- Buka Command Prompt (CMD) Windows sebagai administrator.
- Pastikan anda menginstall pip dan wheel versi terbaru
```bash
python -m pip install --upgrade pip wheel setuptools
```
- Kemudian install dependencies
```bash
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
```
- untuk python 3.5 keatas, anda juga bisa menginstall angle
```bash
python -m pip install kivy.deps.angle
```
- kemudian install kivy
```bash
python -m pip install kivy
```
- kemudian install kivy examples(contoh program kivy)(opsional) untuk memastikan kivy sudah terinstall dengan baik.
```bash
python -m pip install kivy_examples
```
