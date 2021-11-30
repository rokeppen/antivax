import re
from translate import regex
from Bio import SeqIO
import cProfile


def get_subs(proteom):
    result = {proteom[j::i] for i in range(1, len(proteom)) for j in range(i)}
    return ':'.join(result)


def preprocess(dictionary, inp):
    with open(dictionary) as f:
        words = [line.strip() for line in f if line.strip().isalpha()]
        re_words = [regex(word) for word in words]
    proteoms = SeqIO.parse(inp, "fasta")
    subs = dict(zip([seq.id for seq in proteoms], [get_subs(str(seq.seq)) for seq in proteoms]))
    return words, re_words, subs


def hidden_message(words, re_words, proteoms):
    with open('res.txt', 'a+') as file:
        for sid, seq in proteoms.items():
            file.write(sid + '\n')
            file.writelines(words[i] + '\n' for i, reg in enumerate(re_words) if re.search(reg, seq))


dic = 'woordenboek.txt'
human_input, sars_input = 'human_genome.fasta', 'sars_cov2.fasta'
w, r, p = preprocess(dic, sars_input)
cProfile.run('hidden_message(w, r, p)')
