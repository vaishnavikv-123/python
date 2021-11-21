list = []
print("Enter number of elements:")
n = int(input())
print("Enter elements")
for i in range(0, n):
    ele = int(input())
    list.append(ele) 
print(list)
print("The positive numbers are:") 
for num in list:
    if num >= 0:
       print(num, end = " ")