from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import *
from random import *
import sys 
import codecs
import random


app = QApplication([])

############################################ Chicky Page

win = QWidget()
win.setWindowTitle("chicky page")
win.setMaximumSize(600, 400)
win.setMinimumSize(601, 401)

te1 = QTextEdit()
kaydet_buton = QPushButton("Kaydet")

cik = QLabel("•>•")
cik.setAlignment(Qt.AlignCenter)
cik.setStyleSheet("font-size: 200px; font-weight: bold; color: orange;")
win.setStyleSheet("background-color: #fff600;")

layout = QVBoxLayout()
layout.addWidget(cik)
layout.addWidget(te1)
layout.addWidget(kaydet_buton)
win.setLayout(layout)
te1.hide()
kaydet_buton.hide()

win.setWindowIcon(QIcon("cik.png"))
win.show()

############################################ Chicky Control



windik = QWidget()
windik.setWindowTitle("chicky control")
windik.setMaximumSize(600, 700)
windik.setMinimumSize(601, 701)



# kapat tuşu
def buton_tiklandi():
    win.close()
    windik.close()

p1 = QPushButton("kapat")
p1.setMaximumSize(60,30)
p1.clicked.connect(buton_tiklandi)

# isim kutusu 

te2 = QTextEdit("chicky page")
te2.setAlignment(Qt.AlignCenter)
te2.setMaximumSize(500,30)
win.setWindowTitle(te2.toPlainText())



# renk seçimi

gb1 = QGroupBox("görünüm")  
gl1 = QVBoxLayout()  

r1 = QRadioButton("sarı/turuncu")
r2 = QRadioButton("kırmızı/turuncu")
r3 = QRadioButton("mavi/mavi(açık)")
r4 = QRadioButton("yeşil/pembe")
r5 = QRadioButton("RCB/RCB")



def renk_degistir():
    if r1.isChecked():
        win.setStyleSheet("background-color: #fff600;")
        cik.setStyleSheet("font-size: 200px; font-weight: bold; color: orange;")
    elif r2.isChecked():
        win.setStyleSheet("background-color: #ff0000;")
        cik.setStyleSheet("font-size: 200px; font-weight: bold; color: #15ff00;")
    elif r3.isChecked():
        win.setStyleSheet("background-color: #000dff;")
        cik.setStyleSheet("font-size: 200px; font-weight: bold; color: #00d9ff;")
    elif r4.isChecked():
        win.setStyleSheet("background-color: #11ff00;")
        cik.setStyleSheet("font-size: 200px; font-weight: bold; color: #ea00ff;")
    elif r5.isChecked():
        rastgele_renk = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        rastgele_yazi_renk = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        win.setStyleSheet(f"background-color: {rastgele_renk};")
        cik.setStyleSheet(f"font-size: 200px; font-weight: bold; color: {rastgele_yazi_renk};")

def brrr () :
    if r5.isChecked():
        rastgele_renk = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        rastgele_yazi_renk = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        win.setStyleSheet(f"background-color: {rastgele_renk};")
        cik.setStyleSheet(f"font-size: 200px; font-weight: bold; color: {rastgele_yazi_renk};")
        a()
def a():
    QTimer.singleShot(250 , brrr)




r1.toggled.connect(renk_degistir)
r2.toggled.connect(renk_degistir)
r3.toggled.connect(renk_degistir)
r4.toggled.connect(renk_degistir)
r5.toggled.connect(renk_degistir and a)

gl1.addWidget(r1)
gl1.addWidget(r2)
gl1.addWidget(r3)
gl1.addWidget(r4)
gl1.addWidget(r5)
gb1.setLayout(gl1)  

# mod lar 2tene

gb2 = QGroupBox("mod")  
gl2 = QVBoxLayout()   


ra1 = QRadioButton("normal")
ra2 = QRadioButton("not kitabı")


def mod_seç():
    if ra1.isChecked():
        win.setMaximumSize(600, 400)
        win.setMinimumSize(601, 401)
        win.resize(600 , 401)
        te1.hide()
        kaydet_buton.hide()
    elif ra2.isChecked():
        win.setMaximumSize(600, 700)
        win.setMinimumSize(601, 701)
        win.resize(600, 701)
        te1.show()
        kaydet_buton.show()



ra1.toggled.connect(mod_seç)
ra2.toggled.connect(mod_seç)

gl2.addWidget(ra1)
gl2.addWidget(ra2)
gb2.setLayout(gl2)

def baslangic_yazdir():
    try:
        with codecs.open("a.txt", "r", "utf-8") as file:
            te1.setText(file.read())  
    except FileNotFoundError:
        te1.setText("Buraya notunuzu yazabilirsiniz...") 
baslangic_yazdir()

def kaydet():
    with codecs.open("a.txt", "w", "utf-8") as file:
        file.write(te1.toPlainText())


#################################################################################### sonu 

kaydet_buton.clicked.connect(kaydet)
te2.textChanged.connect(lambda: win.setWindowTitle(te2.toPlainText()))

h_layout = QHBoxLayout()
layout2 = QVBoxLayout()
layout2.addWidget(gb1)
layout2.addWidget(gb2)
h_layout.addWidget(te2)
h_layout.addWidget(p1)
layout2.addLayout(h_layout)


windik.setLayout(layout2)

windik.setWindowIcon(QIcon("çark.png"))
windik.show()
windik.showMinimized()

app.exec()