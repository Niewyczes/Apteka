######### Operatory porównania lokalnego i globalne
####################Przykład
### Sprawdź wynik działania następujących operacji:
# l1 = [5,10]
# l2 = [5,11]
#
# print(l1,l2)
# print('l1 == l2 wynik:',l1 == l2)
# print('l1 is l2 wynik:',l1 is l2)
# print('l1 != l2 wynik: ',l1 != l2)
# print('l1 is not l2 wynik:',l1 is not l2)
# print('l1 >= l2 wynik:', l1 >= l2)

## x or y	jeżeli x == False, to y, w przeciwnym razie x
## w przybliżeniu alternatywa
## x and y	jeżeli x == False, to x, w przeciwnym razie y
## w przybliżeniu koniunkcja
## not x	negacja

############## Example:
# a = False
# b = 2
# c = True
#
# print(a or b)
# print(b or a)
# print(c or a)
# print(a or c)
# print(b and a)
# print(a and b)
# print(a and c)

#################Instrukcje sterujące tj. instrukcje warunkowe i pętle
 ################# 1. Instrukcja warunkowa "IF"#########struktura
# if warunek_1:
#     #lista instrukcji         # odstęp/wcięcie w programie 4 spacje lub 1 tablulacja
# elif warunek_2:
#     #lista instrukcji
# elif warunek_3:
#     #lista instrukcji
#     ...
# else:                          # każdy inny przypadek
#     #lista instrukcji

############## Example:
# liczba = int(input('Ile punktów dostałeś z wejściówki'))
# if liczba == 5:
#     print('Ocena 5')
# elif liczba == 4:
#     print('Ocena 4')
# elif liczba == 3:
#     print('Ocena 3')
# else:
#     print('Wejściówka do poprawy')


################ 2. Instrukcja warunkowa "MATCH"#########struktura
# match zmienna:
#     case wartość zmiennej 1:
#         blok instrukcji
#     case wartość zmiennej 2:
#         blok instrukcji
# ....
#     case wartość zmiennej n:
#         blok instrukcji

############## Example:
#dane_osobowe = input('Wpisz "PESEL" albo "nazwisko"'))
#match dane_osobowe:
#    case "PESEL":
#        print('781123242622')
#    case "nazwisko":
#        print('Kowalska')

###########  3. Pętla: for  - iteracja po wektorze liczb
## for i in wektor:  # wektor tworzymy korzystając z funkcji range(początek,koniec)
##     instrukcje

#############
# print(list(range(0,4)))  # range(0,4) odpowiada: 0,1,2,3

############## Example:
# for i in range(1, 6):
#     print('Python'*i)

################# Pętla for - po kolekcji
## for x in kolekcja:  # kolekcja: zbiór, słownik, lista, krotka, sekwencja znaków
##     instrukcje         

############## Example:
# for i in ['Ala','Ola','Tola']:
#     print(i)

################# 4. Pętla:  while
## while warunek:  # pętla dział dopóki warunek jest prawdziwy
##     instrukcje

############## Example:
# i = 0   # i to zmienna tzw iterator który w każdym kroku zwykle zmienia się o jakąś wartość np.1
# while i < 5:
#    print('Lubię Pythona')
#    i = i + 1      # można też zapisać   i += 1

##################### Methods versus function (metoda vs funkcja)
############## Example:
# a = [2, 70, 5, 6]
# a.sort()   # c objectcall method on object
# print(a)

# a = [2, 70, 5, 6]
# a = sorted(a)  # override of a variable (nadpisanie zmiennej)
# print(a)

###### Generally, methods and functions have one or more parameters
###### (Metody i funkcje często mają jeden lub więcej parametrów)

############## Example:
# a = [2, 70, 5, 6]
# a.sort(reverse=True)
# print(a)

#  funkcja wbudowana 
# a = [2, 70, 5, 6]
# a = sorted(a, reverse=True)  # override of a variable
# print(a)

#################### One line if/else statement in Python
########### Example
## Syntax/Składnia: <expression1> if <condition> else <expression2>
## Option 1
# a = 20
# b = 1
# print('większe') if a > b else print('mniejsze')

# Option 2
# a = 1
# b = 20
# x = a > b and print('większe') or print('mniejsze')

# Option 3
# age = 21
# print(('adult', 'kid')[age < 20])  # choice from the tuples

# Option 4
# age = 21
# print(('adult', 'kid')[True])

