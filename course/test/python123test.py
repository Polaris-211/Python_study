n = int(input())
bin_str = bin(n)[2:]
oct_str = oct(n)[2:]
hex_str = hex(n)[2:]
print (f"{bin_str},{oct_str},{hex_str}")

x = input()
if x[0] == '-':
    rx = '-' + x[1:][::-1]
else:
    rx = x[::-1]
print (f"{int(rx)}")

x = input()
if x[0] == '-':
    b = x[1]
    s = x[2]
    g = x[3]
else:
    b = x[0]
    s = x[1]
    g = x[2]
print (f"{g},{s},{b}")

list1=[32,43,12,23,1,3,5]
sum = list1[0] + list1[1] + list1[2] + list1[3] + list1[4] + list1[5] + list1[6]
aver = float(sum/7)
print("sum=",sum)
print(f"aver= {aver:.1f}")

str1 = input()
str2 = input()
print(f"{str1},我想对你说,{str2}")


x = eval(input())
y = int(input())
print(sorted (x[1:-1].split(', ') , key = int, reverse = True)[y-1])