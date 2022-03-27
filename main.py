#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 01:25:06 2022

@author: saeedmasroor
"""
"""
Given any base_codon, there are
9 variations with one nt change,
27 variations with two nt changes,
27 variations with three nt changes
"""
from itertools import product
import pandas as pd
from codon_aa import*

nt = ['A','C','G','T']
base_codons = [(x+y+z) for x in nt for y in nt for z in nt]
# base_codons_times27 = base_codons*27
# base_codons_times27.sort()
# base_codons_times27_sorted = base_codons_times27.sort()
# print()
# print(sum(list(base_codons),()))
# base_codons = list(map("".join, combinations_with_replacement('ATCG',3)))

# print(base_codons)
def MNV_generator_2variations(base_codon):
    nt = ['A','C','G','T']
    Two_nt_vars_codon = [(base_codon[0]+y+z)
              for y in [n for n in nt if n!=base_codon[1]]
              for z in [n for n in nt if n!=base_codon[2]]]+\
             [(x+base_codon[1]+z)
              for x in [n for n in nt if n!=base_codon[0]]
              for z in [n for n in nt if n!=base_codon[2]]]+\
             [(x+y+base_codon[2])
              for x in [n for n in nt if n!=base_codon[0]]
              for y in [n for n in nt if n!=base_codon[1]]]
    output = pd.DataFrame(Two_nt_vars_codon,columns=['Two_nt_vars_codon']) 
    output.insert(loc=0, column='base_codon', value=base_codon)


    # output['pos_1'] = [s[0]!=base_codon[0] for s in Two_nt_vars_codon]
    # output['pos_2'] = [s[1]!=base_codon[1] for s in Two_nt_vars_codon]
    # output['pos_3'] = [s[2]!=base_codon[2] for s in Two_nt_vars_codon]

    output['pos_1_var'] = [(base_codon[0]+'>'+s[0]) if s[0]!=base_codon[0] else False for s in Two_nt_vars_codon ]
    output['pos_2_var'] = [(base_codon[1]+'>'+s[1]) if s[1]!=base_codon[1] else False for s in Two_nt_vars_codon ]
    output['pos_3_var'] = [(base_codon[2]+'>'+s[2]) if s[2]!=base_codon[2] else False for s in Two_nt_vars_codon ]

    single_nt_var_1=[]
    for s in Two_nt_vars_codon:
        for index in range(3):
            # print(single_nt_var_1)
            if s[index]!=base_codon[index]:
                temp = base_codon
                temp = temp[:index]+s[index]+temp[index+1:]
                # print(temp)
                single_nt_var_1.append( temp)
                break
    # print(len(single_nt_var_1))
    output['single_nt_var_1']=single_nt_var_1        


    single_nt_var_2=[]
    for s in Two_nt_vars_codon:
        for index in reversed(range(3)):
            # print(single_nt_var_1)
            if s[index]!=base_codon[index]:
                temp = base_codon
                temp = temp[:index]+s[index]+temp[index+1:]
                # print(temp)
                single_nt_var_2.append( temp)
                break
    # print(len(single_nt_var_2))
    output['single_nt_var_2']=single_nt_var_2  
    

    # amino acids corresponding to each codon type
    output['base_aa'] = [codon_to_aa_mtDNA(s) for s in output.base_codon]
    output['Two_nt_vars_aa']=[codon_to_aa_mtDNA(s) for s in output.Two_nt_vars_codon]
    output['single_nt_var_1_aa'] = [codon_to_aa_mtDNA(s) for s in single_nt_var_1]
    output['single_nt_var_2_aa'] = [codon_to_aa_mtDNA(s) for s in single_nt_var_2]
    
    # if an amino acid from a single nt change is different from
    # base, it is nonsynonymous, further if it is different from 
    # the two_nt_vars_aa (the real aa change) then it is problamatic
    Problamatic_1 = []
    for ind in output.index:
        output.loc[ind,'Problamatic_1'] =\
        (output.loc[ind,'single_nt_var_1_aa']!=
         output.loc[ind,'base_aa'] and
         output.loc[ind,'single_nt_var_1_aa']!=
         output.loc[ind,'Two_nt_vars_aa']) *1
        
        output.loc[ind,'Problamatic_2'] =\
        (output.loc[ind,'single_nt_var_2_aa']!=
         output.loc[ind,'base_aa'] and
         output.loc[ind,'single_nt_var_2_aa']!=
         output.loc[ind,'Two_nt_vars_aa']) *1
        
    output['Problamatic']=output[['Problamatic_1', 'Problamatic_2']].max(axis=1)
    
    
    return(output)


# print(MNV_generator_2variations('ATC'))

DF = pd.DataFrame()
for base_codon in base_codons:
    DF = pd.concat([DF,MNV_generator_2variations(base_codon)],
                   axis=0,ignore_index=True)
DF.to_excel("MNV_2variations_mtDNA.xlsx")
    
#%%

# print(codon_to_aa_mtDNA(DF.Two_nt_vars_codon)   )








