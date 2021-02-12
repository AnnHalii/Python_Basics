# 1
a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)



# 2
s = "This is me red shoes and the seven dwarfs"
print(dir(s))

help(s.split())

words = s.split()
for x in range(0, len(words), 2):
    print(words[x])

# 3
with open('test.txt', 'r') as src, open('new.txt', 'w') as dst:
    dst.write(src.read())











