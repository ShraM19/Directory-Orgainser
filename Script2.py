import os
import shutil
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
len_list=len(dir_list)
print (len_list)

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
         print (one_path)  \
            
         dict1={}
         dict1[dir_list[i]]=one_path
         print (dict1)

         isdir=os.path.isdir(one_path)   
         print (isdir) 

         if (isdir):
            shutil.move(file_path,one_path)
            #os.rmdir(file_path)
            print ("Bye")

         else: 
            directory= ext
            parent_dir= r"C:\Users\Shraddha Mahapatra\Desktop"
            new_path = os.path.join(parent_dir, directory)
            os.mkdir(new_path)
            print ("Hi")
            shutil.move(file_path,new_path)
            #os.rmdir(file_path)     
            print("Hello")
