# First method to use the fstring:
first_name = "Jose"
last_name = "Antonio"
full_name = f"{first_name} {last_name}"
print(full_name)

# Second method to use the fstring:
first_name = "Jose"
last_name = "Antonio"
full_name = f"{first_name} {last_name}"
print(f"Good morning, {full_name.title()}!")

# another way to do the fstring (format String):
first_name = "Michael "
last_name = "Jackson"
print(f"Hello,{first_name}{last_name}")

# assign the entire message to a variable:

first_name = "michael"
last_name = "jackson"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
