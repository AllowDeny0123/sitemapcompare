import sys
from Compare import Compare

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 3:
        a = Compare(f"{sys.argv[1]}", f"{sys.argv[2]}")
        with open("output.output", "w") as file:
            _temp = a.CompareFiles()
            for i in _temp:
                file.writelines("".join(i+'\n'))
            file.close()
    else:
        raise FileNotFoundError("Positional arguments missing!")
        
        