# About

## The Project
Hepatitis C Virus (HCV) is a "notifiable condition" in Maine, meaning that all positive lab results are required by law to be reported to the Department of Health and Human Services (DHHS); it is also classified as either 'Acute' or 'Chronic'. 

This project has three primary goals and deliverables:

#### 1. Creation: [Complete]

Creating a reproducable data view showing patients and what labs they have had preformed. This should be able to be reproduced and updated by anyone working at the CDC. This is meeting a need for a better way to understand the data, since the CDC currently has no way to find trends in HCV.

#### 2. Analysis:

Using the database/data view from goal one, there are two primary research questions this project hopes to find answers for:

1. Hepatitis C Clearance Cascade:

This is the first and highest priority analysis for the project. The CDC is interested in finding out how many people are at each stage of the Hepatitis C 'clearance cascade' - 
* Antibody Test
* RNA Test
* Genotype Test (Optional)
* Cured/Cleared Infection
* Reinfection (Optional)

Monitoring how often pateients make it from one end to the other is important in identifing where resources are lacking and what treatments work.

2. Testing patterns (Prevalence Analysis): 

Looking at the Hepatitis C labs, it will be analyzed what patterns are able to be noticed in the testing behavior. Example testing questions are:
* How many serology tests are patients getting getting before they get a confirmatory viral load? 
* What factors are associated with failure to get a viral load test? 
* What factors are associated with repeat viral loads but not achieving cure? 
* How many cases in a given time period in a given geographic area would be a trigger for a potential outbreak?

#### 3. Reporting:
The final goal of this project would be a rigrous, published paper reporting on the analysis preformed in goal 2. This will be a joint co-authorship between the lead student researcher and the primary stakeholder, using both's domain knowledge to present a compelling analysis. 

### Additonal Reading
In-depth document on Hepatitis C survellience from the National CDC: 
* https://www.cdc.gov/hepatitis/statistics/surveillanceguidance/HepatitisC.htm 

More information about the Hepatitis C clearance cascade: 

* https://www.cdc.gov/mmwr/volumes/72/wr/mm7226a3.htm
* https://www.cdc.gov/mmwr/volumes/73/wr/mm7321a4.htm
* https://journals.sagepub.com/doi/10.1177/00333549231170044 


## The Data

### Original
Oringal datasets are case-patient records meaning data points in the surveillance system represent individuals with Hepatitis C. The CDC collect a wide range of variables on each patient. Some case-patient investigations are more complete than others because of how different Hepatitis C conditions are prioritized. Due to the disease's nautre as a "norifiable condition", there is high confidence that the dataset is representative of the whole population in the state of Maine. However, data records were not reliably complete until 2016. 

In addition to case-patient records which represent investigations (like an epidemiologic survey), there are also labs attached to each patient; these are Hepatitis test results of different types (antibody, RNA viral loads, genotype results). Each patient might have dozens of these for every time they get tested, so there are more labs than individual case-patients. 

This data was seperated into two tables, with the following variables:

| Cases                            |Definition                                
|:----                             |:--                                      |
| Disease                          | Disease status, either acute or chronic |
| HCV_Genotype                     | Genotype test result (genotype)         |
| HCV_Genotype_Detected            | Genotype test result (Y/N)              | 
| HCV_RNA                          | RNA test result                         |
| HCV_RNA_Date                     | RNA test collection date                |
| Investigation_Case_Status	       | Probable/Confirmed Status               |
| Year	                           | Year of Investigation                   |
| Patient_State                    | State, should be Maine                  | 
| Specimen_Collection_Date__HCV_Ge | Genotype test collection date           |
| total_anti_HCV                   | Anti-HCV test result                    |
| total_anti_HCV_Date              | Anti-HCV test collection date           |
| County                           | Patient County                          |
| Patient ID (encoded)             | Encoded Patient Tracker                 |

| **Labs**                         |                                         |
|:----                             |:--                                      |
| Coded_Result                     | Lab Result                              |
| Date_Specimen_Collected          | Specimen collection date                |
| Numeric_Results                  | Lab Result                              |
| Resulted_Test_Name               | Name of test performed                  |
| Test_Result_Code                 | Lab Result                              |
| Text_Result                      | Lab Result                              |
| Reporting_Facility               | Facility that submitted the lab         |
| Patient ID (encoded)             | Encoded Patient Tracker                 |

### Cleaned
The cleaned database combines the labs and case files, with two different views that are for different analytic uses. The primary human view is wider-form, where each patient only gets one row and labs are ordered with test date, type, and result. The longer-form view, best for data analysis, uses the same features but pivoted so patient is no longer the sole indexer. This also allows patient information to be more easily stored, such as county or visited labs. 

## This Repository

### Setup
Included is a Makefile that runs requirements.txt and any directories that need to be created, if they weren't already. Use
```
make setup
```
to install any needed requirements and directories, as well as re-create/update the database. If Make is not installed, 
```
	pip install -r ./create_db/requirements.txt
	python ./create_db/merge_records.py
```
can be run instead.

### Data (Folder)

#### HCV Data
There are 5 data files that pertain to the database creation, with 3 input files needed to clean and create the dataframe and two views that are used as the cleaned output. The first two are .xlsx files, and must be provided by the CDC. These are
- coded_all_cases_combined.xlsx
- coded_all_labs_combined.xlsx

For the dataframe to be updated, both files must be up-to-date and in the format seen above. The third file used as an input is a .csv that is a hardcoded list of all labs that were pulled in from an initial SQL query but were found to be unrealated to HCV. This can be adjusted at any time, as long as a newline is used to seperate lab names and are in all lowercase. 
- bad_test_names_lower

The last two files are the views created by merge_records.py:

- hcv_labs_long.xlsx
- hcv_labs_wide.xlsx

The 'long view' lists each patient/year/test as the indicator, and is the prefered view for coding-based analysis. The 'wide view' uses each patient as an indexer, and is ideal for human anaylsis since it more clearly shows the journey of each patient. 

#### Population Data
For analysis, population estimates data was taken from [census.gov](https://www.census.gov/data/datasets/time-series/demo/popest/2020s-counties-total.html) and [census.gov](https://www.census.gov/data/datasets/time-series/demo/popest/2020s-counties-total.html) and [maine.gov](https://www.maine.gov/dafs/economist/census-information). Other than being combined directly (as they are the same format) and the indexes renamed to remove the state name, no data has been changed or altared in any way from what was available on those websites as of October 24th, 2025.

### Analysis and Figs
These are static folders, and are what was run during the project analyses. They can either be used as the basis for another analysis, used for report creation, or verification if this repo were to be re-created.

### Note: HIPPA Compliance
To maintiain the saftey of sensitive information, this version of the repo has a slightly modified version of the data that does not include county information, which also impacts the EDA and figure generated for class. The private version does account for county, and an analysis is being preformed at that level.

## Contributers

*Lead Student Researcher/Data Scientist* - Joshua Brobst

Joshua Brobst is a Master's in Data Science student at the Roux Institute, and who studied Applied Mathematics and Statistic at the University of Southern Maine. Even before they had COVID-19 alter the outcome of their last two years of high school, the statistical part of epidemiology has fascinated them. They first started exploring the subject with their school's Science Olympiad team, and did some tracking work with COVID-19. Since then, most of their work has been with mathematics education including their first publication through their alma mater. 

They currently work as a part of UNUM Group's CSAT analytics team, although they spent the first two years of the company working in small case renewals underwriting.
