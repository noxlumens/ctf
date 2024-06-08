#!/usr/bin/python3
import os

welcome = '''
Welcome Back,
What are we playing today?

Options:
1) Hackthebox
2) Proving Grounds
3) Tryhackme
'''
print(welcome)
try:
    user_defined_option = input(str("Option: "))
    os.system("clear")
    if user_defined_option == str(1):
        htb_options = input(str("What are we hacking today?\n1) Machines\n2) Season Machine\n3) Starting Point\n4) Fortresses\nOption: "))
        if htb_options == str(1):
            os.system("sudo /usr/sbin/openvpn /<path to ovpn file>")
        elif htb_options == str(2):
            os.system("sudo /usr/sbin/openvpn /<path to ovpn file>")
        elif htb_options == str(3):
            os.system("sudo /usr/sbin/openvpn /<path to ovpn file>")
        elif htb_options == str(4):
            print("I don't have the Fortress vpn file downloaded")
        else:
            print("That's an invalid option")
            exit
    elif user_defined_option == str(2):
        pg_options = print("Loading the Offsec Matrix...")
        os.system('sudo /usr/sbin/openvpn /<path to ovpn file>')
    elif user_defined_option == str(3):
        thm_options = print("Loading the Tryhackme Matrix...")
        os.system('sudo /usr/sbin/openvpn /<path to ovpn file>')
    else:
        print("You chose an options that doesn't exist!")
except KeyboardInterrupt:
    os.system("clear")
    print("\nGuess we aren't doing a CTF today because you exited the program.")
