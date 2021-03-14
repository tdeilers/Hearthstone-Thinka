curve = [25,1,1,1,1,1]
#f = open("joshua.txt", "a")
big = [] 
def add(key):
    curve[key] += 1
    if curve[key] == 26: 
        curve[key] = 1
        add(key + 1) 
def append():
    stng = str(curve[0]) + "/" + str(curve[1]) + "/" + str(curve[2]) + "/" + str(curve[3]) + "/" + str(curve[4]) + "/" + str(curve[5])
    big.append(stng) 
    #f.write(stng + "\n")
while curve[5] != 25: 
    add(0)
    if curve[0] + curve[1] + curve[2] + curve[3] + curve[4] + curve[5] == 30:
        append()
print("done")
print(big) 