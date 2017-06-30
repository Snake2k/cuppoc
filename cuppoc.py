#!/usr/bin/env python2
import os
import sys
import urwid
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
    clear()
    print_separator()
    print("NOTE:")
    print("[!] Checking to see if \"targets.db\" exists or not.")
    print("[!] If it doesn't, cuppoc will make one.")
    print("[!] cuppoc uses AES256 to encrypt your local database.")
    print("[!] This is due to Personally Identifiable Information (PII)")
    print("[!] which will be stored in the database.\n")
    print("[!] You will be asked to enter a password.")
    print("[!] This password is the key to your database. Don't forget :P")
    print("[!] If you have already done this before, " +
          "please use the password you used before to access your db.")
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
    except PYSQLDBERR:
        print("[-] Database doesn't exist or is encrypted.")
        print("[-] If database exists, enter the correct password.")
        db.close()
        print_separator()
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


def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def item_chosen(button, choice):
    response = urwid.Text([u'You chose ', choice, u'\n'])
    done = urwid.Button(u'Ok')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(
        urwid.Pile(
            [response,
             urwid.AttrMap(done, None, focus_map='reversed')]))


def exit_program(button):
    raise urwid.ExitMainLoop()


def print_separator():
    '''
    Prints a separator depending on the terminal's width.
    '''
    SEPARATOR_SYMBOL = "-"
    SEPARATOR_LENGTH = os.popen('stty size', 'r').read().split()[-1]
    print(str(SEPARATOR_SYMBOL) * int(SEPARATOR_LENGTH))


if __name__ == "__main__":
    db_objs = init_cuppoc_db()
    db_conn = db_objs[0]
    db_cursor = db_objs[1]

    choices = ["Create a new target.",
               "List all targets.",
               "Load target.",
               "Delete target.",
               "Exit"]
    main = urwid.Padding(
        menu(u'Welcome to the Common User Password Profiler (cuppoc)!',
             choices),
        left=2, right=2)
    top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
                        align='center', width=('relative', 60),
                        valign='middle', height=('relative', 60),
                        min_width=20, min_height=9)
    urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
    db_conn.close()
    print("[!] Closed connection to db.")
