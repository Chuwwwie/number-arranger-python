def arrange_numbers(numbers):
    numbers.sort()
    return numbers

# Get user input for numbers
num_count = int(input("Enter the number of elements: "))
numbers = []
for i in range(num_count):
    num = int(input("Enter number {}: ".format(i+1)))
    numbers.append(num)

# Arrange the numbers
arranged_numbers = arrange_numbers(numbers)

# Print the arranged numbers
print("Arranged Numbers:", arranged_numbers)
  
