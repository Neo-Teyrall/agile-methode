import numpy as np


def aligne(kmers, all_seq, Tdata ,Qseq):
    output  = []
    for i, seq in enumerate(all_seq):
        print("\r {}/{}".format(i,len(all_seq)),end="")
        a = alignement(seq, kmers,Tdata)
        a["Qseq"] = Qseq
        output.append(a)
    return output


def alignement(sequence, kmers,Tdata):
    output = {"i_val": 0, "hsp": 0, "Qseq": "", "Aseq": "", "Qstart": 0}
    for i, kmer in enumerate(kmers) :
        b, pos  = k_in_seq(kmer,sequence)
        if b :
            j = i + 3
            hsp = 3
            tmp = 0

            while hsp > 0 and  j <( len(kmers)-3) and pos < (len(sequence)-1):
                if sequence[pos] == kmers[j][0]:
                    hsp += 1
                    tmp = 0
                else:
                    hsp -= 1
                    tmp += 1
                j += 1
                pos += 1

                if tmp > 5:
                    break
            new = evalue(len(kmers)+2, Tdata ,hsp)
            if output["i_val"] < new :
                output["i_val"] = new
                output["Aseq"] = sequence
                output["Qstart"] = i
    return  output


def k_in_seq(kmer, seq)-> bool:
    for i in range(len(seq)):
        if kmer == seq[i:i+3]:
            return True , i
    return False , None


def evalue(m, n, hsp):
  return m * n * np.exp(-hsp)


if __name__ == "__main__":
  pass
