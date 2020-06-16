# Corona Prediction

print("-------------------Corona Test-------------------")

print("Answer in yes or no")
a=input("Do you have fever :")
b=input("Do you often feel tired :")
c=input("Does your head ache :")
d=input("Do you have difficulty in breathing :")
e=input("Do you have cough :")
f=input("Does your chest pain :")
g=input("Do you have difficulty in speaking :")

y="Postive...!!!"
z="You should check with a doctor"
n="Negative...!!!"
if a=="yes" and b=="yes" and c=="yes" and d=="yes" and e=="yes" and f=="yes" and g=="yes":
    print(y)
elif a=="no" and b=="no" and c=="no" and d=="no" and e=="no" and f=="no" and g=="no":
    print(n)
elif a=="yes" and e=="yes" and d=="yes" and f=="yes" and g=="yes" and b=="no" and c=="no":
    print(y)
elif a=="no" and e=="no" and d=="no" and f=="no" and g=="no" and b=="yes" and c=="yes":
    print(n)
elif a=="yes" or b=="yes" or c=="yes":
    print(z)
elif e=="yes" or d=="yes" or f=="yes" or g=="yes":
    print(z)
else:
    print("Error")

