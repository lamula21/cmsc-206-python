words = ['the', 'clown', 'ran', 'after', 'the', 'car','and', 'the', 'car', 'ran', 
'into', 'the', 'tent', 'and', 'the', 'tent', 'fell', 'down', 'on', 'the', 'clown', 'and', 'the', 'car']

dic = dict()

for eachWord in words:
    if eachWord not in dic:
        dic[eachWord] = 1
    else:
        dic[eachWord] += 1

print(dic)
