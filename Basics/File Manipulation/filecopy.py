#copyfile() = copies contents of a file
#copy() = copyfile() + permission mode + destination can be a dir
#copy2() = copy + copies metadata

import shutil #file copy module


shutil.copy("Files\copytile.txt","Files\copydir") #src,dst
