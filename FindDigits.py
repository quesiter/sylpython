#String.txt为文本文件
f = open('/home/shiyanlou/Code/String.txt','r+')
line=f.readline()
arr=[]
for x in line:
	if(x.isdigit()):
		arr.append(x)
array="".join(arr)
print(array)

