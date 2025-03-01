import matplotlib.pyplot as plt #využivam na vykreslenie
import random #využivam na nahodne generovanie bodov
import numpy as np #využivam na matematické vypočty
from collections import Counter, defaultdict#Counter využivam na hladanie najčastejšieho prvku v poly
import time #využivam na čas za ktorý mi zbehly jednotlivé časti kodu

dot_count = 40000 #počet bod
k_values = [1, 3, 7, 15]#k susedov
grid_size = 350#velkosť blokov na ktore bude vypisove okno rozdelené

good_count = 0#counter na uspešnoť classifikácie
generated_points = []#pole na generovane body
initial_classes = []#pol ktore obsahuje prvotnú klasifikaciu indexy tried sa zhoduju s indexamy generovaných bodv
grid_points = defaultdict(list)#knižnica na ukladanie ktoré body na nachádzaju v ktorých blokoch siete
start_time = time.time()#spušta časovač na celý beh programu


classes = ['R', 'G', 'B', 'P']#pole tried
#knižnica kde ku každej triede je pridelená farba
class_as_color = {
    'R': 'red',
    'G': 'green',
    'B': 'blue',
    'P': 'purple'
}
#knižnica bodov zo zadania
initial_starting_point = {
    'R': np.array([[-4500, -4400], [-4100, -3000], [-1800, -2400], [-2500, -3400], [-2000, -1400]]),
    'G': np.array([[4500, -4400], [4100, -3000], [1800, -2400], [2500, -3400], [2000, -1400]]),
    'B': np.array([[-4500, 4400], [-4100, 3000], [-1800, 2400], [-2500, 3400], [-2000, 1400]]),
    'P': np.array([[4500, 4400], [4100, 3000], [1800, 2400], [2500, 3400], [2000, 1400]])
}

#zistuje v ktorom bloku sa bod nachádza
def get_grid_cell(x, y):
    return x // grid_size, y // grid_size

def get_neighboring_cells(cell_x, cell_y, level):
    #pole susedov
    neighbors = []
    #level testuje iba 3x3 bloky
    if level == 1:
        #cyklus na prechadzanie po x osi
        for dx in range(-1, 2):
            #cyklus na prechadzanie po y osi
            for dy in range(-1, 2):
                #pridanie do pla susedný blok
                neighbors.append((cell_x + dx, cell_y + dy))
    #level 2 testuje 5x5 bloky
    elif level == 2:
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                neighbors.append((cell_x + dx, cell_y + dy))
    #vracia pole susedných blokv
    return neighbors
def reset():
    #resetuje pole aby obsahovalo iby body zo zadania
    return {cls: points.copy() for cls, points in initial_starting_point.items()}

def euclid(bod, reference):
    #počítanie euklidovskej vzdialenosti medzi dvoma bodmi
    return np.linalg.norm(reference - bod)

def classify(X, Y, k, clas, starting_point, grid):
    global good_count
    global grid_points
    #definuje bod ako tuple
    bod = np.array([X, Y])
    #ploe ktore obsahuje touply (vzdialosť od podu ktorý klasifikujeme, trieda bodu ktory hladameako KNN)
    dist_cls = []
    #definovanie bloku pre klasifikovaný blok v sieti
    grid_x, grid_y = get_grid_cell(X, Y)
    #cyklus ktory berie susedné bloky z levlu 1 3x3
    for cell in get_neighboring_cells(grid_x, grid_y, 1):
        #cyklus ktorý vyberá body z bloku
        for point in grid_points[cell]:
            #zistuje vzdialesot bodu a klasifikovaného bodu
            distance = euclid(bod, point[:2])
            #pridá sa do pola vzdialesť a trida
            dist_cls.append((distance, point[2]))
    #ak sme nanašli dostatok bodv pre KNN
    if len(dist_cls) < k:
        #reset pola
        dist_cls=[]
        #cyklus ktorý berie susedné bloky v 5x5
        for cell in get_neighboring_cells(grid_x, grid_y, 2):
            #berie body z blokov
            for point in grid_points[cell]:
                #zistuje vzdialenosť
                distance = euclid(bod, point[:2])
                #pridáva do pola
                dist_cls.append((distance, point[2]))
    #ak nemáme stále dostatok bodov prechádzame na porovnávanie klasifikovaného bodu zo všetkými
    if len(dist_cls) < k:
        #reset pola
        dist_cls=[]
        #cyklus pre všetky klasifikované body
        for cls, points in starting_point.items():
            #vyberá body
            for point in points:
                #zistuje vzdialenosť
                distance = euclid(bod, point)
                #pridavam do pola
                dist_cls.append((distance, cls))
    #usporiadanie pola podla vzdialeností
    dist_cls.sort(key=lambda x: x[0])
    #vybranie iba k najbližšich bodov
    k_nearest_classes = [x[1] for x in dist_cls[:k]]
    #zistíme najčastejšiu tridu z k najbližích bodov
    most_common_class = Counter(k_nearest_classes).most_common(1)[0][0]
    #ak sa táto trieda rovná s prvotnou klasifikáciou tak pridá counter
    if most_common_class == clas:
        good_count += 1
    #vloženie bodu do knižnice všetkých klasifikovaných bodov
    starting_point[most_common_class] = np.vstack([starting_point[most_common_class], bod])
    #pridanie do knižnice blokv aby sme vedeli v akom bloku sa bod nachádza
    grid_points[(grid_x, grid_y)].append((X, Y, most_common_class))
    #vracia triedu a knižnicu
    return most_common_class, starting_point

