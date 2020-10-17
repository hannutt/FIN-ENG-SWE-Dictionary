
from tkinter import* #tuodaan ohjelmassa tarvittavat kirjastot.
import requests
from bs4 import BeautifulSoup
from tkinter.font import Font 

#luodaan funktio, jolla web-kaavinta toteutetaan.
def getWord():
    #ehtolause, jos Fi_Eng valintaruutu on valittu
    if Fi_Eng.get() == 1:
        #tallennetaan word-muuttujaan käyttäjän syötenttään kirjoittama sana.
        word = Entry.get(wordField)
        #tehdään http-pyyntö parametrina annettuun osoitteeseen. osoitteen loppuun
        #lisätään ylempänä oleva word-muuttuja.
        page = requests.get('https://www.ilmainensanakirja.fi/suomi-englanti/'+word)
        #tallennetaan beautifulsoupin toiminnallisuus soup muuttujaan.
        soup = BeautifulSoup(page.text, 'html.parser')
        #etsitään nettisivulta beuatifulsoupin find toiminnolla word niminen luokka
        wordSearch = soup.find(class_='word')
        #etsitään luokasta kaikki a-tagin sisällä oleva tieto.
        wordSearches = wordSearch.find_all('a') 

        #käydään löydetty sisältö for-silmukassa läpi, tallennetaan se result
        #muuttujaan ja tulostetaan result muuttujan sisältö tekstilaatikkoon.
        for wordSearch in wordSearches:
            textbox.insert(INSERT,'Word in english: ',END)
            result = wordSearch.text
            textbox.insert(INSERT,result,END)
    
    elif Eng_Fi.get() == 1:
        word = Entry.get(wordField)
        page = requests.get('https://www.ilmainensanakirja.fi/englanti-suomi/'+word)
        soup = BeautifulSoup(page.text, 'html.parser')
        wordSearch = soup.find(class_='word')
        wordSearches = wordSearch.find_all('a')

        for wordSearch in wordSearches:
            textbox.insert(INSERT,'Word in finnish: ',END)
            result = wordSearch.text
            textbox.insert(INSERT,result,END)

    elif Fi_Swe.get() == 1:
        word = Entry.get(wordField)
        page = requests.get('https://www.ilmainensanakirja.fi/suomi-ruotsi/'+word)
        soup = BeautifulSoup(page.text, 'html.parser')
        wordSearch = soup.find(class_='word')
        wordSearches = wordSearch.find_all('a')

        for wordSearch in wordSearches:
            textbox.insert(INSERT,'Word in swedish: ',END)
            result = wordSearch.text
            textbox.insert(INSERT,result,END)


    elif Swe_Fi.get() == 1:
        word = Entry.get(wordField)
        page = requests.get('https://www.ilmainensanakirja.fi/ruotsi-suomi/'+word)
        soup = BeautifulSoup(page.text, 'html.parser')
        wordSearch = soup.find(class_='word')
        wordSearches = wordSearch.find_all('a')

        for wordSearch in wordSearches:
            textbox.insert(INSERT,'Word in finnish: ',END)
            result = wordSearch.text
            textbox.insert(INSERT,result,END)

#luodaan funktio, joka tyhjentää syötekentän ja tekstilaatikon sisällön.
def clearFields():
    wordField.delete(0,'end')
    textbox.delete(1.0,'end')
        
#luodaan pohjakomponentti        
root = Tk()
root.title('Dictionary')
#annetaan pohjakomponentille taustaväri.
root.configure(background = 'LightSteelBlue4')
#tallennetaan segoe print fontti labelfont muuttujaan.
labelfont = Font (family = 'Segoe Print')
#luodaan frame-komponentit, joiden avulla sijoitellaan ja asemoidaan muut komponentit.
frame1 = Frame()
#annetaan frame komponenteille taustaväri
frame1.configure(background = 'LightSteelBlue4')

frame2 = Frame()
frame2.configure(background = 'LightSteelBlue4')

frame3 = Frame()
frame3.configure(background = 'LightSteelBlue4')

frame4 = Frame()
frame4.configure(background = 'LightSteelBlue4')
#luodaan tekstilaatikko, jonka leveys on 25 ja korkeus 4.
textbox = Text(root, width = 25, height = 4)

#luodaan tekstikomponentit. text komennolla annetaan niissä täkyvä teksti, font komenolla käytettävä fontti
#bg komennolla taustaväri ja fg komennolla tekstin väri.
name = Label(root, text = 'FI-SWE-ENG Dictionary',font = labelfont,bg = 'LightSteelBlue4',fg = 'white')
typeWord = Label(frame1, text = 'Type a word: ',bg = 'LightSteelBlue4', font = labelfont, fg = 'white')

#luodaan syötekenttä, sisällytetään se frame1-komponenttiin
wordField = Entry(frame1)

#luodaan painikkeet, sisällytetään ne frame4 komponenttiin. command komennolla kerrotaan, mikä funktio suoritetaan jos
#painiketta painetaan.

searchbtn = Button(frame4,text = 'Get translate', command = getWord)
clearbtn = Button(frame4, text = 'Clear fields', command = clearFields)

#luodaan valintaruudut ja niiden tarvitsemat integer-muuttujat.
Fi_Eng = IntVar()
FiToEng = Checkbutton (frame2, text = 'Finnish to English', variable = Fi_Eng, bg = 'LightSteelBlue4', fg = 'white', selectcolor = 'black')

Eng_Fi = IntVar()
EngToFi = Checkbutton (frame2, text = 'English to Finnish', variable = Eng_Fi, bg = 'LightSteelBlue4',fg = 'white', selectcolor = 'black')

Fi_Swe = IntVar()
FiToSwe = Checkbutton (frame3, text = 'Finnish to Swedish', variable = Fi_Swe, bg = 'LightSteelBlue4',fg = 'white', selectcolor = 'black')

Swe_Fi = IntVar()
SweToFi = Checkbutton (frame3, text = 'Swedish to Finnish', variable = Swe_Fi, bg = 'LightSteelBlue4',fg = 'white', selectcolor = 'black')

#pakataan komponentit, side komennolla kerrotaan mihin komponentti halutaan sijoittaa, pady/padx komennoilla
#lisätään tyhjää tilaa komponenttien ympärille.
name.pack()
frame1.pack()
typeWord.pack(side=LEFT)
wordField.pack(side=RIGHT,pady=4,padx=4)
frame2.pack()
FiToEng.pack(side=LEFT)
EngToFi.pack(side=RIGHT)
frame3.pack()
FiToSwe.pack(side=LEFT)
SweToFi.pack(side=RIGHT)
textbox.pack()
frame4.pack()
searchbtn.pack(side=LEFT,pady=4,padx=4)
clearbtn.pack(side=RIGHT,pady=4,padx=4)
mainloop()
