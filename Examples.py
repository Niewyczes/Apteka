import requests ## url, strony www
import wget   ## adresy url
import bs4   ### parsowanie www,   więcej na : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import os    ## dyski i katalogi PC
import urllib.parse  ## parsowanie url, więcej na: https://docs.python.org/3/library/urllib.parse.html
#import urllib
#import parser
from PIL import Image   # praca z plikami graficznymi, więcej: https://pillow.readthedocs.io/en/5.1.x/
from io import BytesIO  #  praca z plikami, więcej na: https://www.tutorialspoint.com/python/python_files_io.htm

# print('####odczyt kodu HTML #######')
url = 'http://www.poranny.pl/'
codeHTML = requests.get(url, verify=True).text # odczyt zawartości strony (HTML)
#print(codeHTML)
soup = bs4.BeautifulSoup(codeHTML, 'html.parser') # tworzenie obiektu BeautifulSoup z zachowaniem struktury kodu strony
# #print(soup)  #
#print(soup.prettify()) # wyświetlenie kodu z zachowaniem struktury
# print('####podstawowe wybrane metody wyodrębniania tekstu w oparciu o znaczniki#######')
#list(print(tag.name) for tag in soup.find_all(True))  # wykaz typów znaczników w kodzie
# print(soup.title)
# print(soup.title.string)
# print('############')
#print(soup.find_all("a"))  # lista której elementy zawierają kod z każdego znacznika <a>
# print('############')
#print(soup.find_all("a")[1]) # kod z pierwszego znacznika <a>
#print(soup.a) # kod z pierwszego znacznika <a> zapisany jako słownik
# print('############')
#print(soup.div['class']) #kod z pierwszego znacznika <div>, zawartość class  tj.  <div class="zafixowanaGora">
# print('############')
url = 'http://ii.uwb.edu.pl/index2.php'
iiUwB = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')
#print(iiUwB)
onetags = iiUwB.find_all('a')[3]
#print(onetags)
#print(onetags.attrs) # sprawdź dostępne klucze w 4-ty z kolei znaczniku <a>
## print('############')
#print(onetags.attrs['href']) # wyświetl zawartość kodu klucz:'href'
# print('#########################################################33')
# url = 'http://www.poranny.pl/'
# poranny = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')
# firstA = poranny.find_all('a')[1]
# print(firstA)
# firstIMG = firstA.img
# print(firstIMG.attrs)
# imageLink = firstIMG.attrs['src']
# print(imageLink)
#
# print('##########################################')
url = 'http://www.poranny.pl/'
poranny = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')
tags = poranny.find_all("img")
#print(tags)
# ############################################################
# #### UWAGA: tu zwróć uwagę na skrócony wariant pisania pętli for ################################
# #### poniżej zostaną użyte wybrane metody dla list i zmiennych typu string, jeżeli ich nie pamiętasz zajrzyj
# #### do poprzednich zajęć lub na stronę: https://www.tutorialspoint.com/python/python_strings.htm
# print("\n".join(set(tag.attrs['src'] for tag in tags)))
# print('#################')
# # setOneTags = list()        # zapisz linki z obrazkami do listy wariant 1
# # for tag in tags:
# #     print(tag['src'])
# #     setOneTags.append(tag['src'])
# # print(setOneTags)
# print('#################')
setOneTags = list(tag['src'] for tag in tags) # zapisz linki z obrazkami do listy wariant 2
#print(setOneTags)
# print('#################')
setOneTagsSplit = list(tag.split('.') for tag in setOneTags) # rozdziel znaki separator '.'
#print(setOneTagsSplit)
# #print('#################')
setOneTagsSplitBool = list('jpg' in tag for tag in setOneTags) # sprawdź czy zawiera fragment tekstu 'jpg'
#print(setOneTagsSplitBool)
indexes = [i for i in range(len(setOneTagsSplitBool)) if setOneTagsSplitBool[i]== True] # numery indeksów
# print(indexes)
urlJPG = list(setOneTags[indexes[i]] for i in range(len(indexes)))
#print(urlJPG)
# # # print('###zapisz obraz z link nr 1#####')
# response = requests.get(urlJPG[0])
# img = Image.open(BytesIO(response.content))  # otwórz plik graficzny
# img.show()      # pokaż zawartość pliku
# img.save('obraz.jpg', "JPEG") # zapisz plik
# #
# print('###pliki pdf zapisz do folderu 3 pliki z #####')
# ################################################3
url = 'http://ii.uwb.edu.pl/index.php?p=981'
#print(url)
page1 = requests.get(url, verify=True).text
#print(page1)
soup = bs4.BeautifulSoup(page1, 'html.parser')
#print(soup)  #
tags = soup.find_all('a')
# ######zwróć uwagę na różnice w treści:
#print(type(tags[1]))
# tags = soup.find('a')
# print(tags)
#
listLink = list()
for link in soup.find_all('a'):
    listLink.append(link.get('href'))
print(listLink)
#
# listLink = list(link.get('href') for link in soup.find_all('a'))
# #print(listLink)
# #print('#####Tu pojawiły się elementy NoneType, należy je usunąć ########')
#listLink1 = list(filter(None,listLink)) # odfiltruj elementy NoneType
# #print(listLink1)
# print('############################')
#listLink2 = [element for element in listLink1 if element.endswith('pdf')] # wybierz linki zakończone ciągiem znaków pdf
#print(listLink2)
# print('#######uwaga czasami zamiast filtrowania wygodniej jest wykorzystać np. obsługę błędu#########')
# ##### więcej o obsłudze błędów i wyjątków możesz znaleźć tu: https://docs.python.org/2/tutorial/errors.html
adresListPDF = list()
for link in listLink:
    try:     # 'złap' błąd
        if link.endswith('pdf'):
            adresListPDF.append(link)
    except(RuntimeError, TypeError, NameError, AttributeError): # można wpisać więcej :)  # pomiń określone błędy
        pass
#
# # # pass - nie reaguj, nic nie wykonuj
# # # break -  wyjście z najbliżej zagnieżdżonej pętli
# # # continue - przejście do następnego kroku iteracji w pętli
#
#print(adresListPDF)
# # print('#######zapisz do pliku #########')
MyNameFolder = 'e:\\DYDAKTYKA\\Bioinformatyka\\Laboratorium2017_18\\filePdfLoad\\'
for link in adresListPDF:
    splitPathFile = os.path.split(link) # wynik to krotka: (ścieżka, nazwa pliku)
    #print(os.getcwd()) # sprawdź jaka jest ścieżka do twojego folderu roboczego
    fileName = splitPathFile[1]
    joinMyNameFolderAndFileName = os.path.join(os.path.dirname(MyNameFolder), fileName)# połącz ścieżkę folderu i nazwe pliku
    #print(joinMyNameFolderAndFileName)
    #wget.download(link, joinMyNameFolderAndFileName)  # load and save file wariant wygodniejszy
    urllib.request.urlretrieve(link, joinMyNameFolderAndFileName)
