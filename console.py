#!/usr/bin/python3
"""entry point of the command interpreter.
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """this class contains implemented commands.
    """
    prompt = '(hbnb) '

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
