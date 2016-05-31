import sys, pickle

#this is the contact list
contacts = pickle.load(open("save.p", 'rb'))

prompt = "> "

def program_menu():
	print("1. Add new contact")
	print("2. See contact list")
	print("3. Find a contact")
	print("4. Change contact information")
	print("5. Help")
	print("6. Quit")

def fc_submenu():
		print("1. Try again")
		print("2. Add new contact")
		print("3. See contact list")
		print("4. Return to main menu")
		choice = input(prompt)
		if choice == "1":
			return True
		elif choice == "2":
			add_contact()
			return True
		elif choice == "3":
			pull_contacts()
		elif choice == "4":
			return True
		else:
			print("Please input a valid option")

#creates dictionary for inputted contact
def add_contact():
	
	#this is how you give a name and number to this contact list
	print("Please give me a name.")
	name = input(prompt)

	running = True

	while running:
		
		#adds a phone number
		print("Please give me a phone number.")
		number = input(prompt)

		if len(number) == 12:
			#stores the outcome of the create_dict function into the temp variable
			temp = {"name" : name, "number" : number}
			running = False

	#adds the temps of the temp variable to the contacts dictionary
	contacts[temp["name"]] = temp
	#saves the contact list
	pickle.dump(contacts, open("save.p", 'wb'))
	print("Contact added\n")

#creates and prints a sorted list of contacts
def pull_contacts():
	contactlist = []
	for key in contacts.keys():
		contactlist += [key]
	contactlist.sort()
	print(contactlist)

#finds contacts in your contacts list
def find_contacts():
	running = True
	while running:
		print("Who are you looking for?")
		find  = input(prompt)
		for k, v in contacts.items():
			if find == k:
				return k
				print(k, v)
				running = False
		print(find + " is not in contact list")
		success = False
		while not success:
			success = fc_submenu()

#changes a persons contact information
def update_contact():
	running = True
	while running:
		update = find_contacts()
		print(update)
		print("Enter new name")
		new_name = input(prompt)
		print("Enter new number")
		new_number = input(prompt)
		if len(new_number) == 12:
			#stores the outcome of the create_dict function into the temp variable
			temp = {"name" : new_name, "number" : new_number}
		contacts.pop(update)
		contacts[temp["name"]] = temp
		pickle.dump(contacts, open("save.p", 'wb'))
		print(new_name + temp)
		print("Contact changed")
		running = False



running = True

#program loop
while running:
	program_menu()
	choice = input(prompt)
	
	if choice == "1":
		add_contact()

	elif choice == "2":
		pull_contacts()

	elif choice == "3":
		update_contact()
	
	elif choice == "4":
		update_contact()

	elif choice == "5":
		print("There is no help")

	elif choice == "6":
		running = False		

	else:
		print("Please input a valid option")