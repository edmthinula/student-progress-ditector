num1 = 10
num2 = 30
num3 = 40
num4 = 50
large = max(num1,num2,num3,num4)
print(large)

pixel = 400

if large == num1:
    print("num1")
elif large == num2:
    print("num2")
elif large == num3:
    print("num3")
else:
    print("num4")

#num1 percentage

percentage_num1 = (pixel/large)*num1
print(percentage_num1)
percentage_num2 = (pixel/large)*num2
print(percentage_num2)
percentage_num3 = (pixel/large)*num3
print(percentage_num3)
percentage_num4 = (pixel/large)*num4
print(percentage_num4)