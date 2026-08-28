person_name = input("What's Your name?\n")
print(f"2-3.\nHello {person_name.lower()}, would you like to learn some python today?")


print(
    f'Albert Einstein once said, "A person who never made a mistake never tried anything new".'
)

famous_person = "Elon Musk"
message = '"You get paid in direct proportion to the difficulty of problems you solve"'
print(f"2-6. Famous Quote 2:\n{famous_person} once said, {message}")


person_name = "\n\t\t\tElon Musk\t\t\t\n"
print(f"2-7. Stripping Names (without using strip()):\n{person_name}")

print(f"2-7. Stripping Names (using lstrip()):\n{person_name.lstrip()}")

print(f"2-7. Stripping Names (using rstrip()):\n{person_name.rstrip()}")

print(f"2-7. Stripping Names (using strip()):\n{person_name.strip()}")

filename = "python_notes.txt"
simple_filename = filename.removesuffix(".txt")
print(simple_filename)
