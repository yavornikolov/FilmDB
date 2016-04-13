#ревизия 1: без функции, работи само единичното добавяне на филм / количество
#ревизия 2: въведени са функции - добавяне, редактиране, триене от масив
#ревизия 3: нещо-като-рекурсия в D/P/I
#ревизия 4: възможност за четене и писане от файл
#!!!!ПРЕДСТОЯТ: нова голяма функция със свойства на филмите (цветен/черно-бял, чувствителен или не); интерфейс...

import json
print ("Здравейте, това е програмата за каталогизиране на филми на Явор!")
all_films = {}
def filmAdd():
    film = input("Въведете името на филма: ").lower()
    amnt = int(input("Въведете брой (като число!): "))
    all_films[film] = amnt

def moreFilmz():
    morefilm = input("Да добавим / променим / изтрием филм? (D/P/I)")
    morefilm = morefilm.lower()
    if morefilm.lower() == "d":
        filmAdd()
        print (all_films)
        saveDB()
        exitApp()
        moreFilmz()
    elif morefilm.lower() == "p":
        print (all_films)
        whichOne = input("Кой е филмът? Напишете името точно!").lower()
        filmkeyz = []
        filmkeyz = all_films.keys()
        if whichOne in filmkeyz:
            newamnt = int(input("Въведете брой (като число!): "))
            all_films[whichOne] = newamnt
            print (all_films)
        else:
            print ("Грешка!")
        saveDB()
        exitApp()
        moreFilmz()
    elif morefilm.lower() == "i":
        print (all_films)
        whichOne = input("Кой е филмът? Напишете името точно!").lower()
        filmkeyz = []
        filmkeyz = all_films.keys()
        if whichOne in filmkeyz:
            del all_films[whichOne]
            print (whichOne, "беше премахнат")
        else:
            print ("Грешка!")
        saveDB()
        exitApp()
        moreFilmz()

def exitApp():
    will_we_exit = input("Искате ли да напуснете програмата? (Y/N)")
    will_we_exit = will_we_exit.lower()
    if will_we_exit == "y":
        exit()

def saveDB():
    will_we_save = input("Искате ли да запаметите базата данни? (Y/N)")
    will_we_save = will_we_save.lower()
    if will_we_save == "y":
        db_for_save = json.dumps(all_films)
        fileDB = open('filmsdb','w')
        fileDB.write(db_for_save)
        fileDB.close()
        print ("Запаметено!")
    
print
will_we_load = input("Да заредим ли файл? (Y/N)")
will_we_load = will_we_load.lower()
if will_we_load == "y":
    fileDB = open("filmsdb","r")
    all_films = json.load(fileDB)
    print(all_films)
    moreFilmz()
elif will_we_load == "n":
    print ("Нека първо добавим поне един филм!")
    filmAdd()
    print (all_films)
    moreFilmz()
else:
    print ("Грешка!")
