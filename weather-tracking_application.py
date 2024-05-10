weather_data = [
    {"date": "2023-10-23", "high": 25, "low": 18, "conditions": "Sunny"},
    {"date": "2023-10-24", "high": 28, "low": 20, "conditions": "Cloudy"},
    {"date": "2023-10-25", "high": 30, "low": 22, "conditions": "Rainy"},
    {"date": "2023-10-26", "high": 27, "low": 21, "conditions": "Partly Cloudy"},
    {"date": "2023-10-27", "high": 24, "low": 19, "conditions": "Windy"},
    {"date": "2023-10-28", "high": 26, "low": 20, "conditions": "Sunny"},
    {"date": "2023-10-29", "high": 22, "low": 17, "conditions": "Clear"},
]

# Calculate the average temperature
total_high = 0
total_low = 0
for day in weather_data:
    total_high += day["high"]
    total_low += day["low"]

average_high = total_high / len(weather_data)
average_low = total_low / len(weather_data)
average_temp = (average_high + average_low) / 2

# Find the day with the highest temperature
highest_temp = 0
highest_temp_day = None
for day in weather_data:
    if day["high"] > highest_temp:
        highest_temp = day["high"]
        highest_temp_day = day

# Print the results
print("Average temperature:", average_temp)
print("Day with highest temperature:", highest_temp_day["date"], highest_temp, "degrees Celsius")
