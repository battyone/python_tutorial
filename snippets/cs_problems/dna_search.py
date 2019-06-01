from enum import IntEnum
from typing import Tuple, List

# IntEnum provides comparison operators (<, >=, etc) unlike Enum
Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

# A condon is three nucleotides

# type alias for condons
Condon = Tuple[Nucleotide, Nucleotide, Nucleotide]

# type alias for gene
Gene = List[Condon]

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def string_to_gene(s: str) -> Gene:
    gene: Gene = []

    for i in range(0, len(s), 3):
        # check if we are at the end
        if(i+2) >= len(s):
            return gene

        condon: Condon = (Nucleotide[s[i]], Nucleotide[
            s[i+1]], Nucleotide[s[i+2]])
        gene.append(condon)
    return gene


def linear_contains(gene: Gene, key_condon: Condon) -> bool:
    for condon in gene:
        if condon == key_condon:
            return True
    return False


def binary_contains(gene: Gene, key_condon: Condon) -> bool:
    low = 0
    high = len(gene) - 1

    while low <= high:
        mid = (high+low)//2
        if gene[mid] < key_condon:
            # current condon is smaller than key_condon, hence search in the upper area
            low = mid + 1
        elif gene[mid] > key_condon:
            # current condon is higher than key_condon, hence search in the lower area
            high = mid - 1
        else:
            return True

    return False


def make_condon(s: str) -> Condon:
    if len(s) != 3:
        raise ValueError

    return (Nucleotide[s[0]], Nucleotide[
        s[1]], Nucleotide[s[2]])


gene: Gene = string_to_gene(gene_str)

acg: Condon = make_condon('ACG')
gat: Condon = make_condon('GAT')

print(linear_contains(gene, acg))
print(linear_contains(gene, gat))

print(acg == gat)

sorted_gene: Gene = sorted(gene)
print(binary_contains(sorted_gene, acg))
print(binary_contains(sorted_gene, gat))
