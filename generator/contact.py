from model.contact import Contact
import random
import string
import datetime
import calendar
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number_of_contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_first_last_name(maxlen):
    capital_letter = string.ascii_uppercase
    symbols = string.ascii_lowercase + string.digits + " "
    return random.choice(capital_letter) + "".join([random.choice(symbols)
                                                    for i in range(random.randrange(maxlen))])

def random_address(maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone_number(maxlen):
    digits = string.digits
    return "+" + "".join([random.choice(digits) for i in range(maxlen)])

def random_email(maxlen):
    name_user = string.ascii_lowercase + string.digits + "_" + "-"
    name_user = "".join([random.choice(name_user) for i in range(random.randrange(1, maxlen))])
    domain_part_1 = string.ascii_lowercase
    domain_part_1 = "".join([random.choice(domain_part_1) for i in range(random.randrange(4, 7))])
    domain_part_2 = string.ascii_lowercase
    domain_part_2 = "".join([random.choice(domain_part_2) for i in range(random.randrange(2, 4))])
    return name_user + "@" + domain_part_1 + "." + domain_part_2

def random_date():
    year = random.randint(1900, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = datetime.date(year, month, day)
    date = list(map(lambda x: int(x), date.strftime("%d.%m.%Y").split(".")))
    date[1] = calendar.month_name[date[1]]
    return date

empty_contact = [Contact(first_name="", last_name="", address="", home_phone="", mobile_phone="",
                       work_phone="", fax="", email_1="", email_2="", email_3="",
                       day="", month="-", year="")]

test_data = empty_contact + \
            [Contact(first_name=random_first_last_name(10), last_name=random_first_last_name(10),
                        address=random_address(20), home_phone=random_phone_number(10),
                        mobile_phone=random_phone_number(10), work_phone=random_phone_number(10),
                        fax=random_phone_number(10), email_1=random_email(12),
                        email_2=random_email(12), email_3=random_email(12),
                        day=repr(random_date()[0]), month=random_date()[1], year=repr(random_date()[2]))
            for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))

