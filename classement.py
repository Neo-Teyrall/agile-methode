def classer(liste):

	liste2 = []
	valeurs_eval = []
	taille_liste = len(liste)
	for i in range(len(liste)):
	        valeurs_eval.append(liste[i]["i_val"])
	while valeurs_eval:  
	    maxi = max(valeurs_eval)
	    for i in range(len(liste)):
	        if liste[i]["i_val"] == maxi:
	            valeurs_eval.remove(maxi)
	            liste2.append(liste[i])
	return liste2

def main():
	classement = classer(liste)

if __name__ == "__main__":
    main()
