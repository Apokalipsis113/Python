sentense = "This is a common interview question"
s = set(sentense.lower())
d = {}
for item in s:
    d[item] = sentense.count(item)
# print(d)
s = sorted(d.items(), key=lambda f: f[1])
print(s[-1])
