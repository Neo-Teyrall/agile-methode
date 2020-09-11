def enregistre(aligned_dicts):
    with open("BLAST_results.txt", 'w') as filout:
        for seq in aligned_dicts:
            if seq["Qstart"]<0:
                spaces = -seq["Qstart"]
                filout.write("E-val:{:>8.4f}|{}\n{:>15}".format(seq["I_val"], seq["Qseq"], "|") + (" " * spaces) + seq["Aseq"] + "\n")
            else:
                spaces = seq["Qstart"]
                filout.write("E-val:{:>8.4f}|".format(seq["I_val"]) + (" " * spaces) + "{}\n{:>15}".format(seq["Qseq"], "|") + seq["Aseq"] + "\n")
            



if __name__ == "__main__":
    test_seq1 = {'I_val':2, 'Qstart':3, 'Qseq':'aaattt', 'Aseq':'tttaaattt'}
    test_seq2 = {'I_val':25, 'Qstart':-1, 'Qseq':'aaattt', 'Aseq':'aattt'}
    test_align = [test_seq1, test_seq2]
    enregistre(test_align)

