# NYC Public School SAT Performance Analysis

## Overview

This project involves an in-depth analysis of the SAT performance of New York City (NYC) public schools. The SAT, a standardized test conducted annually, is critical for high school students in the United States. It assesses their literacy, numeracy, and writing skills, playing a vital role in college admissions. 

The analysis focuses on three main questions:
1. Identifying which schools are best for math.
2. Determining the top 10 performing schools based on total SAT scores.
3. Analyzing which NYC borough shows the highest variability in SAT scores.

## Dataset

The dataset, named `schools.csv`, comprises various metrics from NYC public schools, including average scores in math, reading, and writing sections of the SAT.

## Tools and Libraries

- **Python:** A versatile programming language used for data analysis.
- **Pandas:** A Python library used for data manipulation and analysis.

## Methodology

### 1. Identifying Best Math Schools

- **Filtering Criteria:** Schools with an average math score of 640 or higher.
- **Sorting:** Schools are sorted in descending order based on their math scores.
- **Output:** A list of schools that excel in the math section of the SAT.

### 2. Top 10 Performing Schools

- **Total SAT Calculation:** A new column `total_SAT` is created, summing the average scores in math, reading, and writing.
- **Grouping and Sorting:** Schools are grouped by name, and their mean total SAT scores are calculated and sorted.
- **Output:** A list of the top 10 schools based on their total SAT scores.

### 3. Borough Analysis

- **Grouping by Borough:** The dataset is grouped by borough, and statistical measures (count, mean, standard deviation) for total SAT scores are calculated.
- **Variability Analysis:** The borough with the highest standard deviation in total SAT scores is identified, indicating the most variability in school performance.
- **Output:** Statistical overview of the borough with the highest variability in SAT scores.

## Results and Discussion

The results from this analysis provide valuable insights into the performance of schools in different aspects of the SAT. The identification of schools excelling in math and those with high overall SAT scores can aid stakeholders in making informed decisions. Additionally, the borough analysis highlights areas with greater disparities in educational outcomes, which can be a focal point for policy intervention.

## Conclusion

This project showcases an effective use of data analysis techniques to derive meaningful insights from educational data. It reflects the power of Python and Pandas in handling and analyzing large datasets, providing a basis for informed decision-making and policy formulation in the educational sector.

## Repository Structure

- `README.md`: This file, containing an overview of the project and methodology.
- `analysis_script.py`: The Python script used for the analysis.
- `schools.csv`: The dataset used for this project.

## How to Run the Script

1. Ensure Python and Pandas are installed on your machine.
2. Clone this repository.
3. Run `analysis_script.py` to perform the analysis.

## From DataCamp 
https://app.datacamp.com/workspace/w/43fd6d81-efb6-4e41-b042-d714dd366438/edit

