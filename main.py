from projet import *
from  enregistre import *
from kmer import *
import sys
from alignment import *
from classement import *

if __name__ == "__main__" :
    # 1
    fasta_file, query = get_argument(sys.argv)
    sequence_dict = lit_fasta(fasta_file)
    genome_size = len(sequence_dict)#database_length(sequence_dict)
    print("LARA WORK ")
    # 2
  # prise en charge d'un fichier en argument puis retour de sa séquence dans une liste puis transformation de la site en chaine de caractère
    Seq_query = lit_fasta_max(query)
    Seq_query = str(Seq_query[0])
   # Retour terminal de la séquence et de sa taille 
    #print(Seq_query)
    taille_Seq_query=len(Seq_query)
    #print(taille_Seq_query)
   # Retour terminal de la liste de K-mer
    k_mer = k_merisation(Seq_query, taille_Seq_query)
    print("MAX WORK ")
    # 3
    print(" kmers", k_mer)
    aligned = aligne(k_mer, sequence_dict, genome_size, Seq_query)
    #print(aligned)
    print("W & P WORK ")
    classe = classer(aligned)
    print("DYLAN WORK ")
    # 4
    enregistre(classe)

    # 5
    print("APO WORK ")
