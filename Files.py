# Make a function that takes personal information as arguments, e.g., name,
# last name, phone number, address, etc. Then make another function that
# saves the data onto a file. Make sure that it works by checking that the
# file was created and that it contains the right data.
# Add to the previous program a function for opening up the same file which the data was saved on.
# Make sure that it works by making the function print out the data.
#
import json


def build_personal_info(first_name: str, last_name: str, phone_number: str, address: str, **other_info: str):
    personal_info = dict()
    personal_info['first_name'] = first_name
    personal_info['last_name'] = last_name
    personal_info['phone_number'] = phone_number
    personal_info['address'] = address

    for key, value in other_info.items():
        personal_info[key] = value

    return personal_info


my_personal_info = build_personal_info('Mary', 'Smith', '0978038976', 'London', age='29', gender='female')


def save_info():
    with open("my_data.json", "w+") as data_info:
        data_info.write(json.dumps(my_personal_info))


save_info()


def check_info():
    with open("my_data.json") as data_info:
        checking_file = data_info.read()
        info_in_dict = json.loads(checking_file)
    return info_in_dict


def print_info():
    print(check_info())


print_info()