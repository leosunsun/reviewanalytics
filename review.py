data = []
count = 0
with open ('reviews.txt', 'r') as f: 
	for line in f: 
		data.append(line)
		count += 1  #count=count+1 的快写法
		if count % 1000 == 0: #%为整除符号，这里表示的是：if count除以1000的余数为0
			print (len(data))
print(len(data))
print(data[0])
print('------------')
print(data[1])