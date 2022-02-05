##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# with open("birthdays.csv", mode='a') as bfl:
#     bfl.write("\nPraku,pkb2022yahoo@email.com,2022,1,10")

# 2. Check if today matches a birthday in the birthdays.csv
import pandas
from datetime import *
datafm = pandas.read_csv("birthdays.csv")

td = datetime.now().date()

cy = td.year
cm = td.month
cd = td.day

today_birthday = datafm[(datafm["year"] == cy) & (datafm["month"] == cm) & (datafm["day"] == cd)]
# print(today_birthday)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
from random import *
import os

x = os.listdir("./letter_templates")
letters = []

if not today_birthday.empty:
    # print(today_birthday)
    letter = choice(x)
    with open(f"./letter_templates/{letter}", 'r') as file:
        data = file.read()

    name_list = today_birthday["name"].tolist()
    birth_dict = today_birthday.to_dict('records')
    print(name_list)
    for name in name_list:
        letters.append(data.replace('[NAME]', name))
else:
    print(f"No birthday today {td}")

# 4. Send the letter generated in step 3 to that person's email address.
import requests
import smtplib

# dob = datetime(year=2013, month=9, day=16)

my_mail = "pkb2022yahoo@gmail.com"
to_add = "pkb2022@yahoo.com"

# my_mail = "pkb2022@yahoo.com"
# to_add = "pkb2022yahoo@gmail.com"

my_pass = "Ankit@1992"
# my_pass = "pohjnynvfwzhltyz"

w_smtp = "smtp.gmail.com"
# w_smtp = "smtp.mail.yahoo.com"

with smtplib.SMTP(w_smtp) as connect:
    connect.starttls()
    connect.login(user=my_mail, password=my_pass)
    for letter in letters:
        print(f"To mail is {today_birthday[today_birthday['name'] == name]['email'].to_string(index=False)}\n")
        connect.sendmail(from_addr=my_mail, to_addrs=to_add, msg=f"subject:Warm Birthday Wishes! \n\n {letter}")


# data = pandas.read_csv("quotes.txt").values.tolist()
#
# print(len(data))
# print("".join(choice(data)))

print("testing........")
birth_dict = today_birthday.to_dict('records')
print(birth_dict)
