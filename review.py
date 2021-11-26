data = []
count = 0
with open ('reviews.txt', 'r') as f: 
	for line in f: 
		data.append(line)
		count += 1  #count=count+1 的快写法
		if count % 1000 == 0: #%为整除符号，这里表示的是：if count除以1000的余数为0
			print (len(data))
print ('档案读取完毕，共有', len(data),'条留言')

sum_len = 0
for d in data: 
	sum_len = sum_len + len(d)
print('留言的平均长度为', sum_len/len(data)) 

new = []
for d in data: 
	if len(d) < 100: 
		new.append(d)
print('共有', len(new), '笔留言长度小于100')
