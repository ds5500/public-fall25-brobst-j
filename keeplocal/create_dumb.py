import numpy as np
import pandas as pd
from pathlib import Path

downloads_path = Path.home()/ "Downloads"

### Patient Ids ------------------

## Read in files

chronic_cases = pd.read_csv(downloads_path / 'Chronic Hep B and C Cases(in).csv')
lab_results = pd.read_csv(downloads_path / 'Lab results_individual(in).csv')

## Get unique patient ids
i1 = chronic_cases['Patient Local ID']
i2 = lab_results['Patient Local ID']

uni_list = list(set(pd.concat([i1,i2])))

## Randomize id list
m = [x + 1 for x in range(len(uni_list))]
np.random.shuffle(m)

n = [f'PAT{x:0>7}'for x in m]

## Save key
key = (pd.DataFrame(n,uni_list).reset_index())
key.columns = ['original','coded']

## Merge with originals
encoded1 = pd.merge(chronic_cases, key, how = 'left', left_on = 'Patient Local ID', right_on = 'original')
encoded2 = pd.merge(lab_results, key, how = 'left', left_on = 'Patient Local ID', right_on = 'original')

encoded1 = encoded1.drop(['Patient Local ID','original'],axis = 1)
encoded2 = encoded2.drop(['Patient Local ID','original'],axis = 1)

## Print to Excel
encoded1.to_excel(downloads_path /'[CODED] Chronic Hep B and C Cases(in).xlsx')
encoded2.to_excel(downloads_path /'[CODED] Lab results_individual(in).xlsx')
key.to_excel(downloads_path /'[CODED] Key.xlsx')
