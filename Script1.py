import os
import shutil
old_path = r"C:\Users\Shraddha Mahapatra\Desktop\Test"
dir_list = os.listdir(old_path)
print("Files and directories in '", old_path, "' :")
# prints all files
print(dir_list)
print ('hello world')
print (type(dir_list))
len1=0
len_list=0
ext=""
ch=''
len_list=len(dir_list)

for (i) in range (0,len_list,1):
   print (dir_list[i])
   len1= len(dir_list[i])

   for (j) in range (len1-1,0,-1):
      ch=dir_list[i][j]

      if ch=='.':
         ext=(dir_list[i][j:len1])
         print (ext)
         mid_path= os.path.abspath(dir_list[i])
         print (mid_path)

         if ext==".docx":
            directory= "All MSWords" 
            parent_dir= r"C:\Users\Shraddha Mahapatra\Desktop"
            new_path = os.path.join(parent_dir, directory)
            if (not(os.path.exists(new_path))):  
               os.mkdir(new_path)
               shutil.move(mid_path,new_path)
               os.rmdir(mid_path)
               print("Hello Word")
            else:
               print("No word")  

         elif ext==".xlsx":
            directory= "All Excel Sheets" 
            parent_dir= r"C:\Users\Shraddha Mahapatra\Desktop"
            new_path = os.path.join(parent_dir, directory)
            if (not(os.path.exists(new_path))):  
               os.mkdir(new_path)
               shutil.move(mid_path,new_path)
               #os.rmdir(mid_path)
               print("Hello Excel")
            else:
               print("No Excel")   

         elif ext==".pdf":
            directory= "All PDFs" 
            parent_dir= r"C:\Users\Shraddha Mahapatra\Desktop"
            new_path = os.path.join(parent_dir, directory)
            if (not(os.path.exists(new_path))):  
               os.mkdir(new_path)
               shutil.move(mid_path,new_path)
               os.rmdir(mid_path)
               print("Hello PDF") 
            else:
               print("No PDF")             