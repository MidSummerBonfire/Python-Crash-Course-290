#list for birds
#using input(), append(), sort(), for loop to display birds on every line, pop() to delete 2nd bird,
#remove() to remove by name, display all modified list using print()

#print intial list
birds = ['robin','crow','penguin','chicken']
print(birds)

#print appended user input list
birds.append(input("please name a bird species\n\n"))
print(f"appended list: {birds}\n\n")

#using sort
birds.sort()
print(f"sorted list: {birds}\n\n")

#using for loop
for bird in birds:
    print(bird)
print("\n\n")

#pop method
pop_bird = birds.pop(1)
print(f"{pop_bird} was removed because it was second on the list, and {birds} are left on the list \n\n")

#remove method
removed_birds = "robin"
birds.remove(removed_birds)
print(f" the following bird was removed: {removed_birds}")
print(f'{birds} are the birds that remain')