
uscno = int(input("Enter the uscno: "))
name = input("Enter name: ")
units = int(input("Enter the number of units: "))

if units <= 100:
    amount = units * 1.50

elif units <= 300:
    amount = 150 + (units - 100) * 2.50

else:
    amount = 650 + (units - 300) * 3.50

print('uscno: ', uscno)
print("Name: ", name)
print("Units Consumed: ", units)
print("Net Amount: %0.2f" % amount)
