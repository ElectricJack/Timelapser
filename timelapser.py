#!/usr/bin/python -tt
#timelapser.py

import sys, time, os
from daemon import Daemon

class TimelapseDaemon(Daemon):
	def getIndexStr(index, digits):
		indexStr = "";
		while digits > 0:
			indexStr = ""+(index % 10)+indexStr
			--digits
			index = (int)(index / 10)
		return indexStr

	def run(self):
		running = True
		index = 0
		while running:
			indexStr = getIndexStr(index, 4)
			imageName = 'img'+indexStr+'.jpg'
			os.system('fswebcam -r 1280x720 '+imageName)
			++index
			time.sleep(1);

if __name__ == "__main__":
	daemon = TimelapseDaemon('/var/run/timelapser.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			print 'Timelapse Daemon Started'
			daemon.start()
		elif 'stop' == sys.argv[1]:
			print 'Timelapse Daemon Stopped'
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			print 'Timelapse Daemon Restarting'
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)