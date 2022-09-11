"""
Imagine that you're planning a party and plan to invite ten of your classmates.
To help with the planning,use the list data structure and initialize it with 10 first names
from your current SEC290 class roster. If the class size is less than 10, then make the list smaller.
The initial list should be created with the names inside of it.

Next, use the sort method to sort the list.
Then display each name, one per line, using a for loop.

Someone whispers in your ear that one of the guests can't make it.
You'll need to delete this guest and add a replacement.

Use a print statement to display, "Oops! It turns out one of your guests can't make it."

Use the input() function to query the user for the index of the guest that can't make it.
Since input() always returns a string, you'll need to use the int() function to convert the index provided to an integer.

Use the pop() and the guest's index to remove the guest from the list. Since it's best practice to keep the user informed,
display a confirmation message to the user including the guest's name.
Note that pop() returns the value of the element deleted.

Since you now have an open spot, use the input() function to query the user for another guest name and add that name
to the list using the append() method.

Sort the list again and display each name in another for loop."""

#***Guest list app***

#-list with 10 names-
guests = ['Yasmeen', 'Anissa', 'Zoe', 'Andrew', 'Gustavo', 'Tyler', 'Kevin', 'Tiana', 'Nyree', 'Eliasib']


#-sort list-
guests.sort()


#-for loop-
print(f"Proposed Guest List:\n\n")
for guest in guests:
    print(guest)

    
#-Delete guest-
print(f"\n\nOops! It turns out one of your guests can't make it.")
missing_guest = input(f"\nPlease enter the index of the guest to be deleted from list: ")
guest_pop = guests.pop(int(missing_guest))
print(f"{guest_pop} has been removed from the guest list.")


#-append guest-
new_guest = input("please invite another guest as a replacement: ")
guests.append(new_guest.title())

#-final sort for loop-
print("\nNew Guest List:")
guests.sort()
for guest in guests:
    print(guest)

#exit function
input('\n\npress any key to close window')
exit()