######## Function: break() and continue()
## Funkcja break() jest używana często do zakończenia pętli (for, while)
## continue() pozwala opuścić blok instrukcji i wrócić do początku pętli.

####### Example: the program prints out only odd numbers: 1 3 5 7 9
# for x in range(1, 10):
#     if x % 2 == 0:  # Modulo, sprawdź, czy x jest parzystą liczbą
#         continue
#     print(x)

############################## Python module random
## Random module implements pseudo-random number generators for various distributions.

### Example:  random - returns a random float number between 0 and 1
# import random     # generator liczb losowych
# print(random.sample(range(10000),4))
# print(random.choice(range(10000)))

################################## Python function
## Syntax: def function_name(input_argument1, input_argument2, ... ,input_argumentN):
##       instructions
##      return output_argument   or  return output_arguments
##
##
## Calling the function (wywołanie funkcji )
## name_function(value of input_argument1, ... ,value of input_argumentN)

### Example

# def sum_numbers(x, y):
#     sum_xy = x + y
#     return sum_xy

# print('Result is equal:', sum_numbers(3,5))

####################  Python function:  anonymous function lambda()
#########  Funkcja anonimowa lambda()
## Syntax:     lambda input_arguments: instruction

################# Example
# resultLambda1 = lambda x, y: x + y
# print('Wynik wywołania funkcji lambda:', resultLambda1(3,5))

################# Example
# name = 'Ala'
# resultLambda2 = lambda oneWord: oneWord.upper()
# print(resultLambda2(name))

##############################################################
######### Funkcje wyższego rzędu:  map(), filter(), reduce()

######################3 Function map()
## Funkcja map() wykonuje operacje z użyciem funkcji na każdym elemencie listy/tupli/słownika:
## Syntax: map(function_name, iter)
## function_name - name of function with one input parameter
## iter is list or dictionary or tuples
## output parameter of mam is list type.
## map() realize operation by using function on each elements of list/tuple/dictionary

######### Example: construct your own function + map()
# def power(number):
#     result = number**2
#     return(result)
#
# list_number = [2, 10, 15, 100, -5]  # equivalent to [double(n) for n in listNumber]
# result_map = map(power, list_number)

# print(list(result_map))  # dump to list

######### Example: construct lambda() + map()
# list_word = ['dnA','RnA']
# upper_letter = lambda one_word: one_word.upper()
# result_lambda = map(upper_letter, list_word)  # equivalent to map(lambda one_word: one_word.upper(), list_word)
# print('Result: ', list(result_lambda))

####################  Function filter()
## Funkcja filter filtruje elementy sekwencji przy użyciu podanej funkcji,
## która musi zwracać wartość True lub False:
## Syntax: filter(function, sequence)

######### Example
# list1 = [1,2,3,4]
# def even(x):
#  if x%2 == 0:
#     return True
#  else:
#     return False
#
# resultFilter = filter(even, list1)
# print(list(resultFilter))


################# Function reduce()
## Funkcja reduce() pobiera dane z sekwencji i zwraca na ich podstawie pojedynczą
## wartość np. sumę liczb. Struktura: functools.reduce(function0, sequence, [initial_value]);
## reduce() realizuje operacje zdeklarowane w function0 na pierwszych dwóch elementów sekwencji, następnie
## wykonuje function0 dla wyniku i trzeciego elementu, aż do wyczerpania elementów sekwencji

## Funkcja reduce() się w pakiecie functools, zawierającym szereg użytecznych funkcji 
## wyższego rzędu

######## Example
# import functools, operator
# resultLambda1 = lambda x, y: x + y
# list1 = [1,2,3,4]
# resultReduce1 = functools.reduce(resultLambda1, list1,0)
# print(resultReduce1)

######### Przykłady funkcji wbudowanych:  zip(),  enumerate()
##### Function zip()##########################################################################
# zip() creates pair of elements (tuples) from two list
# zip() tworzy za to listę tupli z podanych elementów

######### Example
# list1 = [1,3,5]
# list2 = [2,4,6]
# resultZip = zip(list1, list2)
# print(list(resultZip))

