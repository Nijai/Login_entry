import re
def show_time_of_pid(line):
  #print(line)
  pattern2 = r"\[(\d*)\]"  #working
  pattern1 = r"^[A-Z][a-z]* [0-9]* [00-24]+:[00-59]+:[00-59]+\w*"
  result1 = re.search(pattern1, line)
  result2 = re.search(pattern2, line)
  if result1 == None or result2 == None :
    return " "
  return str(result1[0]) + " pid:"+str(result2[1])

L=[]
L.append(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))

L.append(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"))

L.append(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)"))

L.append(show_time_of_pid("Jul 6 14:03:08 computer.name CRON[29440]: USER (naughty_user)"))

L.append(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\""))

L.append(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)"))

L.append(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)"))

print("Todays Login History: ")
for i in range(len(L)):
  print(L[i])