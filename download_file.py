from base64 import b64decode
from zipfile import ZipFile
import csv
import io



class downloadFile:

    def __init__(self, file):
        self.list = []
        self.data = file

        filename = self.data['nazwa_pliku']
        content = self.data['plik_zawartosc']
        decoded = b64decode(content)
        with open(filename, 'wb') as file:
            file.write(decoded)
            file.close()

        zf = ZipFile(filename, 'r')
        print("\u001b[36mPobrano pliki: ", zf.namelist())

        with zf.open(zf.namelist()[1]) as csv_file:
            text_file = io.TextIOWrapper(csv_file, encoding="utf-8")
            csv_reader = csv.reader(text_file, delimiter=";")

            for row in csv_reader:
                self.list.append(row)

        zf.close()








