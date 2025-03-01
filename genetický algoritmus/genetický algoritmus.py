import random
import tkinter
import time
import matplotlib.pyplot as plt

start_time= time.time()
canvas = tkinter.Canvas(height=800, width=800)
canvas.pack()
#lock staty
farmar_count = 100 # nastavitelny pocet na simulacie
genoms = 28  # nastavitelny pocet genomov max 28
generacie = 1000  # nastavitelny pocet na kolko generacii cheme simulaciu spustit



# Ddefinuje obejkt farmara ktory ma v sebe jeho pohybi ako genom a fittnes
class Farmar:
    def __init__(self):
        self.geni = random_gen(genoms)  # volanie funkcie na random generaciu
        self.fittnes = 0  # setuje fittnes na 0

farby ={
    1: 'mediumspringgreen', 2: 'cornflowerblue', 3: 'peru', 4: 'lightsteelblue', 5: 'skyblue', 6: 'orchid', 7: 'orange', 8: 'gold', -1: 'gray', 0:'white',
    9: 'sienna', 10: 'turquoise', 11: 'coral', 12: 'thistle', 13: 'green', 14: 'darkslategray', 15: 'red', 16: 'aqua', 17: 'olive',
    18: 'coral', 19: 'orange', 20: 'dimgray', 21: 'pink', 22: 'violet', 23: 'greenyellow', 24: 'khaki', 25: 'hotpink', 26: 'tomato', 27: 'teal',
    28: 'orchid'

}
def print_final(pole, fit):
    y = 60
    inedx = 0
    colour= 'white'
    for _ in range(10):
        x = 40
        for j in range(12):
            if pole[inedx] in farby:
                colour = farby[pole[inedx]]
            canvas.create_rectangle(x, y, x + 60, y + 60, fill=colour)
            if pole[inedx] == -1:
                canvas.create_text(x + 30, y + 30, text="K", fill='red',font='20')
            else:
                canvas.create_text(x + 30, y + 30, text=pole[inedx],fill='black',font='20')
            inedx += 1
            x = x + 60
        
        y = y + 60
    text= "fittnes"+ str(fit)
    canvas.create_text(400, 20, text= text,font='10')


def create_array():  # vytvorenie tabulky s poziciami kameno ktore su ouznacene v poly ako -1
    # je to liearne pole ktore je oddelene podla riadkov po 12 takze posuny su uskutocnovane skokmi medzi indexmi v tabulke hore a dole ideme po 12 do prava a do lava ideme po 1
    game_board = [0] * 120
    game_board[17] = -1
    game_board[25] = -1
    game_board[40] = -1
    game_board[50] = -1
    game_board[80] = -1
    game_board[81] = -1
    return game_board


def random_gen(count):  # nageneruje pohybi danych členov v populacii
    #nemoze sa opakovat
    #return random.sample(range(1, 44), count)
    #moze sa opakaovať
    return random.choices(range(1, 44),k=count)


# vytvory pole ktore obsahuje nam zadany pocet farmarov
def create_population(population_size):
    ludia = []
    for k in range(population_size):
        ludia.append(Farmar())  # vytvory novu instanciu farmara
    return ludia


def print_array(array):  # vypise nam array (cisto len na vizualizacne ucely pri kodovanie)
    count = 0
    for prt in range(10):
        for j in range(12):
            print(array[count], end=' | ')
            count += 1
        print('')
    print("--------------------------------------------------")


#
# ---------------------------------------------------------------
# pozanmky na vstupne body pola + excel tabulka na vyzualizaciu ulozena na pracovnej ploche pod nazvom (tabulka UI)
# z hora 1-12 (0-11)
# z prava 13-22 (11,23,35,47,59,71,83,95,107)
# z dola 34-23 (108-119)
# z lava 44-35 (0,12,24,36,48,60,72,84,96,108)
# Dictionary to map genome values to movement functions

