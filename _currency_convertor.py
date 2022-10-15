with open("currency.txt","r") as f:
    lines =f.readlines()

currencyDict={}

for line in lines:
    parsed=line.split('\t')
    currencyDict[parsed[0]] = parsed[1] 

# print(currencyDict)
print("Available options are:")
[print(item) for item in currencyDict.keys() ]

amount=int(input("Enter the ampunt you wanna convert: "))
currency=input("please enter one of these currencies : ")

print(f"{amount}INR = {amount*float(currencyDict[currency])} {currency}")