# INTRO
Numberplate recognition using Python, OpenCV

# Stappenplan
Dit vergemakkelijk jouw leven op een Pi

## Stap 1: installeren Pete Scargill script
Login op jouw Pi als gebruiker pi.

```bash
pi@rpasberrypi: $ sudo pip install -y libjpeg-dev zlib1g-dev libfreetype6-dev liblcms1-dev libopenjp2-7 libtiff5
pi@rpasberrypi: $ pip install virtualenv
pi@rpasberrypi: $ virtualenv ~/venv
pi@rpasberrypi: $ source ~/venv/bin/activate
pi@rpasberrypi: (venv)$ pip install numpy imutils pytesseract opencv-python pillow
pi@rpasberrypi: (venv)$ git clone https://github.com/pappavis/KentekenplaatHerkenning
pi@rpasberrypi: (venv)$ cd KentekenplaatHerkenning
```

## Stap 2: Python kentekenplaat herkenning
Probeer een output

```bash
pi@rpasberrypi: (venv)$ python ./KentekenplaatHerkenning.py
```

# origineel
Zie origineel <a href="https://bitbucket.org/api/2.0/snippets/scargill/kAR5qG/master/files/script.sh">hier</a>

