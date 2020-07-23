from datetime import timedelta, date, time, datetime

def add_time(start, duration, day=None):
  # TODO CHECKING

  startTime = datetime.strptime(start, '%I:%M %p')

  sp = duration.split(':')
  durDelta = timedelta(0, int(sp[0])*60*60 + int(sp[1])*60)
  nt = startTime + durDelta
  new_time = nt.strftime('%I:%M %p').strip('0')

  return new_time

