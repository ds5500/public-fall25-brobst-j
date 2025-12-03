# Hepatitis C Clearence Cascade V3
**Lead Student:** Joshua Brobst             **Lead Student Email:** brobst.j@northeastern.edu

**Stakeholder:** Chloe Manchester           **Stakeholder Email:** chloemanchester@northeastern.edu

**Instructor:** Phillip Bogden

## The Project
Hepatitis C Virus (HCV) is a "notifiable condition" in Maine, meaning that all positive lab results are required by law to be reported to the Department of Health and Human Services (DHHS); it is also classified as either 'Acute' or 'Chronic'. 

This project has three primary goals and deliverables:

#### 1. Creation: [Complete]

Creating a reproducable data view showing patients and what labs they have had preformed. This should be able to be reproduced and updated by anyone working at the CDC. This is meeting a need for a better way to understand the data, since the CDC currently has no way to find trends in HCV.

#### 2. Analysis:

Using the database/data view from goal one, there are two primary research questions this project hopes to find answers for:

1. Hepatitis C Clearance Cascade:

This is the first and highest priority analysis for the project. The CDC is interested in finding out how many people are at each stage of the HCV 'clearance cascade' - 
* Antibody Test
* RNA Test
* Genotype Test (Optional)
* Cured/Cleared Infection
* Reinfection (Optional)

Monitoring how often pateients make it from one end to the other is important in identifing where resources are lacking and what treatments work.

2. Testing patterns (Prevalence Analysis): 

Looking at the HCV labs, it will be analyzed what patterns are able to be noticed in the testing behavior. Example testing questions are:
* How many serology tests are patients getting getting before they get a confirmatory viral load? 
* What factors are associated with failure to get a viral load test? 
* What factors are associated with repeat viral loads but not achieving cure? 
* How many cases in a given time period in a given geographic area would be a trigger for a potential outbreak?

#### Reporting:
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
Oringal datasets are case-patient records meaning data points in the surveillance system represent individuals with HCV. The CDC collect a wide range of variables on each patient. Some case-patient investigations are more complete than others because of how different HCV conditions are prioritized. Due to the disease's nautre as a "norifiable condition", there is high confidence that the dataset is representative of the whole population in the state of Maine. However, data records were not reliably complete until 2016. 

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

![alt text](../figs/positive_rna_per_year.png)

## The Plan

### Goals
This will be a continuation of my capstone work, specifically with the minor goal of finishing the p analysis (along with any other analyses that may prove insightful that are discovered on the way) and co-authoring the publication. This is in line with the Capstone class, where the primary goals were creating the data view and doing an analysis on the clearance cascade. 

### Regular Check-ins
While I currently do not have set plans to meet with my faculity advisor on a set cadence, I do currently meet with my stakeholder weekly for at least 30 minutes (up to an hour) to discuss the previous week's work and next steps. This is something I will continue to do in the spring, with one or two meetings during winter break. 

Faculity meetings will be determined based on where the Capstone class ends, and at one points it feels realistic to have specific pieces of the paper written. 

### Timeline
* **November 2025**
    * **27th**: Finish evaluation on the clearence cascade, specifically looking at the reliablity of RNA negatives from different reporting labratories. 

* **December 2025**
    * **4th**: Present on semester findings and learnings.

* **January 2026**
    *  Finish analysis on prevelance analysis, provided vital records can be obtained.

* **February 2026**
    * Start first draft of report.
    * Preform adhoc analysis that arise through working on writing report. 
    * Revise timeline for second half of semester

* **March 2026**
    * Second draft of report, start publication process with board (this will be done through stakeholder, we do already have IRB approval through the state CDC's methods).
    * Spring break. 

* **April 2026**
    * Revise. 

* **May/June 2026**
    * While I will have graduated at this point, from May 31st to  June 4th there is a national epidemiology confrence my stakeholder has encouraged me to apply for, and I would like to attend assuming fanacial ability. 

### Grading
* The primary deliverable will be the peer-reviewed paper
* To supliment this, there will be monthly check-ins due at each meeting with my advisor. These check-ins are written reports that detail what I’ve acomplished and struggled with throughout the past month, and what I’ll do next in the forthcoming month before the next meeting.
