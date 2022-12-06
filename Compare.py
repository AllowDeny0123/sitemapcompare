from File import File
from functools import singledispatchmethod

class Compare:
    
    """Functional class which compares objects of class 'File'"""
    
    @singledispatchmethod
    def __init__(self, file1: File, file2: File) -> None:
        """Defines init method"""
        self._file1 = file1
        self._file2 = file2
    
    @__init__.register
    def _(self, file1: str, file2: str) -> None:
        self._file1 = File(file1)
        self._file2 = File(file2)

    def CompareFiles(self) -> list[str]:
        """Method that compares contents of files"""
        _contents1 = self._file1.content
        _contents2 = self._file2.content
        _result: list[str] = []
        for i in _contents1:
            if i not in _contents2:
                _result.append(i)
        return _result
