
dna2rna = {'A':'A', 'a':'a', 'T':'U', 't':'u', 'G':'G', 'g':'g', 'C':'C', 'c':'c'}
dna2cdna = {'A':'T', 'a':'t', 'T':'A', 't':'a', 'G':'C', 'g':'c', 'C':'G', 'c':'g'}
rna2crna = {'A':'U', 'a':'u', 'T':'A', 't':'a', 'G':'C', 'g':'c', 'C':'G', 'c':'g'}


def transcribe(seq):
    rna = ''
    for i in seq:
        rna += dna2rna[i]
    return rna
    
def reverse(seq):
    return seq[::-1]

def complement(seq):
    cstrand = ''
    if 'u' in seq.lower():
        for i in seq:
            cstrand += rna2crna[i]
    else:
        for i in seq:
            cstrand += dna2cdna[i]
    return cstrand

def reverse_complement(seq):
    reverse_cstrand = complement(reverse(seq))
    return reverse_cstrand
        

def count_gc(seq):
    gc = seq.lower().count('g') + seq.lower().count('c')
    answer = gc / len(seq) * 100
    return f'{round(answer, 2)}%'

def dna_or_rna(seq):
    if set(seq.lower()) == set('atgc'):
        return 'dna'
    elif set(seq.lower()) == set('augc'):
        return 'rna'    

def get_sequence_length(seq):
    return len(seq)

commands = {'transcribe': transcribe, 'reverse': reverse, 'complement':complement, 'reverse_complement': reverse_complement, 'count_gc': count_gc, 
'dna_or_rna': dna_or_rna, 'get_sequence_length': get_sequence_length}

def check(args):
    if len(args)  < 2:
        raise ValueError('Input sequences and command')
    elif args[-1] not in commands:
        raise ValueError('No such command')
    else:
        for seq in args[:-1]:
            if set(seq.lower()) == set('autgc') and set(seq.lower()) != set('atgc') and set(seq.lower()) != set('augc'):
                raise ValueError('Input dna or rna')
def run_dna_rna_tools(*args):
    seqs = args[:-1]
    cmd = args[-1]
    output = []
    check(args)
    if len(seqs) == 1:
        return(commands[cmd](seqs[0]))
    else:
        for seq in seqs:
            output.append(commands[cmd](seq))
        if len(output) > 1:
            return(output)
        else:
            return(output[0])
    
    