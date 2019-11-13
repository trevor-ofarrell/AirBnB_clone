#!/usr/bin/python3
"""console for airbnb project"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class for command module"""
    prompt = "(hbnb) "
    newdict = {'BaseModel': BaseModel,
               'User': User,
               'Amenity': Amenity,
               'City': City,
               'State': State,
               'Place': Place,
               'Review': Review}

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not line:
            print("** class name missing **")
        elif line in self.newdict.keys():
            new = self.newdict[line]()
        else:
            print("** class doesn't exist **")
        print(new.id)
        new.save()

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class name and id"""
        args = line.split()
        if args is None or args == [] or args[0] is None:
            print("** class name missing **")
        elif args[0] not in self.newdict.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] in storage.all().keys():
            print(storage.all()[args[0] + '.' + args[1]])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if args is None or args == [] or args[0] is None:
            print("** class name missing **")
        elif args[0] not in models:
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] in storage.all().keys():
            del storage.all()[args[0] + "." + args[1]]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name"""
        args = line.split()
        if args != [] and args[0] not in self.newdict.keys():
            print("** class doesn't exist **")
        elif args != []:
            strlist = []
            for k, v in storage.all().items():
                temp = k.split(".")
                if temp[0] == args[0]:
                    strlist.append(str(v))
            print(strlist)
        else:
            strlist = []
            for obj in storage.all().values():
                strlist.append(str(obj))
            print(strlist)

    def do_update(self, line):
        """Updates an instance by adding or updating an attribute"""
        args = line.split()
        if args is None or args == [] or args[0] is None:
            print("** class name missing **")
        elif args[0] not in self.newdict.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif args[0] + "." + args[1] in storage.all().keys():
            setattr(storage.all()[args[0] + "." + args[1]], args[2],
                    args[3][1:-1] if args[3][0] is '"' or args[3][0] is "'"
                    else float(args[3]) if '.' in args[3] else int(args[3]))
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
