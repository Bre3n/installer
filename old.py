import datetime
import os
import os.path
import shutil
import subprocess
import sys
import time
import tkinter
import zipfile
from distutils.spawn import find_executable
from os import environ, listdir, path
from os.path import isdir, isfile, join
from tkinter import filedialog


def czas():
    now_time = datetime.datetime.now()
    current_time = now_time.strftime("%H-%M-%S")
    return current_time


def kontent(link, var):
    if var == 1:
        nazwadocx = f"lista.docx"
        nazwatxt = f"lista.txt"
        docxFile = f"{sciezka}/mods-backup/link/{nazwadocx}"
        txtFile = f"{sciezka}/mods-backup/link/{nazwatxt}"
        downloader(link, docxFile, 0)
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


def changelog(co):
    ch = open(f"{sciezka}/mods-backup/logs/latest.txt", "a")
    ch.write(f"\n[{czas()}]  {co}")
    ch.close()


def downloader(url: str, path: str, var):
    print("\n")
    if var == 1:
        changelog(f"Pobieranie z args({url}, {path})")
    else:
        changelog(f"Pobieranie linku z args({url}, {path})")
    if var == 1:
        name = str(path)
        name = name.replace(f"{sciezka}/mods/", "")
        name = name.replace(f".jar", "")
    elif var == 0:
        name = str(path)
        name = name.replace(f"{sciezka}/mods-backup/link/", "")
    elif var == 2:
        name = str(path)
        name = name.replace(f"{sciezka}/shaderpacks/", "")
        name = name.replace(f".zip", "")

    name = name.split("-")
    name = name[0]
    if len(name) < max_dlugosc:
        for i in range(max_dlugosc - len(name)):
            name = name + " "
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get("content-length", 0))
    with open(path, "wb") as file, tqdm(
        desc=f"{name}",
        total=total,
        unit="iB",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)
    if var == 1:
        changelog(f"Pobrano")
    else:
        changelog(f"Pobierano link")


def crystal(ver):
    sciezkaa = f"C:/Users/{user}/AppData/Roaming/Crystal-Launcher"
    if path.exists(f"{sciezkaa}") == True:
        changelog(f"Wykryto Crystala")
        if settings[3] == "P":
            aa = input(
                "\n\tWykryto instancję Crystal Launcher, chcesz dodać mody do paczki modów Crystal Launcher? (y/n)\n"
            )
            print("\n\n")
        elif settings[3] == "T":
            aa = "y"
        else:
            aa = "n"
        if aa == "y":
            print(
                f'Paczka modów będzie dostępna do wybrania w Crystal Launcher "Przeglądaj paczki" pod nazwą Forge-{ver}'
            )
            print("\nProszę chwilę poczekać")
            if path.exists(f"{sciezkaa}/instances") == False:
                os.mkdir(f"{sciezkaa}/instances")
            if path.exists(f"{sciezkaa}/instances/u.Forge-{ver}") == False:
                os.mkdir(f"{sciezkaa}/instances/u.Forge-{ver}")
            if path.exists(f"{sciezkaa}/instances/u.Forge-{ver}/.minecraft") == True:
                shutil.rmtree(f"{sciezkaa}/instances/u.Forge-{ver}/.minecraft")
            shutil.copytree(
                f"{sciezka}", f"{sciezkaa}/instances/u.Forge-{ver}/.minecraft"
            )
            f = open(f"{sciezkaa}/instances/u.Forge-{ver}/.fmlversion", "w")
            f.write("1.16.5-36.1.2")
            f = open(f"{sciezkaa}/instances/u.Forge-{ver}/fml_installed.ini", "w")
            f.write("1.16.5-36.1.2")
            print("\nUkończono przenoszenie modów do Crystal Launcher")
            changelog(f"Przeniesiono mody do Crystala")


