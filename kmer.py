from Bio import SeqIO
import math
import sys

#Ce programme python permet de récupérer, en ligne commande, le nom d'un fichier fasta (deuxième argument). Puis d'en retourner la taille de la séquence ainsi qu'une liste de k-mer de taille 3.

def lit_fasta_max (nom_fichier) :
	Seq_query = []
	with open(nom_fichier, "r") as fasta_file:
		for record in SeqIO.parse(fasta_file, "fasta"):
			#print(str(record.seq)[30:])
			Seq_query.append(str(record.seq)[30:])
	fasta_file.close()
	return Seq_query

def k_merisation (Seq_query, taille_Seq_query) :
    k_mer = []
    for i in range(taille_Seq_query-2) :
        k_mer.append(str(Seq_query[i:i+3]))
    return k_mer




if __name__ == '__main__':
    
   # prise en charge d'un fichier en argument puis retour de sa séquence dans une liste puis transformation de la site en chaine de caractère
    nom_fichier = sys.argv[1]
    Seq_query = lit_fasta(nom_fichier)
    Seq_query = str(Seq_query[0])
   # Retour terminal de la séquence et de sa taille 
    print(Seq_query)
    taille_Seq_query=len(Seq_query)
    print(taille_Seq_query)
   # Retour terminal de la liste de K-mer
    k_mer = k_merisation(Seq_query, taille_Seq_query)
    print(k_mer)
