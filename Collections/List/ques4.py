#Reverse a list.
num = [2, 6, 3, 4, 10, 16, 19, 28, 39, 60]
reverse_list = []
for i in range(len(num)-1,-1,-1):
    reverse_list.append(num[i])
print("The reversed list is:", reverse_list)