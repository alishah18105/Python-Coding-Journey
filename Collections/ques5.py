#Count the occurrences of each element.
num = [1, 2, 3, 4, 5, 10, 1, 2, 3, 4, 5]
from collections import Counter
count = Counter(num)
print("The count of each element in the list is:", count)
counter = {}
for i in num:
    if i in counter:
        counter[i]+=1
    else:
        counter[i]=1
print("The count of each element in the list is:", counter)