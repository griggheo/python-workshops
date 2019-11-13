total = 0 # This is a global variable

def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is a local variable
   print(f'Inside the function local total: {total}')
   return total

# Now you can call sum function
sum(1, 2)
print(f'Outside the function global total: {total}')
