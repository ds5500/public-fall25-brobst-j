import pandas as pd
import numpy as np

hcv = pd.read_excel("../data/hcv_labs_long.xlsx",index_col=0)


rna = hcv[hcv['test_type'] == 'rna'].copy().dropna(subset=['test_facility']).reset_index(drop=True)
RNA_COUNT = len(rna)

facils = pd.DataFrame(rna.test_facility.value_counts())
facils['share'] = facils['count'].apply(lambda x: round(((x/RNA_COUNT) * 100),3))

neg = rna[rna['test_result'] == 'negative'].reset_index(drop=True)
NEG_COUNT = len(neg)

neg_facils = neg.test_facility.value_counts()
facils['neg_share'] = neg_facils.apply(lambda x: round(((x/NEG_COUNT) * 100),3))

rna_posneg_only = rna[(rna['test_result'] == 'negative') | (rna['test_result'] == 'positive')].reset_index(drop=True)
POSNEG_COUNT = len(rna_posneg_only)

rna_posneg_facils = rna_posneg_only.test_facility.value_counts()
facils['posneg_share'] = rna_posneg_facils.apply(lambda x: round(((x/POSNEG_COUNT) * 100),3))

p = len(rna_posneg_only[rna_posneg_only['test_result'] == 'negative'])/27397


Z = 1.96 * np.sqrt(((1-p)*p)/POSNEG_COUNT)

ct = pd.crosstab(rna_posneg_only['test_facility'], rna_posneg_only['test_result'])