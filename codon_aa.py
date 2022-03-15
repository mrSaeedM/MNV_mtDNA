#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 21:08:51 2022

@author: saeedmasroor
"""
"""
    Differences between the vertebrate mtDNA code and
    the "Universal" code :
    Note that AUA and AUG (AUR) are both Met codons,
    UGA codes for Trp rather than being a Stop codon such
    that Trp is now two-fold degenerate (UGR),
    and AGA and AGG (AGR) codons are read as Stops
    instead of Arg. The mtDNA code thus has four Stops.
    Slightly different mtDNA codes are found in Drosophila 
    and other invertebrate groups.
"""
codon_to_aa_dict = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'M', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',

        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',

        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',

        'UGU': 'C', 'UGC': 'C', 'UGA': 'W', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'Stop', 'AGG': 'Stop',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
        }
#library
# codon_dict = {
#         'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
#         'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
#         'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Met', 'AUG': 'Met',
#         'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',

#         'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
#         'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
#         'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
#         'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',

#         'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
#         'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
#         'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
#         'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',

#         'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Trp', 'UGG': 'Trp',
#         'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
#         'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Stop', 'AGG': 'Stop',
#         'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
#         }
aa_to_codon_dict = {}
for k, v in codon_to_aa_dict.items():
    aa_to_codon_dict[v] = aa_to_codon_dict.get(v, []) + [k]

aa_to_codon_dict.get('L')
#function codon to amino acid
def codon_to_aa_mtDNA(codon):
    codon = codon.replace(" ", "")
    codon = codon.upper()
    codon = codon.replace("T", "U")
    aa = codon_to_aa_dict.get(codon,
            "Not a valid codon.")
    return aa


def aa_to_codons_mtDNA(aa):
    aa = aa.replace(" ", "")
    aa = aa.capitalize()
    codons = aa_to_codon_dict.get(aa,
                "not a valid amino acid")
    return codons

print(aa_to_codons_mtDNA('sT o p'))
print(codon_to_aa_mtDNA('AgU'))
