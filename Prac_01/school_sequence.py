'''
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
'''

x = int(input("Input number x: "))
y = int(input("Input number y: "))
print("Show the (E)ven numbers from " + str(x) + " to " + str(y))
print("Show the (O)dd numbers from " + str(x) + " to " + str(y))
print("Show the (S)quares from " + str(x) + " to " + str(y))
print("(Q)uit")

choice = str(input(">>>"))

while choice != "Q":
    if choice == "E":
        for i in range(x, y, 1):
            if i % 2 == 0:
                print(i)
    elif choice == "O":
        for j in range(x, y, 1):
            if j % 2 == 1:
                print(j)
    elif choice == "S":
        print("something")
    else:
        print("Invalid option")
    x = int(input("Input number x: "))
    y = int(input("Input number y: "))
    print("Show the (E)ven numbers from " + str(x) + " to " + str(y))
    print("Show the (O)dd numbers from " + str(x) + " to " + str(y))
    print("Show the (S)quares from " + str(x) + " to " + str(y))
    print("(Q)uit")
    choice = str(input(">>>"))