def farmar_move(hracie_pole, farmar_instance, genoms_c, s_board,swch):

    #nie su povolene random moves kedže chceme aby najlepši z danej generacie vždy zbehli rovnako

    z = 1
    check = 0
    for zet in range(genoms_c):
        k = farmar_instance.geni[zet]  # zjednodusena pracovna premenna ktora obsahuje jeden gen daneho farmara

        if k in moves: #ak sa tag nachadza v moves
            index, move_function = moves[k] #tak ho rozodeli na index a pohybovu funkciu
            if hracie_pole[index] in (1, -1):  # sleduje ci je na vstupe kamen alebo či tam uz nahodou nebol
                z -= 1
            else:
                hracie_pole[index] = 1 #označi prejdeny bod
                s_board[index] = z #zapise do poknej tabluky
                check= move_function(hracie_pole, index, s_board, z,check) #prejde na pohybovu funkciu
        z += 1
    #print_array(s_board)
    #check=0 # odkomentuj ak je povolena vnutro farmova blokacia
    if swch==1: #tk vypis posledneho najlepsieho farmara
        
        if check == 0:
            print_final(s_board, hracie_pole.count(1))
        elif check==1:
            print_final(s_board, hracie_pole.count(1)-100)


    fit_value = hracie_pole.count(1)  # spocitame kolko je 1 na poly to nam reprezentuje nas fittnes koeficient podla ktoreho posudzujeme schopnosti nasiech farmarov
    
    if check == 0:
        return int( fit_value)
    elif check == 1:
        return int(fit_value-100)


# =====================================================================================
# definovane pohyby podla mojho turbo špeci algoritmu ktoremu chapem len ja
def dole(pole, akt, sh_board, krok,chck):
    # print(akt,"dole")
    ciklus = 0

    while ciklus < 10 and chck !=1:

        if akt + 12 < 120:# chcek či nevíde z pola
            if pole[akt + 12] == 0: # pozre na ten čo má ist či je volny
                pole[akt + 12] = 1 # ak hej setne ho na 1
                sh_board[akt + 12] = krok # označuje v ktorom kroku prašiel ake policka
                akt = akt + 12 #posunie sa na nove pole ktore si teraz označil

            elif pole[akt + 12] == 1 or pole[akt + 12] == -1 and akt + 1 != 120 and akt - 1 != -1:# ak nomže z dovodu zabratie pola vo vyhradenom smere
                #pozrie či može ist do prava
                if akt + 1 != 12 and akt + 1 != 24 and akt + 1 != 36 and akt + 1 != 48 and akt + 1 != 60 and akt + 1 != 72 and akt + 1 != 84 and akt + 1 != 96 and akt + 1 != 108 and akt + 1 != 120 and  pole[akt + 1] == 0:
                    # ak ano označi ho a posunie sa nanho a zoroven prejde do pohybovej funkcie ktora zabezpečuje pohyb do prava
                    pole[akt + 1] = 1
                    sh_board[akt + 1] = krok
                    chck=do_prava(pole, akt + 1, sh_board, krok,chck)
                    break
                elif akt - 1 != 11 and akt - 1 != 23 and akt - 1 != 35 and akt - 1 != 47 and akt - 1 != 59 and akt - 1 != 71 and akt - 1 != 83 and akt - 1 != 95 and akt - 1 != 107 and akt - 1 != -1 and \
                        pole[akt - 1] == 0:
                    # ak nemože ist do prava a može do lava tak označi prvok na lavo a prejde do funkcie kotra zabezpečuje pohyb do lava
                    pole[akt - 1] = 1
                    sh_board[akt - 1] = krok
                    chck=do_lava(pole, akt - 1, sh_board, krok,chck)
                    break
                else:  # ak nemože ani do prava ani do lava vieme že sa sekol a skonči svoj pohyb
                    return 1


            else:#ak nemože ani do prava ani do lava vieme že sa sekol a skonči svoj pohyb
                break


        else:#ak vide z šachovnice tak skonči
            break
        ciklus += 1#zabezpečuje maximalny size pola v danom smere aby nevznikly nespravne vyseldky alebo infinit loop

    return chck

# zvisne funkcie funguju tak ako ta pred tym len v inom smere
def hore(pole, akt, sh_board, krok,chck):
    # print(akt,"hore")
    ciklus = 0
    while ciklus < 10 and chck !=1:

        if akt - 12 > -1:
            if pole[akt - 12] == 0:
                pole[akt - 12] = 1
                sh_board[akt - 12] = krok
                akt = akt - 12

            elif pole[akt - 12] == 1 or pole[akt - 12] == -1 and akt + 1 != 120 and akt - 1 != -1:


                if akt - 1 != 11 and akt - 1 != 23 and akt - 1 != 35 and akt - 1 != 47 and akt - 1 != 59 and akt - 1 != 71 and akt - 1 != 83 and akt - 1 != 95 and akt - 1 != 107 and akt - 1 != -1 and \
                        pole[akt - 1] == 0:
                    pole[akt - 1] = 1
                    sh_board[akt - 1] = krok
                    chck=do_lava(pole, akt - 1, sh_board, krok,chck)
                    break
                elif akt + 1 != 12 and akt + 1 != 24 and akt + 1 != 36 and akt + 1 != 48 and akt + 1 != 60 and akt + 1 != 72 and akt + 1 != 84 and akt + 1 != 96 and akt + 1 != 108 and akt + 1 != 120 and \
                        pole[akt + 1] == 0:
                    pole[akt + 1] = 1
                    sh_board[akt + 1] = krok
                    chck=do_prava(pole, akt + 1, sh_board, krok,chck)
                    break

                else:
                    return  1

            else:
                break
        else:
            break
        ciklus += 1

    return chck


