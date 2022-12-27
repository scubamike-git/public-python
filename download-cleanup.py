import os
import magic
import re
print("\n")
print("DIRECTORY:")
print("\n")
print("FILES:")
ms=magic.open(magic.MAGIC_NONE)
ms.load()

regex='text|image|InternetShortcut|executable'
for root, dirs, files in os.walk(os.environ['<***DIRECTORY***>']):
    for filename in files:
        fullpath=os.path.join(root,filename)
        # print(filename)
        output=magic.from_file(fullpath)
        # print("\t" + output)
        print(filename + "--" + output)
        if re.search(regex,output) is not None:
            # print "\tReg Matched"
            os.remove(fullpath)
            print("----Removed:" + filename)
            print("-----------" +  output)
        else:
            print("----Keeping File:" + filename)
            print("----------------" + output)
print("Done!")
