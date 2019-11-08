#!/usr/bin/python3
"""console for airbnb project"""
import cmd

class HBNBCommand(cmd.Cmd):

    """class for command module"""

    def do_EOF(self, line):
       return True

    def do_quit(self, line):
       return True

    def do_prompt(self):
       "Change the interactive prompt"
       self.prompt = "(hbnb)"