########### Function enumerate
## Enumerate() adds a counter to an iterable and returns it in the form of the enumerating object.
##
# def main():
#     print("#### function enumerate ###")
#     a = ['a', 'b', 'c']
##    b = [(0, 'a'), (1, 'b')] # sprawdź poniższe również dla zmiennej b
#
#     for i in enumerate(a):
#         print(i)        # [(0, 'a'), (1, 'b')]
#
#     print("#######")
#     for i in enumerate(a):
#         for j in i:
#             print('j element:', j)
#     print("#######")
#     for i in enumerate(a):
#         for j in i[1]:
#             print('j element:', j)
#
# if __name__ == '__main__':
#     main()

###### Inne funkcje wbudowane i wyższego rzędu:
## You can use the following operations available as a function:
## Math operations: add(), sub(), mul(), floordiv(), abs()
## Logical operations: not_(), truth()
## Bitwise operations: and_(), or_(), invert()
## Comparisons: eq() -> equal to, ne() -> not equal, lt()->less than,
## le()-less or equal, gt() -> greater than, and ge() -> greater or equal
## Object identity: is_(), is_not()

# import functools, operator
# list2 = [1,2,3,4]
# resultReduce2 = functools.reduce(operator.mul, list2, 1)
# print(resultReduce2)


############################### Teoria: Funkcja z dowolną liczbą argumentów wejściowych (*args)  #########################
### def nazwa_funkcji(*args):
###    instrukcje
##     return obiekt                 *args - krotka argumentów pozycyjnych

###### Wyrażenie “args” bierze się z od słowa “arguments” czyli argumenty i jest to zazwyczaj zmienna,
###### która zawiera tuple argumentów pozycyjnych. Wyrażenia z jedną gwiazdką (*) używamy gdy do funkcji
### chcemy przekazać dowolną liczbę argumentów pozycyjnych (czyli takich dla których
### przy wywołaniu funkcji nie podajemy ich nazwy, a przypisanie wartości bazuje na kolejności argumentów dlatego
### args - argumenty umieszczane są w krotce/tupli po której możemy iterować args[0], args[1] itd.
## używamy *args gdy nie są istotne dla nas nazwy zmiennych
### Pamiętaj aby parametr *args umieszczać na końcu listy parametrów w definicji funkcji!


################################## Przykład 1  suma dowolnego ciągu cyfr
# def suma(*args):
#     if not args:                        # wkazane jest kontrolowanie przypadku braku argumentów
#         return('brak argumentów')
#     return(sum(args))
#
# print(suma(1,2,3))
# print(suma(1,2,3,4,5,6))


################################### Przykład 2:  suma dowolnego ciągu cyfr plus wartość stałej
# def suma2(x,*args):
#     sumaLiczb = x + sum(args)
#     return(sumaLiczb)
#
# print(suma2(100,1,2,3))

#################################### Przykład 3:  suma pierwszych 4 cyfr dowolnego ciągu cyfr
# def suma3(*args):
#     if bool(args):
#         sumaLiczb = args[0] + args[1] + args[2] + args[3]
#     else:
#         sumaLiczb = 0
#     
#      print(sumaLiczb)
#     return(None)
#
# suma3(1,2,3,4,5,6,7,8,9,10)
# suma3()

#########################################################################################################
######### funkcje z dowolną liczbą argumentów kluczowych (**kwargs) ############
### ** kwargs pozwala przekazywać zmienną długość argumentów ze słowami kluczowymi do funkcji.
### W przypadku gdy do naszej funkcji chcemy przekazywać argumenty, które wyróżniają
### się nazwą możemy użyć parametru z dwoma gwiazdkami (**).
### Przekazane w ten sposób argumenty są dostępne w funkcji w postaci słownika.
### Jego pary klucz-wartość stanowią nazwa i wartość przekazanego argumentu.
### używamy **kwargs gdy istotna dla nas jest nazwa zmiennych

# def nazwa_funkcji(**kwargs):
#     instrukcje
#     return obiekt       # kwargs - słownik argumentów kluczowe

######## wstaw jako argument funkcji:  *kwargs  ########################################

## “kwargs” z j.ang. “keyword arguments” czyli argumenty nazwane
## i zmienna taka zawiera pary nazwa-wartość argumentu.

## Przykład
# def slownik(**kwargs):
#    for klucz, wartosc in kwargs.items():
#        print(klucz, wartosc)
#
# slownik(a=1, b=2, c=3)

# def witaj(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))
#
# witaj(name="yasoob")



######### Example
### 2 sklepy z różnymi produktami
# def test_kwargs(id_sklep = 0, liczba_pracownikow = 5, **kwargs):
#     print(id_sklep)
#     print(liczba_pracownikow)
#     print(kwargs)
#
# test_kwargs(liczba_pracownikow = 3, mleko=100, woda=500)
# test_kwargs(2, liczba_pracownikow = 15, drabina=500, cement=200)

