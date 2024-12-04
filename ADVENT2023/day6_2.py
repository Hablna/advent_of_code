import re
tim_dis=[]
with open('entrer', 'r') as file:
    for time in file:
        time = re.split(':',time)
        time = [i for i in time[1] if i != ' ']
        heure = ''
        for i in time :
            heure+=i
        heure = heure.strip()
        tim_dis.append(heure)
    #print(tim_dis)
    point = 0

    for temps_chargement in range(0, int(tim_dis[0])):
        dure_trajet = int(tim_dis[0]) - temps_chargement
        distance_parcourue = temps_chargement * dure_trajet
    
        if distance_parcourue >= int(tim_dis[1]) :
            point += 1
    print(point)