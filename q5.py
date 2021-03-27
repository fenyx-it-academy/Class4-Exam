# Input ile girilen bir cumledeki sayilarin ve harflerin miktarini hesaplayan bir fonksiyon yaziniz.
# Ornek input: hello world! 123
# Output:
# HARFLER: 10
# SAYILAR: 3


def calculate():
    a = 0
    b = 0
    entry = input("Enter your message")
    for x in entry:
        if x.isdigit():
            a+=1
        if x.isalpha():
            b+=1
    print("Number of digit is: ", a, "Number of letter is: ",b )


calculate()