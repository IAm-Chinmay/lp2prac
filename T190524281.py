print("Hello GoOoGle App Engine")
def add(n):
  add = 0
  for i in n:
    add += i
  return add

a = int(input("How many elements to be added :"))
ele = []
for i in range(a):
  k = int(input("Enter input for element no. ",i))
  ele.append(k)

add(ele)
