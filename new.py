import os
import shutil
one_path=r"C:\Users\Shraddha Mahapatra\Desktop\Test\Book1.xlsx"
new_path=r"C:\Users\Shraddha Mahapatra\Desktop"
shutil.move(one_path,new_path)
os.rmdir(one_path) 