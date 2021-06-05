s=[1]
i=0
num = int(input("What's the number? "))

while i <= num:
    s.append(s[i-1]+s[i])
    i=i+1
print(s)