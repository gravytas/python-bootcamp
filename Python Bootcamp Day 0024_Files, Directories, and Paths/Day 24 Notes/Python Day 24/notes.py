###auto open and close file (in read-only mode) and can specify what do with with the 'with' operator and set as variable 'file'
###mode=w is open is write mode

#with open("my_files.txt") as file:
    #contents = file.read()
    #print(contents)

###overwrite a file
#with open("my_files.txt", mode="w") as file:
    #file.write("New text.")

###open in append mode - add extra data to text file; won't overwrite what is there
#with open("my_files.txt", mode="a") as file:
    #file.write("\nNew text.")

###opening a file in write mode that doesn't exist creates that file in the same directory
#with open("New_file.txt", mode="w") as file:
    #file.write("I am the new file")

#File Path notes:

#absolute file path
# / - root
# /Users/gravytas/Desktop/python...

#relative file path
# starts with current folder (./) then add in file path as usual
# ./Desktop/python...
#back up to a parent folder - '../' (one step up to parent folder)

###Challenge - pull file from desktop (absolute)
#with open("/Users/[%username%]/Desktop/my_files.txt") as file:
    #contents = file.read()
    #print(contents)

###Challenge - pull file from desktop (relative)
#with open("../../my_files.txt") as file:
    #contents = file.read()
    #print(contents)







##open file
#file = open("my_files.txt")

##reads file contents as string
#contents = file.read()
#print(contents)

##need to close files we open
#file.close()