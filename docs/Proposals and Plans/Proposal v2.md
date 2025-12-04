# Hepatitis C Clearence Cascade V2 10/30/2025
**Lead Student:** Joshua Brobst             **Lead Student Email:** brobst.j@northeastern.edu

**Stakeholder:** Chloe Manchester           **Stakeholder Email:** chloemanchester@northeastern.edu
    

## The Project
Hepatitis C is a "notifiable condition" in Maine, meaning that all positive lab results are required by law to be reported to the Department of Health and Human Services (DHHS). It is also classified as either 'Acute' or 'Chronic'. 

There are four primary questions this project hopes to find answers for:

**1. Hepatitis C Clearance Cascade:** This is the first and highest priority analysis for the project. The CDC is interested in finding out how many people are at each stage of the Hepatitis C 'clearance cascade' - 
* Antibody Test
* RNA Test
* Genotype Test (Optional)
* Cured/Cleared Infection
* Reinfection (Optional)

Monitoring how often pateients make it from one end to the other is important in identifing where resources are lacking and what treatments work.

**2. Testing patterns:** Looking at the Hepatitis C labs, it will be analyzed what patterns are able to be noticed in the testing behavior. Example testing questions are:
* How many serology tests are patients getting getting before they get a confirmatory viral load? 
* What factors are associated with failure to get a viral load test? 
* What factors are associated with repeat viral loads but not achieving cure? 

**3. Time-space analysis:** There is interest in developing a cluster-detection algorithm for Hepatitis C. For example, how many cases in a given time period in a given geographic area would be a trigger for a potential outbreak.

**4. Infectious disease modelling:** There is interest in understanding how increased Hepatitus C screening and cure might affect prevalence of Hepatitis C. For example, if 10% more people achieve cure, how will rates go down over time? This would be mostly new to the field, with some papers on Hepatitus C disease modelling that can be used as a starting point.


### The Data

#### Original
Oringal datasets are case-patient records meaning data points in the surveillance system represent individuals with Hepatitis C. The CDC collect a wide range of variables on each patient. Some case-patient investigations are more complete than others because of how different Hepatitis C conditions are prioritized. Due to the disease's nautre as a "norifiable condition", there is high confidence that the dataset is representative of the whole population in the state of Maine. However, data records were not reliably complete until 2016. 

In addition to case-patient records which represent investigations (like an epidemiologic survey), there are also labs attached to each patient; these are Hepatitis test results of different types (antibody, RNA viral loads, genotype results). Each patient might have dozens of these for every time they get tested, so there are more labs than individual case-patients. 

This data was seperated into two tables, with the following variables:

| Cases                            |Definition                               | Labs                    |Definition                       | 
|:----                             |:--                                      |:--                      |:---                             |
| Disease                          | Disease status, either acute or chronic | Coded_Result            | Lab Result                      |
| HCV_Genotype                     | Genotype test result (genotype)         | Date_Specimen_Collected | Specimen collection date        |
| HCV_Genotype_Detected            | Genotype test result (Y/N)              | Numeric_Results         | Lab Result                      |
| HCV_RNA                          | RNA test result                         | Resulted_Test_Name      | Name of test performed          |
| HCV_RNA_Date                     | RNA test collection date                | Test_Result_Code        | Lab Result                      |
| Investigation_Case_Status	       | Probable/Confirmed Status               | Text_Result             | Lab Result                      |
| Year	                           | Year of Investigation                   | Reporting_Facility      | Facility that submitted the lab |
| Patient_State                    | State, should be Maine                  | Patient ID (encoded)    | Encoded Patient Tracker         |
| Specimen_Collection_Date__HCV_Ge | Genotype test collection date           |                         |                                 |
| total_anti_HCV                   | Anti-HCV test result                    |                         |                                 |
| total_anti_HCV_Date              | Anti-HCV test collection date           |                         |                                 |
| County                           | Patient County                          |                         |                                 |
| Patient ID (encoded)             | Encoded Patient Tracker                 |                         |                                 |

#### Cleaned
The cleaned database combines the labs and case files, with two different views that are for different analytic uses. The primary view is wider-form, where each patient only gets one row and labs are ordered with test date, type, and result. 

![alt text](../figs/positive_rna_per_year.png)

### Additonal Reading
In-depth document on Hepatitis C survellience from the National CDC: 
* https://www.cdc.gov/hepatitis/statistics/surveillanceguidance/HepatitisC.htm 

More information about the Hepatitis C clearance cascade: 

* https://www.cdc.gov/mmwr/volumes/72/wr/mm7226a3.htm
* https://www.cdc.gov/mmwr/volumes/73/wr/mm7321a4.htm