def do_prava(pole, akt, sh_board, krok,chck):
    # print(akt,"prava")
    ciklus = 0
    while ciklus < 12 and chck !=1:
        if akt + 1 < 120:
            if akt + 1 != 12 and akt + 1 != 24 and akt + 1 != 36 and akt + 1 != 48 and akt + 1 != 60 and akt + 1 != 72 and akt + 1 != 84 and akt + 1 != 96 and akt + 1 != 108 and akt + 1 != 120:
                if pole[akt + 1] == 0:
                    pole[akt + 1] = 1
                    sh_board[akt + 1] = krok
                    akt = akt + 1

                elif pole[akt + 1] == 1 or pole[akt + 1] == -1:

                    if akt + 12 < 120 and pole[akt + 12] == 0:
                        pole[akt + 12] = 1
                        sh_board[akt + 12] = krok
                        chck=dole(pole, akt + 12, sh_board, krok,chck)
                        break
                    elif akt - 12 > 0 and pole[akt - 12] == 0:
                        pole[akt - 12] = 1
                        sh_board[akt - 12] = krok
                        chck=hore(pole, akt - 12, sh_board, krok,chck)
                        break
                    else:
                        return  1


            else:
                break
        else:
            break
        ciklus += 1

    return chck


def do_lava(pole, akt, sh_board, krok,chck):
    # print(akt,"lava")
    ciklus = 0
    while ciklus < 12 and chck !=1:
        if akt - 1 > -1:
            if akt - 1 != 11 and akt - 1 != 23 and akt - 1 != 35 and akt - 1 != 47 and akt - 1 != 59 and akt - 1 != 71 and akt - 1 != 83 and akt - 1 != 95 and akt - 1 != 107 and akt - 1 != -1:
                if pole[akt - 1] == 0:
                    pole[akt - 1] = 1
                    sh_board[akt - 1] = krok
                    akt = akt - 1

                elif pole[akt - 1] == 1 or pole[akt - 1] == -1:
                    if akt - 12 > 0 and pole[akt - 12] == 0:
                        pole[akt - 12] = 1
                        sh_board[akt - 12] = krok
                        chck=hore(pole, akt - 12, sh_board, krok,chck)
                        break
                    elif akt + 12 < 120 and pole[akt + 12] == 0:
                        pole[akt + 12] = 1
                        sh_board[akt + 12] = krok
                        chck=dole(pole, akt + 12, sh_board, krok,chck)
                        break

                    else:
                        return  1

            else:
                break
        else:
            break
        ciklus += 1

    return chck

moves = {
    1: (0, dole), 2: (1, dole), 3: (2, dole), 4: (3, dole),
    5: (4, dole), 6: (5, dole), 7: (6, dole), 8: (7, dole),
    9: (8, dole), 10: (9, dole), 11: (10, dole), 12: (11, dole),
    13: (11, do_lava), 14: (23, do_lava), 15: (35, do_lava),
    16: (47, do_lava), 17: (59, do_lava), 18: (71, do_lava),
    19: (83, do_lava), 20: (95, do_lava), 21: (107, do_lava),
    22: (119, do_lava),
    23: (119, hore), 24:(118, hore), 25:(117, hore),
    26: (116, hore), 27:(115, hore), 28:(114, hore),
    29: (113, hore), 30:(112, hore), 31:(111, hore),
    32: (110, hore), 33:(109, hore), 34:(108, hore),
    35: (108, do_prava),36:(96, do_prava), 37:(84, do_prava),
    38: (72, do_prava), 39:(60,do_prava),40:(48,do_prava),
    41: (36, do_prava),42:(24, do_prava), 43:(12, do_prava),
    44: (0,do_prava),
    
}
# =====================================================================================================
#genetick algorithm
def vyber_top_farmar(populacia,pocet):

    upratane_pole= sorted(populacia, key=lambda x: x.fittnes, reverse=True)
    return upratane_pole[:pocet]
