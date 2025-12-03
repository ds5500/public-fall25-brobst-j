import pandas as pd

raw = pd.read_excel('../data/hcv_labs_wide.xlsx',header = [0,1])
no_header = raw.drop('lab_number',axis = 1).drop(index = 0)


long = pd.read_excel('../data/hcv_labs_long.xlsx',index_col=0)
long['lab_number'] = long.groupby('patient_id').cumcount() + 1

## Mapper for the possible stages
stages_mapper = {0: 'Negative Antibody',
                 1: 'Positive Antibody',
                 2: 'Negative RNA',
                 3: 'Positive RNA',
                 4: 'Cleared'}

cc_list = []

for pat in long['patient_id'].drop_duplicates():

    ## Initialize each patient
    labs_list = long[long['patient_id'] == pat].reset_index(drop = True)
    stage = 0
    infection = 1 ## Start with first infection, infection >1 means reinfection
    for lab in labs_list.itertuples(index=True):

        ## Get stage information
        if (lab.test_type == 'antibody') & (lab.test_result == 'positive') & (stage == 0): ## Only time a positive antibody matters
            stage = 1
        elif (lab.test_type == 'rna') & (lab.test_result == 'negative'):
            if stage >= 3: ## Means they must have had a positive RNA
                stage = 4
            else:
                stage = 2
        elif (lab.test_type == 'rna') & (lab.test_result == 'positive'):
            if stage == 4: ## Must have been marked as cleared
                infection += 1
            stage = 3
        elif (lab.test_type == 'genotype'): ## Only done when rna is positve
            stage = 3
        
        ## Complile lab info
        lab_info = {
            'patient':lab.patient_id,
            'infection': infection,
            'year': lab.test_date.year,
            'lab_n': lab.lab_number,
            'stage': stage
        }

        cc_list.append(lab_info)
## 2m 27.2s

cc_df = pd.DataFrame(cc_list)

## Focusing on just the cc, we only need the most recent test each year(?)
patient_status =(
    cc_df
    .copy()
    .drop_duplicates(['patient','infection','year'],keep='last')
    .drop('lab_n',axis = 1)
    .reset_index(drop = True)
)

patients_now = (
    patient_status
    .copy()
    .dropna()
    .drop_duplicates('patient',keep='last')
    .reset_index(drop = True)
)

## Just focus on CC for now, worry about testing patterns after.