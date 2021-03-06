Herken een auto kenteken met Python, OpenCV

# Stappenplan & benodigheden
Je benodig een Raspberry Pi, maar ook Windows is goed.
De instructies gelden voor Raspberry Pi en MacOS, voor de beeld moet je een desktopomgeving opstarten.

## Stap 1: Maak een python virtual environment
Login op jouw Pi als gebruiker pi. 
Deze instructies werken ook op Windows & Mac.

Stap 1. Installeren diverse bibliotheken
```bash
(venv) pi@raspberrypi: $ sudo apt install -y libjpeg-dev zlib1g-dev libfreetype6-dev liblcms1-dev libopenjp2-7 libtiff5 python3-pip
```

## Stap 2. OpenCV voorbereiden
```bash
pi@raspberrypi: $ sudo apt install -y python-is-python3 python3-pip python3-opencv 
pi@raspberrypi: $ python3 -m pip install virtualenv
pi@raspberrypi: $ mkdir ~/venv/
pi@raspberrypi: $ python3 -m virtualenv ~/venv/venv
pi@raspberrypi: $ source ~/venv/venv/bin/activate
```

## Stap 3. Installeer python bibliotheken
```bash
(venv) pi@raspberrypi:$ pip install --upgrade pytesseract numpy imutils opencv-python pillow pytesseract scikit-image
```

## Stap 4: Clone deze repo
Voor je deze code uitvoer moet je dit ook clone!

```bash
(venv) pi@raspberrypi:$ git clone https://github.com/pappavis/PythonKentekenplaatHerkenning
```


## Stap 5: Python kentekenplaat herkenning
Probeer een output

<img src="./assets/minicooper1.jpg" width="40%" height="40%">

```bash
(venv) pi@raspberrypi:$ cd PythonKentekenplaatHerkenning
(venv) pi@raspberrypi:$ python ./kentekenherkenning1.py
De herkende kenteken is: IHR 26 BR 9044
```

# Experimenteel
 - <a href="./kentekenherkenningANPR.py" title="experimenteer" target="_blank">kentekenherkenningANPR.py</a> heeft commandline interface.
 - <a href="./meterTemplateMatch01.py" target="_blank">meterTemplateMatch01.py</a> probeert middels template een kenteken en/of elektrameter waarde uitlezen.

# Opmerkingen
 - In het map "assets" staat veel testdata. De enige goede is <a href="./assets/minicooper1.jpg" target="_blank">minicooper1.jpg</a>, de overige herkent hij nauwelijks/niet.

# CREDITS
Zie origineel <a href="https://circuitdigest.com/microcontroller-projects/license-plate-recognition-using-raspberry-pi-and-opencv">hier</a>

