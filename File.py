import os
from ResultSet import ResultSet
from bs4 import BeautifulSoup
from FileException import FileException

class File:

    """Base minimal class of file"""

    def __init__(self, path:str) -> None:
        """Defines init method"""
        if os.path.exists(path) == True:
            self._path: str = path
        else:
            raise FileException("Cannot open file! Check filename or destination folder")

    def GetContents(self) -> BeautifulSoup:
        _rawcontent: list[str]
        with open(f"{self._path}", "r", encoding="utf-8") as file:
            _rawcontent = file.readlines()
            file.close()
        _stringcontents = "".join([i for i in _rawcontent])
        return BeautifulSoup(_stringcontents, features="xml")

    def URLTagsToResultSet(self) -> ResultSet:
        return ResultSet(self.GetContents().findAll("url"))  # type: ignore

    @property
    def path(self) -> str:
        """Path property of file"""
        return self._path

    @property
    def content(self) -> list[str]:
        """Cleaned contents of file"""
        return self.URLTagsToResultSet().CleanupSet()
