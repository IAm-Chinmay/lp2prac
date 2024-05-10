print("Hello GoOoGle App Engine")
def add(n):
  add = 0
  for i in n:
    add += i
  return add

a = int(input(f"How many elements to be added :"))
ele = []
for i in range(a):
  k = int(input(f"Enter input for element no. {i + 1} : "))
  ele.append(k)

a = add(ele)

print("Addition is :", a)



