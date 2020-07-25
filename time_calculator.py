# V2: using no imports, no checks
def add_time(start, duration, day=None):
  sec = convert_12_to_sec(start)
  sec = sec + convert_dur_to_sec(duration)

  r = convert_sec_to_12(sec)
  print(r)
  day_part = ""
  if r[1]==1:
    day_part = " (next day)"
  elif r[1]>1:
    day_part = " (" + str(r[1]) + " days later)"
  new_time = r[0] + day_part
  return new_time

def convert_dur_to_sec(dur):
  """convert e.g. 3:12 (hours:minutes) in seconds"""
  p = dur.split(':')
  return int(p[0])*60*60 + int(p[1])*60

# PM (post meridiem, after noon)
# 12:00 AM = 00:00 (0s)
# 01:00 AM = 01:00 (1h)
# 12:00 PM = 12:00 (12h)
# 01:00 PM = 13:00 (12+1h)
# 11:59 PM = 23:59 (12h+11h+59m)
# NOT: 00:00
def convert_12_to_sec(time):
  """convert a 12-hour-time string into seconds.
  time: 11:06 PM
  """
  p1 = time.split(':')
  p2 = p1[1].split(' ')
  if p2[1]=='PM':
    if p1[0] != '12':
      p1[0] = int(p1[0]) + 12
  elif p1[0]=='12': # am
    p1[0] = '00'
  sec = int(p1[0])*60*60
  sec = sec + int(p2[0])*60
  return sec

# sec: 60 
def convert_sec_to_12(sec):
  """convert seconds into a time string.
  return a list with time and remaining days"""
  mode = 'AM'
  h_total = int(sec / 3600)
  rem = sec % 3600
  m = int(rem / 60)
  d = int(h_total / 24)
  h24 = h_total % 24
  h12 = h24
  if h24 >= 12:
    mode = "PM"
    if h24 > 12:
      h12 = h24 - 12
  time = str(int(h12)) + ":" + add_zero(m) + " " + mode
  return [time, int(d)]
  
def add_zero(num):
  """Add zero-padding before num"""
  z = str(int(num))
  if len(z) == 1:
    z = '0' +  z
  return z