########################################## Zapamiętaj:
#### 1. “args” i “kwargs” możesz zastąpić dowolnymi innymi nazwami zmiennych
#### 2. Pamiętaj umieszczając w definicji funkcji wyrażenie z jedną lub dwoma gwiazdkami
### pozwalamy na przekazywanie do niej argumentów w dowolniej liczbie i nazwie.
### bez konieczności konkretnego określenia tych parametrów.
### 3. Pamiętaj o kolejności – wyrażenie z dwoma gwiazdkami
### musi być na końcu, z jedną gwiazdką wcześniej, a pozostałe zdefiniowane argumenty na początku.


#### Gwiazdek możesz również używać w wywołaniu funkcji.
#### Jest to tak zwane rozpakowywanie list i słowników z argumentami.
#### Jeżeli funkcja przyjmuje kilka argumentów i posiadasz listę,
#### która zawiera argumenty, które chcesz przekazać do tej funkcji
#### wystarczy poprzedzić nazwę listy gwiazdką zamiast podawać kolejne argumenty ręcznie.

# list_arg = [1, 3, 5]
#
# def rozpakowywanie(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#
#
# rozpakowywanie(*list_arg)     # odpowiednik dużo dłuższego kodu:   rozpakowywanie(list_arg[0], list_arg[1], list_arg[2])
############################################################################################################################################

#########################################################################3
##                      ZADANIA
# # ################################ Task 1
## Write a program using if statement, loop, break(), continue() which takes 2 digits: x, y as input and
### calculate multiplication x*y. The program working if x, y are integer. 
## The program stops working if x or y is equal to 0

## Korzystając z instrukcji sterujących napisz program który będzie wczytywał kolejno z klawiatury 2 liczby,
## a następnie obliczał i wyświetlał na ekranie iloczyn wprowadzonych przez użytkownika liczb,
## program kończy działanie jeżeli uzytkownik wprowadzi cyfrę 0. Użytkownik może wykonać obliczenia tylko na
## liczbach całkowitych (wstaw odpowiedni warunek).

## # ################################ Task 2
## Napisz program, który wyświetli twoje imię i nazwisko, aż zostanie wprowadzone
## poprawny PIN, jeśli nie, wyświetli się komunikat "PIN niepoprawny" 
## Przyjmij że poprawny PIN to 24, a program działa aż znajdzie poprawny pin.
## Argument wejściowy: 2 losowe liczby z przedziału 0-9
## a) 1-wariant rozwiązania zadania: użyj while, break()
## b) 2-wariant rozwiązania zadania: użyj "one line statement"
## c) 3-wariant rozwiązania zadania: utwórz funkcję

################################## Task 3
## utwórz moduł silnia, w którym znajdzie się funkcja silnia (użyj lammbda)
## korzystając z modułu silnia, oblicz symbol Newtona 
## (tu wzór http://www.fizykon.org/wzory/wzory_matem_kombinatoryka.htm)
## dla dowolnych 2 liczb wskazanych przez użytkownika
## a) 1-wariant rozwiązania zadania: użyj lammbda
## b) 2-wariant rozwiązania zadania: użyj funkcji wbudowanej prod z pakietu math

# ########################## Task 4
# # Write a script to filter out only the even items from a list (i.e. made from range(1, 100))
# # using filter() and lambda functions.
# #  The numbers obtained should be printed in a comma-separated sequence on a single line.

######################### Task 5
#### Write a script, using reduce(), which will multiply elements in range (1, 100)

# ########################## Task 6
## Wczytaj poniższy fragment tekstu opisujący komputer
## Napisz funkcję która ustali liczbę występujących w tym tekście kluczowych wyrazów
## Ciąg nazw i liczba wyszukiwanych wyrazów jest dowolna, jednak:
## a) kluczowe wyrazy stanowią 2 kweredy: "komputera", "skaner"
## b) inne dodatkowe kluczowe wyrazy wprowadza użytkownik w formie listy

