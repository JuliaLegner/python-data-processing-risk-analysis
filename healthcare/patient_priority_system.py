#COMP1888 (2025-2026) Programming for Data Science
#CW1 Portfolio, Deadline 12/11/2025
#Student ID 001260070
# Portfolio Question 3d

patients = {
    "P001": {"name": "John Smith", "age": 45, "gender": "M", "conditions": ["diabetes", "hypertension"]},
    "P002": {"name": "Mary Jones", "age": 62, "gender": "F", "conditions": ["arthritis"]},
    "P003": {"name": "David Brown", "age": 38, "gender": "M", "conditions": ["diabetes", "obesity"]},
    "P004": {"name": "Sarah Wilson", "age": 55, "gender": "F", "conditions": ["hypertension", "asthma"]},
    "P005": {"name": "Tom Davis", "age": 70, "gender": "M", "conditions": ["heart_disease", "diabetes"]}
}

medications = {
    "P001": [("Metformin", 500, "mg", 2), ("Lisinopril", 10, "mg", 1)],
    "P002": [("Ibuprofen", 400, "mg", 3)],
    "P003": [("Metformin", 1000, "mg", 2), ("Atorvastatin", 20, "mg", 1)],
    "P004": [("Amlodipine", 5, "mg", 1), ("Albuterol", 90, "mcg", 2)],
    "P005": [("Metformin", 500, "mg", 2), ("Aspirin", 81, "mg", 1), ("Carvedilol", 25, "mg", 2)]
}

lab_results = {
    "P001": {"glucose": 145, "bp_systolic": 135, "bp_diastolic": 85, "cholesterol": 210},
    "P002": {"glucose": 95, "bp_systolic": 120, "bp_diastolic": 75, "cholesterol": 185},
    "P003": {"glucose": 160, "bp_systolic": 140, "bp_diastolic": 90, "cholesterol": 240},
    "P004": {"glucose": 100, "bp_systolic": 145, "bp_diastolic": 92, "cholesterol": 195},
    "P005": {"glucose": 155, "bp_systolic": 150, "bp_diastolic": 95, "cholesterol": 220}
}


def urgency_care(patients, medications, lab_results):
    prio = []

    for id in patients:
        pn_age = 0

        details = patients[id]
        name = details["name"]
        age = details["age"]
        cond = details["conditions"]


        if age > 70:
            pn_age += 25
        elif age > 60:
            pn_age += 15
        else:
            pn_age += 0


        pn_condition = 10 * len(cond)

        p_labs = lab_results[id]
        glucose = p_labs["glucose"]
        bp_systolic = p_labs["bp_systolic"]
        cholesterol = p_labs["cholesterol"]

        pn_lab = 0

        if glucose > 110:
            pn_lab += 8

        if bp_systolic > 130:
            pn_lab += 8

        if cholesterol > 200:
            pn_lab += 8

        patient_meds = medications[id]
        num_medications = len(patient_meds)

        pn_medication = 0
        if num_medications >= 3:
            pn_medication = 15

        end_score = pn_age+ pn_condition+ pn_lab + pn_medication

        level = ""
        if end_score >= 60:
            level = "CRITICAL"
        elif end_score >= 45:
            level = "HIGH"
        elif end_score >= 30:
            level = "MODERATE"
        else:
            level = "LOW"

        p_priority = {
            "patient_id": id,
            "name": name,
            "priority_score": end_score,
            "urgency_level": level
        }

        prio.append(p_priority)

    prio.sort(key=lambda x: x["priority_score"], reverse=True)

    return prio

rslt = urgency_care(patients, medications, lab_results)

print("\n")
print(f"{'Patient-ID':<15} {'Name':<15} {'Priority Score':<15} {'Urgency Level'}")
print("-" * 70)

for p in rslt:
    print(f"{p['patient_id']:<15} {p['name']:<15} {p['priority_score']:<15} {p['urgency_level']}")

