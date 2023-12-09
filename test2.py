def validate(value):
    try:
        value = int(value)
    except ValueError:
        print("integer need")
        return  value,False 
    else:
        if value in range(0,121,20):
            return value,True
        else :
            print("not in range")
            return value,False
while True:      
    while True:
        p = input("pass : ")
        x = validate(p)
        print(type(x[0]))
        if x[1] :
            print(x)
            break
        else :
            continue
    while True:
            p = input("defer : ")
            y = validate(p)
            print(type(y[0]))
            if y[1] :
                print(y)
                break
            else :
                continue
    while True:
            p = input("fail : ")
            t = validate(p)
            print(type(t[0]))
            if t[1] :
                print(t)
                break
            else :
                continue

    if x+y+t == 120:
         break
    else:
         print("total incorrect")