def modyjakie(link, var, tryb):
    global buforr
    niema.clear()
    content = []
    content.clear()
    brakujace.clear()
    changelog("Wywolano modyjakie()")
    if path.exists(f"{sciezka}/mods-backup/link") == False:
        os.mkdir(f"{sciezka}/mods-backup/link")
    print("Generowanie linku")
    changelog("Generowanie linku")
    line_count, content = kontent(link, 1)
    if line_count < 2 or line_count % 2 != 0:
        print("\n\nNie ma modów do pobrania, albo źle skonfigurowano listę modów!!!")
        time.sleep(2)
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
            f for f in listdir(f"{sciezka}/mods/") if isdir(join(f"{sciezka}/mods/", f))
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
        wybor5 = "N"
        if tryb == 0:
            for i in range(bufor):
                if any(onlyfiles[i] in s for s in content) == False:
                    print(f"\t\n{onlyfiles[i]}")
                    a = True
            if a == True:
                wybor5 = input(
                    "\nWykryto inne mody niebędące w paczce wymaganych usunąć? (y/n) "
                )
                wybor5 = wybor5.upper()
        for i in range(bufor):
            if tryb == 0:
                if wybor5 == "Y":
                    if any(onlyfiles[i] in s for s in content) == False:
                        os.remove(f"{sciezka}/mods/{onlyfiles[i]}")
            elif tryb == 4:
                if any(onlyfiles[i] in s for s in content) == True:
                    os.remove(f"{sciezka}/mods/{onlyfiles[i]}")
        for i in range(int(line_count / 2)):
            if path.exists(f"{sciezka}/mods/{content[i]}") == False:
                niema.append(content[i])
                brakujace.append(content[i + int(line_count / 2)])
        if tryb <= 3:
            for i in range(len(niema)):
                downloader(brakujace[i], f"{sciezka}/mods/{niema[i]}", 1)
                changelog(f"Pobieranie {brakujace[i]}")
        if buforr == True:
            for i in range(len(onlydir)):
                shutil.move(
                    f"{sciezka}/mods-backup/bufor/{onlydir[i]}",
                    f"{sciezka}/mods/{onlydir[i]}",
                )
        shutil.rmtree(f"{sciezka}/mods-backup/bufor")
        if path.exists(f"{sciezka}/mods-backup/link") == True:
            shutil.rmtree(f"{sciezka}/mods-backup/link")


