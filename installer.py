#lat
def downloader(url, path, var):
    with open(path, "wb") as f:
        response = requests.get(url, stream=True)
        total = response.headers.get("content-length")

        if total is None:
            f.write(response.content)
        else:
            if var == 1:
                downloaded = 0
                total = int(total)
                for data in response.iter_content(
                    chunk_size=max(int(total / 1000), 1024 * 1024)
                ):
                    downloaded += len(data)
                    f.write(data)
                    done = int(50 * downloaded / total)
                    sys.stdout.write(
                        "\r[{}{}]{}{}".format(
                            "█" * done,
                            "." * (50 - done),
                            f" {round(100*downloaded/total)}%",
                            f" {round(downloaded/1000)}KB/{round(total/1000)}KB  ",
                        )
                    )
                    sys.stdout.flush()
            else:
                downloaded = 0
                total = int(total)
                for data in response.iter_content(
                    chunk_size=max(int(total / 1000), 1024 * 1024)
                ):
                    f.write(data)


if __name__ == "__main__":
    import os
    import subprocess
    import sys
    import time
    from os import path

    user = os.getlogin()
    p = "python.exe"
    a = []
    aa = []
    czyjest = ""
    buffor = False
    sciezka = f"C:/Users/{user}/AppData/Roaming/.minecraft"
    ver = ["Python39", "Python38", "Python37"]
    temp = f"C:/Users/{user}/AppData/Local/Temp"

    os.system("cls")
    print("Uruchamianie instalatora")

    if path.exists(f"C:/Users/{user}/AppData/Roaming/.minecraft") == False:
        os.mkdir(f"C:/Users/{user}/AppData/Roaming/.minecraft")
    if path.exists(f"{sciezka}/mods-backup") == False:
        os.mkdir(f"{sciezka}/mods-backup")
    if path.exists(f"{sciezka}/mods-backup/version") == False:
        os.mkdir(f"{sciezka}/mods-backup/version")

    for p in sys.path:
        a.append(p)
    for i in range(len(a)):
        b = str(a[i])
        b = b.replace("\\", "/")
        b = b.split("/")
        if (
            b[len(b) - 1] == ver[0]
            or b[len(b) - 1] == ver[1]
            or b[len(b) - 1] == ver[2]
        ):
            ile = i
    try:
        subprocess.check_output("python -V", shell=True)
    except subprocess.CalledProcessError as e:
        buffor = True
        if path.exists(f"{sciezka}/mods-backup/version/zmienne.bat") == False:
            f = open(f"{sciezka}/mods-backup/version/zmienne.bat", "w")
            f.write('@echo off\ncls\nsetx path "%*;%*\Scripts;%PATH%"\npause\nexit')
            f.close()
        try:
            subprocess.call([f"{sciezka}/mods-backup/version/zmienne.bat {a[ile]}"])
        except Exception:
            os.system(f"{sciezka}/mods-backup/version/zmienne.bat {a[ile]}")
        os.remove(f"{sciezka}/mods-backup/version/zmienne.bat")
    try:
        import doctext
        import requests
    except ImportError:
        os.system(f"pip install docx-text")
        os.system(f"pip install requests")

    if buffor == True:
        import doctext as doctxt
        import requests

        os.system("cls")
        print("\n\nWłącz instalator raz jeszcze!")
        time.sleep(5)
        exit()

    import doctext as doctxt

    sciezkaver = f"{sciezka}/mods-backup/version"
    docxFile = f"{sciezkaver}/vers.docx"
    downloader(
        "https://www.dropbox.com/scl/fi/6g9rd90x6gby0gmwv92sm/Document.docx?dl=1&rlkey=xevc9u66c8i7253eu4qw8502l",
        docxFile,
        0,
    )
    doc_text = doctxt.DocFile(doc=docxFile)
    doctext = doc_text.get_text()
    txtFile = f"{sciezkaver}/vers.txt"
    fdoc = open(txtFile, "w")
    fdoc.write(doctext)
    fdoc.close()
    os.remove(f"{sciezkaver}/vers.docx")
    f = open(txtFile, "r")
    line_count = 0
    for line in f:
        if line != "\n":
            line_count += 1
    with open(txtFile) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    for i in range(int(line_count) + 1):
        content.remove("")
    if path.exists(f"{sciezkaver}/ver.txt") == True:
        os.remove(f"{sciezkaver}/ver.txt")
    f = open(f"{sciezkaver}/ver.txt", "a")
    for i in range(len(content)):
        f.write(f"{content[i]}\n")
    f.close()
    os.remove(f"{sciezkaver}/vers.txt")

    if path.exists(f"{sciezkaver}/version.txt") == False:
        print("Aktualizowanie instalatora")
        downloader(content[1], f"{sciezkaver}/instalator.py", 1)
        f = open(f"{sciezkaver}/version.txt", "w")
        f.write(f"{content[0]}")
        f.close()
        os.remove(f"{sciezkaver}/ver.txt")
        print(
            "\n\nWłącz instalator raz jeszcze!\n\n",
        )
        time.sleep(5)
    else:
        with open(f"{sciezkaver}/version.txt") as f:
            contentv = f.readlines()
            contentv = [x.strip() for x in contentv]
        if content[0] != contentv[0]:
            print("Aktualizowanie instalatora")
            downloader(content[1], f"{sciezkaver}/instalator.py", 1)
            f = open(f"{sciezkaver}/version.txt", "w")
            f.write(f"{content[0]}")
            f.close()
            os.remove(f"{sciezkaver}/ver.txt")
            print("\n\nWłącz instalator raz jeszcze!\n\n")
            time.sleep(5)
        else:
            os.remove(f"{sciezkaver}/ver.txt")
            subprocess.call(["python", f"{sciezkaver}/instalator.py"])
