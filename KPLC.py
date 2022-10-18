# Python3 implementation to calculate the
# electricity bill
# Function to calculate the
# electricity bill

#Name of the Power Company
print("                 KENYA POWER & LIGHTING COMPANY LIMITED ")
print("                       Power Bill Receipt.")
print("...............................................................................")

#customer's details.
print('\n')
x=input("Firstname: ")
y=input("Secondname: ")
z=input("Metre Number: ")
m=int(input("Previous Reading: "))
n=int(input("Current Reading: "))

def calculateBill(units):
    
    if (units <= 100):
        return units * 10; 
    elif (units <= 200):
        return ((100 * 10) +(units - 100) * 15);
    elif (units <= 300):
        return ((100 * 10) +(100 * 15) +(units - 200) * 20);
    elif (units > 300):
        return ((100 * 10) +(100 * 15) +(100 * 20) +(units - 300) * 25);
    return 0;
# Driver Code
units= n - m
print("Total Cost: ",calculateBill(units));
# This code is contributed by Code_Mech