import re

text = """The rain in Spain
        is the single line
        The tai"""
web_server = "my_server"
port = 8080

print(f"Web server : {web_server}")
print(f"Port : {port}")
print(f"Regular Expression: ,{web_server}")
y= re.search("^The", text)
print(y)

txt = "The rain in Spain"
x = re.findall("aia", txt)
print(len(x))


print(re.search("tai$", text))
print(re.split(" ", text))
print(re.findall("he", text))

print(f"Output of Findall: {re.findall("he", text)}")