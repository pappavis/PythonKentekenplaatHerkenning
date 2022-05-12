Herken een auto kenteken met Python, OpenCV

# Stappenplan & benodigheden
Je benodig een Raspberry Pi, maar ook Windows is goed.
De instructies gelden voor Raspberry Pi en MacOS, voor de beeld moet je een desktopomgeving opstarten.

## Stap 1: Maak een python virtual environment
Login op jouw Pi als gebruiker pi. 
Deze instructies werken ook op Windows & Mac.

```bash
pi@raspberrypi: $ sudo apt install -y python-is-python3
pi@raspberrypi: $ python3 -m pip install virtualenv
pi@raspberrypi: $ source ~/venv/bin/activate
(venv) pi@raspberrypi: $ python -m pip install pipx
```

Installeren diverse bibliotheken
```bash
(venv) pi@raspberrypi: $ sudo apt install -y python3-pip python3-opencv
(venv) pi@raspberrypi: $ sudo apt install -y libjpeg-dev zlib1g-dev libfreetype6-dev liblcms1-dev libopenjp2-7 libtiff5 python3-pip
```

Installeer python bibliotheken
```bash
(venv) pi@raspberrypi:$ pipx install pytesseract
(venv) pi@raspberrypi:$ pip install --upgrade numpy imutils pytesseract opencv-python pillow
```

## Stap 2: Clone deze repo
Voor je deze code uitvoer moet je dit ook clone!

```bash
(venv) pi@raspberrypi:$ git clone https://github.com/pappavis/PythonKentekenplaatHerkenning
```


## Stap 3: Python kentekenplaat herkenning
Probeer een output

```bash
(venv) pi@raspberrypi:$ cd PythonKentekenplaatHerkenning
(venv) pi@raspberrypi:$ python ./kentekenherkenning1.py
```

<img src="https://github.com/pappavis/KentekenplaatHerkenning/blob/main/voorbeeld_20210817140540-kentekenherkennen.jpg" width="40%" height="40%">

# CREDITS
Zie origineel <a href="https://circuitdigest.com/microcontroller-projects/license-plate-recognition-using-raspberry-pi-and-opencv">hier</a>

