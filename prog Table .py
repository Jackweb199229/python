n=int(input("Enter you want the table: "))
for i in range(1,11):
	print("{} x {} = {} " .format(n,i,n*i))
	i+=1
#    		OR
print("____________________________\n")
n = int(input(" Enter you want the table : "))
for i in range(1,11):
	print(f"{n} x {i} = {n*i} ")
	i+=1
# OR 
print("____________________________\n")
n = int(input(" Enter you want the table : "))
for i in range(1,11):
	t=n*i
	print(f"{n} x {i} = {t} ")
	i+=1