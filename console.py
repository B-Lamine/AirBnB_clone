#!/usr/bin/python3
"""entry point of the command interpreter.
"""


from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """this class contains implemented commands.
    """
    prompt = '(hbnb) '

    def do_create(self, class_name):
        """
        """
        if class_name:
            if class_name in globals():
                my_class = eval(class_name)
                model = my_class()
                model.save()
                print(model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """End-of-file (Ctrl+D) exits the program
        """
        print('')
        return True

    def emptyline(self):
        """emptyline doesn't execute any command
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
