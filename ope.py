'''x = input("Enter the number: ")
y = input("Enter the number : ")
z= input("Enter the number : ")

if x>y and x>z:
    print("x is the largest")
elif y>z and y>x:
    print("y is the largest")
else:
    print("z is the largest")'''


#Task 2 
'''
Frnd1_= float(input("Enter the CGPA : "))
Frnd2_ =float( input("Enter the CGPA : "))
Frnd3_ =float( input("Enter the CGPA : "))

Average = (Frnd1_ + Frnd2_ + Frnd3_)/3

print("Average cgpa of these three friend: " , Average)
if Frnd1_<Frnd2_ and Frnd3_>Frnd1_:

    print("Friend 1  has the lowest cgpa")

elif Frnd1_>Frnd2_ and Frnd3_>Frnd2_:

    print("Friend 2 has the lowest cgpa")
else:
   print("Friend 3 has the lowest cgpa")
    '''

#task 3 

a = 7
b = 4

not_a = ~a
not_b = ~b
print(not_a)
print(not_b)

''' details :

7 = 00000111
flipping , ~7 = 11111000
flipping again + 1 ,11111000=00000111+1 = 00001000 which is -8 

'''