# text = 'Wczytywanie do komputera tekstów, ilustracji, fotografii, itp. jest '   \
#        'możliwe dzięki urządzeniom zewnętrznym zwanym skanerami. Skaner to ' \
#        'urządzenie umożliwiające wprowadzenie do komputera grafiki i tekstu. ' \
#        'Dzięki zamianie skanowanej płaszczyzny na postać cyfrową może ona zostać ' \
#        'wyświetlona na ekranie monitora i zapisana na dysku w odpowiednim formacie ' \
#        'oraz może zostać poddana komputerowej obróbce. Skanery dzielimy na dwie podstawowe ' \
#        'grupy: ręczne (np. czytniki kodów paskowych) oraz stacjonarne. Najpopularniejszym ' \
#        'typem skanerów są skanery stacjonarne płaskie, które umożliwiają skanowanie ' \
#        'dokumentów o formacie A3 lub A4 i ich pochodnych. Są one podłączane do ' \
#        'komputerów przez port równoległy, uniwersalną magistralę szeregową lub sterownik SCSI.'
#
# print(text)

# ########################## Task 7
## Utwórz funkcję o nazwie "ZdanieRozdziel.py", która wczyta od użytkownika pewien dowolny tekst,'
## a następnie podzieli go na zdania (zakładamy, że jednoznacznie kropka rozdziela zdania)'
## funkcja w zależności od ustawionych kolejnych parametrów wejściowych funkcji 
## (ustaw domyślnie argumenty wejściowe: True), 
## może ale nie musi wyświetlić następujące informacje: 
## ile w każdym zdaniu jest fragmentów rozdzielonych przez określony znak np. ',', ';' 
## (domyślnie argument wejściowy to przecinek: ',')
## ile w każdym zdaniu jest wyrazów (zakładamy, że spacja oddziela wyrazy w zdaniu)
## użyj odpowiednich metod dla zmiennych typu string 
## np. split do rozdzielenia elementów: x = ‘blue,red,green’,   x.split(“,”)

# ########################## Task 8
## Zaprojektuj program służący do obsługi prostej bazy danych dla sklepu z
## dowolnej branży o różnej liczbie pracowników. Program zapisuje do kolejnych list
## liczby produktów dostarczonych w danym dniu (nazwa listy odpowiada nazwie towaru)
## liczba towarów powinna być zapamiętana 

# Przetestuj swój program dla różnych przypadków dostawy towaru
# Pamiętaj że asortyment sprzedawanego towaru ulega zmianie
# Użyj kwargs
# ########################## Task 9
## W module pole_prostokata.py 
## Zdefiniuj funkcję która obliczy pole powierzchni prostokąta
## W module pole_trojkata.py 
## Zdefiniuj funkcję która obliczy pole powierzchni trójkąta
# W module pola.py
## Korzystając z modułów pole_prostokata i pole_trojkata
## napisz funkcję która ma możliwość obliczenia pola prostokąta, trójkąta i kwadratu
## Użyj zmiennych globals, utwórz moduł globals.py w którym będą przechowywane 
## domyślne wartości dla boków prostokąta, trójkąta, kwadratu (równe 1)
# ########################## Task 10
## Zdefiniuj funkcję wyższego rzędu która ma możliwość obliczenia
## pole powierzchni prostokąta i pola powierzchni trójkąta
## Nie modyfikując zawartości w/w funkcji, użyj dekoratora i dodaj możliwość 
## obliczenia pola kwadratu

# ########################## Task 11
## Utwórz funkcję która umożliwia logowanie na serwer
## Ma dwa argumenty wejściowe:
## user i password (domyślne wartości odpowiednio: 'edek2003', 'Wsx123')
## a) nie modyfikując zawartości w/w funkcji, użyj dekoratora i dodaj dodatkowe
## pola tj. host, port
## b) nie modyfikując zawartości w/w funkcji, użyj dekoratora i  daj możliwość 
## wprowadzania dodatkowych innch pól użytkownikowi (wprowadzane jako słownik
##  np. {'data_base': 'https://pl.wikipedia.org'})

# ########################## Task 12 * dla chętnych
## Zdefiniuj funkcję ciag_gometryczny, która dla podanych trzech parametrów:
## n=numer elementu ciągu, a1=wartość pierwszego elementu ciągu (domyślnie: 1),
## q=wartość iloczynu ciągu geometrycznego (domyślnie: 2) 
## zwróci w zależności od ustawianych parametrów funkcji
## a) wartość n-tego elementu ciągu geometrycznego

## Następnie korzystając z dekoratora udoskonal swoją funkcję,
## dodaj możliwość obliczenia sumy elementów ciągu geometrycznego





