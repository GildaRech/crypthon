import sys, os, shutil
from pytLoc import pytLoc

#try:
os.system("PATH %PATH%;%CD%")
#except:
#    pass


pyLoc=pytLoc.pytLoc
def is_locked(file):
    with open(str(file), "r") as fichier:
        content=fichier.read()
        if not "import" in content:
            if not "def" in content:
                if  not "return" in content:
                    if not "class" in content:
                        return True
        fichier.close()
    return False
help=""" crypthon V 1.0: a python command line tool that helps sharing and storing securely python source code files
         thanks to a simple and yet very strong and resilient string encryption. 
         It also provides an obsfucation with decryption at runtime.
         Author: Gilda Bansimba | https://github.com/GildaRech/pyLoc 
         usage: crypthon [option] 
         Options and arguments. All default python interpreter options and arguments also work. 
                -check: checks for a shared file integrity located in the same directory with its text file signature. 
                        e.g. crypthon -check locked_file1.py 
                -loc:   locks a file with the given key from which is randomly generated a one time pad security key.
                        e.g: crypthon -loc file.py password 
                        NOTE: file can be replaced by any of the following: 
                            - a list of python files. e.g: crypthon -loc file1.py file2.py password 
                            - . : for all python files in the current working directory. e.g. crypthon -loc . passowrd 
                            - * : for all python files in the current working directory and its subdirectories or subfolders.
                                  e.g. crypthon -loc * password
                            - *** : for all python source files stored on the entire disc partition. e.g crypthon -loc *** password
                -unloc: unlocks a locked file with the given password from which is randomly generated a one time pad security key.
                        e.g. crypthon -unloc file.py password
                        NOTE: all of the above mentioned parameters still apply.
                -keygen: displays the generated one time pad security key from the given password for the given file.
                        e.g. crypthon -keygen file.py password
                -True:  locks or unlocks the python file without keeping a copy of the original plaintext file or encrypted source file.
                        e.g. crypthon -loc file.py password -True 
                             crypthon -loc file.py password -False
                -Share: creates a folder with prefix SHARE_ containing the locked file (s) and text file (s) containing its (their) signature (s).
                For more info on crypthon or to report a bug or view the entire source code of crypthon,
                please visit the project's page at https://github.com/GildaRech/crypthon. Any collaboration is welcome.                  
                                 
"""
params=['-h', '-loc', '-unloc', '-keygen', '-True', '-False', '-share']
if len(sys.argv)==1:
    print("crypthon v 1.0, @Gilda_Bansimba")
    print(" Invalid argument. Please type crypthon -h for help.")
    sys.exit()
elif sys.argv[1].startswith(".\\")==True:
        file=sys.argv[1].replace(".\\", "")
elif len(sys.argv)==2 and sys.argv[1].endswith(".py")==True:
    os.system("python "+str(sys.argv[1]))
    sys.exit()
elif len(sys.argv)==2 and sys.argv[1] not in params and sys.argv[1].endswith(".py")==False:
    print("file "+str(sys.argv[1])+" is not a python file or does not exist in this directory. Try "+str(sys.argv[1])+".py instead")
    sys.exit()
elif len(sys.argv)==2 and sys.argv[1]=="-h":
     print(help)
     sys.exit()
elif len(sys.argv)==4 and sys.argv[1]=="-keygen":
    with open(sys.argv[2], "r") as f:
        length=len(f.read())
        f.close()
    print(pyLoc(sys.argv[2]).genKey(sys.argv[3], length))
    sys.exit()