def mody(wybor):
    if wybor == 1:
        wersjamc = "1.16.5"
    elif wybor == 2:
        wersjamc = "1.12.2"
    changelog("Wywolano mody()")
    global kopia
    if wybor == 1:
        mod_jakie = listar[0]
        ver = "1.16.5"
    elif wybor == 2:
        mod_jakie = listar[1]
        ver = "1.12.2"
    if path.exists(f"{sciezka}/mods.zip") == True:
        os.remove(f"{sciezka}/mods.zip")
    if path.exists(f"{sciezka}/mods-backup") == False:
        os.mkdir(f"{sciezka}/mods-backup")
    if path.exists(f"{sciezka}/mods") == True:
        if settings[2] == "P":
            wybor4 = input(
                "\nWykonac backup istniejąych modów? Możesz je usunąć w .minecraft/mods-backup/ (y/n) "
            )
        elif settings[2] == "T":
            wybor4 = "y"
        else:
            wybor4 = "n"
        if wybor4 == "y":
            print(f"Tworzenie kopii zapasowej modów (mods-backup/mods-{czas()})")
            shutil.move(f"{sciezka}/mods", f"{sciezka}/mods-backup/mods-{czas()}")
    wybor2 = input(
        "1. Pobranie modów\n2. Podmiana plików z backupa\n3. Pobranie modów opcjonalnych\n4. Usuń mody opcjonalne\n5. Pobieranie shaderów\n6. Info o modach\n\n7. Cofnij\n"
    )
    if wybor2.isnumeric() == True:
        if int(wybor2) == 1:
            modyjakie(mod_jakie, wybor, 0)
            if path.exists(f"{sciezka}/mods-backup/mods_{wybor}") == True:
                shutil.rmtree(f"{sciezka}/mods-backup/mods_{wybor}")
                shutil.copytree(
                    f"{sciezka}/mods", f"{sciezka}/mods-backup/mods_{wybor}"
                )
                changelog(f"Przeniesiono mody do backupa {wybor}")
            else:
                shutil.copytree(
                    f"{sciezka}/mods", f"{sciezka}/mods-backup/mods_{wybor}"
                )
                changelog("Przeniesiono mody do backupa {wybor}")
            crystal(ver)
            a = input("\n\n\nWciśnij Enter aby zacząć ponownie...")
            if a == "":
                return 1
            else:
                return 0
        elif int(wybor2) == 2:
            if path.exists(f"{sciezka}/mods-backup/mods_{wybor}") == True:
                if path.exists(f"{sciezka}/mods") == True:
                    shutil.rmtree(f"{sciezka}/mods")
                shutil.copytree(
                    f"{sciezka}/mods-backup/mods_{wybor}", f"{sciezka}/mods"
                )
                changelog(f"Przeniesiono mody z backupa {wybor}")
            else:
                print("Nie można przywrocic backupa ponieważ nigdy nie pobrano modów")
                wybor3 = input("Czy chcesz pobrać mody (y/n) ")
                changelog("Nie ma backupa modow")
                if wybor3 == "y":
                    modyjakie(mod_jakie, wybor, 0)
                else:
                    return 0
            crystal(ver)
            a = input("\n\n\nWciśnij Enter aby zacząć ponownie...")
            if a == "":
                return 1
            else:
                return 0
        elif int(wybor2) == 3:
            if wybor == 1:
                mod_jakie = listaopc[0]
            elif wybor == 2:
                mod_jakie = listaopc[1]
            modyjakie(mod_jakie, wybor, 3)
            crystal(ver)
            a = input("\n\n\nWciśnij Enter aby zacząć ponownie...")
            if a == "":
                return 1
            else:
                return 0
        elif int(wybor2) == 4:
            if wybor == 1:
                mod_jakie = listaopc[0]
            elif wybor == 2:
                mod_jakie = listaopc[1]
            modyjakie(mod_jakie, wybor, 4)
            crystal(ver)
            a = input("\n\n\nWciśnij Enter aby zacząć ponownie...")
            if a == "":
                return 1
            else:
                return 0
        elif int(wybor2) == 5:
            if wybor == 1:
                mod_jakie = listasha[0]
            elif wybor == 2:
                mod_jakie = listasha[1]
            if path.exists(f"{sciezka}/mods-backup/link") == False:
                os.mkdir(f"{sciezka}/mods-backup/link")
            line_count, content = kontent(mod_jakie, 1)
            if line_count < 2 or line_count % 2 != 0:
                print(
                    "\n\nNie ma modów do pobrania, albo źle skonfigurowano listę modów!!!"
                )
                time.sleep(2)
                return 0
            else:
                for i in range(int(line_count / 2)):
                    print(f"{i+1}. {content[i]}")
                print(
                    '\nPodaj numery shaderow jakie chcesz pobrać (aby zakończyć wciśnij "n")'
                )
                wyborr6 = True
                wybor6 = []
                while wyborr6 == True:
                    buforwyb = input()
                    if buforwyb.isnumeric() == True:
                        buforwyb = int(buforwyb)
                        if buforwyb > int(line_count / 2) or buforwyb < 1:
                            print("Nie ma shadera o takim numerze")
                        else:
                            wybor6.append(buforwyb)
                    else:
                        wyborr6 = False
                if path.exists(f"{sciezka}/shaderpacks") == True:
                    shutil.rmtree(f"{sciezka}/shaderpacks")
                os.mkdir(f"{sciezka}/shaderpacks")
                for i in range(len(wybor6)):
                    aaa = wybor6[i] - 1
                    bufbuf = content[aaa].replace(" ", "")
                    downloader(
                        f"{content[aaa+int(line_count/2)]}",
                        f"{sciezka}/shaderpacks/{bufbuf}.zip",
                        2,
                    )
                    with zipfile.ZipFile(
                        f"{sciezka}/shaderpacks/{bufbuf}.zip", "r"
                    ) as zip_ref:
                        zip_ref.extractall(f"{sciezka}/shaderpacks/")
                    if path.exists(f"{sciezka}/shaderpacks/{bufbuf}.zip") == True:
                        os.remove(f"{sciezka}/shaderpacks/{bufbuf}.zip")
                if path.exists(f"{sciezka}/mods-backup/link") == True:
                    shutil.rmtree(f"{sciezka}/mods-backup/link")
            crystal(ver)
            a = input("\n\n\nWciśnij Enter aby zacząć ponownie...")
            if a == "":
                return 1
            else:
                return 0
        elif int(wybor2) == 6:
            onlyfiles = [
                f
                for f in listdir(f"{sciezka}/mods/")
                if isfile(join(f"{sciezka}/mods/", f))
            ]
            if path.exists(f"{sciezka}/mods-backup/link") == False:
                os.mkdir(f"{sciezka}/mods-backup/link")
            mod_jakie = [listar[wybor - 1], listaopc[wybor - 1], listasha[wybor - 1]]
            line_count, content = kontent(f"{mod_jakie[0]}", 1)

            line_count, contentt = kontent(f"{mod_jakie[1]}", 1)

            line_count, contenttt = kontent(f"{mod_jakie[2]}", 1)
            print(f"\n\nModyfikacje na wersję {wersjamc}")
            print("\n\nMody wymagane:\n")
            for i in range(int(len(content) / 2)):
                contentbuf = content[i]
                contentbuf = contentbuf.split("-")
                output = contentbuf[0]
                if len(contentbuf[0]) < max_dlugosc:
                    for j in range(max_dlugosc - len(contentbuf[0])):
                        output = output + " "
                if any(contentbuf[0] in s for s in onlyfiles) == True:
                    print(f"\t{output}\t(Zainstalowane)")
                else:
                    print(f"\t{output}\t(Niezainstalowane)")
            print("\n\nMody opcjonalne:\n")
            for i in range(int(len(contentt) / 2)):
                contentbuf = contentt[i]
                contentbuf = contentbuf.split("-")
                output = contentbuf[0]
                if len(contentbuf[0]) < max_dlugosc:
                    for j in range(max_dlugosc - len(contentbuf[0])):
                        output = output + " "
                if any(contentbuf[0] in s for s in onlyfiles) == True:
                    print(f"\t{output}\t(Zainstalowane)")
                else:
                    print(f"\t{output}\t(Niezainstalowane)")
            print("\n\nShadery:\n")
            for i in range(int(len(contenttt) / 2)):
                contentbuf = contenttt[i]
                contentbuf = contentbuf.split("-")
                print(f"\t{contentbuf[0]}")
            if path.exists(f"{sciezka}/mods-backup/link") == True:
                shutil.rmtree(f"{sciezka}/mods-backup/link")
            a = input("\n\n\nWciśnij Enter aby zacząć ponownie...")
            if a == "":
                return 1
            else:
                return 0
        elif int(wybor2) == 7:
            return 1
        else:
            print("\nNie ma takiego wyboru")
            time.sleep(1)
            mody(wybor)
    else:
        print("\nNie ma takiego wyboru!")
        time.sleep(1)
        mody(wybor)


