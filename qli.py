li=[12,134,-1.4,23,43]
positive=[n for n in li if n >= 0]
negative=[n for n in li if n < 0]
print("positive",positive)
print("negative",negative)
squares=[n**2 for n in li]
print(squares)
words=['SUBIN''LIST']
vowels=[ch for ch in words if ch.lower() in "aeiou"]
print(vowels)

          
