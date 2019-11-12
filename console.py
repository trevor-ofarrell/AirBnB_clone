#!/usr/bin/python3
"""console for airbnb project"""
import cmd
from models.base_model import BaseModel

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
        if line == "BaseModel":
            new = BaseModel()
            new.save()
            print(new.id)
        elif not line:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Quit command to exit the program"""
        args = line.split()
        if not args[0]:
            print("** class name missing **")
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
        if args[0] and not args[1]:
            print("** instance id missing **")
        if args[1] == BaseModel.id:
            print(self.__str__())
        elif args[0] and args[1] != BaseModel.id:
            print("** no instance found **")
            
        
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
