#tutorial_36 (strings are immutable)
name = "string"
print(name.replace('t','T'))
# directly do not change in string
name.replace('t','T')
print(name) # same output as string
#output
print(name[1])
print("===================\n")
# no chamge in string
'''name[1] = 'T'
print(name)  '''
print("\n")
print("=====================\n")
# tutorial_37 (assignment operator)
n=1
for i in range(1,11):
	i*=2
	print(f"2 x {n} = {i}")
	n+=1