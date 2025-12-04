import pandas as pd
import matplotlib.pyplot as plt

raw = pd.read_excel('./data/hcv_labs_long.xlsx',index_col=0)
population = pd.read_excel('./data/population estimates maine counties (2015-2024).xlsx').drop(['County'],axis=1).T.reset_index()

just_rna = raw[raw['test_type'] == 'rna'].copy().dropna(subset = ['test_date']).reset_index(drop = True)
just_rna['test_year'] = just_rna['test_date'].dt.year.astype(int)

## Drop duplicate ids/results/year
by_year = just_rna.drop_duplicates(['patient_id','test_result','test_year']).reset_index(drop = True)[['test_result','test_year']]

vc = by_year.value_counts(['test_year','test_result']).reset_index()

positive_cases = vc[vc['test_result'] == 'positive'].copy().drop(['test_result'],axis = 1)

positive_cases_sorted = positive_cases.sort_values('test_year')[3:13].reset_index(drop=True)

## Now for the ratio
positive_ratio = positive_cases_sorted['count'] / population[0]

positive_ratio.index = positive_cases_sorted['test_year']

## Plotting
fig, ax = plt.subplots()

positive_ratio.plot(ax=ax)

plt.xlabel('Year')
plt.ylabel('Ratio of Unique Positive RNA Tests to Population')
plt.title("Ratio of Unique Positive RNA Tests to Population for Each County Per Year")
plt.legend(
    loc='lower right',
    bbox_to_anchor=(1.3, 0),
)
plt.tight_layout()
plt.savefig('./figs/positive_rna_per_year.png')
