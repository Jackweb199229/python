# python

for i in range(7):
    for j in range(5):
        if((i==0 or i==3 or i==6) and (j>=1 and j<=3) or ( j==0 and (i>=1 and i<=2)) or (j==4 and (i>=4 and i<=5)) ):
            print("*" , end=" ")
        else:
            print(" " , end=" ")
    print()
for i in range(7):
    for j in range(7):
        if( j==0 or j==6 or ((i==j) and (j>0 and j<4)) or (i==1 and j==5 ) or (i==2 and j==4)  ):
            print("*" , end=" ")
        else:
            print(" " , end=" ")
    print()
