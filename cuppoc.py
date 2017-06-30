#!/usr/bin/env python2
import os
import sys
from time import sleep
from pysqlcipher import dbapi2 as sqlite
from pysqlcipher.dbapi2 import DatabaseError as PYSQLDBERR


class Target:
    '''
    This class describes all information on a target.
    It is in accordance with the
    National Institute of Standards and Technology (NIST)
    The more you know, the more the password possibilities.
    '''
    def __init__(self):
        self.id = 0
        self.first_name = ""
        self.middle_name = ""
        self.last_name = ""
        self.sex = ""
        self.dob = ""
        self.nick_names = ""
        self.aliases = ""
        self.ssn = ""
        self.home_address = ""
        self.email_address = ""
        self.passport_number = ""
        self.vehicle_plate_number = ""
        self.drivers_license_number = ""
        self.credit_card_number = ""
        self.birthplace = ""
        self.phone_number = ""
        self.school_name = ""
        self.college_name = ""
        self.undergraduate_degree = ""
        self.graduate_degree = ""
        self.doctorate_degree = ""
        self.occupation = ""
        self.misc = ""


def init_cuppoc_db():
    '''
    Use pysqlcipher to create an encrypted targets.db or
    open the existing one with the correct key.
    '''
    while True:
        print("NOTE:")
        print("[!] Checking to see if \"targets.db\" exists or not.")
        print("[!] If it doesn't, cuppoc will make one.")
        print("[!] cuppoc uses AES256 to encrypt your local database.")
        print("[!] This is due to Personally Identifiable Information (PII)")
        print("[!] which will be stored in the database.\n")
        print("[!] You will be asked to enter a password.")
        print("[!] This password is the key to your database. Don't forget :P")
        print("[!] If you have already done this before,")
        print("[!] Then please use the password you used before.")
        db = sqlite.connect("./targets.db")
        cursor = db.cursor()
        user_key = raw_input("> Please enter the password for database: ")
        cursor.execute("PRAGMA key='%s'" % user_key)
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS Targets (" +
                           "ID INTEGER PRIMARY KEY," +
                           "First_Name TEXT," +
                           "Last_Name TEXT)")
            print("[+] Done... Starting cuppoc!")
            print_separator()
            sleep(3)
            break
        except PYSQLDBERR:
            print("[-] Database doesn't exist or is encrypted.")
            print("[-] If database exists, enter the correct password.")
            print_separator()
            db.close()
            sys.exit(0)
    return [db, cursor]


def clear():
    '''
    Check if the current platform is Windows or not.
    Then clear the screen with cls or clear.
    '''
    if sys.platform == "win32" or sys.platform == "win64":
        os.system("cls")
    else:
        os.system("clear")


def create_target(db, cursor):
    '''
    Create a new target on the local db.
    '''
    print("Create target under construction")


def list_targets(db, cursor):
    '''
    List all existing targets in the local db.
    '''
    print("List targets under construction")


def load_target(db, cursor):
    '''
    Load a specific target from the local db.
    '''
    print("Load targets under construction")


def delete_target(db, cursor):
    '''
    Delete existing target.
    '''
    print("Delete targets under construction")


def exit_program(db, cursor):
    '''
    The most complicated of all the available functions!
    '''
    print("Exiting program...")
    db.close()
    sys.exit(1)


def print_separator():
    '''
    Prints a separator depending on the terminal's width.
    '''
    print(str(SEPARATOR_SYMBOL) * int(SEPARATOR_LENGTH))


SEPARATOR_SYMBOL = "-"
SEPARATOR_LENGTH = os.popen('stty size', 'r').read().split()[-1]

if __name__ == "__main__":
    clear()
    print_separator()

    db_objs = init_cuppoc_db()
    db_conn = db_objs[0]
    db_cursor = db_objs[1]

    main_menu = {1: create_target,
                 2: list_targets,
                 3: load_target,
                 4: delete_target,
                 5: exit_program}
    while True:
        clear()
        print_separator()
        print("Welcome to Common User Password Profiler On Crack (CUPPOC)!")
        print("1. Create a new target")
        print("2. List targets")
        print("3. Load target")
        print("4. Delete target")
        print("5. Exit")
        try:
            choice = main_menu[input("> ")]
            print_separator()
            choice(db_conn, db_cursor)
        except KeyError:
            print("Invalid selection. Returning to main menu.")
            print_separator()
            sleep(3)
