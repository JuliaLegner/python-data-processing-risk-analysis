# 🐍 Python Data Processing & Risk Analysis

### Applied Python portfolio covering healthcare risk analysis, weather data processing and password security tools

A collection of Python projects demonstrating **data processing, analytical problem-solving, rule-based scoring, aggregation and core programming concepts**.

The portfolio was developed during the **Programming for Data Science** module of my MSc Data Science and Its Applications and contains three applied areas: **healthcare analytics, weather data processing and password-security tools**.

The healthcare analysis forms the most substantial component, combining multiple datasets to calculate patient risk scores, analyse healthcare operations and create a rule-based priority system.

---

## 🎯 Project Overview

The objective of this portfolio was to apply Python programming concepts to practical data-processing and analytical problems.

Across the projects, I worked with:

- 🐍 Python programming
- 🔄 Loops and conditional logic
- 🧩 Functions
- 📚 Lists, tuples and dictionaries
- 🧹 Missing-data handling
- 🔗 Multi-source data integration
- 📊 Data aggregation
- 🏷️ Rule-based classification
- 🔢 Sorting and ranking
- 💻 Interactive user input and formatted outputs

---

# 🏥 1. Healthcare Risk & Operations Analysis

The healthcare project is the largest component of the portfolio.

It uses patient information, laboratory results, appointment records and medication data to demonstrate how Python can transform structured records into useful analytical outputs.

---

## 🩺 Patient Risk Scoring

A rule-based risk scoring system was developed to assess patients using several factors:

- age
- existing medical conditions
- blood glucose
- systolic blood pressure
- cholesterol

The program combines these factors into a **total risk score** for each patient.

Results are then sorted from highest to lowest score, allowing higher-risk cases to be identified quickly.

### 🔄 Risk Scoring Workflow

```text
Patient Information
        +
Laboratory Results
        │
        ▼
  Extract Risk Factors
        │
        ▼
Apply Rule-Based Scoring
        │
        ▼
 Calculate Total Score
        │
        ▼
 Rank Patients by Risk
```

This exercise demonstrates the use of **functions, dictionaries, loops, conditional logic, scoring systems and sorting**.

---

## 🏨 Appointment & Department Analysis

Appointment records were analysed to generate operational healthcare metrics.

The program:

- calculates total appointment duration by department
- converts appointment minutes into hours
- counts appointments handled by each doctor
- compares activity across departments
- identifies the busiest doctor and department

Individual appointment records are aggregated using dictionaries and reusable Python functions.

This demonstrates how raw operational records can be transformed into concise management-level summaries.

---

## 💊 Medication Analysis

The medication analysis processes prescription information across multiple patients.

The program calculates:

- number of medications per patient
- frequency of individual medications
- most frequently prescribed medications
- patients taking three or more medications

Python's `collections.Counter` functionality is used to efficiently aggregate medication occurrences.

### Techniques demonstrated

`Dictionaries` · `Nested Loops` · `Counter` · `Aggregation` · `Filtering` · `Frequency Analysis`

---

## 🚨 Patient Priority System

The final healthcare exercise combines **three separate data sources**:

```text
Patient Records
      +
Medication Records
      +
Laboratory Results
      │
      ▼
 Data Integration
      │
      ▼
Risk Factor Evaluation
      │
      ▼
Priority Score Calculation
      │
      ▼
Urgency Classification
      │
      ▼
Patient Prioritisation
```

The priority calculation considers four main areas:

- 👤 Age
- 🩺 Existing medical conditions
- 🧪 Laboratory abnormalities
- 💊 Number of medications

Each patient receives a total score and is assigned to an urgency category:

```text
Low
Moderate
High
Critical
```

The final results are sorted in descending order so that the highest-priority patients appear first.

This exercise demonstrates how **multiple datasets can be integrated through a common identifier and transformed into a structured decision-support output**.

> ⚠️ **Important:** This scoring system was developed as an academic Python programming exercise and is not a clinically validated medical risk model.

---

# 🌦️ 2. Weather Data Processing

The weather project demonstrates fundamental data-cleaning and transformation techniques using daily weather records.

The dataset contains information including:

- date
- temperature
- rainfall

The program processes these records and produces a structured weather summary.

### 🧹 Data Processing

The workflow includes:

- identifying incomplete observations
- skipping records with missing or invalid values
- processing temperature and rainfall information
- classifying observations as wet or dry
- sorting weather records
- displaying results in a structured format

### ☔ Weather Classification

