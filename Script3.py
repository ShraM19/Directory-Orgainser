import os
import shutil
old_path=r"C:\Users\Shraddha Mahapatra\Desktop\Home"
folder_list=os.listdir(old_path)
print("Folders in '", old_path, "' :")
print(folder_list)
for folder in folder_list:
    path="C:\\Users\\Shraddha Mahapatra\\Desktop\\Home\\" + folder
    print (path)
    file_list=os.listdir(path)
    print ( "Files in '", path, "' :")

    print(file_list)
    for file in file_list:
        file_path=path+"\\" + file
        print ("@", file_path)
        if (file in dict1):
            new_path=dict1[file]
            print ("*", new_path) 
            shutil.move(file_path,new_path)
          