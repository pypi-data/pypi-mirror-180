from datetime import datetime
import json

import models
from rich import print

with open("data.json", "r") as fh:
    reg_form_data_list = [fh.read()]

reg_num = 1
attendee_num = 1
for reg_form_data in reg_form_data_list:
    reg_form_dict = json.loads(reg_form_data)
    reg_form_dict["reg_num"] = reg_num
    for attendee_dict in reg_form_dict["attendees"]:
        attendee_dict["attendee_num"] = attendee_num
        attendee_num += 1
    registration = models.Registration(**reg_form_dict)
    print(registration)
    reg_num += 1

p = models.Payment(
    **{"_id": 123456, "amount": 400.0, "reg_num": 1, "timestamp": datetime.now()}
)
print(p)
