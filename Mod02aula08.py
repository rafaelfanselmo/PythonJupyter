set1={1,2,3,4,5}
set2={"red","blue","green"}
set3={"maca", "banana","manga"}

print("banana" in set3)

#add e update quase a mesma coisa
set3.add("jaca")
print(set3)
set2.update(["pink","magenta"])
print(set2)

set2.remove("blue")
print(set2)
set2.discard("red")
print(set2)

set4 = set1.union(set2)
set4.update(["pink"]) #conjunto não permite inserir valores duplicados
print(set4)

res = set1.issubset(set4)
print(res)

set5 = set4.intersection(set1)
print(set5)
