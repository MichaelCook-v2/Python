# Add two matrixes [[2, -2] [5,3]]

# [[2, 2],[5,3]]
x=[[2,-2]]
y=[[5,3]]
r=[]
result=[[0,0],[0,0]]
for i in range(len(x)):
    n=[]
for j in range((len(x))):
    z=0
    for k in range(len(x)):
        xx = x[k]
        yy = y[j]
        z += xx[j] + yy[k]
n.append(z)
r.append(n)

print(r)







# while (x<2):
#     while(y<2)
#     listThree =listOne[[x] [y]] + listTwo[[x][y]]
#     y+=1
#   y=0
#   x+=1
  
  
# print(listThree)
