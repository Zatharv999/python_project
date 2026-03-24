"""Write a program to show students' grades by entering five subject marks and calculating average marks and grades. For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?"""
a=int(input("maths: "))
b=int(input("science: "))
c=int(input("english: "))
d=int(input("sst: "))
e=int(input("sanskrit: "))
x=(a+b+c+d+e)/5
if 91<= x <= 100:
    print ("A1")
elif 81<= x <= 90:
    print ("A2")
elif 71<= x <= 80:
    print ("B1") 
elif 61<= x <= 70:
    print ("B2")
elif 51<= x <= 60:
    print("C1")
elif 35<= x <=50:
    print("C2")
else: 
    print ("failed")
    