def forge(wybor):
    if wybor == 1:
        forge_sciezka = f"{temp}/forge-instalation-1.16.5"
        forge_url = (
            "https://www.dropbox.com/s/98rbxhqqew6otz2/forge-installer-1.16.5.jar?dl=1"
        )
    else:
        forge_sciezka = f"{temp}/forge-instalation-1.12.2"
        forge_url = (
            "https://www.dropbox.com/s/qvet4nvptz8ie0i/forge-installer-1.12.2.jar?dl=1"
        )
    if path.exists(forge_sciezka) == False:
        os.mkdir(forge_sciezka)
    downloader(forge_url, f"{forge_sciezka}/forge-installer.jar", 1)
    sys.stdout.write("\n")
    changelog("Pobrano")
    changelog("Wypakowano forge'a")
    print("Wyodrębnianie pliku")
    print("Instalacja...")
    print("WYBIERZ INSTALCJĘ KLIENTA, SCIEŻKĘ I KLIKNIJ INSTALUJ!")
    os.system(f"{forge_sciezka}/forge-installer.jar")
    print("Pomyślnie zainstalowano")
    changelog("Zainstalowano Forge")
    if path.exists("forge-installer.jar.log") == True:
        os.remove("forge-installer.jar.log")
    global abool
    abool = True


def java():
    if path.exists(f"{temp}/java-instalation") == False:
        os.mkdir(f"{temp}/java-instalation")
    downloader(java_url, f"{temp}/java-instalation/java-installer.zip", 1)
    with zipfile.ZipFile(f"{temp}/java-instalation/java-installer.zip", "r") as zip_ref:
        zip_ref.extractall(f"{temp}/java-instalation/")
    changelog("Pobrano")
    changelog("Wypakowano jave")
    print("Wyodrębnianie pliku")
    print("Instalacja...")
    subprocess.call([f"{temp}/java-instalation/java-installer.exe"], shell=True)
    print("Pomyślnie zainstalowano")
    changelog("Zainstalowano Jave")
    return 1


def java_ver():
    java_version = subprocess.check_output(
        ["java", "-version"], stderr=subprocess.STDOUT
    )
    return java_version


