studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

print("Original names:")
for name in studentNames:
    print(name + " Evans")

new_name = input("Please enter a name to add: ")
studentNames.append(new_name)

print("\nUpdated list:")
for name in studentNames:
    print(name + " Evans")
