import pandas as pd

df = pd.read_excel('../data/merged.xlsx')

## Get just the tests and results
tests = df[['test_name','result']].copy().drop_duplicates()

## Clean the tests in a function, so it can be repeated on the full dataset.
def clean_tests(data):

    ## Drop admitence tests
    no_admit = tests[tests['test_name'] != 'Admit Date Time'].copy()

    ## Standardize naming
    no_admit['test_name'] = (
        no_admit['test_name']
        .str.lower()
        .str.replace('hepatitis c virus', 'hcv')
        .str.replace('hepatitis c', 'hcv')
        .str.replace('hep c', 'hcv')
    )
    hcv_lower = no_admit.copy().drop_duplicates()

    only_hcv = hcv_lower[hcv_lower['test_name'].str.contains('hcv',na= False)].copy()
    not_hcv =  hcv_lower[~hcv_lower['test_name'].str.contains('hcv',na= False)].copy()['test_name'].drop_duplicates()
    
    only_hcv_tests = hcv_lower[hcv_lower['test_name'].str.contains('hcv',na= False)].copy()['test_name'].drop_duplicates()
