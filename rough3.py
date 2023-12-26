import os
file='new.pdf'
ext=os.path.splitext(file)
print (ext)

#   src_path = os.path.join(parent_dir,j)
   #   dst_path = os.path.join(directory, j)
   #   os.rename(src_path, dst_path)
   # elif ext==".pdf" and os.path.exists(path):  
   #   directory= "PDFs" 
   #   parent_dir= r"C:\Users\Shraddha Mahapatra\Desktop"
   #   path = os.path.join(parent_dir, directory)
   #   os.mkdir(path) 
   #   src_path = os.path.join(parent_dir, j)
   #   dst_path = os.path.join(directory, j)
   #   os.rename(src_path, dst_path)