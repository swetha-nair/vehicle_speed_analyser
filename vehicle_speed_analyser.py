def check_speed(speed):
    
  if speed <= 60:     
        status = "safe"
    
  elif speed <= 80:
        status = "warning"
    
  else:
        status = "overspeed"
    
  return status


def read_speed_file():
    
  speed_file = open ("speed.txt", "r")
    
  for entries in speed_file:
        speed = int(entries.strip())
        status = check_speed(speed)
        print(speed, status)
        speed_report.write(f"{speed} {status}\n")
    
  speed_file.close()
  speed_report.close()

speed_report = open ("speed_report.txt", "w")
speed_report.write("vehicle speed report\n")

read_speed_file()
