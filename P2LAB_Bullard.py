# Received miles/gallon amount for the input from user
miles_per_gallon = float(input())

# Received dollars/gallon amount for the input from user
dollars_per_gallon = float(input())

# Calculating the input
dollars_per_mile = dollars_per_gallon / miles_per_gallon

# Cost for 20 miles
your_value1 = 20 * dollars_per_mile

# Cost for 75 miles
your_value2 = 75 * dollars_per_mile

# Cost for 500 miles
your_value3 = 500 * dollars_per_mile

# Show the results  
# With the output, here
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')
