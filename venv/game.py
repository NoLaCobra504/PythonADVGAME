import shutil
import time
import os
import sys
import pygame
import msvcrt as m
from ascii_Headings import intro , emotd

def paktc():
    print("Press any key to continue . . .")

def wait():
    m.getch()

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.5)
    value = input("> ").lower()
    return value

def dialog1():
    running = True
    size = os.get_terminal_size()
    a = "\n" * (size.lines - 2)
    while running:
        os.system('cls')
        time.sleep(1)
        typingPrint("Hello.\n")
        time.sleep(1)
        typingPrint("Welcome to the LOST PUZZLES!!!!!!!!\n")
        time.sleep(1)
        typingPrint("What is your NAME?\n")
        command = input(a+"> ")
        if command == "quit" or command == "exit":
            running = False
            return running
        os.system('cls')
        typingPrint("Well Hello There " + command)
        command = input(a+"> ")
        if command == "quit" or command == "exit":
            running = False
            return running
    return False
def main():
    os.system('cls')
    time.sleep(1)
    intro()
    paktc()
    wait()
    
    while True:
        dialog1()
    
def run():
    main()
    emotd()
    # while True:
    #     return False
