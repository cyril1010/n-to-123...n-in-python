#   SAMPLE INPUT : 5
#   SAMPLE OUTPUT : 12345
#   --------------------
#Get user input
n = int(input("Enter number : "))

# Create an empty list and later insert values from 1 to n
myList = []

# Used while loop to get values start from 1
i=1
while (i<=n):
    myList.append(i)
    i = i+1

# Convert the integer list to string list
myNewList = [str(i) for i in myList]

#Create an empty string
num = ''

#On each iteration the numbers(which are strings) will get concatenated to the 'num' variable
for i in myNewList:
    num = num+i
#To print the final output
print(num)
