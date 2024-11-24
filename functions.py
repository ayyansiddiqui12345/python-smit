def convert_c_to_f(celsius):
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit
#input 
celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_output = convert_c_to_f(celsius_input)

print(f"{celsius_input}°C is equal to {fahrenheit_output}°F")
