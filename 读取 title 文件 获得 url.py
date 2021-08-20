with open("title.txt", 'r') as file:
    s = file.read()
    # print(s)
s = s.split("\n")

title = s[2]
url = s[3]
print(title)
print(url)
