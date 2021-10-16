#last
import ctypes
import datetime
import os
import os.path
import shutil
import socket
import subprocess
import sys
import tkinter
import zipfile
from distutils.spawn import find_executable
from os import environ, listdir, path
from os.path import isdir, isfile, join
from tkinter import filedialog

try:
    import qtmodern.windows as Modern
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
except ImportError:
    os.system("pip install PyQt5")
    os.system("pip install qtmodern")
    abool = True


try:
    import doctext as dockon
    import requests
except ImportError:
    os.system("pip install docx-text")
    os.system("pip install requests")
    abool = True


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


def download(url, pathh):
    with open(pathh, "wb") as f:
        response = requests.get(url, stream=True)
        total = response.headers.get("content-length")

        if total is None:
            f.write(response.content)


def czas():
    now_time = datetime.datetime.now()
    current_time = now_time.strftime("%H-%M-%S")
    return current_time


def changelog(co):
    ch = open(f"{sciezka}/mods-backup/logs/latest.txt", "a")
    ch.write(f"\n[{czas()}]  {co}")
    ch.close()


def java_ver():
    java_version = subprocess.check_output(
        ["java", "-version"], stderr=subprocess.STDOUT
    )
    return java_version


def pliki(var):
    global i
    if path.exists(f"C:/Users/{user}/AppData/Roaming/.minecraft") == False:
        os.mkdir(f"C:/Users/{user}/AppData/Roaming/.minecraft")
    if path.exists(f"{sciezka}/mods-backup") == False:
        os.mkdir(f"{sciezka}/mods-backup")
    if path.exists(f"{sciezka}/mods-backup/version/") == False:
        os.mkdir(f"{sciezka}/mods-backup/version/")
    if path.exists(f"{sciezka}/mods-backup/logs/") == False:
        os.mkdir(f"{sciezka}/mods-backup/logs/")
    if var == 1:
        if path.exists(f"{sciezka}/mods-backup/logs") == False:
            os.mkdir(f"{sciezka}/mods-backup/logs")
        else:
            if path.exists(f"{sciezka}/mods-backup/logs") == False:
                os.mkdir(f"{sciezka}/mods-backup/logs")
            if (
                path.exists(f"{sciezka}/mods-backup/logs/changelog-{now_date}-9.txt")
                == True
            ):
                os.remove(f"{sciezka}/mods-backup/logs/changelog-{now_date}-9.txt")
            if (
                path.exists(f"{sciezka}/mods-backup/logs/changelog-{now_date}.txt")
                == True
            ):
                while (
                    path.exists(
                        f"{sciezka}/mods-backup/logs/changelog-{now_date}-{i}.txt"
                    )
                    == True
                ):
                    i = i + 1
            else:
                if path.exists(f"{sciezka}/mods-backup/logs/latest.txt") == True:
                    os.rename(
                        f"{sciezka}/mods-backup/logs/latest.txt",
                        f"{sciezka}/mods-backup/logs/changelog-{now_date}.txt",
                    )
                else:
                    f = open(f"{sciezka}/mods-backup/logs/latest.txt", "w")
                    f.close()


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        global qtRectangle
        self.setFixedSize(650, 630)
        self.Inicjacja()
        self.setStyleSheet(
            "QMainWindow{background-color: "
            + f"#{background_color_hex};"
            + "border: 3px solid ;"
            + "border-top-color: #b071da;"
            + "border-left-color: #71bbda;"
            + "border-right-color: #a4df6d;"
            + "border-bottom-color: #d0a080;}"
        )
        self.setWindowTitle(f"Ugułem jest ZAYEBIŚCIE v{wersja}")
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText(f"")
        self.label.move(175, 460)
        self.label.resize(300, 50)
        self.label.setStyleSheet(background_default)
        self.label.setFont(QFont(font, 15))
        self.label.hide()

        # * hidden
        self.serv = QtWidgets.QPushButton(self)
        self.serv.setText(f"")
        self.serv.resize(90, 40)
        self.serv.setStyleSheet(background_button)
        self.serv.setFont(QFont("{font}", 20))
        self.serv.hide()

        # * wersja
        self.wersje = QtWidgets.QPushButton(self)
        self.wersje.setText(f"v{wersja}")
        self.wersje.move(580, 580)
        self.wersje.resize(50, 25)
        self.wersje.setStyleSheet(f"background-color: #800080;")
        self.wersje.setFont(QFont("{font}", 15))

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.move(175, 35)
        self.b1.resize(300, 50)
        self.b1.setStyleSheet(background_button)
        self.b1.setFont(QFont(font, 15))

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.move(175, 120)
        self.b2.resize(300, 50)
        self.b2.setStyleSheet(background_button)
        self.b2.setFont(QFont(font, 15))

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.move(175, 205)
        self.b3.resize(300, 50)
        self.b3.setStyleSheet(background_button)
        self.b3.setFont(QFont(font, 15))

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.move(175, 290)
        self.b4.resize(300, 50)
        self.b4.setStyleSheet(background_button)
        self.b4.setFont(QFont(font, 15))

        self.b5 = QtWidgets.QPushButton(self)
        self.b5.move(175, 375)
        self.b5.resize(300, 50)
        self.b5.setStyleSheet(background_button)
        self.b5.setFont(QFont(font, 15))

        self.b6 = QtWidgets.QPushButton(self)
        self.b6.move(175, 460)
        self.b6.resize(300, 50)
        self.b6.setStyleSheet(background_button)
        self.b6.setFont(QFont(font, 15))
        self.b6.hide()

        self.b7 = QtWidgets.QPushButton(self)
        self.b7.move(175, 545)
        self.b7.resize(300, 50)
        self.b7.setStyleSheet(background_button)
        self.b7.setFont(QFont(font, 15))
        self.b7.hide()

        self.tak = QtWidgets.QPushButton(self)
        self.tak.move(125, 155)
        self.tak.resize(100, 50)
        self.tak.setText("Tak")
        self.tak.setStyleSheet(background_button)
        self.tak.setFont(QFont(font, 15))
        self.tak.hide()

        self.nie = QtWidgets.QPushButton(self)
        self.nie.move(425, 155)
        self.nie.resize(100, 50)
        self.nie.setText("Nigdy")
        self.nie.setStyleSheet(background_button)
        self.nie.setFont(QFont(font, 15))
        self.nie.hide()

        self.pytaj = QtWidgets.QPushButton(self)
        self.pytaj.move(275, 155)
        self.pytaj.resize(100, 50)
        self.pytaj.setText("Pytaj")
        self.pytaj.setStyleSheet(background_button)
        self.pytaj.setFont(QFont(font, 15))
        self.pytaj.hide()

        self.msg = QMessageBox(self)
        self.msg.move(10, 10)
        self.msg.setGeometry(835, 415, 200, 200)
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Okno ZAYEBIŚCIE")
        self.msg.setStyleSheet(f"background-color: white")

        self.labelpro = QtWidgets.QLabel(self)
        self.labelpro.setText(f"")

        self.labelpro.move(85, 125)
        self.labelpro.resize(50, 50)
        self.labelpro.setStyleSheet(background_default)
        self.labelpro.setFont(QFont(font, 15))

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(85, 175, 480, 50)

        self.labelpro2 = QtWidgets.QLabel(self)
        self.labelpro2.setText(f"")
        self.labelpro2.move(85, 280)
        self.labelpro2.resize(50, 50)
        self.labelpro2.setStyleSheet(background_default)
        self.labelpro2.setFont(QFont(font, 15))

        self.progressBar2 = QProgressBar(self)
        self.progressBar2.setGeometry(85, 325, 480, 50)

        self.bsha = QtWidgets.QPushButton(self)
        self.bsha.move(510, 10)
        self.bsha.resize(130, 50)
        self.bsha.setText("Pokaż listę")
        self.bsha.setStyleSheet(background_button)
        self.bsha.setFont(QFont(font, 15))
        self.bsha.hide()

        self.bsha2 = QtWidgets.QPushButton(self)
        self.bsha2.move(510, 70)
        self.bsha2.resize(130, 50)
        self.bsha2.setText("Usuń shadery")
        self.bsha2.setStyleSheet(background_button)
        self.bsha2.setFont(QFont(font, 15))
        self.bsha2.hide()

        self.lsha = QtWidgets.QLabel(self)
        self.lsha.move(110, 135)
        self.lsha.resize(425, 50)
        self.lsha.setText("")
        self.lsha.setStyleSheet(background_default)
        self.lsha.setFont(QFont(font, 15))
        self.lsha.hide()

        self.tsha = QLineEdit(self)
        self.tsha.move(220, 210)
        self.tsha.resize(205, 50)
        self.tsha.setStyleSheet(background_default)
        self.tsha.setFont(QFont(font, 20))
        self.tsha.hide()

        self.menu()

        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setText(
            "Mam dobrą i złą wiadomość.\n\nDobra - Inicjacja przeprowadzona pomyślnie.\n\nZła - Program nie działa.\n\nZakończono wsparcie programu, praktycznie żadne funkcje prócz usuwania modów nie działają\n\nMożliwe że ten przeobrazi się na inny podobnego typu lecz znacznie lepszy\n\n\n(work in progress)"
        )
        self.msg.exec_()
        self.msg.setIcon(QMessageBox.Information)

    def wersjee(self, funkcje):
        self.odlacz()

        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.b5.hide()

        self.b6.hide()
        self.b7.setText("Cofnij")
        self.b7.show()
        self.tak.hide()
        self.nie.hide()
        self.wersje.hide()
        self.pytaj.hide()

        self.progressBar.hide()
        self.progressBar2.hide()

        self.labelpro.hide()
        self.labelpro2.hide()

        self.serv.hide()

        self.labelinf = QtWidgets.QLabel(self)
        self.labelinf.setText(f" {wersja}")
        self.labelinf.move(295, 120)
        self.labelinf.resize(50, 50)
        self.labelinf.setStyleSheet(background_default)
        self.labelinf.setFont(QFont(font, 15))
        self.labelinf.show()

        self.labelinf2 = QtWidgets.QLabel(self)
        self.labelinf2.setText(f" Jest to wersja z dnia: ")
        self.labelinf2.move(215, 205)
        self.labelinf2.resize(215, 50)
        self.labelinf2.setStyleSheet(background_default)
        self.labelinf2.setFont(QFont(font, 15))
        self.labelinf2.show()

        self.labelinf3 = QtWidgets.QLabel(self)
        self.labelinf3.setText(f"{dzien}")
        self.labelinf3.move(260, 290)
        self.labelinf3.resize(115, 50)
        self.labelinf3.setStyleSheet(background_default)
        self.labelinf3.setFont(QFont(font, 15))
        self.labelinf3.show()

        self.b7.clicked.connect(lambda: self.infoprogram(funkcje))

        self.label.move(170, 35)
        self.label.resize(300, 50)
        self.label.setText(f" Aktualna wersja programu to: ")
        self.label.show()

    def infoprogram(self, funkcje):
        self.odlacz()
        self.labelinf.hide()
        self.labelinf2.hide()
        self.labelinf3.hide()
        self.label.hide()

        funkcje()

    def menu(self):
        self.label.setText(f"")

        self.b1.show()
        self.b2.show()
        self.b3.show()
        self.b4.show()
        self.b5.show()

        self.b6.hide()
        self.b7.hide()
        self.tak.hide()
        self.nie.hide()
        self.pytaj.hide()
        self.label.hide()

        self.progressBar.hide()
        self.progressBar2.hide()

        self.labelpro.hide()
        self.labelpro2.hide()

        self.wersje.show()

        self.serv.hide()

        self.odlacz()

        self.wersje.clicked.connect(lambda: self.wersjee(self.menu))

        self.b1.setText("Wersja Forge 1.16.5")
        self.b1.clicked.connect(lambda: self.wersjemcUI(1, 1))

        self.b2.setText("Wersja Forge 1.12.2")
        self.b2.clicked.connect(lambda: self.wersjemcUI(2, 1))

        self.b3.setText("Usuń wszystkie mody")
        self.b3.clicked.connect(self.usunmody)

        self.b4.setText("Ustawienia")
        self.b4.clicked.connect(self.ustawieniaUI)

        self.b5.setText("Wyjdź")
        self.b5.clicked.connect(self.wyjscie)

    def wersjemcUI(self, var, czy):
        if czy == 1:
            pass
        if path.exists(f"{sciezka}/mods") == True:
            if settings[2] == "P":
                if czy == 1:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText("Czy utworzyć kopię zapasową modów?")
                    msgBox.setWindowTitle("Okno ZAYEBIŚCIE")
                    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.No)
                    Tak = msgBox.button(QMessageBox.Ok)
                    Nie = msgBox.button(QMessageBox.No)
                    Tak.setText("Tak")
                    Nie.setText("Nie")

                    returnValue = msgBox.exec()
                    if returnValue == QMessageBox.Ok:
                        shutil.move(
                            f"{sciezka}/mods", f"{sciezka}/mods-backup/mods-{czas()}"
                        )
            elif settings[2] == "P":
                shutil.move(f"{sciezka}/mods", f"{sciezka}/mods-backup/mods-{czas()}")

        self.odlacz()

        self.b1.show()
        self.b2.show()
        self.b3.show()
        self.b4.show()
        self.b5.show()
        self.b6.show()
        self.b7.show()
        self.label.hide()
        self.progressBar.hide()
        self.progressBar2.hide()
        self.labelpro.hide()
        self.labelpro2.hide()

        self.bsha.hide()
        self.bsha2.hide()
        self.tsha.hide()
        self.lsha.hide()
        self.wersje.show()

        self.serv.show()
        self.serv.clicked.connect(lambda: self.serwerInit(var))

        if var == 1:
            self.serv.setText("1.16.5")
        else:
            self.serv.setText("1.12.2")

        self.serv.move(35, 35)
        self.serv.setFont(QFont(font, 20))
        self.serv.show()

        self.b1.setText("Pobieranie modów")
        self.b1.clicked.connect(lambda: self.modypobierz(var))

        self.b2.setText("Podmiana modów z backupa")
        self.b2.clicked.connect(lambda: self.Podmiana(var))

        self.b3.setText("Pobieranie modów opcjonalnych")
        self.b3.clicked.connect(lambda: self.opcj(var))

        self.b4.setText("Usuń mody opcjonalne")
        self.b4.clicked.connect(lambda: self.opcjusun(var))

        self.b5.setText("Info o modach")
        self.b5.clicked.connect(lambda: self.info(var))

        self.b6.setText("Więcej opcji")
        self.b6.clicked.connect(lambda: self.moreopc(var))

        self.b7.setText("Cofnij")
        self.b7.clicked.connect(self.menu)

        self.wersje.clicked.connect(
            lambda: self.wersjee(lambda: self.wersjemcUI(var, czy))
        )

    def moreopc(self, var):
        self.odlacz()
        self.b1.setText("Pobieranie shaderów")
        self.b1.clicked.connect(lambda: self.sha(var))

        self.b2.setText("Pobieranie texturpack'a")
        self.b2.clicked.connect(lambda: self.textur(var))

        self.b3.hide()
        self.b4.hide()
        self.b5.hide()
        self.b6.hide()
        self.label.hide()

        self.b7.setText("Cofnij")
        self.b7.clicked.connect(lambda: self.wersjemcUI(var, 0))
        self.wersje.clicked.connect(lambda: self.wersjee(lambda: self.moreopc(var)))

    def textur(self, var):
        self.odlacz()
        self.b1.hide()
        self.b2.hide()
        self.bsha.show()
        self.bsha2.show()
        self.tsha.show()
        self.lsha.show()
        self.label.hide()
        self.wersje.clicked.connect(lambda: self.wersjee(lambda: self.textur(var)))
        self.lsha.setText(" Wpisz wybrany numer i wciśnij Enter")
        self.b7.clicked.connect(lambda: self.moreopc(var))
        outputres = ""
        content = ""
        bufor = ""
        if var == 1:
            mod_jakie = listares[0]
        elif var == 2:
            mod_jakie = listares[1]
        if path.exists(f"{sciezka}/mods-backup/link") == False:
            os.mkdir(f"{sciezka}/mods-backup/link")
        line_count, content = self.kontent(mod_jakie, 1)
        self.progressBar2.hide()
        if line_count < 2 or line_count % 2 != 0:
            self.msg.setText(
                "Nie ma resourcepacka do pobrania, albo źle skonfigurowano listę!!!"
            )
            self.msg.setIcon(QMessageBox.Warning)
            returnValue = self.msg.exec_()
        else:
            for i in range(int(line_count / 2)):
                outputres += f"{i+1}. {content[i]}\n"
            self.texturinf(0, outputres)
            self.bsha.clicked.connect(lambda: self.shaders(0, outputres))
            self.bsha2.clicked.connect(lambda: self.shaders(1, outputres))

            self.tsha.returnPressed.connect(
                lambda: self.texturdownload(line_count, content)
            )

    def texturinf(self, var, outputres):
        self.msg.setIcon(QMessageBox.Information)
        if var == 0:
            self.msg.setText("Lista Texturpacków")
            self.msg.setDetailedText(outputres)
            returnValue = self.msg.exec_()
            self.msg.setDetailedText("")
        if var == 1:
            if path.exists(f"{sciezka}/resourcepacks") == True:
                shutil.rmtree(f"{sciezka}/resourcepacks")
                os.mkdir(f"{sciezka}/resourcepacks")
                self.msg.setText("Usunięto Texturpacki")
                returnValue = self.msg.exec_()

    def texturdownload(self, line_count, content):
        if path.exists(f"{sciezka}/resourcepacks") == False:
            os.mkdir(f"{sciezka}/resourcepacks")

        self.msg.setIcon(QMessageBox.Information)
        wybor = self.tsha.text()
        print(wybor)
        if wybor.isnumeric() == True:
            buforwyb = int(wybor)
            if buforwyb > int(line_count / 2) or buforwyb < 1:
                self.msg.setText("Nie ma resourcepacka o takim numerze")
                returnValue = self.msg.exec_()
                return 0
        else:
            self.msg.setText("Nie ma resourcepacka o takim numerze")
            returnValue = self.msg.exec_()
            return 0

        aaa = int(wybor) - 1
        ugule = content[aaa].replace(" ", "")
        bufor = int(int(wybor) + (line_count / 2))
        self.progressBar2.show()
        self.Downloader(content[bufor - 1], f"{sciezka}/resourcepacks/{ugule}", 2)

        if path.exists(f"{sciezka}/mods-backup/link") == True:
            shutil.rmtree(f"{sciezka}/mods-backup/link")

        self.msg.setText(f"Pomyślnie pobrano resourcepack '{content[aaa]}'")
        returnValue = self.msg.exec_()
        self.crystal(wybor)
        self.msg.setIcon(QMessageBox.Information)
        self.progressBar2.hide()

    def serwerInit(self, var):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(
            f"Skkrrrt. Pssst. Ugułem 2115, 2137 elo. Jak trafiłeś tu przez misclick kliknij Dalej"
        )
        msgBox.setWindowTitle("Okno ZAYEBIŚCIE")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.No)
        Tak = msgBox.button(QMessageBox.Ok)
        Nie = msgBox.button(QMessageBox.No)
        Tak.setText("Dalej")
        Nie.setText("Pusiak")
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.No:
            if var == 1:
                serwer = listaserv[0]
            elif var == 2:
                serwer = listaserv[1]
            if path.exists(f"{sciezka}/mods-backup/link") == False:
                os.mkdir(f"{sciezka}/mods-backup/link")
            line_count, content = self.kontent(serwer, 1)
            root = tkinter.Tk()
            root.withdraw()
            currdir = os.getcwd()
            sciezkaserw = filedialog.askdirectory(
                parent=root, initialdir=currdir, title="Wybierz proszę ścieżkę serwera"
            )
            if sciezkaserw == "":
                return 0
            self.msg.setText("Czekej chwile")
            self.msg.exec_()
            for filename in os.listdir(sciezkaserw):
                file_path = os.path.join(sciezkaserw, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception:
                    pass
            self.Downloader(content[0], f"{sciezkaserw}/serwer.zip", 0)
            with zipfile.ZipFile(f"{sciezkaserw}/serwer.zip", "r") as zip_ref:
                zip_ref.extractall(f"{sciezkaserw}/")
            if path.exists(f"{sciezkaserw}/serwer.zip") == True:
                os.remove(f"{sciezkaserw}/serwer.zip")
            if path.exists(f"{sciezkaserw}/server.properties") == True:
                os.remove(f"{sciezkaserw}/server.properties")
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            f = open(f"{sciezkaserw}/server.properties", "w")
            f.write(
                f"#Minecraft server properties\n#Wed Apr 14 19:05:16 CEST 2021\nallow-flight=true\nallow-nether=true\nbroadcast-console-to-ops=true\nbroadcast-rcon-to-ops=true\ndifficulty=3\nenable-command-block=false\nenable-jmx-monitoring=false\nenable-query=false\nenable-rcon=false\menable-status=true\menforce-whitelist=false\nentity-broadcast-range-percentage=100\nforce-gamemode=false\nfunction-permission-level=2\ngamemode=survival\ngenerate-structures=true\ngenerator-settings=\nhardcore=false\nlevel-name=world\nlevel-seed=1327282970654172467\nlevel-type=terraforged\nmax-build-height=256\nmax-players=20\nmax-tick-time=-1\nmax-world-size=29999984\nmotd=A Minecraft Server\nnetwork-compression-threshold=256\nonline-mode=false\nop-permission-level=4\nplayer-idle-timeout=0\nprevent-proxy-connections=false\npvp=true\nquery.port=25565\nrate-limit=0\nrcon.password=\nrcon.port=25575\nresource-pack=\nresource-pack-sha1=\nserver-ip={local_ip}\nserver-port=25565\nsnooper-enabled=true\nspawn-animals=true\nspawn-monsters=true\nspawn-npcs=true\nspawn-protection=0\nsync-chunk-writes=true\ntext-filtering-config=\nuse-native-transport=true\nview-distance=6\nwhite-list=false"
            )
            f.close()
            bufor = content[0]
            content.remove(bufor)
            if path.exists(f"{sciezkaserw}/mods") == False:
                os.mkdir(f"{sciezkaserw}/mods")
            for i in range(len(content)):
                print(content[i])
            for i in range(int(len(content) / 2)):
                self.Downloader(
                    content[int(i + (len(content) / 2))],
                    f"{sciezkaserw}/mods/{content[i]}",
                    0,
                )
            self.msg.setText("Kuniec")
            self.msg.exec_()
            return 0

    def shaders(self, var, outputshaders):
        self.msg.setIcon(QMessageBox.Information)
        if var == 0:
            self.msg.setText("Lista Shaderów")
            self.msg.setDetailedText(outputshaders)
            returnValue = self.msg.exec_()
            self.msg.setDetailedText("")
        if var == 1:
            if path.exists(f"{sciezka}/shaderpacks") == True:
                shutil.rmtree(f"{sciezka}/shaderpacks")
                os.mkdir(f"{sciezka}/shaderpacks")
                self.msg.setText("Usunięto shadery")
                returnValue = self.msg.exec_()

    def shadownload(self, line_count, content):
        self.msg.setIcon(QMessageBox.Information)
        wybor = self.tsha.text()
        if wybor.isnumeric() == True:
            buforwyb = int(wybor)
            if buforwyb > int(line_count / 2) or buforwyb < 1:
                self.msg.setText("Nie ma shadera o takim numerze")
                returnValue = self.msg.exec_()
                return 0
        else:
            self.msg.setText("Nie ma shadera o takim numerze")
            returnValue = self.msg.exec_()
            return 0

        aaa = int(wybor) - 1
        ugule = content[aaa].replace(" ", "")
        bufor = int(int(wybor) + (line_count / 2))
        self.progressBar2.show()
        self.Downloader(content[bufor - 1], f"{sciezka}/shaderpacks/{ugule}.zip", 2)

        with zipfile.ZipFile(f"{sciezka}/shaderpacks/{ugule}.zip", "r") as zip_ref:
            zip_ref.extractall(f"{sciezka}/shaderpacks/")
        if path.exists(f"{sciezka}/shaderpacks/{ugule}.zip") == True:
            os.remove(f"{sciezka}/shaderpacks/{ugule}.zip")
        if path.exists(f"{sciezka}/mods-backup/link") == True:
            shutil.rmtree(f"{sciezka}/mods-backup/link")

        self.msg.setText(f"Pomyślnie pobrano shader '{content[aaa]}'")
        returnValue = self.msg.exec_()
        self.crystal(wybor)
        self.msg.setIcon(QMessageBox.Information)
        self.progressBar2.hide()
        return 0

    def sha(self, wybor):
        self.odlacz()
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.b5.hide()
        self.b6.hide()
        self.label.hide()
        self.progressBar.hide()
        self.progressBar2.hide()
        self.labelpro.hide()
        self.labelpro2.hide()
        self.b7.clicked.connect(lambda: self.moreopc(wybor))
        self.bsha.show()
        self.bsha2.show()
        self.tsha.show()
        self.lsha.show()
        self.wersje.clicked.connect(lambda: self.wersjee(lambda: self.sha(wybor)))
        self.lsha.setText(" Wpisz wybrany numer shaderów i wciśnij Enter")

        if path.exists(f"{sciezka}/shaderpacks") == False:
            os.mkdir(f"{sciezka}/shaderpacks")
        outputshaders = ""
        if wybor == 1:
            mod_jakie = listasha[0]
        elif wybor == 2:
            mod_jakie = listasha[1]
        if path.exists(f"{sciezka}/mods-backup/link") == False:
            os.mkdir(f"{sciezka}/mods-backup/link")
        line_count, content = self.kontent(mod_jakie, 1)
        self.progressBar2.hide()
        if line_count < 2 or line_count % 2 != 0:
            self.msg.setText(
                "Nie ma modów do pobrania, albo źle skonfigurowano listę modów!!!"
            )
            self.msg.setIcon(QMessageBox.Warning)
            returnValue = self.msg.exec_()
        else:
            for i in range(int(line_count / 2)):
                outputshaders += f"{i+1}. {content[i]}\n"
            self.shaders(0, outputshaders)
            self.bsha.clicked.connect(lambda: self.shaders(0, outputshaders))
            self.bsha2.clicked.connect(lambda: self.shaders(1, outputshaders))

            self.tsha.returnPressed.connect(
                lambda: self.shadownload(line_count, content)
            )

    def info(self, wybor):
        if wybor == 1:
            wersjamc = "1.16.5"
        elif wybor == 2:
            wersjamc = "1.12.2"
        outputr = []
        outputopc = []
        outputsha = []
        onlyfiles = [
            f
            for f in listdir(f"{sciezka}/mods/")
            if isfile(join(f"{sciezka}/mods/", f))
        ]
        if path.exists(f"{sciezka}/mods-backup/link") == False:
            os.mkdir(f"{sciezka}/mods-backup/link")
        mod_jakie = [listar[wybor - 1], listaopc[wybor - 1], listasha[wybor - 1]]
        line_count, content = self.kontent(f"{mod_jakie[0]}", 1)

        line_count, contentt = self.kontent(f"{mod_jakie[1]}", 1)

        line_count, contenttt = self.kontent(f"{mod_jakie[2]}", 1)
        for i in range(int(len(content) / 2)):
            contentbuf = content[i]
            contentbuf = contentbuf.split("-")
            output = contentbuf[0]
            if len(output) < max_dlugosc:
                for j in range(max_dlugosc - len(output)):
                    output = output + " "
            if any(contentbuf[0] in s for s in onlyfiles) == True:
                outputr.append(f"\t{output}\t(Zainstalowane)")
            else:
                outputr.append(f"\t{output}\t(Niezainstalowane)")
        for i in range(int(len(contentt) / 2)):
            contentbuf = contentt[i]
            contentbuf = contentbuf.split("-")
            output = contentbuf[0]
            if len(output) < max_dlugosc:
                for j in range(max_dlugosc - len(output)):
                    output += " "
            if any(contentbuf[0] in s for s in onlyfiles) == True:
                outputopc.append(f"\t{output}\t(Zainstalowane)")
            else:
                outputopc.append(f"\t{output}\t(Niezainstalowane)")
        for i in range(int(len(contenttt) / 2)):
            contentbuf = contenttt[i]
            contentbuf = contentbuf.split("-")
            for i in range(len(contentbuf)):
                outputsha.append(contentbuf[i])
        if path.exists(f"{sciezka}/mods-backup/link") == True:
            shutil.rmtree(f"{sciezka}/mods-backup/link")

        outputmessage = f"Modyfikacje na wersję {wersjamc}\n\nMody wymagane:\n"
        for i in range(int(len(outputr))):
            outputmessage += f"\n{outputr[i]}"

        outputmessage += f"\n\nMody opcjonalne:"
        for i in range(int(len(outputopc))):
            outputmessage += f"\n{outputopc[i]}"

        outputmessage += f"\n\nShadery:\n"
        for i in range(int(len(outputsha))):
            outputmessage += f"\n\t{outputsha[i]}"

        self.msg.setText(
            f"Informacja na temat modów dostępna w rozpisce poniżej \u2193 \u2193 \u2193"
        )
        self.msg.setFont(QFont(font, 15))
        self.msg.setDetailedText(f"{outputmessage}")
        returnValue = self.msg.exec_()
        self.msg.setDetailedText("")

    def modypobierz(self, wybor):
        self.odlacz()
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.b5.hide()
        self.b6.hide()
        self.label.hide()
        self.progressBar.hide()
        self.progressBar2.hide()
        self.labelpro.hide()
        self.labelpro2.hide()
        self.wersje.clicked.connect(
            lambda: self.wersjee(lambda: self.modypobierz(wybor))
        )
        self.b7.clicked.connect(lambda: self.wersjemcUI(wybor, 0))
        jakie = 1
        self.modyjakie(jakie, wybor, 0)
        if path.exists(f"{sciezka}/mods-backup/mods_{wybor}") == True:
            shutil.rmtree(f"{sciezka}/mods-backup/mods_{wybor}")
            shutil.copytree(f"{sciezka}/mods", f"{sciezka}/mods-backup/mods_{wybor}")
            changelog(f"Przeniesiono mody do backupa {wybor}")
        else:
            shutil.copytree(f"{sciezka}/mods", f"{sciezka}/mods-backup/mods_{wybor}")
            changelog("Przeniesiono mody do backupa {wybor}")
        self.crystal(wybor)

    def opcjusun(self, wybor):
        self.odlacz()
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.b5.hide()
        self.b6.hide()
        self.label.hide()
        self.b7.clicked.connect(lambda: self.wersjemcUI(wybor, 0))
        jakie = 2
        self.modyjakie(jakie, wybor, 4)
        self.crystal(wybor)
        self.msg.setText("Usunięto mody opcjonalne")
        self.msg.adjustSize()
        returnValue = self.msg.exec_()

    def opcj(self, wybor):
        self.odlacz()
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.b5.hide()
        self.b6.hide()
        self.label.hide()
        self.b7.clicked.connect(lambda: self.wersjemcUI(wybor, 0))
        jakie = 2
        self.modyjakie(jakie, wybor, 3)
        self.crystal(wybor)

    def modyjakie(self, wybor, var, tryb):
        self.wersje.clicked.connect(
            lambda: self.wersjee(lambda: self.modyjakie(wybor, var, tryb))
        )

        if var == 1:
            if wybor == 1:
                link = listar[0]
                link2 = listaopc[0]
            elif wybor == 2:
                link = listaopc[0]
                link2 = listar[0]
        elif var == 2:
            if wybor == 1:
                link = listar[1]
                link2 = listaopc[1]
            elif wybor == 2:
                link = listaopc[1]
                link2 = listar[1]
        self.labelpro.show()
        self.labelpro2.show()
        niema.clear()
        self.b7.hide()
        self.serv.hide()
        self.wersje.hide()
        content = []
        content.clear()
        brakujace.clear()
        buforr = False
        changelog("Wywolano modyjakie()")
        if path.exists(f"{sciezka}/mods-backup/link") == False:
            os.mkdir(f"{sciezka}/mods-backup/link")
        changelog("Generowanie linku")
        line_count, content = self.kontent(link, 1)
        line_countt, contentt = self.kontent(link2, 1)
        if line_count < 2 or line_count % 2 != 0:
            self.msg.setText(
                "Nie ma modów do pobrania, albo źle skonfigurowano listę modów!!!"
            )
            self.msg.setIcon(QMessageBox.Warning)
            returnValue = self.msg.exec_()
            return 0
        else:
            if path.exists(f"{sciezka}/mods") == False:
                changelog(f"Utworzono C:/Users/{user}/AppData/Roaming/.minecraft/mods")
                os.mkdir(f"{sciezka}/mods")
            onlyfiles = [
                f
                for f in listdir(f"{sciezka}/mods/")
                if isfile(join(f"{sciezka}/mods/", f))
            ]
            onlydir = [
                f
                for f in listdir(f"{sciezka}/mods/")
                if isdir(join(f"{sciezka}/mods/", f))
            ]
            if path.exists(f"{sciezka}/mods-backup/bufor") == False:
                os.mkdir(f"{sciezka}/mods-backup/bufor")
            for i in range(len(onlydir)):
                shutil.move(
                    f"{sciezka}/mods/{onlydir[i]}",
                    f"{sciezka}/mods-backup/bufor/{onlydir[i]}",
                )
                buforr = True
            bufor = int(len(os.listdir(f"{sciezka}/mods")))
            a = False
            kurlaniewiem = []
            kurlaniewiemstr = ""

            if tryb == 0:
                for i in range(bufor):
                    if any(onlyfiles[i] in s for s in content) == False:
                        if any(onlyfiles[i] in s for s in contentt) == False:
                            a = True
                            kurlaniewiem.append(onlyfiles[i])
                            kurlaniewiemstr = kurlaniewiemstr + f"{onlyfiles[i]}\n"
            if a == True:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Question)
                msgBox.setText(
                    f"Wykryto niezgodne mody z dostępnymi opcjami  \n\nUSUNĄĆ JE?"
                )
                msgBox.setDetailedText(f"{kurlaniewiemstr}")
                msgBox.layout().addItem(
                    QSpacerItem(400, 0, QSizePolicy.Minimum, QSizePolicy.Expanding),
                    msgBox.layout().rowCount(),
                    0,
                    1,
                    msgBox.layout().columnCount(),
                )
                msgBox.setWindowTitle("Okno ZAYEBIŚCIE")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.No)
                Tak = msgBox.button(QMessageBox.Ok)
                Nie = msgBox.button(QMessageBox.No)
                Tak.setText("Tak")
                Nie.setText("Nie")
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    for i in range(len(kurlaniewiem)):
                        os.remove(f"{sciezka}/mods/{kurlaniewiem[i]}")

            for i in range(int(line_count / 2)):
                if path.exists(f"{sciezka}/mods/{content[i]}") == False:
                    if content[i] == paczkamodow:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Question)
                        msgBox.setText(
                            f"Jeden z modów, okazał się być paczką zip. Pobrać?"
                        )
                        msgBox.setWindowTitle("Okno ZAYEBIŚCIE")
                        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.No)
                        Tak = msgBox.button(QMessageBox.Ok)
                        Nie = msgBox.button(QMessageBox.No)
                        Tak.setText("Tak")
                        Nie.setText("Nie")
                        returnValue = msgBox.exec()
                        if returnValue == QMessageBox.Ok:
                            niema.append(paczkamodow)
                            brakujace.append(content[i + int(line_count / 2)])
                    else:
                        niema.append(content[i])
                        brakujace.append(content[i + int(line_count / 2)])
            if tryb <= 3:
                kur = False
                if len(niema) != 0:
                    ab = 100 / int(len(niema))
                self.labelpro.show()
                self.labelpro.resize(65, 35)
                self.labelpro2.resize(250, 35)
                self.progressBar.show()
                self.progressBar2.show()
                for i in range(len(niema)):
                    self.labelpro.setText(f"{i}/{len(niema)}")
                    self.progressBar.setValue(int(ab * i + 1))
                    if niema[i] == paczkamodow:
                        self.Downloader(brakujace[i], f"{sciezka}/{paczkamodow}.zip", 1)
                        with zipfile.ZipFile(
                            f"{sciezka}/{paczkamodow}.zip", "r"
                        ) as zip_ref:
                            zip_ref.extractall(f"{sciezka}/")
                        if path.exists(f"{sciezka}/{paczkamodow}.zip") == True:
                            os.remove(f"{sciezka}/{paczkamodow}.zip")
                    else:
                        self.Downloader(brakujace[i], f"{sciezka}/mods/{niema[i]}", 1)
                    changelog(f"Pobieranie {brakujace[i]}")
                    kur = True
                if kur == True:
                    self.labelpro.setText(f"{len(niema)}/{len(niema)}")
                    self.progressBar.setValue(int(ab * int(len(niema))))
            if buforr == True:
                for i in range(len(onlydir)):
                    shutil.move(
                        f"{sciezka}/mods-backup/bufor/{onlydir[i]}",
                        f"{sciezka}/mods/{onlydir[i]}",
                    )
            shutil.rmtree(f"{sciezka}/mods-backup/bufor")
            if path.exists(f"{sciezka}/mods-backup/link") == True:
                shutil.rmtree(f"{sciezka}/mods-backup/link")
            if tryb == 4:
                for i in range(len(onlyfiles)):
                    if (
                        any(onlyfiles[i] in s for s in content) == True
                        and any(onlyfiles[i] in s for s in contentt) == False
                    ):
                        os.remove(f"{sciezka}/mods/{onlyfiles[i]}")
            else:
                self.msg.setText("Pomyślnie pobrano")
                returnValue = self.msg.exec_()
            self.wersjemcUI(var, 0)

    def Podmiana(self, wybor):
        if path.exists(f"{sciezka}/mods-backup/mods_{wybor}") == True:
            if path.exists(f"{sciezka}/mods") == True:
                shutil.rmtree(f"{sciezka}/mods")
            shutil.copytree(f"{sciezka}/mods-backup/mods_{wybor}", f"{sciezka}/mods")
            changelog(f"Przeniesiono mody z backupa {wybor}")
            self.msg.setText("Pomyślnie przeniesiono z backupa")
            returnValue = self.msg.exec_()
        else:
            self.msg.setText(
                "Nie można przywrocic backupa ponieważ nigdy go uwcześniej nie pobrano"
            )
            self.msg.adjustSize()
            returnValue = self.msg.exec_()
        self.crystal(wybor)

    def crystal(self, wybor):
        if wybor == 1:
            ver = "1.16.5"
        elif wybor == 2:
            ver = "1.12.2"
        crystalbool = False
        sciezkaa = f"C:/Users/{user}/AppData/Roaming/Crystal-Launcher"
        if path.exists(f"{sciezkaa}") == True:
            changelog(f"Wykryto Crystala")
            if settings[3] == "P":
                if path.exists(f"{sciezka}/mods") == True:
                    if settings[3] == "P":
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Information)
                        msgBox.setText(
                            "Wykryto instancję Crystal-Launcher, przenieść mody?"
                        )
                        msgBox.setWindowTitle("Okno ZAYEBIŚCIE")
                        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.No)
                        Tak = msgBox.button(QMessageBox.Ok)
                        Nie = msgBox.button(QMessageBox.No)
                        Tak.setText("Tak")
                        Nie.setText("Nie")
                        returnValue = msgBox.exec()
                        if returnValue == QMessageBox.Ok:
                            self.msg.setText(
                                "Proszę poczekać, może to trochę potrwać. Może to wygląć jakby program się scrashował, ale ugułem to gunwo prawda"
                            )
                            returnValue = self.msg.exec()
                            crystalbool = True
                    elif settings[3] == "T":
                        crystalbool = True
                    if crystalbool == True:
                        if path.exists(f"{sciezkaa}/instances") == False:
                            os.mkdir(f"{sciezkaa}/instances")
                        if path.exists(f"{sciezkaa}/instances/u.Forge-{ver}") == False:
                            os.mkdir(f"{sciezkaa}/instances/u.Forge-{ver}")
                        if (
                            path.exists(
                                f"{sciezkaa}/instances/u.Forge-{ver}/.minecraft"
                            )
                            == True
                        ):
                            shutil.rmtree(
                                f"{sciezkaa}/instances/u.Forge-{ver}/.minecraft"
                            )
                        shutil.copytree(
                            f"{sciezka}",
                            f"{sciezkaa}/instances/u.Forge-{ver}/.minecraft",
                        )
                        f = open(f"{sciezkaa}/instances/u.Forge-{ver}/.fmlversion", "w")
                        f.write("1.16.5-36.1.2")
                        f = open(
                            f"{sciezkaa}/instances/u.Forge-{ver}/fml_installed.ini", "w"
                        )
                        f.write("1.16.5-36.1.2")
                        changelog(f"Przeniesiono mody do Crystala")
                    if settings[3] == "P" and crystalbool == True:
                        self.msg.setText("Przeniesiono mody do Crystal-Launcher")
                        returnValue = self.msg.exec()

    def ustawieniaUI(self):
        self.odlacz()
        self.label.setText(f"")
        self.b1.show()
        self.b2.show()
        self.b3.show()
        self.b4.show()
        self.b5.show()
        self.b6.hide()
        self.b7.hide()
        self.label.hide()
        self.tak.hide()
        self.nie.hide()
        self.pytaj.hide()
        self.wersje.clicked.connect(lambda: self.wersjee(self.ustawieniaUI))
        self.b1.setText("Wybierz ścieżkę instalacji")
        self.b1.clicked.connect(lambda: self.ustawienia(0))

        self.b2.setText("Przywróć domyślną ścieżkę")
        self.b2.clicked.connect(lambda: self.ustawienia(1))

        self.b3.setText("Tworzenie kopii zapasowej")
        self.b3.clicked.connect(lambda: self.ustawienia(2))

        self.b4.setText("Crystal Launcher")
        self.b4.clicked.connect(lambda: self.ustawienia(3))

        self.b5.setText("Cofnij")
        self.b5.clicked.connect(self.menu)

    def ustawienia(self, var):
        self.wersje.clicked.connect(lambda: self.wersjee(lambda: self.ustawienia(var)))
        if var == 0:
            root = tkinter.Tk()
            root.withdraw()
            currdir = os.getcwd()
            sciezka = filedialog.askdirectory(
                parent=root, initialdir=currdir, title="Wybierz proszę ścieżkę serwera"
            )
            if sciezka != "":
                f = open(
                    f"C:/Users/{user}/AppData/Roaming/.minecraft/mods-backup/version/args.txt",
                    "w",
                )
                f.write(f"{wersja}\n{sciezka}\n{settings[2]}\n{settings[3]}")
                f.close()
                self.msg.setText(f"Ustawiono scieżkę {sciezka}")
                self.msg.adjustSize()
                returnValue = self.msg.exec_()
        elif var == 1:
            sciezka = f"C:/Users/{user}/AppData/Roaming/.minecraft"
            f = open(
                f"C:/Users/{user}/AppData/Roaming/.minecraft/mods-backup/version/args.txt",
                "w",
            )
            f.write(f"{wersja}\n{sciezka}\n{settings[2]}\n{settings[3]}")
            f.close()
            self.msg.setText("Przywrócono domyślną ścieżkę")
            self.msg.adjustSize()
            returnValue = self.msg.exec_()
        elif var == 2:
            self.odlacz()
            self.b1.hide()
            self.b2.hide()
            self.b3.hide()
            self.b4.hide()
            self.b5.clicked.connect(self.ustawieniaUI)
            self.label.move(70, 35)
            self.label.resize(505, 90)
            self.label.show()
            self.label.setText(
                f" Czy tworzyć kopię zapasową modów automatycznie?\n Możesz znaleźć je w : \n %appdata%/.minecraft/mods-backup"
            )
            self.tak.show()
            self.nie.show()
            self.pytaj.show()
            self.tak.clicked.connect(lambda: self.kopia(1, 1))
            self.pytaj.clicked.connect(lambda: self.kopia(1, 2))
            self.nie.clicked.connect(lambda: self.kopia(1, 3))
        elif var == 3:
            self.odlacz()
            self.b1.hide()
            self.b2.hide()
            self.b3.hide()
            self.b4.hide()
            self.label.show()
            self.b5.clicked.connect(self.ustawieniaUI)
            self.label.move(70, 35)
            self.label.resize(525, 50)
            self.label.setText(
                f" Czy przerzucać mody do Crystal-Launcher automatycznie?"
            )
            self.tak.show()
            self.nie.show()
            self.pytaj.show()
            self.tak.clicked.connect(lambda: self.kopia(2, 1))
            self.pytaj.clicked.connect(lambda: self.kopia(2, 2))
            self.nie.clicked.connect(lambda: self.kopia(2, 3))

    def kopia(self, tryb, var):
        if tryb == 1:
            if var == 1:
                settings[2] = "T"
            elif var == 2:
                settings[2] = "P"
            elif var == 3:
                settings[2] = "N"
        elif tryb == 2:
            if var == 1:
                settings[3] = "T"
            elif var == 2:
                settings[3] = "P"
            elif var == 3:
                settings[3] = "N"
        f = open(
            f"C:/Users/{user}/AppData/Roaming/.minecraft/mods-backup/version/args.txt",
            "w",
        )
        f.write(f"{wersja}\n{sciezka}\n{settings[2]}\n{settings[3]}")
        f.close()
        self.msg.setText("Pomyślnie ustawiono!")
        returnValue = self.msg.exec_()

    def wyjscie(self):
        exit()

    def usunmody(self):
        self.msg.setText("Usunięto")
        returnValue = self.msg.exec_()
        user = os.getlogin()
        sciezka = f"C:/Users/{user}/AppData/Roaming/.minecraft"
        if path.exists(f"{sciezka}/mods") == True:
            shutil.rmtree(f"{sciezka}/mods")
            os.mkdir(f"{sciezka}/mods")
        if path.exists(f"C:/Users/{user}/AppData/Roaming/Crystal-Launcher") == True:
            if (
                path.exists(
                    f"C:/Users/{user}/AppData/Roaming/Crystal-Launcher/instances/u.Forge-1.16.5"
                )
                == True
            ):
                shutil.rmtree(
                    f"C:/Users/{user}/AppData/Roaming/Crystal-Launcher/instances/u.Forge-1.16.5"
                )
                os.mkdir(
                    f"C:/Users/{user}/AppData/Roaming/Crystal-Launcher/instances/u.Forge-1.16.5"
                )
            if (
                path.exists(
                    f"C:/Users/{user}/AppData/Roaming/Crystal-Launcher/instances/u.Forge-1.12.2"
                )
                == True
            ):
                shutil.rmtree(
                    f"C:/Users/{user}/AppData/Roaming/Crystal-Launcher/instances/u.Forge-1.12.2"
                )
                os.mkdir(
                    f"C:/Users/{user}/AppData/Roaming/Crystal-Launcher/instances/u.Forge-1.12.2"
                )

    def odlacz(self):
        try:
            self.b1.disconnect()
        except Exception:
            pass
        try:
            self.b2.disconnect()
        except Exception:
            pass
        try:
            self.b3.disconnect()
        except Exception:
            pass
        try:
            self.b4.disconnect()
        except Exception:
            pass
        try:
            self.b5.disconnect()
        except Exception:
            pass
        try:
            self.b6.disconnect()
        except Exception:
            pass
        try:
            self.b7.disconnect()
        except Exception:
            pass
        try:
            self.tak.disconnect()
        except Exception:
            pass
        try:
            self.nie.disconnect()
        except Exception:
            pass
        try:
            self.pytaj.disconnect()
        except Exception:
            pass
        try:
            self.bsha.disconnect()
        except Exception:
            pass
        try:
            self.bsha2.disconnect()
        except Exception:
            pass
        try:
            self.tsha.disconnect()
        except Exception:
            pass
        try:
            self.serv.disconnect()
        except Exception:
            pass
        try:
            self.wersje.disconnect()
        except Exception:
            pass

    def kontent(self, link, var):
        if var == 1:
            nazwadocx = f"lista.docx"
            nazwatxt = f"lista.txt"
            docxFile = f"{sciezka}/mods-backup/link/{nazwadocx}"
            txtFile = f"{sciezka}/mods-backup/link/{nazwatxt}"
            self.Downloader(link, docxFile, 0)
            doc_text = dockon.DocFile(doc=docxFile)
            doctext = doc_text.get_text()
            fdoc = open(f"{sciezka}/mods-backup/link/{nazwatxt}", "w")
            fdoc.write(doctext)
            fdoc.close()
        else:
            txtFile = link
        f = open(txtFile, "r")
        line_count = 0
        content = []
        for line in f:
            if line != "\n":
                line_count += 1
        with open(txtFile) as f:
            content = f.readlines()
            content = [x.strip() for x in content]
        if var == 1:
            for i in range(int(line_count) + 1):
                content.remove("")
        f.close()

        return line_count, content

    def Downloader(self, url, path_pliku, var):
        nazwa = str(path_pliku)
        nazwa = nazwa.replace(f"{sciezka}/", "")
        nazwa = nazwa.replace(f"mods/", "")
        nazwa = nazwa.replace(f"mods-backup/link/", "")
        nazwa = nazwa.replace(f"shaderpacks/", "")
        nazwa = nazwa.replace(f".zip", "")
        nazwa = nazwa.split("-")
        nazwa = nazwa[0]
        self.labelpro2.setText(f"{nazwa}")
        with open(path_pliku, "wb") as f:
            response = requests.get(url, stream=True)
            total_length = response.headers.get("content-length")

            if total_length is None:
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(100 * dl / total_length)
                    self.progressBar2.setValue(int(done))

    def forge(self, wybor):
        if wybor == 1:
            forge_sciezka = f"{temp}/forge-instalation-1.16.5"
            forge_url = "https://www.dropbox.com/s/dxb6y05ozgmq1u6/forge-installer-1.16.5.jar?dl=1"
        else:
            forge_sciezka = f"{temp}/forge-instalation-1.12.2"
            forge_url = "https://www.dropbox.com/s/qvet4nvptz8ie0i/forge-installer-1.12.2.jar?dl=1"
        if path.exists(forge_sciezka) == False:
            os.mkdir(forge_sciezka)
        self.Downloader(forge_url, f"{forge_sciezka}/forge-installer.jar", 1)
        sys.stdout.write("\n")
        changelog("Pobrano")
        changelog("Wypakowano forge'a")
        self.msg.setText("WYBIERZ INSTALCJĘ KLIENTA, SCIEŻKĘ I KLIKNIJ INSTALUJ!")
        self.msg.exec_()
        os.system(f"{forge_sciezka}/forge-installer.jar")
        changelog("Zainstalowano Forge")
        if path.exists("forge-installer.jar.log") == True:
            os.remove("forge-installer.jar.log")
        abool = True

    def java(self):
        if path.exists(f"{temp}/java-instalation") == False:
            os.mkdir(f"{temp}/java-instalation")
        self.Downloader(java_url, f"{temp}/java-instalation/java-installer.zip", 1)
        with zipfile.ZipFile(
            f"{temp}/java-instalation/java-installer.zip", "r"
        ) as zip_ref:
            zip_ref.extractall(f"{temp}/java-instalation/")
        changelog("Pobrano")
        changelog("Wypakowano jave")
        print("Wyodrębnianie pliku")
        print("Instalacja...")
        subprocess.call([f"{temp}/java-instalation/java-installer.exe"], shell=True)
        print("Pomyślnie zainstalowano")
        changelog("Zainstalowano Jave")
        return 1

    def Inicjacja(self):
        global sciezka
        global wersja
        global max_dlugosc
        global user
        global now_date
        global settings
        global niema
        global brakujace
        global listar
        global listaopc
        global listasha
        global listaserv
        global temp
        global java_url
        global background_button
        global background_color_hex
        global buforr
        global pobieranie
        global abool
        global paczkamodow
        global listares
        global font
        global background_default
        global dzien
        pobieranie = 0
        abool = False
        background_button_hex = "0d7377"
        background_color_hex = "323232"
        background_default = (
            f"background-color: #{background_button_hex};border: 1px solid #ead5c7;"
        )
        background_button = (
            "QPushButton{"
            + f"background-color: #{background_button_hex};border: 1px solid #ead5c7;"
            + "}"
            + "QPushButton::pressed{"
            + "background-color : #0b575b;}"
        )
        font = "OldEnglish"
        paczkamodow = "RLCraft"
        user = os.getlogin()
        sciezka = f"C:/Users/{user}/AppData/Roaming/.minecraft"
        listar, listaopc, listasha, listaserv, listares = [], [], [], [], []

        dzien = "26.04.2021"

        # ! listy [0]  - 1.16.5   [1] - 1.12.2

        listar = [
            "https://www.dropbox.com/scl/fi/s0xutxzqe6o8rfycd5tv5/lista.docx?dl=1&rlkey=ybf92si2patftxz6d7c2embna",
            "https://www.dropbox.com/scl/fi/w0kcaysox1f5k1koro5ll/lista.docx?dl=1&rlkey=h5ckij6g2wx60qf1rph2mtk9q",
        ]
        listaopc = [
            "https://www.dropbox.com/scl/fi/viv7t49jg156jl8mvuico/opcjonalne.docx?dl=1&rlkey=wixj5d4b2qt30iophtzbtuv8y",
            "https://www.dropbox.com/scl/fi/xq285ldk3hkomjbt0bq7g/opcjonalne.docx?dl=1&rlkey=wtt887lrrmbdktzjbqaerk6dn",
        ]
        listasha = [
            "https://www.dropbox.com/scl/fi/peeggsvw01v0sbr3a36bu/shadery-1.16.5.docx?dl=1&rlkey=zvnbb7mlp1d9mtdp73t5pytq8",
            "https://www.dropbox.com/scl/fi/sme4ts4rywcd92td3y6y4/shadery-1.12.2.docx?dl=1&rlkey=dvwn2ybrx9hqg0jttn8ibyadv",
        ]
        listaserv = [
            "https://www.dropbox.com/scl/fi/xpniq5bzvgpy7tbc3oy5d/lista.docx?dl=1&rlkey=pd34sxjgvuo8739ywt8iaygls",
            "https://www.dropbox.com/scl/fi/8iyvs7ne3aijs08ru73mv/lista.docx?dl=1&rlkey=qloh4g6a7ifmujz86rpvg14l3",
        ]
        listares = [
            "https://www.dropbox.com/scl/fi/m522qhd40qtqlc142s0ij/lista.docx?dl=1&rlkey=v5t6hnjza7jac9alismqbqhtx",
            "https://www.dropbox.com/scl/fi/m4oqtz1nzf5mz6gx25v1m/lista.docx?dl=1&rlkey=ul1vi7diqk85i96v0c8ezq1qq",
        ]
        pliki(0)
        if path.exists(f"{sciezka}/mods-backup/version/args.txt") == False:
            f = open(f"{sciezka}/mods-backup/version/args.txt", "w")
            f.write(f"C:/Users/{user}/AppData/Roaming/.minecraft\nP\nP")
            f.close()

        now_date = str(datetime.date.today())
        now_date = now_date.replace(":", ".")
        i, buforr = 1, False
        if path.exists(f"C:/Users/{user}/AppData/Roaming/.minecraft") == False:
            os.mkdir(f"C:/Users/{user}/AppData/Roaming/.minecraft")

        line_count, contentv = self.kontent(
            f"{sciezka}/mods-backup/version/version.txt", 0
        )
        wersja = contentv[0]
        line_countt, settings = self.kontent(
            f"{sciezka}/mods-backup/version/args.txt", 0
        )
        if line_countt < 4:
            f = open(
                f"C:/Users/{user}/AppData/Roaming/.minecraft/mods-backup/version/args.txt",
                "w",
            )
            f.write(f"{wersja}\nC:/Users/{user}/AppData/Roaming/.minecraft\nP\nP")
            f.close()
            for i in range(4 - line_countt):
                settings.append("")
            settings[0], settings[1], settings[2], settings[3] = (
                wersja,
                sciezka,
                "P",
                "P",
            )

        pliki(0)
        sciezka = settings[1]

        temp = f"C:/Users/{user}/AppData/Local/Temp"
        java_url = "https://www.dropbox.com/s/almafuv9vr4xch3/java-installer.zip?dl=1"
        niema = []
        brakujace = []
        max_dlugosc = 30

        now_date = str(datetime.date.today())
        now_date = now_date.replace(":", "-")

        ch = open(
            f"C:/Users/{user}/AppData/Roaming/.minecraft/mods-backup/logs/latest.txt",
            "a",
        )
        ch.write("----------------------------------------------")
        ch.write(f"\n[{czas()}]  Utworzono plik changelog")
        ch.write(f"\n[{czas()}]  Uruchamianie programu")
        ch.close()

    def check(self, wybor):
        global abool
        jar = str(find_executable("java"))
        if jar == "None":
            print("\nNie wykryto oprogramowania JAVA")
            print("Pobieranie...")
            changelog("Nie wykryto oprogramowania JAVA")
            self.java()
            shutil.rmtree(f"{temp}/java-instalation")
            print(f"Wersja oprogramowania JAVA to ")
            print(java_ver())
            changelog(f"Wykryto oprogramowania JAVA wersja {java_ver()}")
        else:
            print("\nPomyślnie wykryto oprogramowania JAVA")
            print(f"Wersja oprogramowania JAVA to ")
            changelog(f"Wykryto oprogramowania JAVA wersja {java_ver()}")
            print(java_ver())
        if wybor == 1:
            if path.exists(f"{sciezka}/versions/1.16.5-forge-36.2.2") == False:
                print("\nNie wykryto oprogramowania FORGE 1.16.5-forge-36.2.2")
                print("Pobieranie...")
                changelog("Nie wykryto oprogramowania FORGE")
                self.forge(wybor)
            else:
                print("\nPomyślnie wykryto oprogramowanie FORGE 1.16.5-forge-36.2.2")
                changelog("Wykryto oprogramowania Forge wersja: 1.16.5-forge-36.2.2")
        else:
            if path.exists(f"{sciezka}/versions/1.12.2-forge-14.23.5.2854") == False:
                print("\nNie wykryto oprogramowania FORGE")
                changelog("nie wykryto oprogramowania Forge")
                print("Pobieranie...")
                self.forge(wybor)
            else:
                print("\nPomyślnie wykryto oprogramowanie FORGE")
                print("Wersja FORGE to 1.12.2-forge-14.23.5.2854")
                changelog(
                    "Wykryto oprogramowania Forge wersja: 1.12.2-forge-14.23.5.2854"
                )
        if abool == True:
            exit()


if __name__ == "__main__":
    suppress_qt_warnings()
    app = QApplication(sys.argv)
    win = MyWindow()
    mw = Modern.ModernWindow(win)
    mw.move(qtRectangle.topLeft())
    mw.show()
    sys.exit(app.exec_())
