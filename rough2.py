# import os, shutil
# # path = "/volume1/Users/Transfer/"
# # moveto = "/volume1/Users/Drive_Transfer/"
# # files = os.listdir(path)
# # files.sort()
# # for f in files:
# #     src = path+f
# #     dst = moveto+f
# #     shutil.move(src,dst)
#old_path = r"C:\Users\Shraddha Mahapatra\Desktop\Me"
new_path = r"C:\Users\Shraddha Mahapatra\Desktop\Worddocuments"
shutil.move(old_path,new_path)

import os
os.rename(old_path, new_path)