#COMP1888 (2025-2026) Programming for Data Science
#CW1 Portfolio, Deadline 12/11/2025
#Student ID 001260070
# Portfolio Question 3b


appointments = [
    {"patient": "P001", "date": "2024-01-10", "doctor": "Dr. Smith",
     "department": "Cardiology", "duration": 30},
    {"patient": "P002", "date": "2024-01-10", "doctor": "Dr. Jones",
     "department": "Orthopedics", "duration": 45},
    {"patient": "P001", "date": "2024-01-15", "doctor": "Dr. Brown",
     "department": "Endocrinology", "duration": 30},
    {"patient": "P003", "date": "2024-01-20", "doctor": "Dr. Smith",
     "department": "Cardiology", "duration": 60},
    {"patient": "P004", "date": "2024-02-01", "doctor": "Dr. Wilson",
     "department": "Pulmonology", "duration": 30},
    {"patient": "P005", "date": "2024-02-05", "doctor": "Dr. Smith",
     "department": "Cardiology", "duration": 45}
]


def get_department_hours(appointments):
    dept_mins = {}
    for appt in appointments:
        dept = appt["department"]
        dept_mins[dept] = dept_mins.get(dept, 0) + appt["duration"]
    return {d: m/60 for d, m in dept_mins.items()}


def docs(appointments):
    doc_n = {}
    for appt in appointments:
        doc = appt["doctor"]
        doc_n[doc] = doc_n.get(doc, 0) + 1
    return doc_n


def max_dep(data_dict):
    return max(data_dict, key=data_dict.get), max(data_dict.values())



dept_hours = get_department_hours(appointments)
doctor_counts = docs(appointments)

busiest_dept, max_hours = max_dep(dept_hours)
busiest_doc, max_appts = max_dep(doctor_counts) # Added this line to define busiest_doc and max_appts



print("\n Department Hours:")

for dept, hours in sorted(dept_hours.items()):
    print(f"  {dept:20s}: {hours:.2f} hours")

print(f"\n Busiest Dept: {busiest_dept} ({max_hours:.2f} hours)")
print(f" Busiest Doctor: {busiest_doc} ({max_appts} appts)")
