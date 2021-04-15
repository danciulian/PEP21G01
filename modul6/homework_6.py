""" Homework 5 - needs to be presented before exam day
O fabrica de masini are nevoie de un obiect iterabil care sa contina seriile si loturile masinilor produse
in ziua respectiva.

Seriile si loturile sunt numere intregi de tip int

Un lot este alcatuit din 20 de masini si primele 10 din lot sunt cu volan pe dreapta iar urmatoarele 10
cu volan pe stanga

Numerotarea loturilor incepe de la prima masina produsa cu seria 1 si lot 1

Ziua de lucru stocata in obiectul contruit de voi poate incepe cu orice numar de serie si numarul de bucati
produse in acea zi poate avea orice valoare

Obiectul iterat va returna numerele loturilor din care fac parte masinile din acea zi, numerotarea lor
a inceput de la prima masina produsa cu seria 0 si lot 0

Masinile cu serii pare sunt cu volan pe dreapta iar cele cu serii impare cu volan pe stanga

1)Definire: 40p
  - Creati o clasa pentru un obiect iterabil
   a) constructorul primeste doua argumente de tip int, seria de inceput si numarul de bucati.
   ex: (101, 41) 10p

   b) obiectul are doua metode: prima returneaza o lista cu seriile cu volan pe dreapta si a doua o
   lista cu seriile cu volan pe stanga 15p

   c) interator-ul returnat de object va contine loturile din care fac parte seriile din
   obiectul curent  15p

2) Executie: 40p
- Creati o instanta a clasei de mai sus dand ca argumente: serie_inceput 314, bucati 90. 10p
- Iterati obiectul creat si salvati fiecare valoare din iteratie in acelas fisier pe linie noua. 30p

3) Documentatie: 20p
   a) adaugati type hints 5p
   a) documentati modulul 5p
   b) documentati clasele 5p
   c) documentati metodele 5p
"""


class CarFactory():
    series_lhd = []
    series_rhd = []
    work_done_lhd = []
    work_done_rhd = []

    def __init__(self, beginning_series: int, no_pieces: int):
        self.beginning_series = beginning_series  #seria de inceput
        self.no_pieces = no_pieces                #numarul de bucati
    def __iter__(self):
        all_series = []
        for series in self.work_done_lhd + self.work_done_rhd:
            all_series.append(series)
        return CarIter(all_series)

    def lhd(self):
        list_no = [] #aici am pus toate masinile de la 314 la 404
        for i in range(self.beginning_series, self.no_pieces + self.beginning_series + 1):
            list_no.append(i)
        print('toate serile:', list_no)

        start_rest = self.beginning_series % 10
        start_rest_list = list_no[:10 - start_rest]
        print('start_rest_list:', start_rest_list)

        end_rest = (self.no_pieces + self.beginning_series) % 10
        end_rest_list = list_no[-end_rest - 1:]
        print('end_rest_list:', end_rest_list)

        grupe_10 = []
        for i in range(self.beginning_series // 10, (self.no_pieces + self.beginning_series) // 10):
            if i % 2 == 0:
                grupe_10.append(i)
        print('grupe_10:', grupe_10)
        for j in grupe_10:
            for k in range(0, 10):
                self.series_lhd.append((10 * j)+ k)
        print('series_lhd_I:', self.series_lhd)

        for j in range(0, 10 - len(start_rest_list)):
            if (self.beginning_series // 10) % 2 == 0:
                self.series_lhd.pop(0)
        print('series_lhd_II:', self.series_lhd)

        if ((self.no_pieces + self.beginning_series) // 10) % 2 == 0:
            self.series_lhd.extend(end_rest_list)
        self.work_done_lhd = self.series_lhd


        return self.work_done_lhd


    def rhd(self):
        list_no = [] #aici am pus toate masinile de la 314 la 404
        for i in range(self.beginning_series, self.no_pieces + self.beginning_series + 1):
            list_no.append(i)
        print('toate serile:', list_no)

        start_rest = self.beginning_series % 10
        start_rest_list = list_no[:10 - start_rest]
        print('start_rest_list:', start_rest_list)

        end_rest = (self.no_pieces + self.beginning_series) % 10
        end_rest_list = list_no[-end_rest - 1:]
        print('end_rest_list:', end_rest_list)

        grupe_10 = []
        for i in range(self.beginning_series // 10, (self.no_pieces + self.beginning_series) // 10):
            if i % 2 != 0:
                grupe_10.append(i)
        print('grupe_10:', grupe_10)
        for j in grupe_10:
            for k in range(0, 10):
                self.series_rhd.append((10 * j)+ k)
        print('series_rhd_I:', self.series_rhd)

        if (self.beginning_series // 10) % 2 != 0:
            for j in range(0, 10 - len(start_rest_list)):
                self.series_rhd.pop(0)
        print('series_rhd_II:', self.series_rhd)

        if ((self.no_pieces + self.beginning_series) // 10) % 2 != 0:
            self.series_rhd.extend(end_rest_list)
        self.work_done_rhd = self.series_rhd


        return self.work_done_rhd

class CarIter():
    def __init__(self, series):
        self.series = series

    def __iter__(self):
        return self

    def __next__(self):
        if not self.series:
            raise StopIteration
        else:
            return self.series.pop(0)


obj_carfactory1 = CarFactory(34, 64)
print("LHD method:", obj_carfactory1.lhd())
print("RHD method:", obj_carfactory1.rhd())

# with open('iuliu02', 'w') as file:
for i in obj_carfactory1:
    print(i)
