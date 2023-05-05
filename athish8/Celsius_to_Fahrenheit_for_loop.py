# Define a list of Celsius temperatures
# Define an empty list to store Fahrenheit temperatures
# Convert each Celsius temperature to Fahrenheit using a for loop
# Print the resulting list of Fahrenheit temperatures
celsius_temps = [0,10,20,30,40]
fahrenheit_temps = []
for temp in celsius_temps:
    fahrenheit_temp = (temp * 9/5) + 32
    fahrenheit_temps.append(fahrenheit_temp)
    print(fahrenheit_temps)
