import sys
import socket
import inspect
import argparse
import core.dgas
import core.dgas
from datetime import datetime




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
	if not args.threat:
		return
	threatName = args.threat.lower().strip()
	
	# Check we have code for given threat name
	supported = []
	for name, obj in inspect.getmembers(core.dgas):
		if inspect.isclass(obj) and "_dga" in name:
			supported.append(name.split("_")[0])
	if threatName not in supported:
		return
	
	# Set date
	if args.date:
		date = datetime.strptime(args.date, "%Y-%m-%d")
	else:
		date = datetime.now()

	# Load class and get domains
	className = threatName + "_dga"
	handlerClass = getattr(core.dgas, className)
	obj = handlerClass()
	obj.setSeed(5)
	obj.setDate(date)
	obj.generateDomains()
	print obj.getDomains()
	print "here"

if __name__ == '__main__':
    main()