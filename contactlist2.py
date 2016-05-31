import sys, pickle

#this is a contact template
class Person:

	def __init__(self, name, number):
		self.name = name
		self.number = number

	def __repr__(self):
		return self.name + " " + self.number

#this is the contact list
with open("save3.p", 'rb') as f:
	contacts = pickle.load(f)

prompt = "> "

def program_menu():
	print("1. Add new contact")
	print("2. See contact list")
	print("3. Find a contact")
	print("4. Change contact information")
	print("5. Help")
	print("6. Print contacts dictionary")
	print("7. Quit")

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

			new_person = Person(name, number)

			running = False

	contacts.update({new_person.name : new_person})
	#saves the contact list
	with open("save3.p", 'wb') as f:
		pickle.dump(contacts, f)
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
				print(k, v)
				running = False
			else:
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
		name = input(prompt)
		print("Enter new number")
		number = input(prompt)
		if len(number) == 12:
			
			new_person = Person(name, number)
		
		contacts.pop(update)
		
		contacts[new_person.name] = new_person
		
		with open("save3.p", 'wb') as f:
			pickle.dump(contacts, f)


		print(new_person.name + new_person.returninfo())
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
		print(contacts)

	elif choice == "7":
		running = False		

	else:
		print("Please input a valid option")