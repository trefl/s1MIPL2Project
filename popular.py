import re
from collections import Counter
from matplotlib import pyplot as plt
from prettytable import PrettyTable


class popularStreet:

    def __init__(self, dict_1, list_1, list_2, client):
        self.dict = dict_1
        self.sList = list_1
        self.cList = list_2
        self.client = client

    def in_the_province(self):
        streetList = []
        for e in self.dict:
            tempList = []
            tempDict = {}
            for row in self.sList.list:
                if len(row) > 2:
                    if e['WOJ'] == row[0]:
                        tempList.append(row[7])

            for name in tempList:
                if name not in tempDict:
                    tempDict[name] = 1
                else:
                    tempDict[name] = tempDict[name] + 1

            sortDict = {k: v for k, v in sorted(tempDict.items(), key=lambda v: v[1], reverse=True)}
            first_pair = next(iter((sortDict.items())))

            streetList.append([e['WOJ'], first_pair[0], first_pair[1]])
        print("\nLista najpopularniejszych ulic w danym województwie:\n")
        for e in self.dict:
            for i in range(len(streetList)):
                if e['WOJ'] == streetList[i][0]:
                    print(f'\u001b[0mWojewództwo \u001b[36;1m{e["NAZWA"]} '
                          f'\u001b[0m- najpopularniejszą ulicą jest ulica '
                          f'\u001b[36;1m{streetList[i][1]} \u001b[0mwystępującą '
                          f'\u001b[36;1m{streetList[i][2]} \u001b[0mrazy')

    def top_100_categories(self):

        tempList = []
        tempDict = {}

        for row in self.sList.list:
            if len(row) > 2:
                tempList.append(row[7])

        for name in tempList:
            if name not in tempDict:
                tempDict[name] = 1
            else:
                tempDict[name] = tempDict[name] + 1

        top100 = Counter(tempDict).most_common(100)

        # Nazwy ulic według kategorii w listach top 100
        treeList = ["Akacjowa", "Brzozowa", "Bukowa", "Dębowa", "Jarzębinowa", "Jesionowa", "Jodłowa", "Kasztanowa",
                    "Klonowa", "Lipowa", "Modrzewiowa", "Orzechowa", "Sosnowa", "Świerkowa", "Topolowa", "Wierzbowa",
                    "Wiśniowa"]
        otherList = ["Boczna", "Cicha", "Długa", "Dolna", "Główna", "Górna", "Graniczna", "Jasna", "Krótka", "Maja",
                     "Miła", "Miodowa", "Nowa", "Okrężna", "Poprzeczna", "Prosta", "Przemysłowa", "Radosna",
                     "Spacerowa", "Spokojna", "Warszawska", "Wąska", "Wesoła", "Widokowa", "Wspólna", "Zacisze"]
        colorList = ["Tęczowa", "Zielona"]
        natureList = ["Leśna", "Łąkowa", "Ogrodowa", "Parkowa", "Piaskowa", "Pogodna", "Polna", "Południowa", "Sadowa",
                      "Słoneczna", "Stawowa", "Wiosenna", "Wodna"]
        nameList = ["Chopina", "Jana Pawła II", "Kochanowskiego", "Konopnickiej", "Kopernika", "Kościuszki",
                    "Mickiewicza", "Piłsudskiego", "Prusa", "Reja", "Reymonta", "Sienkiewicza", "Sikorskiego",
                    "Słowackiego", "Witosa", "Żeromskiego"]
        plantList = ["Chabrowa", "Jagodowa", "Jaśminowa", "Kalinowa", "Konwaliowa", "Kwiatowa", "Lawendowa", "Makowa",
                     "Malinowa", "Poziomkowa", "Różana", "Wrzosowa"]
        urbanList = ["Cmentarna", "Dworcowa", "Kolejowa", "Kościelna", "Młyńska", "Osiedlowa", "Rynek", "Szkolna",
                     "Wiejska", "Zamkowa"]
        professionList = ["Armii Krajowej", "Sportowa", "Strażacka", "Wojska Polskiego"]

        labelsList = ['Drzewa', 'Inne', 'Kolory', 'Natura', 'Nazwiska', 'Rośliny', 'Zabudowania', 'Zawody']
        sumList = [0, 0, 0, 0, 0, 0, 0, 0]

        for i in top100:
            for tree in treeList:
                if tree == i[0]:
                    sumList[0] += i[1]

            for other in otherList:
                if other == i[0]:
                    sumList[1] += i[1]

            for color in colorList:
                if color == i[0]:
                    sumList[2] += i[1]

            for nature in natureList:
                if nature == i[0]:
                    sumList[3] += i[1]

            for name in nameList:
                if name == i[0]:
                    sumList[4] += i[1]

            for plant in plantList:
                if plant == i[0]:
                    sumList[5] += i[1]

            for urban in urbanList:
                if urban == i[0]:
                    sumList[6] += i[1]

            for profession in professionList:
                if profession == i[0]:
                    sumList[7] += i[1]
        return sumList, labelsList, top100

    def show_streets_in_categories(self):
        sumList = self.top_100_categories()[0]
        labelsList = self.top_100_categories()[1]

        print("\nLista najpopularniejszych 100 ulic przyporządkowanych według kategorii\n")
        for i in range(len(labelsList)):
            print(labelsList[i], ":", sumList[i])

    def show_bar_chart_streets_in_categories(self):
        sumList = self.top_100_categories()[0]
        labelsList = self.top_100_categories()[1]
        plt.bar(labelsList, sumList)
        plt.title("Wykres najpopularniejszych ulic TOP100 \nprzyporządkowanych według kategorii")
        plt.xticks(rotation=0)
        plt.show()

    def show_streets_top100(self):
        top100Dict = self.top_100_categories()[2]
        count = 1
        print("Ranking 100 najpopularniejszych ulic w Polsce")
        for e in top100Dict:
            print(f'{count}. {e[0]}: {e[1]}')
            count += 1

    def show_pie_chart(self):
        sumList = self.top_100_categories()[0]
        labelsList = self.top_100_categories()[1]

        colorsList = ["c", "m", "r", "b", "g", "y", "tab:blue", "tab:brown"]

        plt.pie(sumList, labels=labelsList, colors=colorsList, autopct='%1.1f%%')
        plt.title('Top 100')
        plt.show()

    def input_street(self, order):
        street1 = input(f'Wpisz nazwę {order} ulicy: \n> ')
        streetsDict = self.client.WyszukajUlice(nazwaulicy=street1)
        try:
            streetLen = len(streetsDict)
        except:
            streetLen = 0
        return street1, streetsDict, streetLen

    def compare_street(self):
        street1List = []
        street2List = []
        print("Porównanie ulic pod względem występowania\n")
        street1 = self.input_street("pierwszej")
        streetsDict1 = street1[1]
        street1Len = street1[2]
        street2 = self.input_street("drugiej")
        streetsDict2 = street2[1]
        street2Len = street2[2]

        table = PrettyTable()
        bigger = max(street1Len, street2Len)

        if street1Len > 0:
            for e in streetsDict1:
                street1List.append(e['NazwaMiejscowosci'] + " " + e['Cecha'] + " " + e['Nazwa'])
            if street1Len < bigger:
                for e in range(bigger - street1Len):
                    street1List.append(" ")
        else:
            for e in range(bigger):
                street1List.append(" ")

        if street2Len > 0:
            for e in streetsDict2:
                street2List.append(e['NazwaMiejscowosci'] + " " + e['Cecha'] + " " + e['Nazwa'])
            if street2Len < bigger:
                for e in range(bigger - street2Len):
                    street2List.append(" ")
        else:
            for e in range(bigger):
                street2List.append(" ")

        table.field_names = ["Lp", street1[0], street2[0]]
        for e in range(bigger):
            if e < bigger:
                table.add_row([str(e + 1) + ".", street1List[e], street2List[e]])
            else:
                table.add_row([str(e + 1) + ".", street1List[e], street2List[e]])
        print(table)
        print(f'\nPodsumowanie:\n'
              f'Ulica {street1[0]} występuje w {street1Len} miejscowościach\n'
              f'Ulica {street2[0]} występuje w {street2Len} miejscowościach')

    def connecting_columns(self):
        newList = []
        for row in self.sList.list:
            if len(row) > 2:
                if row[8] == "":
                    newString = (row[7])
                else:
                    newString = (row[7] + " " + row[8])

                newList.append([newString.lower(), row[4], row[5], row[6], row[7], row[8]])

        return newList

    def find_similar_street_in_city(self):
        print("Wyszukiwarka do sprawdzania występowania podobnej ulicy w mieście\n")
        ccList = self.connecting_columns()
        name = input("Wpisz nazwę ulicy:\n > ")
        tempDict = {}

        for row in ccList:
            if len(re.findall(name.lower(), row[0])) > 0:

                if row[1] not in tempDict:
                    tempDict[row[1]] = [1, [row[3] + " " + row[4] + " " + row[5]]]
                else:
                    tempDict[row[1]][0] += 1
                    tempDict[row[1]][1] += [row[3] + " " + row[4] + " " + row[5]]
        count = 0
        for key in tempDict:
            if tempDict[key][0] > 1:
                for row in self.cList.list:
                    if len(row) > 2:
                        if row[7] == key:
                            print("\n")
                            print("Miasto " + row[6] + ":")
                            print(tempDict[key][1])
                            count += 1
        if count > 0:
            print("\nZnaleziono " + str(count) + " miast w których występują podobne ulice.")
        else:
            print("\nNie znaleziono podobnych ulic.")

    def streets_in_city(self):
        print("Lista ulic w danym mieście\n")

        name = input("Wpisz nazwę miejscowości:\n > ")
        cityDict = self.client.WyszukajMiejscowosc(nazwaMiejscowosci=name)
        streetList = self.sList
        count = 0
        if cityDict is not None:
            for key in cityDict:
                count += 1
                print(
                    f'\n{key["Nazwa"]}, Województwo: {key["Wojewodztwo"].lower()}, Powiat: {key["Powiat"]}, Gmina: {key["Gmina"]}')
                tempList = []
                strCount = 0
                for row in streetList.list:
                    if len(row) > 2 and row[4] == key['Symbol']:
                        tempList.append(row[6] + " " + row[7] + " " + row[8])
                        strCount += 1
                if len(tempList):
                    print(tempList)
                    print("Ulice: ", strCount)
                else:
                    print("Ulice: brak")
        print(f'\nZnalezionych miejscowości: {count}')

    def sort_streets_by_cities(self):
        ccList = self.connecting_columns()
        cityDict = {}
        for row in ccList:
            if row[1] not in cityDict:
                cityDict[row[1]] = [[row[0], row[1], row[3], row[4], row[5]]]
            else:
                cityDict[row[1]] += [[row[0], row[1], row[3], row[4], row[5]]]
        return cityDict

    @staticmethod
    def create_dictionary_words(sList):
        wordsList = []
        for row in sList:
            for e in row[0].split():
                if len(e) > 3:
                    wordsList.append(e)
                elif len(e) > 2 and e.isalpha():
                    wordsList.append(e)

        wordsList = list(set(wordsList))
        return wordsList

    @staticmethod
    def find_word(word, words):
        wordsList = words.split()
        count = 0
        for e in wordsList:
            if e == word:
                count += 1
        return count

    def sort_street(self, ciList, words):
        streetDict = {}
        for word in words:
            for row in ciList:
                if self.find_word(word, row[0]) > 0:
                    if word not in streetDict:
                        streetDict[word] = [1, [[row[0], row[1], row[2], row[3], row[4]]]]
                    else:
                        streetDict[word][0] += 1
                        streetDict[word][1] += [[row[0], row[1], row[2], row[3], row[4]]]
        delList = []
        for key in streetDict:
            if streetDict[key][0] < 2:
                delList.append(key)
        for e in delList:
            del streetDict[e]

        return streetDict

    @staticmethod
    def display_street(dict_1):
        if len(dict_1) > 0:
            print("Ulice zawierające słowa: ")

            for key in dict_1:
                tempList = []
                for e in dict_1[key][1]:
                    tempList.append(e[2] + " " + e[3] + " " + e[4])

                print(f'\n{key}[{dict_1[key][0]}] \n{tempList}')
        else:
            print("Brak podobnych ulic")

    def find_similar_street_in_city_auto(self):
        cdict = self.sort_streets_by_cities()
        name = input("Wpisz nazwę miejscowości:\n > ")
        cityDict = self.client.WyszukajMiejscowosc(nazwaMiejscowosci=name)
        count = 0
        if cityDict is not None:
            for key in cityDict:
                count += 1
                print(
                    f'\n{key["Nazwa"]}, Województwo: {key["Wojewodztwo"].lower()}, Powiat: {key["Powiat"]}, Gmina: {key["Gmina"]}')
                try:
                    words = self.create_dictionary_words(cdict[key['Symbol']])
                    sortDict = self.sort_street(cdict[key['Symbol']], words)
                    self.display_street(sortDict)
                except:
                    print("Brak ulic")
