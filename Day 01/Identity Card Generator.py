#ID CARD Generator
print("Identity Card Generator")
print("Enter your Details Below")

fname = input("Enter your First Name: ")
lname = input("Enter your Last Name: ")
Date_of_Birth = input("Enter your Date of Birth(Use DD/MM/YYYY Format): ")
Gender = input("Enter your Gender(Male or Female): ")
Address = input("Enter your Address: ")
School_Name = input("Enter your School Name: ")

print("\n\nYour ID Card is Ready!")
print("Name: " + fname + " " + lname)
print("Date of Birth: " + Date_of_Birth)
print("Age: " + str(2024 - int(Date_of_Birth[6:10])))
print("Gender: " + Gender)
print("Address: " + Address)
print("School Name: " + School_Name)
