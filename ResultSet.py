import re
from bs4 import element

class ResultSet(element.ResultSet):
    
    """Override ResultSet class from bs4.element"""

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    def CleanupSet(self):
        _result: list[str] = []
        for i in self.source:  # type: ignore
            i.contents.remove('\n')
            _result.append(i.contents[0].contents[0])
        return _result
