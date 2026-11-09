#total characters 167/250 , time taken: 1h 2m

r = range(5) 
for i in r:
    pydle(i, r[-i-1],"", "red")
    pydle(i,5-i,"","orange")
for i in r[:2]:
    pydle(0,i,"🦷","black")
    pydle(1,i,"","blue")
    pydle(2,i,"==","white")
pydle(3,0,"==","white")
