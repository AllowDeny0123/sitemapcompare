import sys
from File import File
from Compare import Compare

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        a = Compare(f"{sys.argv[1]}", f"{sys.argv[2]}")
        _outputfilename = "output.output"
        if sys.argv[3]:
            _outputfilename = f"{sys.argv[3]}"
        with open(f"{_outputfilename}", "w") as file:
            _temp = a.CompareFiles()
            for i in _temp:
                file.writelines("".join(i+'\n'))
            file.close()
    else:
        raise FileNotFoundError("Positional arguments missing!")
        
        