a=input()
if ord(a)>=65 and ord(a)<=90 or ord(a)>=97 and ord(a)<=122:
    if (a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U'):
        print("Vowels")
    else:
        print("Consonant")
else:
    print("Invalid")
    
