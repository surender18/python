# def celsiustof():
#     c=int(input("enter temp in celsius"))
#     f=(9/5)*c +32
#     return f

# print(celsiustof())


def celsiustof(c):
    return (9/5)*c +32


c=int(input("Enter temp in celsius"))
f=celsiustof(c)
print(f"{round(f,2)} F")
# print(f"{round(celsiustof(c),2)} F")
 
# inch *2.54 
# for inch to cm