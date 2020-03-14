import time

for i in range(500):
	f= open("test.csv", "w+")
	
	f.write('%d' %i)
	print(i)
	f.close()
	time.sleep(0.001)
