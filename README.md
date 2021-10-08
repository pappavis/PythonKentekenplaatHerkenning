Herken een auto kenteken met Python, OpenCV

# Stappenplan & benodigheden
Je benodig een Raspberry Pi, maar ook Windows is goed.
De instructies gelden voor Raspberry Pi en MacOS, voor de beeld moet je een desktopomgeving opstarten.

## Stap 1: Maakeen python virtual environment
Login op jouw Pi als gebruiker pi. 
Deze instructies werken ook op Windows & Mac.

```bash
pi@raspberrypi: $ pip3 install virtualenv
pi@raspberrypi: $ ~/.local/bin/virtualenv ~/venv
pi@raspberrypi: $ source ~/venv/bin/activate
```

Installeren diverse bibliotheken
```bash
pi@raspberrypi: $ sudo apt install -y python3-pip
pi@raspberrypi: $ sudo apt install -y libjpeg-dev zlib1g-dev libfreetype6-dev liblcms1-dev libopenjp2-7 libtiff5 python3-pip
```

Installeer python bibliotheken
```bash
pi@raspberrypi: (venv)$ pip install numpy imutils pytesseract opencv-python pillow
```

## Stap 2: Clone deze repo
Voor je deze code uitvoer moet je dit ook clone!

```bash
pi@raspberrypi: (venv)$ git clone https://github.com/pappavis/PythonKentekenplaatHerkenning
```


## Stap 3: Python kentekenplaat herkenning
Probeer een output

```bash
pi@raspberrypi: (venv)$ cd PythonKentekenplaatHerkenning
pi@raspberrypi: (venv)$ python ./kentekenherkenning1.py
```

<img src="https://github.com/pappavis/KentekenplaatHerkenning/blob/main/voorbeeld_20210817140540-kentekenherkennen.jpg" width="40%" height="40%">

# CREDITS
Zie origineel <a href="https://circuitdigest.com/microcontroller-projects/license-plate-recognition-using-raspberry-pi-and-opencv">hier</a>