def mutacia_function(farmar_pred_m):
    #definuje noveho farmara do ktoreho bude vlozeny zmutovany farmar kroy bol poslany do funkcie
    zmutovany_farmar= Farmar()
    mutacia_count=2
    zmutovany_farmar.geni= farmar_pred_m.geni.copy()# prekopiruju sa geni
    for _ in range(mutacia_count):
        mutovaci_index= random.randint(0,genoms-1)#nahodne vygeneruje index na ktorom sa bude mutovat
        zmutovany_farmar.geni[mutovaci_index]= random.choice(range(1,44))#zvoly ako sa zmutuje



    return zmutovany_farmar

def krizenie(rodic1,rodic2):
    #bod zmeny je v strede
    bod_krizenia= genoms//2
    #bod_krizenia= random.choice(range(0,genoms-1))

    #vymeni geni v polke
    dieta_1_gen=rodic1.geni[:bod_krizenia]+rodic2.geni[bod_krizenia:]
    dieta_2_gen=rodic2.geni[:bod_krizenia]+rodic1.geni[bod_krizenia:]

    #definuje deti ako farmarov
    dieta1= Farmar()
    dieta2= Farmar()

    #pridely detom ich geny
    dieta1.geni=dieta_1_gen
    dieta2.geni=dieta_2_gen

    return dieta1,dieta2

def dopln_populaciu(top_farmar, populacia,pocet):
    #top 10 farmarov sa prenesie do novej populacie
    nova_populacia= top_farmar.copy()
    #vyberie sa dalšich 20 kory sa budu krížit
    farmari_na_krizenie= populacia[pocet:3*pocet-1]

    for index_f in range(0,len(farmari_na_krizenie)//2):
        #poistka na seg fault
        if index_f+1< len(farmari_na_krizenie):
            #vyberu sa dvaja rodicia jeden zo zaciatku a jeden z konca a poslu sa do funkcie na krizenie 0---> strad <---počet vybraných farmraov
            rodic_1= farmari_na_krizenie[index_f]
            rodic_2= farmari_na_krizenie[len(farmari_na_krizenie)-index_f-1]
            #vartia sa deti
            dieta_1, dieta_2= krizenie(rodic_1,rodic_2)
            #pridame deti do novej populacie
            dieta_1=mutacia_function(dieta_1)
            dieta_2=mutacia_function(dieta_2)
            nova_populacia.append(dieta_1)
            nova_populacia.append(dieta_2)
    #vyberie sa poslednych 20 na mutovanie
    farmari_na_mutovanie= populacia[3*pocet:5*pocet-1]
    for farmar in farmari_na_mutovanie:
        #po jednom sa poslu do funkcie ktora ich zmutuje
        zmutovany_farmar= mutacia_function(farmar)
        #pridaju sa do populacie
        nova_populacia.append(zmutovany_farmar)
    #poistka ak by chybali clenovia tak sa dogeneruju
    while len(nova_populacia)<farmar_count:
        nova_populacia.append(Farmar())

    return nova_populacia
# =====================================================================================================
population = create_population(farmar_count)  # vytvory nam prvotnu populaciu
fit_trend=[]
for gen in range(generacie):#cyklus generacii farmarov
    for i in range(farmar_count):  # ciklus na otestovanie schopnosti farmarov
        board = create_array()  # nova hracia dostka podla nami zadaneho rozmiestnenia kamenov rozmer je nastaveny na 12x10 a 44 vstupnych bodov
        show_board = create_array()  # vytvory hraciu plochu ktora vypisuje v akom kroku presiel ktoru scasť
        fittnes = farmar_move(board, population[i], genoms, show_board, 0)  # po prejdeni nam kalkuluje kolko policok farmar pooral
        population[i].fittnes=fittnes
    #print("top fittnes s genracie\t",gen,"\t:\t",max(population,key=lambda x: x.fittnes).fittnes ) #pribeh generacii a evolucia členov
    fit_trend.append(max(population,key=lambda x: x.fittnes).fittnes)

    pocety= farmar_count//5 #rozdeli populaciu na 5tiny
    top_farmars= vyber_top_farmar(population,pocety)#vyper top farmarov ktory pojdu do dalšej generacie
    population= dopln_populaciu(top_farmars, sorted(population,key=lambda x: x.fittnes, reverse=True),pocety)#doplni populaciu aby sme mali full populaciu

final_board=create_array()#vytvory klasicku bordu
final_show_board=create_array()#vytvory bordu na vysledok
best_farmar= max(population, key= lambda x: x.fittnes)#vyberie sa najlepši farmar z finalnej generacie
farmar_move(final_board, best_farmar, genoms, final_show_board, 1)#nehame ho este raz prebehnut dane pole a vypise sa tk okne jeho dosiahnutý ciel

end_time= time.time()

final_time= end_time-start_time
print("kod bezal: ",final_time,"sekund" )

plt.plot(fit_trend)  
plt.show()