def zobrazit():
    global good_count
    #definovanie vykraslenia na 2x2 a velkosť okna 10x10
    _, axs = plt.subplots(2, 2, figsize=(10, 10))
    #definovanie aby nam tieto okná bralo ako linerane pole
    axs = axs.flatten()
    #čas jednej iterácie
    itr_time = time.time()
    #cyklus pre všetky k hodnoty
    for i, k in enumerate(k_values):
        #reset counteru na úspešnosť klasifikácie
        good_count = 0
        #reset knižnice blokov
        grid_points.clear()
        #reset knižnice aby v nom boly iba body zo zadania
        str_p = reset()
        #vyberieme okno v ktorom vykreslujeme
        ax = axs[i]
        #cyklus ktory vyberá z knižnice pre body zandané zo zadania
        for cls, points in str_p.items():
            for point in points:
                #zistíme blok v ktorom sa bod nachádza
                grid_x, grid_y = get_grid_cell(point[0], point[1])
                #pridáme do knižnice blokov
                grid_points[(grid_x, grid_y)].append((point[0], point[1], cls))

        for cls, points in str_p.items():
            #vykreslenie bodov zo zadania
            ax.scatter(points[:, 0], points[:, 1], color=class_as_color[cls], s=7)
        #vyberanie bodov z generovaných bodov
        for (X, Y), cls in zip(generated_points, initial_classes):
            #klsifíkacia jednotlivých bodv
            new_cls, stt_p = classify(X, Y, k, cls, str_p, grid_points)
        #zistenie úspešnosti
        accuracy = (good_count / dot_count) * 100
        #výpis úspešnosti
        print(f"Classification accuracy for k={k}: {accuracy:.2f}%")
        #zistenie času ukončenia iteracie
        end_time = time.time()
        #prepočet na čas
        total_time = end_time - itr_time
        #rozdelenie na minuty a sekundy
        minutes, seconds = divmod(total_time, 60)
        #výpis času
        print(f"K= {k} time: {int(minutes)} min {seconds:.2f} sec")
        #začatie času novej iterácie
        itr_time = time.time()
        #definovanie aby nam nevykreslovalo osi
        ax.set_xticks([])
        ax.set_yticks([])
        #cyklus na vykreslenie bodv pre dané k
        for cls, points in stt_p.items():
            ax.scatter(points[:, 0], points[:, 1], color=class_as_color[cls], s=7)
    print("---------------------------")
    #vypíše čas celkového behu programu
    end_time = time.time()
    total_time = end_time - start_time
    minutes, seconds = divmod(total_time, 60)
    print(f"Total runtime: {int(minutes)} min {seconds:.2f} sec")
    plt.tight_layout(rect=[0, 0, 1, 1])
    plt.show()

def generate_point(previous_class):
    #definovanie klasi podla ktorej bude generovaný bod
    new_cls=previous_class
    while True:
        #podmienka na šum
        if random.random() < 0.99:
            #ak je červeny vygeneruje sa v x=-5000,500 y=-5000,500
            if new_cls == 'R':
                x, y = np.random.randint(-5000, 500), np.random.randint(-5000, 500)
                cls = 'R'
            # ak je zelený vygeneruje sa v x=-500,5000 y=-5000,500
            elif new_cls == 'G':
                x, y = np.random.randint(-500, 5000), np.random.randint(-5000, 500)
                cls = 'G'
            # ak je modrý vygeneruje sa v x=-5000,500 y=-500,5000
            elif new_cls == 'B':
                x, y = np.random.randint(-5000, 500), np.random.randint(-500, 5000)
                cls = 'B'
            # ak je fialový vygeneruje sa v x=-500,5000 y=-500,5000
            elif new_cls == 'P':
                x, y = np.random.randint(-500, 5000), np.random.randint(-500, 5000)
                cls = 'P'
        else:
            #ak je šum 1 pecento vygeneruje sa x=-5000,5000 y=-5000,5000
            x, y = np.random.randint(-5000, 5000), np.random.randint(-5000, 5000)
            #trieda zostáva
            cls = new_cls
        #definovanie bodu ako tuple
        point = (x, y)
        #zistenie či na danej suradnici už nie je bod
        if point not in generated_points:
            return x, y, cls

def start(dot_count):
    #ak počet bodov neni delitelný počtom tried
    if dot_count % len(classes) != 0:
        raise ValueError("dot_count must be a multiple of the number of colors")
   #definovanie pola pre jednotlive triedy
    counts = {cls: 0 for cls in classes}
    #kolko bodov potrebujem pre 1 tiredu
    total_dots_per_color = dot_count // len(classes)
    #definovanie poradia na seqvenčné generovanie
    color_sequence = ['R', 'G', 'B', 'P']
    #posledná tireda je prázna
    last_cls = None
    #kym nemám dostatok bodov
    while sum(counts.values()) < dot_count:
        # cyklus na definovanie tridy podla seqvencie
        for cls in color_sequence:
            #chcek aby sme zaitili že v jendej triede neni viac bodov ako by malo
            if counts[cls] < total_dots_per_color:
                #poistak aby neboli dve triedy po sebe rovnaké
                if cls == last_cls:
                    continue
                #generovanie daného boud
                X, Y, cls = generate_point(cls)
                #zvyšenie počtu pre danú tiredu
                counts[cls] += 1
                #pridanie bodu do pola všetkých bodov
                generated_points.append((X, Y))
                #pridanie tridy do pola generovaných tried
                initial_classes.append(cls)
                #nastavenie poslednej použitej triedy
                last_cls = cls

    print(f"Counts after generation: {counts}")
    print(f"Total generated points: {counts['R'] + counts['G'] + counts['B'] + counts['P']}")

#spustenie generacie bodv
start(dot_count)
print(f"Simulation for {dot_count} dots")
#spustenie klasifikácie a vykreslovanie
zobrazit()