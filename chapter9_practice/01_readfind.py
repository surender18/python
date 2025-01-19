f=open("poems.txt")
content=f.read()
if("twinkle"in content):
    print("Twinkle is present") 
else:
    print("Twinkle is not present")
print(content)
f.close()