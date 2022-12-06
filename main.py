from Compare import Compare

if __name__ == "__main__":
    a = Compare("1.xml", "2.xml")
    with open("output2.txt", "w") as file:
        _temp = a.CompareFiles()
        for i in _temp:
            file.writelines("".join(i+'\n'))
        file.close()
    
    