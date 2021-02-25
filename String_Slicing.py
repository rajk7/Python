x = 10,20,True,40.5,'abc' 
print(x)
print(type(x)) #tuple

y = {10,40,30,40.5,True,'abc'} #??
print(y)
print(type(y)) #set

z = [10,20,30,40,50] 
print(z)
print(type(z)) #list

print(z[2]) #[30] #[Start]
print(z[2:4]) #[30,40] #[Start : stops]
print(z[ : : 2]) # [10,30,50] #[Start : Stop : Steps]
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

z1 = [10,22.5,True,'Abc'] 
print(z1)

print(z1[2])
print(z1[2:4])
print(z1[ : : 2])

z2 = [10,22.5,True,'Abc'] 
# Mutable Nature
print('***************************')
z2.append('Raj')
print(z2)
z2.remove(True)
print(z2)
z2.pop(3)
print(z2)
z2.insert(2,'Shivam')
print(z2)

print("&&&&&&&&&&&&&&&&&&&&&&&&")
s = "Abc For Tech"
print(s)
print(s[3:6])
print(s[ : :2])
print(s[-1: :-1])
print(s[:8:])
print(s[2:-2:-1])

print('&&&&&&&&&&&&&&&&&&&')
b = (10,20.5,True,"raj")
print(b)
print(type(b))

