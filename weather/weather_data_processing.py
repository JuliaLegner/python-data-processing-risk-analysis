#COMP1888 (2025-2026) Programming for Data Science
#CW1 Portfolio, Deadline 12/11/2025
#Student ID 001260070
# Portfolio Question 2

import datetime

weather_data = [
    ("2024-01-01", 5.2, 10.5),
    ("2024-01-02", 6.1, 0.0),
    ("2024-01-03", 4.8, 15.2),
    ("2024-01-04", 7.0, 2.3),
    ("2024-01-05", -1.5, 0.0),
    ("2024-01-06", 2.0, 6.0),
    ("2024-01-07", 8.4, 0.0),
    ("2024-01-08", 1.2, 12.1),
    ("2024-01-09", 9.5, 5.1),
    ("2024-01-10", -3.1, 11.0),
    ("2024-01-11", 0.0, 0.0),
    ("2024-01-12", 3.3, 20.0),
    ("2024-01-13", 12.5, 0.0),
    ("2024-01-14", 6.0, 7.5),
    ("2024-01-15", -0.2, 4.9),
    ("2024-01-16", 4.0, -1.0),
    ("2024-01-17", 5.5, 0.0),
    ("2024-01-18", 10.2, 30.0),
    ("2024-01-19", None, 3.0),
    ("2024-01-20", 2.4, None),
    ("2024-02-01", -4.0, 0.0),
    ("2024-02-02", 7.2, 0.0),
    ("2024-02-03", 1.1, 6.2),
]

def weather_rec(weather_data):
    weather = []

    for recs in weather_data:
        date, temp, rain = recs

        if rain is None or temp is None:
            continue

        if rain > 10:
            status = "Wet Day"
        else:
            status = "Dry Day"

        avg = round((temp + rain) / 2, 2)

        fin_date = datetime.datetime.strptime(date, '%Y-%m-%d')

        weather.append({
            'date': date,
            'temp': temp,
            'rain': rain,
            'status': status,
            'avg': avg,
            'clean_date': fin_date
             })

    clean_weather = sorted(weather, key=lambda r:r['temp'])
    result = [(record['date'], record['status'], record['avg'])
              for record in clean_weather]

    return result

end_weather = weather_rec(weather_data)
print("\n")
print("US Weather Data January:")
print("-" * 30)
for date, status, average in end_weather:
    print(f"{date}: {status:10} | Avg Temperature: {average:6.2f}")



