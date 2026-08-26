# Examples of how to use the removeprefix()

nostarch_url = "https://google.com"

print(f"without the method removeprefix():\n{nostarch_url}")

print(f"Using the method removeprefix():\n{nostarch_url.removeprefix('https://')}")  # This is temporal because we didn't modify the variable

# modifying the variable which would indeed be a permanent change
simple_url = nostarch_url.removeprefix("https://")
print(f"modifying the variable:\n{simple_url}")
