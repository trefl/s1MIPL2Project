import os
import time

from zeep import Client
from zeep.wsse.username import UsernameToken
from datetime import datetime
from credentials import CREDENTIALS
from download_file import downloadFile
from popular import popularStreet

token = UsernameToken(
    username=CREDENTIALS['username'],
    password=CREDENTIALS['password']
)

client = Client(wsdl=CREDENTIALS['wsdl'], wsse=token)

STATE_DATE = datetime.now()


if client.service.CzyZalogowany():
    dictProvince = client.service.PobierzListeWojewodztw(STATE_DATE)
    cs = client.service
    listSIMC = downloadFile(client.service.PobierzKatalogSIMC(STATE_DATE))
    listULIC = downloadFile(client.service.PobierzKatalogULIC(STATE_DATE))
    popular = popularStreet(dictProvince, listULIC, listSIMC, cs)
    time.sleep(3)


    def mainMenu():
        os.system("cls")
        print("MENU: \n")
        print("1. Lista najpopularniejszych ulic w danym województwie")
        print("2. Lista najpopularniejszych 100 ulic  przyporządkowanych według kategorii")
        print("3. Wykres słupkowy najpopularniejszych 100 ulic  przyporządkowanych według kategorii")
        print("4. Wykres kołowy najpopularniejszych 100 ulic  przyporządkowanych według kategorii")
        print("5. Porównanie ulic pod względem występowania")
        print("6. Wyszukiwarka do sprawdzania występowania podobnej ulicy")
        print("7. Wyszukiwarka do sprawdzania występowania podobnych ulic w mieście")
        print("8. Lista ulic w danym mieście")

        try:
            selection = int(input("\nWybierz numer: "))
            if selection == 1:
                os.system("cls")
                popular.in_the_province()
                input("\nAby powrócić do menu naciśnij Enter: ")
                mainMenu()
            elif selection == 2:
                os.system("cls")
                popular.show_streets_in_categories()
                input("\nAby powrócić do menu naciśnij Enter: ")
                mainMenu()
            elif selection == 3:
                os.system("cls")
                popular.show_bar_chart_streets_in_categories()
                input("\nAby powrócić do menu naciśnij Enter: ")
                mainMenu()
            elif selection == 3:
                os.system("cls")
                popular.show_streets_top100()
                input("\nAby powrócić do menu naciśnij Enter: ")
                mainMenu()
            elif selection == 4:
                os.system("cls")
                popular.show_pie_chart()
                input("\nAby powrócić do menu naciśnij Enter: ")
                mainMenu()
            elif selection == 5:
                os.system("cls")
                popular.compare_street()
                input("\nAby powrócić do menu naciśnij Enter: ")
                mainMenu()
            elif selection == 6:
                os.system("cls")
                popular.find_similar_street_in_city()
                input("\nAby powrócić do menu naciśnij Enter: ")
                mainMenu()
            elif selection == 7:
                os.system("cls")
                popular.find_similar_street_in_city_auto()
                input("\nAby powrócić do menu naciśnij Enter: ")
                mainMenu()
            elif selection == 8:
                os.system("cls")
                popular.streets_in_city()
                input("\nAby powrócić do menu naciśnij Enter: ")
                mainMenu()
            else:
                os.system("cls")
                print("created by Marek Trefler")
                input("\nAby powrócić do menu naciśnij Enter: ")
                mainMenu()
        except:
            os.system("cls")
            print("created by Marek Trefler")
            input("\nAby powrócić do menu naciśnij Enter: ")
            mainMenu()


    mainMenu()








