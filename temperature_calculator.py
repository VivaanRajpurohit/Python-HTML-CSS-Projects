celcius_input = input("Enter the temperature in Celcius: ")
celcius = float(celcius_input)

farenheit = (celcius * 9/5) + 32

print(f"{celcius:.1f} degrees celcius {farenheit:.1f} farenheit temperature")