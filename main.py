from Compare import Compare
import os
from sys import setrecursionlimit

if __name__ == "__main__":
    setrecursionlimit(2000)
    a = Compare("1.xml", "2.xml")
    with open("output2.txt", "w") as file:
        _temp = a.CompareFiles()
        for i in _temp:
            file.writelines("".join(i+'\n'))
        file.close()
    
    