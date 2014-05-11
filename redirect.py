import time
import sys
import subprocess
import io

if __name__ == '__main__':
	valid = True
	serialString = sys.argv[1]
	interface = sys.argv[2]
	number = sys.argv[3]
	if number == str(1):
		filename = 'test.log1'
		f = open("antennaData1","w")
	elif number == str(2):
		filename = 'test.log2'
		f = open("antennaData2","w")
	else:
		print "Invalid arguments for redirect.py"
		valid = False
	f.write(sys.argv[4])
	f.write("\n")
	if (valid):
		filename = 'test.log'
		with io.open(filename, 'wb') as writer, io.open(filename, 'rb', 1) as reader:
		    process = subprocess.Popen(["python","sweep.py",serialString,interface], stdout=writer)
		    while process.poll() is None:
			f.write(reader.read())
			time.sleep(0.5)
		    # Read the remaining
		    f.write(reader.read())
