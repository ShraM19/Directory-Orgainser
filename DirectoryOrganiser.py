import os
import shutil
flag=1
dict1={}
while (flag>0):   
    ch=int(input("Enter choice"))
    if ch==1:
        old_path = r"C:\Users\Shraddha Mahapatra\Desktop\Test"
        dir_list = os.listdir(old_path)
        print("Files and directories in '", old_path, "' :")
        print(dir_list)
        # prints all files
        print (type(dir_list))
        len1=0
        len_list=0
        ext=""
        ch=''
        one_path=""
        old_src=""
        new_src=""
        len_list=len(dir_list)
        print ("Length of list",len_list)

        for (i) in range (0,len_list,1):
            print (dir_list[i])
            len1= len(dir_list[i])
            #print (len1)
            file_path="C:\\Users\\Shraddha Mahapatra\\Desktop\\Test\\" + dir_list[i]
            print ("file path", file_path)

            for (j) in range (len1-1,0,-1):
                ch=dir_list[i][j]
                if ch=='.':
                    ext=(dir_list[i][j:len1])
                    print ("extension",ext)
                    one_path="C:\\Users\\Shraddha Mahapatra\\Desktop\\Home\\"+ ext
                    print (one_path)  
                    
                    '''key=dir_list[i]
                    dict1[key]=old_path
                    print (dict1)'''

                    isdir=os.path.isdir(one_path)   
                    print ("Whether present or not",isdir) 

                    if (isdir):
                        shutil.move(file_path,one_path)
                        
                    else: 
                        directory= ext
                        parent_dir= r"C:\Users\Shraddha Mahapatra\Desktop\Home"
                        new_path = os.path.join(parent_dir, directory)
                        os.mkdir(new_path)
                        shutil.move(file_path,new_path)  
                        flag=flag+1

                    print ("File name",dir_list[i])
                    dict1[dir_list[i]]={"old_src":old_path,"new_src":one_path}
                    print (dict1) 

    if ch==2:
        old_path=r"C:\Users\Shraddha Mahapatra\Desktop\Home"
        folder_list=os.listdir(old_path)
        print("Folders in '", old_path, "' :")
        print(folder_list)

        for element in dict1:
            print (element)
            print(dict1[element]["old_src"])
            print("!",dict1[element]["new_src"])
            shutil.move(dict1[element]["new_src"],dict1[element]["old_src"])

        '''for folder in folder_list:
            path="C:\\Users\\Shraddha Mahapatra\\Desktop\\Home\\" + folder
            print (path)
            file_list=os.listdir(path)
            print("Files in '", path, "' :")
            print(file_list)

            for file in file_list:
                file_path=path+"\\" + file
                print ("@", file_path)
                print ("Dictionary",dict1)
                print ("File_names",file)
                if (file in dict1):
                    new_path=dict1[file]
                    print ("*", new_path)
                    shutil.move(file_path,new_path)
                else:
                    print ("No")'''