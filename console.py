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
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if line == "BaseModel":
            new = BaseModel()
            new.save()
            print(new.id)
        elif not line:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class name and id"""
        args = line.split()
        if args is None or args == [] or args[0] is None:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        elif args[1] in storage.all(self):
            print(self.__str__())
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args[0]:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        elif args[1] in FileStorage.all(self):
            print("destroy coming soon")
        else:
            print("** no instance found **")
        

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name"""
        args = line.split()
        

    def do_update(self, line):
        """Updates an instance by adding or updating an attribute"""
        args = line.split()
        if not args[0]:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        elif args[1] in FileStorage.all(self):
            print("update coming soon")
        else:
            print("** no instance found **")
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()
