# Do not import any Python libraries
# ??? REDO ALL THE STUFF.......
from datetime import timedelta, datetime

def add_time(start, duration, day=None):
  days =["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"] 
  withDay = None

  # input transformation+checking -------------------
  if day is not None:
    day = day.lower()
    if day not in days:
      print("Wrong format for: day")
      return None 
    for i in range(len(days)):
      if day==days[i]:
        weekday='0' + str(i+1) # 01: monday
        withDay = start + ' '+weekday+'.06.2020' # 01.06.2020 = monday
        break   
    
  try:
    if withDay is None:
      startTime = datetime.strptime(start, '%I:%M %p')
    else:
      startTime = datetime.strptime(withDay, '%I:%M %p %d.%m.%Y')
  except:
    print("Wrong format for: start")
    return None
  
  sp = duration.split(':')
  if len(sp)!=2:
    print("Wrong format for: duration")
    return None  


  # calclulate ---------------------------------
  durDelta = timedelta(0, int(sp[0])*60*60 + int(sp[1])*60)
  nt = startTime + durDelta


  # format output -----------------------------
  if withDay is None:
    new_time = nt.strftime('%I:%M %p').strip('0')
  else:
    new_time = nt.strftime('%I:%M %p, %A').strip('0')
    #TODO

  return new_time

