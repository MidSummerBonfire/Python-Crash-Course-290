#print three centered lines
print(f"{'Pet':^20}")
print(f"{'Naming':^20}")
print(f"{'Questionaire':^20}")

#get input of pet name
pet = input("If you had a pet alligator, what would you name it?")
pet_resp = f"I would name it {pet}!"
print(pet_resp)

#print response back
choice_resp = input("why did you pick that name?")
print(choice_resp)