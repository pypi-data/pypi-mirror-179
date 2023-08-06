# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data.
 We have modelled the median house value on given housing data. 

The following techniques have been used: 

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## Procedure to run and install code
   1) Create all required dependencies from env.yml file using the below code
#### Command to create an environment from the env.yml file
conda env create --prefix ./env --file environment.yml
2) Then activate the environment and select the python interpreter path
## activate environment
conda activate < environment name > 
## To excute the script
set remote_server_uri = "http://localhost:5000"
then
1) run the script setup.py to initiate the ml workflow.
2)To run python script  run python < scriptname.py >