# Assessing New York City Leading Causes of Death
Working with the New York City Leading Causes of Death dataset from the NYC Open Data website, this project aims to use the apriori algorithm to extract and assess association rules within the dataset to understand correlations between gender and causes of death.

# Some Concepts
### Association rule mining?
The purpose behind association rule mining is to find associations and relationships between items within a large dataset. These association rules can then be used to discover and possibly explain patterns/trends in data. There are two parts to an association rule: an antecedent and a consequent. The antecedent is some item found within a dataset and the consequent is another item found alongside the antecedent.

### What is the Apriori algorithm?
For the purposes of association rule mining, the apriori algorithm seeks to find the probability that some item A is present given that another item B exists within the same transaction. Essentially, the goal is to extract association rules that show correlations between items in the frequent itemsets to some degree of probability. In the case of this project, two parameters are used to examine association: support and confidence.
 - Support: the percentage of transactions that contain both item A and item B
 $$Support = \frac{frequency(A,B)}{N}$$
 - Confidence: the probability that item A and item B would appear in the same transaction
 $$Confidence = \frac{frequency(A,B)}{frequency(A)}$$
 
 To read more about the Apriori algorithm, see the following documentation from Oracle:
 https://docs.oracle.com/cd/E18283_01/datamine.112/e16808/algo_apriori.htm

# Files
apriori.py (contains the modified apriori algorithm used)  
utils.py (contains functions used within apriori.py)  
data_preprocess.ipynb (steps for data-preprocessing)  
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
The high-confidence association rules suggest that there is a strong correlation between being male and self-harm as well as females and Alzheimers. Our output supports studies that suggest women are more prone to Alzheimers. Moreso, what is surprising is that our output reveals that intential self-harm seems to be the "popular" case among males in terms of cause of death. In terms of mental health, studies have shown that women tend to use certain methods of self-harm moreso than men, however actual death by intentional self-harm seems to be more prevalant in men. Upon further research, the American Foundation for Suicide Prevention determined that "men died by suicide 3.88x more than women" in 2020.
 
### Sources:
https://afsp.org/suicide-statistics/  
https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam

### Collaborative effort by:
Rey Christopher Desales Aparece (rda2126@columbia.edu)  
Stacy Lai (sl4450@columbia.edu)

# Some tech stuff
Programming language and version: Python 3  
Operating systems used: MacOS, Linux (Ubuntu) 
