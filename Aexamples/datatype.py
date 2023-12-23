str1 = " Hello"
str2 = "World"
arn_text = "arn:w:123:456::789"
val = str1 + " " + str2
print (val)
print (len(val))
print (val.lower())
print (val.upper())
print (val.replace("World", "New"))
print(arn_text.split("::"))
print(val.strip())
print(val[1:-5])