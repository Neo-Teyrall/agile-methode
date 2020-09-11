import sys
import os
import argparse
from Bio import SeqIO

def get_argument(arguments):
    if len(arguments) != 3 :
        sys.exit("Error: 2 parameters needed.")
    if os.path.exists(arguments[1]) != 1:  # Verifie la presence de l'input
        sys.exit("Error: {} does not exist.".format(arguments[1]))
    return arguments[1], arguments[2]

def lit_fasta (nom_fichier) :
    sequence_dict = {}
    proteome = []
    with open(nom_fichier, "r") as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            proteome.append(str(record.seq)[30:])
    fasta_file.close()
    sequence_dict[nom_fichier.split(".")[0]] = proteome
    return sequence_dict

if __name__ == "__main__":
    fasta_file, query = get_argument(sys.argv)
    proteome = lit_fasta(fasta_file)