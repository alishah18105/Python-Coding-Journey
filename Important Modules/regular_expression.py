
import re

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
email = "test@example.com"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

pattern = r"^\d{4}-\d{7}$"
phone = "0300-1234567"

if re.match(pattern, phone):
    print("Valid Phone")
else:
    print("Invalid Phone")


text = "My numbers are 123, 456 and 789"
numbers = re.findall(r"\d+", text)
print(numbers) #Output: ['123', '456','789']

text = "My phone is 0300-1234567"
masked = re.sub(r"\d", "*", text)  
print(masked)

text = "Email: test@example.com"
pattern = r"([\w\.-]+)@([\w\.-]+)"

match = re.search(pattern, text)
if match:
    print("Username:", match.group(1)) #test
    print("Domain:", match.group(2))   #example.com