if sys.argv[1] in params:
    if len(sys.argv)==2 and sys.argv[1]=="-h":
        print(help)
        sys.exit()
    elif len(sys.argv)==2 and sys.argv[1] in params:
        print("command incomplete, missing parameters. Type crypthon -h for help.")
        sys.exit()
    elif len(sys.argv)>=3:
        file=sys.argv[2]
        if not file in [".", "*", "***"]:
            if file.endswith(".py")==False:
                print("Not a python file or missing extension .py, please try "+str(file)+".py instead")
                sys.exit()
            elif file.endswith(".py")==True and file not in os.listdir(os.getcwd()):
                print("file "+str(file)+" does not exist in this directory")
                sys.exit()
            elif str(file).endswith(".py")==True and file in os.listdir(os.getcwd()):
                if is_locked(file)==False and sys.argv[1]=="-loc" and len(sys.argv)==3:
                    print("Missing security key. Type crypthon -loc "+str(file)+" password instead.")
                    sys.exit()
                elif is_locked(file)==False and sys.argv[1]=="-loc" and len(sys.argv)==4:
                    pyLoc(file, delete=False).loc(sys.argv[3])
                    print("file locked.")
                    sys.exit()
                elif is_locked(file)==False and sys.argv[1]=="-loc" and len(sys.argv)==5:
                    if sys.argv[4]=="-true" or sys.argv[4]=="-True" or sys.argv[4]=="-TRUE" or sys.argv[4]=="-tRue" or sys.argv[4]=="-trUe" or sys.argv[4]=="-truE":
                        pyLoc(file, delete=True).loc(sys.argv[3])
                        print("file locked.")
                        sys.exit()
                    elif sys.argv[4] in ["-False", "-FALSE", "-false", "-fAlse", "-faLse", "-falSe", "-falsE"]:
                        pyLoc(file, delete=False).loc(sys.argv[3])
                        print("file locked.")
                        sys.exit()
                    else:
                        print("Invalid mode, please specify the mode by -True or -False whether to keep trace or not. Type crypthon -h for help")
                        sys.exit()
                elif is_locked(file)==False and sys.argv[1]=="-loc" and len(sys.argv)==6:
                    if sys.argv[5] in ["-share", "-Share", "-sHare", "-shAre", "-shaRe", "-sharE", "-SHARE"]:
                       if sys.argv[4]=="-true" or sys.argv[4]=="-True" or sys.argv[4]=="-TRUE" or sys.argv[4]=="-tRue" or sys.argv[4]=="-trUe" or sys.argv[4]=="-truE":
                            pyLoc(file, delete=True).loc(sys.argv[3], share=True)
                            print("file locked.")
                            sys.exit()
                       elif sys.argv[4] in ["-False", "-FALSE", "-false", "-fAlse", "-faLse", "-falSe", "-falsE"]:
                            pyLoc(file, delete=False).loc(sys.argv[3], share=True)
                            print("file locked.")
                            sys.exit()
                       else:
                            print("Invalid mode, please specify the mode by -True or -False whether to keep trace or not. Type crypthon -h for help")
                            sys.exit()
                    else:
                        print("Invalid Argument")
                        sys.exit()
                elif is_locked(file)==True and sys.argv[1]=="-unloc" and len(sys.argv)==3:
                    print("Missing security key. Type crypthon -unloc "+str(file)+" password instead.")
                    sys.exit()
                elif is_locked(file)==True and sys.argv[1]=="-unloc" and len(sys.argv)==4:
                    pyLoc(file, delete=False).unlock(sys.argv[3])
                    print("file unlocked.")
                    sys.exit()
                elif is_locked(file)==True and sys.argv[1]=="-unloc" and len(sys.argv)==5:
                    if sys.argv[4]=="-true" or sys.argv[4]=="-True" or sys.argv[4]=="-TRUE" or sys.argv[4]=="-tRue" or sys.argv[4]=="-trUe" or sys.argv[4]=="-truE":
                        pyLoc(file, delete=True).unlock(sys.argv[3])
                        print("file unlocked.")
                        sys.exit()
                    elif sys.argv[4] in ["-False", "-FALSE", "-false", "-fAlse", "-faLse", "-falSe", "-falsE"]:
                        pyLoc(file, delete=False).unlock(sys.argv[3])
                        print("file unlocked.")
                        sys.exit()
                    else:
                        print("Invalid mode, please specify the mode by -True or -False whether to keep trace or not. Type crypthon -h for help")
                        sys.exit()
                elif is_locked(file)==True and sys.argv[1]=="-unloc" and len(sys.argv)==6:
                    if sys.argv[5] in ["-share", "-Share", "-sHare", "-shAre", "-shaRe", "-sharE", "-SHARE"]:
                      print("no "+sys.argv[5]+" argument for -unloc parameter")
                    else:
                        print("Invalid Argument")
                        sys.exit()
        else:
            if sys.argv[1]=="-loc" and len(sys.argv)==3:
                    print("Missing security key. Type crypthon -loc "+str(file)+" password instead.")
                    sys.exit()
            elif sys.argv[1]=="-loc" and len(sys.argv)==4:
                    pyLoc(file, delete=False).loc(sys.argv[3])
                    print("file locked.")
                    sys.exit()
            elif sys.argv[1]=="-loc" and len(sys.argv)==5:
                if sys.argv[4]=="-true" or sys.argv[4]=="-True" or sys.argv[4]=="-TRUE" or sys.argv[4]=="-tRue" or sys.argv[4]=="-trUe" or sys.argv[4]=="-truE":
                    pyLoc(file, delete=True).loc(sys.argv[3])
                    print("file locked.")
                    sys.exit()
                elif sys.argv[4] in ["-False", "-FALSE", "-false", "-fAlse", "-faLse", "-falSe", "-falsE"]:
                    pyLoc(file, delete=False).loc(sys.argv[3])
                    print("file locked.")
                    sys.exit()
                else:
                    print("Invalid mode, please specify the mode by -True or -False whether to keep trace or not. Type crypthon -h for help")
                    sys.exit()
            elif sys.argv[1]=="-loc" and len(sys.argv)==6:
                if sys.argv[5] in ["-share", "-Share", "-sHare", "-shAre", "-shaRe", "-sharE", "-SHARE"]:
                    if sys.argv[4]=="-true" or sys.argv[4]=="-True" or sys.argv[4]=="-TRUE" or sys.argv[4]=="-tRue" or sys.argv[4]=="-trUe" or sys.argv[4]=="-truE":
                        pyLoc(file, delete=True).loc(sys.argv[3], share=True)
                        print("file locked.")
                        sys.exit()
                    elif sys.argv[4] in ["-False", "-FALSE", "-false", "-fAlse", "-faLse", "-falSe", "-falsE"]:
                        pyLoc(file, delete=False).loc(sys.argv[3], share=True)
                        print("file locked.")
                        sys.exit()
                    else:
                        print("Invalid mode, please specify the mode by -True or -False whether to keep trace or not. Type crypthon -h for help")
                        sys.exit()
                else:
                    print("Invalid Argument")
                    sys.exit()
            elif sys.argv[1]=="-unloc" and len(sys.argv)==3:
                    print("Missing security key. Type crypthon -unloc "+str(file)+" password instead.")
                    sys.exit()
            elif is_locked(file)==True and sys.argv[1]=="-unloc" and len(sys.argv)==4:
                pyLoc(file, delete=False).unlock(sys.argv[3])
                print("file unlocked.")
                sys.exit()
            elif sys.argv[1]=="-unloc" and len(sys.argv)==5:
                if sys.argv[4]=="-true" or sys.argv[4]=="-True" or sys.argv[4]=="-TRUE" or sys.argv[4]=="-tRue" or sys.argv[4]=="-trUe" or sys.argv[4]=="-truE":
                    pyLoc(file, delete=True).unlock(sys.argv[3])
                    print("file unlocked.")
                    sys.exit()
                elif sys.argv[4] in ["-False", "-FALSE", "-false", "-fAlse", "-faLse", "-falSe", "-falsE"]:
                    pyLoc(file, delete=False).unlock(sys.argv[3])
                    print("file unlocked.")
                    sys.exit()
                else:
                    print("Invalid mode, please specify the mode by -True or -False whether to keep trace or not. Type crypthon -h for help")
                    sys.exit()
            elif sys.argv[1]=="-unloc" and len(sys.argv)==6:
                if sys.argv[5] in ["-share", "-Share", "-sHare", "-shAre", "-shaRe", "-sharE", "-SHARE"]:
                    print("no "+sys.argv[5]+" argument for -unloc parameter")
                else:
                    print("Invalid Argument")
                    sys.exit()

else:
    if sys.argv[1] in ["-check", "-Check", "-CHECK", "-cHeck", "-chEck", "-cheCk", "-checK"] and len(sys.argv)==3:
        pyLoc(sys.argv[2]).check(sys.argv[2])
        sys.exit()
    else:
        os.system("python "+str(sys.argv[1:]))
        sys.exit()

        


