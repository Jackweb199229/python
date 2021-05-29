size = int(input(" How many elements you want to enter ? "))
list1 = []
for i in range (size):
	elements = (input("enter number: "))
	list1.append(elements)
print("list = " ,  list1[1:3 ])