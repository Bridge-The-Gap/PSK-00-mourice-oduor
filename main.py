print("Hello World \n")
name = input("Enter your name: ")
age = int(input("Enter your Age: "))

print("My name is",name,'\n'"I am",age,"years of age. Young, right?",'\n')


List1 = [12, 4, 56, 17, 8, 99]
print(max(List1),"\n")

def Mean(list2): 
    return sum(list2) / len(list2) 
list2 = [12, 4, 56, 17, 8, 99]
mean = Mean(list2)
print("Mean of list2 =", round(mean,2),"\n")



Var = ['A for Apple','B for Boy','C for Cat','D for Dog','E for Elephant','F for Fish','G for Girl','H for Hen','I for Ice cream','J for Jug','K for Kettle','L for Lion','M for Man','N for Nurse','O for Ostrich','P for Puppy','Q for Queen','R for Rabbit','S for Ship','T for Tree','U for Umbrella','V for Van','W for Woman','X for X-mass tree','Y for Yatch','Z for Zebra']

for item in Var:
    print(item)