def check(wybor):
    global a
    global abool
    jar = str(find_executable("java"))
    if abool == True:
        print("\nUruchom ponowinie instaler aby dokończyć instalacje")
        time.sleep(5)

        exit()
    if jar == "None":
        print("\nNie wykryto oprogramowania JAVA")
        print("Pobieranie...")
        changelog("Nie wykryto oprogramowania JAVA")
        a = java()
        shutil.rmtree(f"{temp}/java-instalation")
        print(f"Wersja oprogramowania JAVA to ")
        print(java_ver())
        changelog(f"Wykryto oprogramowania JAVA wersja {java_ver()}")
        time.sleep(1)
    else:
        print("\nPomyślnie wykryto oprogramowania JAVA")
        print(f"Wersja oprogramowania JAVA to ")
        changelog(f"Wykryto oprogramowania JAVA wersja {java_ver()}")
        print(java_ver())
    if wybor == 1:
        if path.exists(f"{sciezka}/versions/1.16.5-forge-36.0.48") == False:
            print("\nNie wykryto oprogramowania FORGE 1.16.5-forge-36.0.48")
            print("Pobieranie...")
            changelog("Nie wykryto oprogramowania FORGE")
            forge(wybor)
        else:
            print("\nPomyślnie wykryto oprogramowanie FORGE 1.16.5-forge-36.0.48")
            changelog("Wykryto oprogramowania Forge wersja: 1.16.5-forge-36.0.48")
    else:
        if path.exists(f"{sciezka}/versions/1.12.2-forge-14.23.5.2854") == False:
            print("\nNie wykryto oprogramowania FORGE")
            changelog("nie wykryto oprogramowania Forge")
            print("Pobieranie...")
            forge(wybor)
        else:
            print("\nPomyślnie wykryto oprogramowanie FORGE")
            print("Wersja FORGE to 1.12.2-forge-14.23.5.2854")
            changelog("Wykryto oprogramowania Forge wersja: 1.12.2-forge-14.23.5.2854")
    if abool == True:
        print("\nUruchom ponowinie instaler aby dokończyć instalacje")
        time.sleep(5)
        exit()


def main(wybor):
    changelog(f"Wybor wersji {wybor}")
    if wybor.isnumeric() == True:
        wybor = int(wybor)
        if wybor > 0 and wybor < 3:
            changelog("Wywolywanie check()")
            check(wybor)
            changelog("Wywolywanie mody()")
            a = mody(wybor)
            if a == 1:
                return 0
            if wybor == 1:
                print("\n\nWERSJA SERWERA 1.16.5")
            else:
                print("\n\nWERSJA SERWERA 1.12.2")
            print("\nADRES IP: serwermods.tk\nALTERNATYWNE IP: play.serwermods.tk")
            ababa = input("\n\n\nWciśnij Enter aby zacząć ponownie...")
            if ababa == "":
                return 0
        elif wybor == 3:
            if path.exists(f"{sciezka}/mods") == True:
                shutil.rmtree(f"{sciezka}/mods")
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
                if (
                    path.exists(
                        f"C:/Users/{user}/AppData/Roaming/Crystal-Launcher/instances/u.Forge-1.12.2"
                    )
                    == True
                ):
                    shutil.rmtree(
                        f"C:/Users/{user}/AppData/Roaming/Crystal-Launcher/instances/u.Forge-1.12.2"
                    )
            print("Usunięto")
            time.sleep(1)
            return 0
        elif wybor > 5:
            print("Nie ma takiego wyboru")
            time.sleep(1)
    else:
        print("Nie ma takiego wyboru")
        time.sleep(1)
    return 0


