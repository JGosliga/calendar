from clock import Clock
from calendar import Calendar

class CalendarClock(Calendar, Clock):
	def __init__(self, day, month, year, hours=0, minutes=0, seconds=0):
		Calendar.__init__(self, day, month, year)
		Clock.__init__(self, hours, minutes, seconds)

	def tock(self):
		if self._hours == 23 and self._minutes == 59 and self._seconds == 59:
			self.setTime(0,0,0)
			self.advance()
		else:
			self.tick()

	def __str__(self):
		return Calendar.__str__(self) + ", " + Clock.__str__(self)

	def __repr__(self):
		return CalendarClock.__repr__(self)

if __name__ == '__main__':
	x = CalendarClock(30,12,2018,11,50,00)
	print(x)
	for i in range(900000):
		x.tock()
	print(x)