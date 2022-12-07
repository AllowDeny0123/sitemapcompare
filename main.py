import sys
from File import File
from Compare import Compare

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 3:
        a = Compare(f"{sys.argv[1]}", f"{sys.argv[2]}")
        _outputfilename = File("output.output").path
        if sys.argv[3]:
            _outputfilename = sys.argv[3]
        with open(f"{_outputfilename}", "w") as file:
            _temp = a.CompareFiles()
            for i in _temp:
                file.writelines("".join(i+'\n'))
            file.close()
    else:
        raise FileNotFoundError("Positional arguments missing!")
        
        