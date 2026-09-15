#COMP1888 (2025-2026) Programming for Data Science
#CW1 Portfolio, Deadline 12/11/2025
#Student ID 001260070
# Portfolio Question 3c


from collections import Counter

medications = {
    "P001": [("Metformin", 500, "mg", 2), ("Lisinopril", 10, "mg", 1)],
    "P002": [("Ibuprofen", 400, "mg", 3)],
    "P003": [("Metformin", 1000, "mg", 2), ("Atorvastatin", 20, "mg", 1)],
    "P004": [("Amlodipine", 5, "mg", 1), ("Albuterol", 90, "mcg", 2)],
    "P005": [("Metformin", 500, "mg", 2), ("Aspirin", 81, "mg", 1),
             ("Carvedilol", 25, "mg", 2)]
}

# Format: (medication_name, dose, unit, times_per_day)

def sum_medications(med_list):

    all_meds = []
    patient = {}


    for patient_id, meds_list in med_list.items():
        patient[patient_id] = len(meds_list)


        for medication_t in meds_list:
            medication_name = medication_t[0]
            all_meds.append(medication_name)


    med_counts = Counter(all_meds)
    most_meds = med_counts.most_common()



    poly_patients = []

    for patient_id, med_count in patient.items():
        if med_count >= 3:
            patient_info = {
                "patient_id": patient_id,
                "medication_count": med_count
            }
            poly_patients.append(patient_info)


    return most_meds, poly_patients



meds, poly = sum_medications(medications)


print("Most Common Medications:")

rank = 1
for med_name, count in meds:
    print(f"   {rank}. Med.: {med_name}, prescriped to {count} patient(s)")
    rank = rank + 1
print("-" * 40)

print("Patients for Polypharmacy:")

if poly:
    for patient in poly:
        print(f"Patient ID {patient['patient_id']}: {patient['medication_count']} medications")
else:
    print("No polypharmacy patients")