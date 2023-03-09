import networkx as workx
import matplotlib.pyplot as plot

FILE_PATH = './Algorytmy_SGGW/test.txt'


def get_graph():
    que = input('Wczytywania danych z klawiatury(1), czy z pliku tekstowego(2)?\n')
    # Wczytywania danych z klawiatury
    if que == '1':

        try:
            print('Wpisz liczbe wierzchołków i liczbe krawędzi: ')
            # lista typu 'tuple'
            # pierwszy wpisany znak(int) idzie do n, drugi do m
            # split().. znaki rozdzielone spacją
            (n, m)=tuple(map(int,input().split()))
            if n <= 0:
                print('Liczba wierzchołków nie zgadza się. Sprobój ponownie')
                return
            graph=[]
        except ValueError:
            print('TypeError. Sprobój ponownie')
            return
        else:
            try:
                print('Wpisz pary wierzchołków połączonych łukiem.\n'
                      'Spacja jest separatorem liczb w pojedynczej linii')
                # petla wykonuje się 'm' razy. 'm' liczba krawędzi
                for _ in range(m):
                    (a,b)=tuple(map(int,input().split()))
                    # do grafu dodaje się pary wierzchołków połączonych łukiem
                    graph.append((a,b))
            except ValueError:
                print('TypeError. Sprobój ponownie')
                return
            else:
                # zwracamy 'graph' i wychodzimy z metody 'get_graph'
                return graph
    # Wczytywanie z pliku tekstowego
    if que == '2':
        try:
            # odczyt pliku tekstowego .txt
            with open(FILE_PATH) as message:
                dane = message.read().split('\n')
        except FileNotFoundError:
                print('Nie znaleziono pliku tekstowego. Sprobój ponownie')
                return
        else:
            try:
                (n, m)=tuple(map(int,dane[0].split()))
                if n <= 0:
                    print('Liczba wierzchołków nie zgadza się. Sprobój ponownie')
                    return
            except ValueError:
                print('Błąd w pierwiej linii pliku. Napraw to i sprobój ponownie')
                return
            else:
                graph=[]
                if m == len(dane)-1: 
                    for _ in range(1, m+1):
                        (a,b)=tuple(map(int,dane[_].split()))
                        graph.append((a,b))
                else:
                    print('Liczba krawędzi nie zgadza się. Sprobuj ponownie')
                    return
            return graph
    else:
        print("TypeError. Wpisz '1' albo '2'")
 

def dfs_loops(graph):  
    
    inpt = input('Od jakiego wierzchołku zaczynamy? -> ')
    stack=[int(inpt)]
    #'chk'(checked) - lista wierzchołków gdzie już byliśmy
    chk=stack.copy()

    loop_counter = 0
    loops = []
    print(stack)
    
    while True:
        # jezeli stack pusty -> koniec
        if len(stack)==0:
            # Jezeli graf zawiera cykle, wypisujemy ich po kolei
            if loop_counter != 0:
                print(f'Graf zawiera {loop_counter} cykl(e):')
                for _ in range(loop_counter):
                    print(f'{_+1}. {loops[_]}')
            return
        # v - ostatni element listy 'stack'
        v=stack[-1]
        
        for (a,b) in graph:     
            if (a==v) and not (b in chk):
                stack.append(b)
                chk.append(b)
                # Sprawdzamy pętle
                sz=len(stack)
                print(stack)
                for i in range(sz-1):
                    # Jezeli łuk (b, stack[i]) już mamy w liscie 'graph' zapisujemy cykl
                    if (b,stack[i]) in graph:
                        cykl = ""
                        for j in range(i,sz):
                            if j == sz-1:
                                cykl += f"{stack[j]}"
                            else:
                                cykl += f"{stack[j]}->"
                        # Dodajemy do listy cyklow i zwiększamy licznik 'loop_counter'
                        loops.append(cykl)
                        loop_counter += 1
                break
        else:
            # popujemy ostatni element => cofujemy się o krok
            stack.pop()

def showGraph(graph):
        grap = workx.DiGraph()
        temp = []
        for edges in graph:
            # for neightbour in graph[edges]:
            temp.append(edges)

        grap.add_edges_from(temp)
        pos = workx.spring_layout(grap)
        workx.draw_networkx_nodes(grap, pos, node_size=250)
        workx.draw_networkx_edges(grap, pos, edgelist=grap.edges(), edge_color='green')
        workx.draw_networkx_labels(grap, pos)
        plot.show()
        # sys.exit(0)
 
g=get_graph()

# jezeli (g == None) w metodzie get_graph wystąpił bład
if g != None:
    dfs_loops(g)
    showGraph(g)


    # DFS
    # Loops
    # Input
    # GUI
    # Exception