#!/usr/bin/env python3
"""
Unit tests for the mailroom program

"""


contributor_list = [('Ken', 'Murray', '10.00', '4.00'),
                    ('Tew', 'Tangsuk', '2.68', '78268', '265.68'),
                    ('Joe', 'joe', '5.50', '57.89'),
                    ('Tina', 'Tangsuk', '29.02'),
                    ('Nathan', 'Merrill', '20.00')
                    ]


def test_donor_list():
    from mailroom import donor_list
    import unittest
    print("donor_test")
    return True


''' 
def donor_list():
    """Returns a list of donors sorted by first name"""
    names_of_donors = [(name[0] + ' ' + name[1]) for name in contributor_list]
    return names_of_donors


def add_donor(name):
    """Adds a first and last name to the list"""
    contributor_list.append(tuple(name.split(" ")))
    return contributor_list
'''

def test_add_donor():
    from mailroom import add_donor
    import unittest
    print('add_donor')
    return True

def test_is_donor():
    from mailroom import is_donor
    import unittest
    print('is doner')
    return True


'''

def is_donor(check_name):
    """Return true or false"""
    names_of_donors = []
    for name in contributor_list:
        names_of_donors.append(name[0] + " " + name[1])
    for fullname in names_of_donors:
        if fullname.casefold() == check_name.casefold():
            return "true"


def new_donation(donation, donor_name):
    """Adds a new donation to the contribution list"""
    fullname = tuple(donor_name.split(" "))
    firstname = fullname[0]
    lastname = fullname[1]
    counter = 0
    while counter <= len(contributor_list) - 1:
        if (contributor_list[counter])[0] == firstname and (contributor_list[counter])[1] == lastname:
            index = counter
            contributor_list[index] = contributor_list[index] + (str(donation),)
        counter = counter + 1

'''

def test_new_donation():
    from mailroom import new_donation
    import unittest
    print('new donation')
    return True


def test_thankyou_email():
    from mailroom import thankyou_email
    import unittest
    print('thankyou email')
    return True


'''
def thankyou_email(donation, donor_name):
    import datetime
    datestr = str(datetime.datetime.now())  # timestamp for txt files
    dt = datestr[0:4] + datestr[-6:]
    # \n is placed to indicate EOL (End of Line)
    mail_file = f'{donor_name}{dt}.txt'
    thank_you = open(mail_file, 'w+')
    L = [f'Dear {donor_name}: \n',
         '\n',
         '\n',
         f'Thank you for your donation of ${donation}.\n',
         'Your gift is greatly appreciated.\n',
         '\n',
         'Sincerely,\n',
         'Kenneth Murray\n'
         ]
    thank_you.writelines(L)
    thank_you.close()  # to change file access modes
    print(mail_file)
    return mail_file


def print_report():
    print()
    print()
    print('{:25} |  {:12} |   {:12} | {:13}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print("-" * 65)
    index = 0
    for donor_report in contributor_list:
        report_fullname = donor_report[0] + " " + donor_report[1]
        report_num_gifts = int(len(donor_report) - 2)
        report_total_given = '{:,.2f}'.format(float(donor_report[2]))
        if report_num_gifts > 1:
            given_counter = 3
            while given_counter < len(donor_report):
                report_total_given = float("{:.2f}".format(float(report_total_given))) + float(
                    "{:.2f}".format(float(donor_report[given_counter])))
                given_counter = given_counter + 1
        report_average = float(report_total_given) / int(report_num_gifts)
        report_average = "{:.2f}".format(report_average)
        report_total_given = "{:.2f}".format(float(report_total_given))
        print(f'{report_fullname:25} | $ {report_total_given:12} |  {report_num_gifts:12} | $ {report_average:13}')
        index = index + 1
    print()
    print()
    return True
'''

def test_print_report():
    from mailroom import print_report
    import unittest
    print('report')
    return True


def test_mailroom_menu():
    from mailroom import mailroom_menu
    import unittest
    print('menu')
    return True


'''

def mailroom_menu(prompt, dispatch_dict):
    while True:  # loop until quit
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "exit menu":
                break
        except KeyError:
            print("That was an invalid choice.\n"
                  'Please make a selection from the menu\n'
                  'You are now leaving the Mail Room\n'
                  )
            break
    return True
'''


def test_send_letter():
    from mailroom import send_letter
    import unittest
    print('send letter')
    return True


'''

def send_letter():
    name_list = input(
        'To see a list of names please type \"list\" or press enter to continue.  > ')  # If the user types ‘list’, show them a list of the donor names and re-prompt
    if name_list.lower() == "list":
        names_of_donors = donor_list()
        names_of_donors.sort()
        print(names_of_donors)
    response_donor_name = input('Please enter the FIRST and LAST name of a new or existing donor  > ')
    if not is_donor(
            response_donor_name) == "true":  # If the user types a name not in the list, add that name to the data structure and use it.
        add_donor(response_donor_name)
    response_new_donation = input(
        f'what is the amount that {response_donor_name} would like to donate?  > ')  # Once a name has been selected, prompt for a donation amount.
    new_donation(response_new_donation, response_donor_name)
    donation_amount = '{:,.2f}'.format(float(response_new_donation))  # Turn the amount into a number
    print(f'I have recorded a donation in the amount of ${donation_amount}')
    thankyou_email(donation_amount,
                   response_donor_name)  # compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.


def create_report():
    print_report()

'''

def test_create_report():
    from mailroom import create_report
    import unittest
    print('create report')
    return True


def test_send_letters_all():
    from mailroom import send_letters_all
    import unittest
    print('send letters all')
    return True

'''

def send_letters_all():
    """creates messages for  the last donation of all donors"""
    for name_donation in contributor_list:
        name = name_donation[0] + ' ' + name_donation[1]
        donation = name_donation[-1]
        thankyou_email(donation, name)
    return True

'''


def single_test_menu():
    print('single test')
    return True


def test_all_the_things():
    print('test all the things')
    return True


def test_quit():
    from mailroom import quit
    import unittest
    print('quit')
    return True


def unittest_menu(prompt, dispatch_dict):
    while True:  # loop until quit
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "exit menu":
                break
        except KeyError:
            print("That was an invalid choice.\n"
                  'Please make a selection from the menu\n'
                  'You are now leaving the Mail Room unit test\n'
                  )
            break
    return True


def quit():
    print("You are now leaving the Mail Room Unit Test")
    return "exit menu"


main_prompt = ("\nWelcome to the Mail Room Unit Test.\n"
               "Please select and action from the menu.\n"
               "1 - choose an individual test\n"
               "2 - Run all of the tests\n"
               "q - Quit\n"
               )
main_dispatch = {'1': single_test_menu,
                 '2': test_all_the_things,
                 'q': quit
                 }

if __name__ == '__main__':
    '''
    This is a test suite for the mailroom program.
    you will be able to run individual tests or run all of the tests from this menu.
    the default will be to run all of the tests.
    '''

    unittest_menu(main_prompt, main_dispatch)
