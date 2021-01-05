import sys
if len(sys.argv)>1:
    if sys.argv[1]=="sh":
        a_file = open(f"run.sh", "r")
        list_of_lines = a_file.readlines()
        list_of_lines.pop(0)
        list_of_lines.pop(1)
        a_file = open(f"run.sh", "w")
        a_file.writelines(list_of_lines)
        a_file.close()
    elif sys.argv[1]=="bat":
        a_file = open(f"run.bat", "r")
        list_of_lines = a_file.readlines()
        list_of_lines.pop(1)
        list_of_lines.pop(2)
        a_file = open(f"run.bat", "w")
        a_file.writelines(list_of_lines)
        a_file.close()