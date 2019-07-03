# DBS_Project

Database Systems Sommer Semester FU Berlin final project - Mini facebook page 

## Getting Started

### Where to find data

Original Data can be found at FU Berlin kvv web system

### How to run data processing scripts

All scripts can be found if scripts folder. Original folders should be in original files_data folder, You should also have processed_data folder on your disc

1. Preprocess original files to make it readable by pandas, run preprocess_excel.py on all original files
1.1 Replace all files from original_data folder by processed data from processed_data folder it is really important cause without nothing will be wokring properly
2. In order to rename columns to proper names (original names are from twitter we need to rename it) run extract_data_from_users.py
3. Run remove_invalid_users.py to get rid of useless user records
4. Run get_user_age_and_income.py to get user age and income columns
5. Run get_hobby to create hobby1.csv and hobby2.csv files 
6. Run get_is_fan_relation.py to get is_fan relations csv data file 

## Front end part


### Prerequisites
```
-dateutil
-tqdm
-pandas
-csv
```


## Authors

* [tugot17](https://github.com/tugot17)
* [timruet](https://github.com/timruet)
* [MarcelGlab](https://github.com/MarcelGlab)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
