import datetime

import pandas
from random import *
import smtplib
from datetime import *

print(datetime.now().date())
print(datetime.now().weekday())
print(datetime.now().time())

dob = datetime(year=2013, month=9, day=16)
print(dob)


# my_mail = "pkb2022yahoo@gmail.com"
# to_add = "pkb2022@yahoo.com"

# my_mail = "pkb2022@yahoo.com"
# to_add = "pkb2022yahoo@gmail.com"

# my_pass = "Ankit@1992"
# my_pass = "pohjnynvfwzhltyz"

# w_smtp = "smtp.gmail.com"
# w_smtp = "smtp.mail.yahoo.com"

# with smtplib.SMTP(w_smtp) as connect:
#     connect.starttls()
#     connect.login(user=my_mail, password=my_pass)
#     connect.sendmail(from_addr=my_mail, to_addrs=to_add, msg="subject:Hillo \n\n This is test mail from python")


# data = pandas.read_csv("quotes.txt").values.tolist()
#
# print(len(data))
# print("".join(choice(data)))

