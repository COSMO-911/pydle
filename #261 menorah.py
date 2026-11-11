for x in range(5):
    pydle(x,3,"","yellow")
    if not x%2:
        pydle(x,2,"","yellow")
        pydle(x,1,"^","")
        pydle(x,0,"","orange")
pydle(2,4,"","yellow")
