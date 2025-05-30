# pattern_drawing.py

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
height = 0

# Outer loop using while
while height < size:
    # Inner loop using for
    for col in range(size):
        print("*", end="")  
    print()  
    height  += 1
