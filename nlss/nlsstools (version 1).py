from pathlib import Path
import sys

def fileName():
    def get_script_name():
        try:
            return Path(__file__).name
        except NameError:
            return Path(sys.argv[0]).name
    def get_script_name():

        try:
            return Path(__file__).name
        except NameError:
            return Path(sys.argv[0]).name
    def print_filename():
        script_name = get_script_name()
        print(script_name)
    print_filename()
