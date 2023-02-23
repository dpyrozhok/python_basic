
inp = [int(input('Enter 1st number ')), int(input('Enter 2nd number ')), int(input('Enter 3rd number '))]

inp.sort()

print(f"You entered 3 values: {inp}")
print (f"Two minimum values are: {inp[0]} and {inp[1]}")
print (f"Maximum of minumum values is: {inp[1]}")