
n = int(input("Enter the num: "))

t3 = (n-1)//3
t5 = (n-1)//5
t15 = (n-1)//15

s3 = 3 * t3 * (t3+1)/2
s5 = 5 * t5 * (t5+1)/2
s15 = 15 * t15 * (t15+1)/2

print((s3+s5)-s15)
