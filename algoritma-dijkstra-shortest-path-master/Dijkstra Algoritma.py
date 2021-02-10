# coding: utf-8
from pprint import pprint
import colorama
from colorama import Fore, Style, Back
from colorama import init 

def dijkstra(graph,start,target):
    inf = float('inf')
##    for u in graph:
##        for v ,w in graph[u]:
##           inf = inf + w                   #menghitung panjang seluruh jarak antar vertex
    dist = dict([(u,inf) for u in graph])   #buat semua jarak antar vertex menjadi infinity/sama dengan jumlah seluruh jarak antar vertex
    prev = dict([(u,None) for u in graph])  #buat dictionary, semua titik vertex dan bernilai None
    q = graph.keys()                        #buat List q, berisi semua Node
    dist[start] = 0                         #dist[start]=0, Deklarasi Asal dengan nilai 0
    #helper function
    def x(v):
        return dist[v]                      #untuk mengembalikan Node yang bernilai paling kecil
    #
    while q != []:                          #selama q tidak kosong!
        u = min(q, key=x)                   #mengambil node yang ada di q dengan jarak yang paling pendek
        q.remove(u)                         #Menghapus Node u
        for v,w in graph[u]:                #Node,Jarak yang ada di graph[u]
            alt = dist[u] + w               #Menyimpan jarak dari Node asal ke Node Selanjutnya
            if alt < dist[v]:               #Cek, apakah alt lebih kecil dari destination V
                dist[v] = alt               #Ubah nilai Distination B degan Alt
                prev[v] = u                 #Ganti Node Asal dari si Next(dist[v])/Menyimpan asal node sebelumnya yang terpendek
    #?way?
    trav = []                               #Array Travel
    jarak=[]
    temp = target                           #temp = tujuan
    while temp != start:                    #Selama temp tidak sama dengan Asal
        if prev[temp]==None:
            break
        trav.append(prev[temp])             #simpan Node sebelumnya dari temp
        jarak.append(dist[temp]-dist[prev[temp]])
        temp = prev[temp]                   #temp = Node sebelumnya,datang dari mana\
    trav.reverse()                          #balikkan List travel
    trav.append(target)                     #tambhkan Node Tujuan
    jarak.reverse()
    return trav,jarak,dist[target]

def PrintTravel(graph,start,end):
    node,jarak,total=dijkstra(graph,start,end)    #memanggil fungsi Dijkstra
    hasil=""                                #deklarasi hasil
    if len(node)==1:                        #jika panjang dari node==1?,panjang node satu jika dari asal ke tujuan tidak ada jalan, maka yang di simpan hanya node tujuan
        hasil="Tidak ada rute dari {0} ke {1}".format(start,end)
    else:
        for i in range(0,len(node)):        #perulangan List node
            if i==0:                        #jika i==0
                hasil=hasil + "\n \n \n" + Fore.WHITE + "Rute Tercepat:" + Style.RESET_ALL     #hasil=hasil+node yang ke i
            else:
                hasil=hasil+" \n \n" + Back.GREEN + Fore.BLACK + node[i-1] + Style.RESET_ALL + " " + Fore.YELLOW +str(jarak[i-1])+" km"+" -> "+ Back.GREEN + Fore.BLACK + node[i] + Style.RESET_ALL 
    hasil=hasil+"\n \nTotal Jarak = " + Back.BLUE + Fore.WHITE + str(total) + " km" + Style.RESET_ALL + "\n \n \n"
    return hasil

kota = {
    "jakarta" : [('bogor',56.2), ('bekasi', 19.7)],
    'bogor' : [('cianjur', 60.2)],
    'bekasi' : [('purwakarta', 78.6), ('cikampek', 59.5)],
    'purwakarta' : [('bandung', 57.4)],
    'bandung' : [('sumedang', 46.5),('cianjur', 64.9),('nagreg', 40.5)],
    'nagreg' : [('garut', 31),('malangbong', 34.8)],
    'malangbong' : [('tasikmalaya', 44.4)],
    'garut' : [('tasikmalaya', 52.9)],
    'tasikmalaya' : [('ciamis', 18.5)],
    'ciamis' : [('banjar', 28.1), ('majalengka', 104)],
    'banjar' : [],
    'sumedang' : [('majalengka', 46.5)],
    'cianjur' : [('bandung', 64.9)],
    'cikampek' : [('subang', 54.2)],
    'subang' : [('majalengka', 78.2)],
    'majalengka' : [('cirebon', 35.3)],
    'cirebon' : []
    }

choice = "y"
while choice == "y":
    print(Fore.CYAN+"  ____  _____   ___         _    _   ___                                 _    _       ")
    print(Fore.CYAN+" |  _ \|_   _| |_ _| _ __  | |_ (_) |_ _| _ __ ___   _ __    ___   _ __ | |_ (_) _ __ ")
    print(Fore.CYAN+" | |_) | | |    | | | '_ \ | __|| |  | | | '_ ` _ \ | '_ \  / _ \ | '__|| __|| || '__|")
    print(Fore.CYAN+" |  __/  | | _  | | | | | || |_ | |  | | | | | | | || |_) || (_) || |   | |_ | || |   ")
    print(Fore.CYAN+" |_|     |_|(_)|___||_| |_| \__||_| |___||_| |_| |_|| .__/  \___/ |_|    \__||_||_|   ")
    print(Fore.CYAN+"                                                    |_|                               ")
    print(Back.CYAN+Fore.BLACK+"---------------------------------------------------- HITUNG JARAK DISTRIBUSI LOGISTIK"+Style.RESET_ALL)  
                                             
    print("  Daftar Gudang:")
    print(Fore.GREEN+"    ▄ Bekasi                ▄ Subang                                              ")
    print(Fore.GREEN+"    ▄ Bogor                 ▄ Majalengka                                          ")
    print(Fore.GREEN+"    ▄ Purwakarta            ▄ Cirebon                                                  ")
    print(Fore.GREEN+"    ▄ Cianjur               ▄ Tasikmalaya                                              ")
    print(Fore.GREEN+"    ▄ Cikampek              ▄ Banjar                                              ")
    print(Fore.GREEN+"    ▄ Bandung               ▄ Cianjur                                              ")
    print(Fore.GREEN+"    ▄ Sumedang              ▄ Garut                                            "+Style.RESET_ALL)
    print("\n  Gudang Pusat : Jakarta")
    print("_______________________________________________________                                                                  ")
    print("Masukan Kota Tujuan: ")
    try:
        tujuan = raw_input().lower()
        travel=PrintTravel(kota,"jakarta",tujuan)
        print(travel)
    except KeyError:
        print("Nama kota tidak terdaftar.")
    print("Hitung Jarak Lagi? (y/n)")
    choice = raw_input()


