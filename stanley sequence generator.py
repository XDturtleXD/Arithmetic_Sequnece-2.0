def S(n):
    return int(format(n-1 , 'b'),3)

while(True):
    try:
        a = input("Please enter the number you desire(Enter others to shut down):")
        a = int(a)
        i = 0
        while(i<=a):
            print(S(i+1),end=" ") 
            i = i + 1
    except Exception as ex:
        print (ex)
        break
    print(" ")
    i = 1
