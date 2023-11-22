num1 = 0
pro_tuple = ()
pro_list = []
while num1 < 40:
        num1 = int(input("num1 : "))
        num2 = int(input("num2 : "))
        num3 = int(input("num3 : "))
        pro_tuple = (num1,num2,num3)
        pro_list.append(pro_tuple)

for i in pro_list:
        print(i[0],i[1],i[2])


# print(pro_tuple[0])
# print(pro_list)