Conditional logic is used to classify each valid observation based on rainfall:

```text
Rainfall detected
      │
      ├── Yes → Wet Day
      │
      └── No  → Dry Day
```

This project demonstrates the practical use of **loops, conditionals, data validation and sorting**.

---

# 🔐 3. Password Security Tools

The portfolio also contains two interactive Python applications focused on password security.

---

## 🛡️ Password Strength Checker

The password-strength checker evaluates a user-entered password against several characteristics.

These include:

- password length
- lowercase characters
- uppercase characters
- numbers
- special characters
- common or predictable patterns

The program produces a final password-strength score between:

```text
0 ─────────────────────────────── 100
Weak                              Strong
```

The resulting score is then translated into user feedback indicating whether the password is weak or sufficiently strong.

This demonstrates:

`String Processing` · `Conditional Logic` · `Functions` · `User Input` · `Pattern Detection`

---

## 🔑 Password Generator

A second interactive program generates random passwords based on user-defined requirements.

Users can specify whether the generated password should contain:

- uppercase letters
- lowercase letters
- numbers
- special characters

The program then dynamically constructs the available character pool and generates a password based on the selected requirements.

This demonstrates the use of **user input, randomisation, string manipulation and conditional program logic**.

---

# 🛠️ Technologies & Skills

## 💻 Python

`Python` `Functions` `Loops` `Conditional Logic`  
`Dictionaries` `Lists` `Tuples` `String Processing`

## 📊 Data Processing

`Data Cleaning` `Missing Data Handling` `Data Integration`  
`Aggregation` `Filtering` `Sorting` `Classification`

## 🧠 Analytical Techniques

`Risk Scoring` `Priority Ranking` `Frequency Analysis`  
`Operational Analysis` `Rule-Based Classification`

## 📦 Python Libraries & Modules

`datetime` `collections` `re` `string` `random`

---

# 📁 Repository Structure

```text
python-data-processing-risk-analysis/
│
├── README.md
│
├── healthcare/
│   ├── patient_risk_analysis.py
│   ├── appointment_analysis.py
│   ├── medication_analysis.py
│   └── patient_priority_system.py
│
├── weather/
│   └── weather_data_processing.py
│
├── password-tools/
│   ├── password_strength_checker.py
│   └── password_generator.py
│
├── images/
│   ├── healthcare_risk_output.png
│   ├── patient_priority_output.png
│   └── weather_analysis_output.png
│
└── report/
    └── COMP1888_CW1_Portfolio.pdf
```

---

# 💡 Key Learning Outcomes

This portfolio demonstrates my progression from **fundamental Python programming to more structured data-processing and analytical tasks**.

Key areas developed through the project include:

- writing reusable Python functions
- working with nested data structures
- processing and validating records
- combining information from multiple datasets
- aggregating data into meaningful summaries
- developing rule-based scoring systems
- ranking observations according to calculated metrics
- translating analytical logic into understandable outputs

The healthcare exercises particularly strengthened my understanding of **data integration, aggregation, analytical scoring and transforming raw records into decision-support information**.

---

# ⚠️ Limitations

These projects were developed as programming exercises using relatively small provided datasets.

They are intended to demonstrate **Python programming and analytical techniques rather than production-ready systems**.

In particular, the healthcare risk and priority scores are rule-based academic exercises and **should not be interpreted as clinically validated medical models**.

The weather and password applications similarly demonstrate programming concepts rather than production systems.

---

# 🚀 Future Improvements

Potential extensions to this portfolio include:

- migrating the analyses to **Pandas DataFrames**
- implementing automated data-validation checks
- adding unit testing
- introducing exception handling
- creating analytical visualisations with **Matplotlib**
- developing interactive dashboards with **Power BI**
- processing larger external datasets
- creating more reusable and modular Python functions

The healthcare component could also be extended into a larger analytics project incorporating exploratory data analysis, visualisation and dashboard-based reporting.

---

# 🎓 Academic Context

Originally developed for **COMP1888 – Programming for Data Science** during Term 1 of the **MSc Data Science and Its Applications** programme at the University of Greenwich.

For this GitHub portfolio, the coursework is presented as a collection of applied Python projects demonstrating my development in **programming, data processing and analytical problem-solving**.

---

# 👩🏼‍💻 Author

**Julia Legner**  
MSc Data Science and Its Applications  
University of Greenwich

**Portfolio Focus:** Data Analytics • Business Intelligence • Python • Data Science
