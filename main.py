import sys
import socket
import inspect
import argparse

def getIP(d):
	try:
		data = socket.gethostbyname_ex(d)
		ip = repr(data[2])
		return ip
	except Exception:
		return False

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--date", help="date for which to generate domains")
	parser.add_argument("-t", "--threat", help="threat name of dga to run")
	args = parser.parse_args()

	if args.date:
		date = datetime.strptime(args.date, "%Y-%m-%d")
	else:
		date = datetime.now()	


if __name__ == '__main__':
    main()