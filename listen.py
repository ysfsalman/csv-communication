import time

while True:
	f=open("test.csv", "r")
	p = f.read()
	print(p)	
	f.close()
	time.sleep(0.001)
