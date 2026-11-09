for i in range(5):
    pydle(i, 0, "", "blue")
    pydle(i, 4, "", "blue")
    pydle(0, i, "", "brown")
    if i % 4:
        pydle(i, 2, "", "red")
        pydle(i, 3, "", "yellow")
    else:
        pydle(i, i, "", "yellow")
        pydle(4, 1, "", "blue")
        pydle(4, 3, "", "red")

