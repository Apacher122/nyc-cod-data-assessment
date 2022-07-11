# Assessing New York City Leading Causes of Death
Working with the New York City Leading Causes of Death dataset from the NYC Open Data website, this project aims to use tha apriori algorithm to extract and assess association rules within the dataset to understand correlations between gender and causes of death.

# Files
apriori.py (contains the modified apriori algorithm used)
utils.py (contains functions used within apriori.py)
data_preprocess.upynb (steps for data-preprocessing)
new_data.csv (integrated dataset)
output.txt  (our own output)
dataset.csv (original dataset)
run.sh (script to run program)

# Method
### The raw data file was pre-processed using the following steps:
 1. All the records with value 'All Other Causes' in the 'Leading Cause' column were removed.
 2. All the values in the column 'Sex' were transformed from ['M','F','Male','Female'] to ['Male','Female']
 3. All the rows containing the value 'Not Stated/Unknown' for the column 'Race Ethnicity' were removed.
 4. Finally, only the columns ['Leading Cause', 'Sex', 'Race Ethnicity'] were kept and the new dataframe is written as new_data in csv format.
 These steps are contained within "data_preprocess.ipynb"

### Variations to the Apriori Algorithm:
Pruning is used within the apriori algorithm to reduce the size of the candidateSet by removing infrequent itemsets.

### How to Run:
  bash run.sh new_data.csv (minimum-support) (minimum-confidence)

### Command-line arguments used to produce output.txt:
  bash run.sh new_data.csv 0.02 0.5


# Understanding output.txt
### TW: Death, Suicide, Self-Harm
The high-confidence association rules suggest that there is
        a strong correlation between being male and self-harm as well as
        females and Alzheimer. What makes this compelling is that this
        supports studies that suggest women are more prone to Alzheimers.
        However, what is surprising is that intential self-harm seems to be
        the "popular" case among males in terms of cause of death. In terms
        of mental health, studies have shown that women tend to use certain
        methods of self-harm moreso than men, however actual death by 
        intentional self-harm seems to be more prevalant in men. Upon further 
        research, the American Foundation for Suicide Prevention determined 
        that "men died by suicide 3.88x more than women" in 2020.
 
### Sources:
https://afsp.org/suicide-statistics/  
https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam

### Collaborative effort by:
Rey Christopher Desales Aparece (rda2126@columbia.edu)  
Stacy Lai (sl4450@columbia.edu)
