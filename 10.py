t=input()
ele=input()
n1=t.split(" ")
n=int(n1[0])
k=int(n1[1])
e=ele.split(" ")
l=len(e)
s=0
for i in range(k):
    s=s+int(e[i])
print(s)    
