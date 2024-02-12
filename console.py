#!/usr/bin/python3

import json
import cmd
from models.user import User
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """A simple CRUD command for user data management"""

    CLASSES = {
            'BaseModel' : BaseModel,
            'User' : User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review,
            }

    prompt = "(hbnb) "

    def __init__(self):
        super().__init__()
        self.users = {} #a dictionary to store users


    def do_create(self, line):
        """this creates a new user syntax"""
        args = line.split()
        if not args:
            print("class name missing")
            return
        class_name = args[0]
        if class_name not in self.CLASSES:
             print("** class doesn't exist **")
             return
        try:
            object = self.CLASSES[class_name]()
            object.save()
            print(object.id)
        except Exception as E:
            print(E)

    def do_destroy(self, line):
        """this deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
             print("** class name missing **")
             return

        class_name = args[0]
        if class_name not in self.CLASSES:
             print("** class doesn't exist **")
             return

        if len(args) < 2:
             print("** instance id missing **")
             return

        object_id = args[1]
        key = "{}.{}".format(class_name, object_id)
        if key in self.users:
              del self.users[key]
              self.save_to_json() # Save changes to JSON file
        else:
            print("** no instance found **")
    
    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        object_id = args[1]
        key = "{}.{}".format(class_name, object_id)
        if key in self.users:
            print(self.users[key])
        else:
            print("** no instance found **")

    def do_all(self, line):
        """This Prints all string representation of all instances
        based or not on the class name."""
        args = line.split()
        if args and args[0] not in self.CLASSES:
            print("** class doesn't exist **")
            return

        objects = [str(obj) for obj in self.users.values()
                            if not args or obj.__class__.__name__ == args[0]]
        print(objects)


    def do_update(self, line):
        """This Updates an instance based on the class
                name and id by adding or updating attribute."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        object_id = args[1]
        key = "{}.{}".format(class_name, object_id)
        if key not in self.users:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        obj = self.users[key]
        # Update the attribute
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def save_to_json(self):
        """This Save the users dictionary to a JSON file."""
        with open("file.json", "w") as f:
            json.dump(self.users, f)

    def do_quit(self, line):
        """This Quits command to exit the program."""
        return True

    def do_EOF(self, line):
        """this handles EOF (Ctrl+D) to exit the program."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
