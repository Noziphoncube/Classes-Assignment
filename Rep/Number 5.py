formulae = lambda c: c*9/5 + 32

temps_in_celcius = [0,87,5,37]

temps_in_fahrenheit=list(map(formulae, temps_in_celcius))

print("Temperature In Celcius: ", temps_in_celcius)
print("Temperature In Fahrenheit: ", temps_in_fahrenheit)
