import sys
import os


if __name__ == '__main__':
    try:
        os.environ["FUNCTION"]
    except KeyError:
        os.environ["FUNCTION"] = "add"

    try:
        if (os.environ["FUNCTION"] == "add"):
            print(int(sys.argv[1])+int(sys.argv[2]))
        elif (os.environ["FUNCTION"] == "subtract"):
            print(int(sys.argv[1])-int(sys.argv[2]))
        elif (os.environ["FUNCTION"] == "multiply"):
            print(int(sys.argv[1])*int(sys.argv[2]))
        elif (os.environ["FUNCTION"] == "divide"):
            print(int(sys.argv[1])+int(sys.argv[2]))
        else:
            exit(2)
    except IndexError:
        exit(2) 
