li=(input("enter the  string"))
print(li)
vowels="aeiouAEIOU"
vowels_li=[]
for char in li:
    if char in vowels:
       vowels_li.append(char)
print("vowels of the given string",vowels_li)

