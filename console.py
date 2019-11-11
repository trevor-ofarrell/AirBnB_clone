#!/usr/bin/python3
"""console for airbnb project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class for command module"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Create command to exit the program"""
        return True

    def do_show(self, line):
        """Quit command to exit the program"""
        return True

    def do_destroy(self, line):
        """EOF command to exit the program"""
        return True

    def do_all(self, line):
        """Quit command to exit the program"""
        return True

    def do_update(self, line):
        """EOF command to exit the program"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
