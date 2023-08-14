#!/usr/bin/python3
"""entry point of the command interpreter.
"""


from models import storage
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """this class contains implemented commands.
    """
    prompt = '(hbnb) '

    def do_update(self, line):
        """update attributes of instance of given class and id.
          Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not line:
            print("** class name missing **")
            return
        arg_list = line.split()
        if arg_list[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        objs_dict = storage.all().copy()
        key = '.'.join(arg_list[0:2])
        if key not in objs_dict.keys():
            print("** no instance found **")
            return
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return
        if len(arg_list) == 3:
            print("** value missing **")
            return
        my_obj_dict = objs_dict[key]
        if arg_list[2] in my_obj_dict:
            value_type = type(my_obj_dict[arg_list[2]])
            arg_list[3] = value_type(arg_list[3])
        my_obj_dict[arg_list[2]] = arg_list[3]
        my_class = eval(arg_list[0])
        my_obj = my_class(**my_obj_dict)
        my_obj.save()

    def do_create(self, class_name):
        """create instance of a given class and print its id
        """
        if class_name:
            if class_name not in globals():
                print("** class doesn't exist **")
            else:
                my_class = eval(class_name)
                model = my_class()
                model.save()
                print(model.id)
        else:
            print("** class name missing **")

    def do_all(self, class_name):
        """
        """
        if class_name and class_name not in globals():
            print("** class doesn't exist **")
        else:
            tmp_list = []
            objs_dict = storage.all().copy()
            if class_name:
                my_class = eval(class_name)
                for obj in objs_dict.values():
                    tmp_list.append(str(my_class(**obj)))
                print(tmp_list)
            else:
                classes = []
                for key in objs_dict.keys():
                    class_name = key.split('.')[0]
                    if class_name not in classes:
                        classes.append(class_name)
                for class_name in classes:
                    my_class = eval(class_name)
                    for obj in objs_dict.values():
                        tmp_list.append(str(my_class(**obj)))
                print(tmp_list)

    def do_show(self, line):
        """given class and id, print dictionary representation of
            corresponding instance
        """
        if line:
            args_list = line.split()
            if args_list[0] not in globals():
                print("** class doesn't exist **")
            else:
                if len(args_list) == 1:
                    print("** instance id missing **")
                else:
                    objs_dict = storage.all()
                    key = '.'.join(args_list)
                    if key not in objs_dict:
                        print("** no instance found **")
                    else:
                        my_class = eval(args_list[0])
                        my_model = my_class(**objs_dict[key])
                        print(my_model)
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """destroy instance of given class and id from storage
        """
        if line:
            args_list = line.split()
            if args_list[0] not in globals():
                print("** class doesn't exist **")
            else:
                if len(args_list) == 1:
                    print("** instance id missing **")
                else:
                    objs_dict = storage.all()
                    key = '.'.join(args_list)
                    if key not in objs_dict:
                        print("** no instance found **")
                    else:
                        del objs_dict[key]
                        storage.save()
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
