# 📊 Project Findings

## Overview

This portfolio applies core Python programming techniques to three practical areas:

- 🏥 Healthcare data processing and risk prioritisation
- 🌦️ Weather data processing
- 🔐 Password security tools

The exercises demonstrate how Python can be used to clean, process, combine and interpret structured data while producing clear outputs for different use cases.

---

# 🏥 Healthcare Risk & Operations Analysis

## 🩺 Patient Risk Analysis

Patient information and laboratory results were combined using a common patient ID.

A rule-based scoring system evaluated:

- age
- number of existing medical conditions
- blood glucose
- systolic blood pressure
- cholesterol

Points were assigned according to predefined thresholds and combined into a total risk score.

The resulting patient scores were sorted in descending order so that patients with the highest calculated risk appeared first.

### 💡 Key Finding

The exercise demonstrated how multiple individual risk indicators can be transformed into a single interpretable score and used to prioritise records.

It also demonstrated the importance of linking datasets correctly through a common identifier before performing calculations.

> ⚠️ The risk scores used in this project were defined for an academic programming exercise and are not clinically validated.

---

## 🏨 Appointment Analysis

Healthcare appointment records were analysed to understand activity across doctors and departments.

The program aggregated appointment duration by department and converted total appointment time from minutes into hours.

It also counted how many appointments were handled by each doctor.

### 💡 Key Finding

Individual appointment records can be transformed into operational summaries through aggregation.

Rather than reviewing appointments individually, the resulting metrics make it possible to compare workload across departments and doctors.

This exercise demonstrated:

- dictionary aggregation
- counting
- reusable functions
- loops
- data summarisation

---

## 💊 Medication Analysis

Medication records were processed to understand prescription frequency and medication use at patient level.

The analysis calculated:

- the number of medications taken by each patient
- how frequently individual medications appeared
- which medications occurred most frequently
- which patients were taking three or more medications

Python's `Counter` functionality was used to aggregate medication names efficiently.

### 💡 Key Finding

The exercise demonstrated how nested records can be transformed into both patient-level and dataset-level summaries.

A single processing workflow could therefore answer two different questions:

```text
Patient Level
→ How many medications is each patient taking?

Dataset Level
→ Which medications occur most frequently?
```

---

## 🚨 Patient Priority Analysis

The final healthcare exercise extended the previous analyses by combining:

```text
Patient Information
        +
Medication Data
        +
Laboratory Results
        │
        ▼
Combined Patient Profile
        │
        ▼
Priority Score
        │
        ▼
Urgency Category
```

The priority score incorporated four factors:

1. age
2. number of medical conditions
3. laboratory abnormalities
4. medication count

Each patient was assigned a total score and corresponding urgency category:

- Low
- Moderate
- High
- Critical

The final output was sorted in descending order so that the patients with the highest calculated urgency appeared first.

### 💡 Key Finding

This was the most comprehensive exercise in the portfolio because it moved beyond analysing one dataset independently.

Instead, multiple sources were integrated to create a new decision-support variable: **patient priority**.

The exercise demonstrates a basic version of a common analytics workflow:

```text
Multiple Data Sources
        ↓
Data Integration
        ↓
Feature Evaluation
        ↓
Scoring
        ↓
Classification
        ↓
Prioritisation
```

> ⚠️ The priority categories and scoring rules are academic examples only and should not be interpreted as medical recommendations.

---

# 🌦️ Weather Data Processing

The weather project processed daily weather observations containing information such as date, temperature and rainfall.

Before analysing each record, the program checked whether required values were available.

Records containing missing or invalid information were excluded from subsequent processing.

Valid observations were then classified according to rainfall conditions.

```text
Rainfall > 0
    ↓
Wet Day

No Rainfall
    ↓
Dry Day
```

The processed weather information was displayed in a structured format and could be sorted to make comparisons easier.

### 💡 Key Finding

The exercise demonstrated why **data validation should occur before analysis**.

By checking for missing or invalid observations before calculations were performed, the program avoided processing incomplete records.

The project also demonstrated how simple conditional logic can transform continuous numerical information into understandable categories.

---

# 🔐 Password Security Analysis

## 🛡️ Password Strength Checker

The password-strength checker evaluates a user-entered password using several characteristics, including:

- length
- uppercase characters
- lowercase characters
- numerical characters
- special characters
- common patterns

The program combines these checks into a password-strength score between **0 and 100**.

Common patterns reduce the resulting score, while characteristics associated with stronger passwords increase it.

The final score is translated into user-facing feedback.

### 💡 Key Finding

The project demonstrates how several independent conditions can be combined into a single scoring system.

It also demonstrates interactive Python programming through `input()`, string processing and conditional feedback.

---

## 🔑 Password Generator

The password generator allows the user to define which types of characters should be included in a generated password.

Available options include:

- uppercase characters
- lowercase characters
- numbers
- special characters

The program dynamically builds the available character set according to the user's selections before generating a random password.

### 💡 Key Finding

The exercise demonstrates how user input can dynamically change program behaviour rather than relying on fixed parameters.

---

# 🧠 Overall Technical Findings

Across the projects, several recurring programming and data-analysis concepts were applied.

### Data Structures

Python dictionaries, lists and tuples were used to organise and access structured records.

### Data Validation

Missing or invalid values were identified before further processing where relevant.

### Data Integration

Healthcare datasets were connected through patient IDs, demonstrating how information from separate sources can be combined.

### Aggregation

Loops, dictionaries and `Counter` were used to convert individual records into summary statistics.

### Rule-Based Scoring

Multiple variables were transformed into combined scores for the password and healthcare applications.

### Classification

Numerical or calculated values were converted into interpretable categories such as:

```text
Wet / Dry

Low / Moderate / High / Critical

Weak / Strong Password
```

### Ranking

Calculated patient scores were sorted to prioritise higher-scoring records.

---

# 🎯 Overall Takeaway

The portfolio demonstrates my progression from fundamental Python concepts toward more structured analytical workflows.

The most important progression across the exercises was moving from:

```text
Basic Python Logic
        ↓
Structured Data Processing
        ↓
Data Validation
        ↓
Aggregation
        ↓
Multiple Dataset Integration
        ↓
Calculated Metrics
        ↓
Classification & Prioritisation
```

The healthcare exercises were particularly useful for developing my understanding of how separate datasets can be integrated and transformed into structured analytical outputs.

These foundations were subsequently developed further throughout my MSc through larger projects involving **Pandas, statistical analysis, machine learning, data visualisation and business-focused analytics**.

---

## 🎓 Academic Context

These exercises were originally completed for **COMP1888 – Programming for Data Science** as part of the MSc Data Science and Its Applications programme at the University of Greenwich.

This findings document summarises the main analytical outcomes and programming concepts demonstrated by the portfolio.

---

## 👩🏼‍💻 Author

**Julia Legner**  
MSc Data Science and Its Applications  
University of Greenwich
