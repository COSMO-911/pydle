r = range(5)
for x in r:
    for y in r:
        pydle(x,y,"","white")
    if x>1:
        pydle(x,1,"","yellow")
        pydle(x-1,2,"","yellow")
        pydle(x-3,3,"","yellow")
        pydle(x-1,3,"","orange")
        pydle(x-3,4,"","orange")
pydle(3,0,"","yellow")
pydle(4,2,"","orange")
