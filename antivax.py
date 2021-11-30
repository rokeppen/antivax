from translate import regex
import re
from Bio import SeqIO


def search_word(proteom, word):
    for i in range(1, len(proteom)//len(word)+1):
        for j in range(i):
            res = re.search(regex(word), str(proteom[j::i]))
            if res:
                return res.start()*i+j, i, res.group(0)
    return None


def get_data(inp, word):
    proteoms = SeqIO.parse(inp, "fasta")
    for seq in proteoms:
        print(seq.id)
        print(search_word(seq.seq, word))


sars_input = 'sars_cov2.fasta'
get_data(sars_input, 'geert')
