
liste = [['le', 'Article défini', 'None'],
         ['crayon', 'Nom commun', 'Verbe'],
         ['est', 'Nom commun', 'Verbe'],
         ['vert', 'Adjectif', 'None'],
         ['et', 'Conjonction de coordination', 'None'],
         ['sur', 'Préposition', 'None'],
         ['la', 'Forme d’article défini', 'None'],
         ['table', 'Nom commun', 'Verbe'],
         ['rouge', 'Adjectif', 'None'], [], [], [], [], [], [], [], [], [], [], []]

c1 = 0

for i in liste:
    if i == []:
        pass
    else:
        for i in range(len(liste[c1])):
            art = str(liste[c1]).find(str("Article"))
            art1 = str(liste[c1]).find(str("article"))
            print(liste[c1][1])
            if liste[c1][1] == "Nom commun":
                
                print("oui")
            break
    c1 += 1