def ustawienia():
    global sciezka
    global wersja
    while True:
        os.system("cls")
        print(
            f"1. Wybierz ścieżkę instalacji (domyślnie %appdata%/.minecraft  obecnie  {sciezka})\n2. Przywróć domyślną ścieżkę\n3. Tworzenie kopii zapasowej\n4. Crystal Launcher\n\n5. Cofnij\n"
        )
        wybor = input()
        if wybor.isnumeric() == True:
            if int(wybor) == 1 or int(wybor) == 2:
                if int(wybor) == 1:
                    root = tkinter.Tk()
                    root.withdraw()
                    currdir = os.getcwd()
                    sciezka = filedialog.askdirectory(
                        parent=root, initialdir=currdir, title="Wybierz proszę ścieżkę"
                    )
                    if sciezka == "":
                        sciezka = f"C:/Users/{user}/AppData/Roaming/.minecraft"
                elif int(wybor) == 2:
                    sciezka = f"C:/Users/{user}/AppData/Roaming/.minecraft"
                f = open(
                    f"C:/Users/{user}/AppData/Roaming/.minecraft/mods-backup/version/args.txt",
                    "w",
                )
                f.write(f"{wersja}\n{sciezka}\n{settings[2]}\n{settings[3]}")
                f.close()
            elif int(wybor) == 3:
                print(
                    f"T - Twórz kopię automatycznie    P - Zawsze pytaj    N - Nie twórz kopii           obecnie  {settings[2]}\n"
                )
                wybor = input()
                wybor = wybor.upper()
                if wybor == "T" or wybor == "P" or wybor == "N":
                    if wybor == "T":
                        settings[2] = "T"
                    elif wybor == "P":
                        settings[2] = "P"
                    elif wybor == "N":
                        settings[2] = "N"
                    f = open(
                        f"C:/Users/{user}/AppData/Roaming/.minecraft/mods-backup/version/args.txt",
                        "w",
                    )
                    f.write(f"{wersja}\n{sciezka}\n{settings[2]}\n{settings[3]}")
                    f.close()
                else:
                    print("Nie ma takiej opcji!")
                    time.sleep(1)
            elif int(wybor) == 4:
                print(
                    "Działa tylko w momencie kiedy wykryje instancję Crystal Launcher!"
                )
                print(
                    f"T - Automatycznie przenoś    P - Zawsze pytaj    N - Nie przenoś           obecnie  {settings[3]}"
                )
                wybor = input()
                wybor = wybor.upper()
                if wybor == "T" or wybor == "P" or wybor == "N":
                    if wybor == "T":
                        settings[3] = "T"
                    elif wybor == "P":
                        settings[3] = "P"
                    elif wybor == "N":
                        settings[3] = "N"
                    f = open(
                        f"C:/Users/{user}/AppData/Roaming/.minecraft/mods-backup/version/args.txt",
                        "w",
                    )
                    f.write(f"{wersja}\n{sciezka}\n{settings[2]}\n{settings[3]}")
                    f.close()

            elif int(wybor) == 5:
                return 0


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


if __name__ == "__main__":
    # os.system("mode con cols=160 lines=45")
    abool = False
    user = os.getlogin()
    sciezka = f"C:/Users/{user}/AppData/Roaming/.minecraft"
    listar, listaopc, listasha = [], [], []
    # listy [0]  - 1.16.5   [1] - 1.12.2
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

    if path.exists(f"{sciezka}/mods-backup/version/args.txt") == False:
        f = open(f"{sciezka}/mods-backup/version/args.txt", "w")
        f.write(f"C:/Users/{user}/AppData/Roaming/.minecraft\nP\nP")
        f.close()

    try:
        import doctext as dockon
        import requests
        from tqdm import tqdm
    except ImportError:
        os.system("pip install docx-text")
        os.system("pip install requests")
        os.system("pip install tqdm")
        abool = True
    while True:
        now_date = str(datetime.date.today())
        now_date = now_date.replace(":", ".")
        i, buforr = 1, False
        if path.exists(f"C:/Users/{user}/AppData/Roaming/.minecraft") == False:
            os.mkdir(f"C:/Users/{user}/AppData/Roaming/.minecraft")

        line_count, contentv = kontent(f"{sciezka}/mods-backup/version/version.txt", 0)
        wersja = contentv[0]
        line_countt, settings = kontent(f"{sciezka}/mods-backup/version/args.txt", 0)
        settings[0]
        if line_countt < 4:
            f = open(f"{sciezka}/mods-backup/version/args.txt", "w")
            f.write(f"{wersja}\nC:/Users/{user}/AppData/Roaming/.minecraft\nP\nP")
            f.close()

        pliki(0)
        sciezka = settings[1]
        print(sciezka)
        bool = True
        while bool == True:
            os.system("cls")
            wybor = input(
                f"Wersja: {wersja}\n\n1. Wersja Forge 1.16.5\n2. Fosilsy (Forge 1.12.2)\n3. Usuń wszystkie mody\n\n4. Ustawienia\n5. Wyjdź\n"
            )
            if wybor.isnumeric() == True:
                if int(wybor) > 0 and int(wybor) < 4:
                    bool = False
                elif int(wybor) == 4:
                    ustawienia()
                    pliki(1)
                    bool = True
                elif int(wybor) == 5:
                    exit()

        temp = f"C:/Users/{user}/AppData/Local/Temp"
        java_url = "https://www.dropbox.com/s/almafuv9vr4xch3/java-installer.zip?dl=1"
        niema = []
        brakujace = []
        max_dlugosc = 30

        now_date = str(datetime.date.today())
        now_date = now_date.replace(":", "-")

        ch = open(f"{sciezka}/mods-backup/logs/latest.txt", "a")
        ch.write("----------------------------------------------")
        ch.write(f"\n[{czas()}]  Utworzono plik changelog")
        ch.write(f"\n[{czas()}]  Uruchamianie programu")
        ch.close()

        main(wybor)
