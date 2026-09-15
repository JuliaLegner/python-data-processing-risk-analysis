#COMP1888 (2025-2026) Programming for Data Science
#CW1 Portfolio, Deadline 12/11/2025
#Student ID 001260070
# Portfolio Question 3a

patients = {
    "P001": {"name": "John Smith", "age": 45, "gender": "M", "conditions": ["diabetes", "hypertension"]},
    "P002": {"name": "Mary Jones", "age": 62, "gender": "F", "conditions": ["arthritis"]},
    "P003": {"name": "David Brown", "age": 38, "gender": "M", "conditions": ["diabetes", "obesity"]},
    "P004": {"name": "Sarah Wilson", "age": 55, "gender": "F", "conditions": ["hypertension", "asthma"]},
    "P005": {"name": "Tom Davis", "age": 70, "gender": "M", "conditions": ["heart_disease", "diabetes"]}
}

lab_results = {
    "P001": {"glucose": 145, "bp_systolic": 135, "bp_diastolic": 85, "cholesterol": 210},
    "P002": {"glucose": 95, "bp_systolic": 120, "bp_diastolic": 75, "cholesterol": 185},
    "P003": {"glucose": 160, "bp_systolic": 140, "bp_diastolic": 90, "cholesterol": 240},
    "P004": {"glucose": 100, "bp_systolic": 145, "bp_diastolic": 92, "cholesterol": 195},
    "P005": {"glucose": 155, "bp_systolic": 150, "bp_diastolic": 95, "cholesterol": 220}
}


def calculate_risk(patients, lab_results):
    rslt = []

    for id in patients:
        score = 0
        patient_data = patients[id]
        lab_data = lab_results[id]

        age = patient_data["age"]
        conditions = patient_data["conditions"]

        if age > 70:
            score += 25
        elif age > 60:
            score += 15
        else:
            score += 0

        score += 10 * len(conditions)

        lab = 0
        if lab_data["glucose"] > 110:
            lab += 8
        if lab_data["bp_systolic"] > 130:
            lab += 8
        if lab_data["cholesterol"] > 200:
            lab += 8

        score += lab

        rslt.append((id, score))


    return rslt


my_results = calculate_risk(patients, lab_results)


my_results.sort(key=lambda x: x[1], reverse=True)


print("Risk Score:")
print("-" * 20)
for patient, score in my_results:
    patient_name = patients[patient]["name"]
    print(f"{patient}| {patient_name} : {score} points")
