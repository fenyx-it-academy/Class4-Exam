
# Write a Python program that accepts a string and calculate the number of digits
# andletters.

stre =input("enter the string-->")
countl = 0
countn = 0
counto = 0
for i in stre:
    if i.isalpha():
        countl += 1
    elif i.isdigit():
        countn += 1
    else:
        counto += 1
print("Harfler --", countl)
print("Sayilar --", countn)
