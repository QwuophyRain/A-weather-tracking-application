def create_weather_data():
  """
  Creates an empty list to store daily weather data.
  """
  return []

def add_weather_data(data, date, high, low, conditions):
  """
  Adds a new day's weather data to the list.
  """
  data.append({
      "date": date,
      "high": high,
      "low": low,
      "conditions": conditions
  })

def calculate_average_temp(data):
  """
  Calculates the average temperature for the week.
  """
  total_high = 0
  total_low = 0
  for day in data:
    total_high += day["high"]
    total_low += day["low"]
  return (total_high + total_low) / len(data)

def find_hottest_day(data):
  """
  Finds the day with the highest temperature.
  """
  hottest_day = None
  highest_temp = float("-inf")
  for day in data:
    if day["high"] > highest_temp:
      highest_temp = day["high"]
      hottest_day = day
  return hottest_day

# Example usage
weather_data = create_weather_data()
add_weather_data(weather_data, "2024-02-19", 25, 18, "Sunny")
add_weather_data(weather_data, "2024-02-20", 28, 20, "Cloudy")
add_weather_data(weather_data, "2024-02-21", 30, 22, "Sunny")
# ... Add more days

average_temp = calculate_average_temp(weather_data)
hottest_day = find_hottest_day(weather_data)

print("Average temperature:", average_temp)
print("Hottest day:", hottest_day["date"], "with a high of", hottest_day["high"], "degrees")
