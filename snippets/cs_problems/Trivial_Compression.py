from sys import getsizeof
import random


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # start with sentinel

        for nucleotide in gene.upper():
            self.bit_string <<= 2  # add (shift left) two bits

            if nucleotide == 'A':
                self.bit_string |= 0b00  # change last to bits to 00
            elif nucleotide == 'C':
                self.bit_string |= 0b01  # change last to bits to 01
            elif nucleotide == 'G':
                self.bit_string |= 0b10  # change last to bits to 10
            elif nucleotide == 'T':
                self.bit_string |= 0b11  # change last to bits to 11
            else:
                raise ValueError(f'Invalid Nucleotide:{nucleotide}')

    def decompress(self) -> str:
        gene: str = ''
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # -1 to exclude the sentinel
            # get the last two (relevant) bits
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += 'A'
            elif bits == 0b01:
                gene += 'C'
            elif bits == 0b10:
                gene += 'G'
            elif bits == 0b11:
                gene += 'T'
            else:
                # this should be impossible ;-)
                raise ValueError(f'Invalid bits:{bits}')
        return gene[::-1]  # reverse

    def __repr__(self):
        return f'{self.bit_string: b}'


original: str = 'AGGATTCCGG'
g = CompressedGene(original)
print(f'{getsizeof(original)} bytes')
print(f'{getsizeof(g.bit_string)} bytes')
print(f'Original: {original}')
print('Compressed: ', g)
decom: str = g.decompress()
print(f'Decompressed: ' + decom)

#
d = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

for _ in range(0, 1000):
    s = ''.join([d[i] for i in random.choices(range(0, 4), k=10)])
    gene = CompressedGene(s)
    print(s)
    print(gene)
