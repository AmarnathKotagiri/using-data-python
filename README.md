[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8539596&assignment_repo_type=AssignmentRepo)
# Using Data THA
Create a new Python file. This file should contain all the code used for the following exercise. Take screen captures of the output in the Python console.

To submit, please perform the following:
1. Save a script file for Python with the following name: `tha_lastname_firstname.py` where lastname is your last name and firstname is your first name.
1. Save your screenshots of your output to the directory `assets`. This directory exists at the same leve as `data`.
1. Link your screenshots in `submission.md` where appropriate. That is, if you have screenshots supporting your answers, link those screenshots next to your answer.
1. Answer questions in `submission.md`, linking any screenshots as necessary.
1. Save your exported data files to the directory `data` for this repository.
1. Push your assignment to GitHub.

### Context of Assignment
You currently work in the Information Systems department for a consulting firm working with the state government agency that oversees the healthcare system in California. Your administrator, Randall Cunningham, reports directly to the CIO of your company. You have been asked to join a team charged with assessing the condition of the healthcare system in California. Several surveys were emailed to a random sample of 61 hospitals and the results have been recorded in the file [CaliforniaHospitalData.csv](data/CaliforniaHospitalData.csv). Additionally, you have been provided with personnel data containing employee information within the file [CaliforniaHospitalData_Personnel.txt](data/CaliforniaHospitalData_Personnel.txt). See the tables below for more metadata.

This first table provides the variables in the hospital data.

| Variable | Description |
|:---|:---|
| HospitalID | The primary key of each hospital |
| Name | The legal name of the hospital |
| Zip | Zipcode where the hospital is located |
| Website | The url for the hospital’s website |
| TypeControl | Indicates the primary managing entity of the hospital |
| Teaching | Indicates teaching status |
| DonorType | This field indicates the most prominent group of donors |
| NoFTE | Number of full-time employees registered at the hospital |
| NetPatRev | Net patient revenue |
| InOperExp | Estimate of the inpatient operating costs |
| OutPerExp | Estimate of the outpatient operating costs |
| OperRev | Operating revenue of the hospital |
| OperInc | Operating Income is the operating revenue less the operating expenses |
| AvlBeds | The number of available beds in the hospital |

This second table provides the data for the personnel data.

| Variable | Description |
|:---|:---|
| HospitalID | The foreign key of the hospital where position is held |
| Work_ID | Primary key of the personnel |
| LastName | The last name of the personnel |
| FirstName | First name of the personnel |
| Gender | Gender of the individual |
| PositionID | The foreign key for the position held |
| PositionTitle | The title of this position |
| Compensation | The annual amount the position is compensated for service |
| MaxTerm | The maximum number of years an individual can serve in this position |
| StartDate | The beginning of service for this position |

Your purpose for this assignment is to pre-process this data for the Business Intelligence team. They need to perform descriptive analyses on the data and have requested you to provide a clean start for them.

Using Python, import the data and combine both into a single dataframe. Note, both files have the column HospitalID. Use this column to merge the files. That is, each employee has a unique position at one or more hospitals; these positions need to be combined with the correct hospital. Each hospital has one unique employee listed in the data.

After the data has been merged, please remove the following columns of data:
* duplicate columns
* `Work_ID`
* `PositionID`
* `Website`

Select only those hospitals that are *Small/Rural* and have 15 or more available beds. Exclude hospitals with a negative operating income. Export your data as tab-delimited and name the file `hospital_data_new.txt`. Save this to the directory `data`.

Open the newly created file in Python as a new dataframe. Change the name of the following columns:
* `NoFTE` to `FullTimeCount`
* `NetPatRev` to `NetPatientRevenue`
* `InOperExp` to `InpatientOperExp`
* `OutOperExp` to `OutpatientOperExp`
* `OperRev` to `Operating_Revenue`
* `OperInc` to `Operating_Income`

Select two of the existing hospitals in the data and create a new position for each hospital. Insert yourself as the new employee at those two hospitals; put in your first name and last name. Put today’s date as the start date. Select one of the positions as shown in the table below and fill out the data accordingly. Fill in the rest of the columns as you choose. You should have two new rows of data. Save the data frame as `new_merge`.

| PositionTitle | Compensation | MaxTerm |
|:---|---:|:---:|
| Regional Representative | 46978 | 4 |
| State Board Representative | 89473 | 3 |
| Acting Director | 248904 | 8 |
| Safety Inspection Member | 23987 | 2 |

Convert any date-time columns into a datetime datatype. Confirm your changes by outputting the datatypes for all columns to your Python console.
* Using the `new_merge` data, select all hospitals that are non-profit with more than 250 employees, unless the net patient revenue is smaller than $109,000. Remove the columns containing employee information and save it as a new dataframe. Export the data as a new tab-delimited file.
* Using the `new_merge` data, select all the *Regional Representatives* who work at a hospital with operating income greater than $100,000. Save this as a new dataframe and then export it as a new file.
