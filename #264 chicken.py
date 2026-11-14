r = range(5)
for i in r:
    for j in r:
        if i>1:
            pydle(i,j+1,"","white")
    pydle(i, 0 if i%2==0 else 4, "", "red")
for i in 11,15,16: pydle(i%5, i//5, "", "orange")
pydle(3,4,"","white")
pydle(3,2,"","black")
pydle(0,0,"","black")
