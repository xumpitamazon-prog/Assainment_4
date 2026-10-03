from datetime import datetime

new = datetime.now()
formatted_now = new.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", formatted_now)




# 2


import json

Student = {
    "name" : "Sadman Hosan",
    "age" : 22,
    "department" : "Arts"
}

json_string = json.dumps(Student)
print(json_string)
