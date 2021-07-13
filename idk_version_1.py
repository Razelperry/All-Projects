import os
import shutil
import wikipedia

print("Welcome to IDK,")

while True:

    com = input(f"""type commands and do stuff, type the 'all coms' command to see all the commands you can use : """)

    if com == "all coms":
        print("""all the commands are given below... 
        _____________________________________________________
        |                                                   |
        |1.mkflr - used to make a folder                    |
        |2.mkfl - used to make a .txt file                  |
        |5.fledit - used to edit a text file                |
        |6.wiki - used to search something on wikipedia     |
        |7.delete fl - used to delete any type of files     |
        |8.delete flr - used to delete folders              |
        |9.cd - used to change directory                    |
        -----------------------------------------------------""")

    elif com == "mkfl":
        fln = input("What do you want to name your txt file (make sure to add an extention after the name) : ")
        fl = open(fln, "w")
        infl = input("write things in " + fln + " : ")
        fl.write(infl)
        fl.close()

    elif com == "fledit":
        fln = input("enter the name of the file you want to edit...(make sure to add an extention after the name) : ")
        with open(fln) as f:
            for line in f:
                print(line)
            with open(fln, 'a') as f:
                fl = input("Enter more text to " + fln + " : ")
                f.write(fl)
                f.close()
    
    elif com == "delete fl":
        fln = input("Enter the file path you want to delete(Make sure to add the extension of the file you are trying to edit) : ")
        os.remove(fln)

    elif com == "mkflr":
        flrn = input("What do you want to name your new folder : ")
        os.makedirs(flrn)
        print("folder created you now get into that folder by using the cd command")

    elif com == "cd":
        drn = input("enter the name of your directory : ")
        os.chdir(drn)

    elif com == "delete flr":
        flr_path = input("enter file path : ")
        shutil.rmtree(flr_path)

    elif com == "wiki":
        search_title = input("What do you want to search in wikipedia : ")
        results_for_wiki_search = wikipedia.summary(search_title, sentences = 5)
        print(results_for_wiki_search)