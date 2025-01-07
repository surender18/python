# print("Dear \< |Name|>\, \n")
# print("Dear ' |Name|', \n")
# print("Your are selected! \n")
# print("Dear '< |Date| >', \n")
# print("...")



letter='''Dear <|Name|>,
You are selected!
<|Date|>
'''
# print(letter)
print(letter.replace("<|Name|>","jack").replace("<|Date|>","03Jan2024"))


  
