Herken een auto kenteken met Python, OpenCV

# Stappenplan & benodigheden
Je benodig een Raspberry Pi, maar ook Windows is goed.
De instructies gelden voor Raspberry Pi en MacOS, voor de beeld moet je een desktopomgeving opstarten.

## Stap 1: installeren bibliotheken
Login op jouw Pi als gebruiker pi.

```bash
pi@raspberrypi: $ sudo apt install -y libjpeg-dev zlib1g-dev libfreetype6-dev liblcms1-dev libopenjp2-7 libtiff5 python3-pip
pi@raspberrypi: $ pip3 install virtualenv
pi@raspberrypi: $ virtualenv ~/venv
pi@raspberrypi: $ source ~/venv/bin/activate
pi@raspberrypi: (venv)$ pip install numpy imutils pytesseract opencv-python pillow
pi@raspberrypi: (venv)$ https://github.com/pappavis/PythonKentekenplaatHerkenning
```

## Stap 2: Python kentekenplaat herkenning
Probeer een output

```bash
pi@raspberrypi: (venv)$ cd PythonKentekenplaatHerkenning
pi@raspberrypi: (venv)$ python ./kentekenherkenning1.py
```

<img src="https://github.com/pappavis/KentekenplaatHerkenning/blob/main/voorbeeld_20210817140540-kentekenherkennen.jpg" width="40%" height="40%">

# CREDITS
Zie origineel <a href="https://circuitdigest.com/microcontroller-projects/license-plate-recognition-using-raspberry-pi-and-opencv">hier</a>

