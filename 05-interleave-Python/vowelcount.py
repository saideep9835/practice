a = "Abc def!!! a? yzyzyz!"
b= "aeiouAEIOU"
c=0

for i in range(len(a)): 
    if a[i] in b:
        c=c+1
print(c)

