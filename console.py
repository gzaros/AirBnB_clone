#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Exit the command interpreter on EOF (Ctrl+D).
        """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
