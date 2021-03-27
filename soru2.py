usr=int(input('sayi:'))
key=[]
value=[]
for i in range(1,usr):
    key.append(i)
    value.append(i*i)
dictionary=dict(zip(key,value))
print(dictionary)

