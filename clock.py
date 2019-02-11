class Clock:
	def __init__(self,
				hours=0,
				minutes=0,
				seconds=0):
		self._hours = hours
		self._minutes = minutes
		self._seconds = seconds

	def displayTime(self):
		# Display the time, inserting any necessary placeholders
		if self._minutes < 10:
			colon1 = ":0"
		else:
			colon1 = ":"
		if self._seconds < 10:
			colon2 = ":0"
		else:
			colon2 = ":"
		print ("The time is " + str(self._hours) + colon1 + str(self._minutes) + colon2 + str(self._seconds))

	def setTime(self, hours, minutes, seconds=0):
		# Set the clock time
		if 24 > hours >= 0 and 60 > minutes >= 0 and 60 > seconds >= 0:
			self._hours = hours
			self._minutes = minutes
			self._seconds = seconds
		else:
			print("Set a valid time")

	def getTime():
	 	return (self, self._hours, self._minutes, self._seconds)

	def tick(self):
		if self._seconds == 59:
			self._seconds = 0
			if self._minutes == 59:
				self._minutes = 0
				self._hours = 0 if self._hours==23 else self._hours+1 
			else:
				self._minutes += 1
		else:
			self._seconds += 1

	def __str__(self):
		return str(self._hours) + ":" + str(self._minutes) + ":" + str(self._seconds)


if __name__ == '__main__':
	x = Clock()
	x.setTime(23,58)
	print(x)
	x.displayTime()
	for i in range(130):
		x.tick()
	print(x)
	print(x.getTime)