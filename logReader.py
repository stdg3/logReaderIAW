from curses import raw
from os import stat
from pprint import pprint
from re import S


file_namex = "log_example.txt"


class iawReader:
    """
    engine
    """
    def __init__(self, file) -> None:
        """
        constructure method: init var's at first call of class
        """
        self.file_name = file
        self.line = None
        self.status = None
        self.db = {}

    def startReader(self):
        """
        method's name start without "_" char, it's mean safety call 
        """
        self._readFile()

    def _readFile(self):
        """
        starting read file, by "with" operator to autoClose file
        """
        with open(self.file_name, "r", encoding="utf8") as file:
            for raw_line in file:
                """
                get every line
                """
                if self._isCorrectLine(raw_line):
                    self._standardizeLine()
                    date = self._getLogDate()
                    person = self._getLogPerson(date)
                    status = self._getLogStatus(person)
                    
                    iArray =  len(self.db[date][person]["i"])
                    oArray =  len(self.db[date][person]["o"])
                    if status == "CheckIn": # and iArray == 0 or oArray == iArray:
                        # time = self._getLogTime()
                        # self.db[date][person]["i"].append(time)
                        pass
                    else:
                        pass
                        # time = self._getLogTime()
                        # self.db[date][person]["o"].append(time)
                        # print("out")
                        
                    
                        # input()
                    # print(self.line)
        
        pprint(self.db)

                

    def _isCorrectLine(self, data) -> bool:
        """
        if line has no data about check-IN/OUT return false for getting next line immediately
        """
        checkIndex = data.find("  ")
        # print(data, checkIndex)
        # input()
        if data[checkIndex + 2].isnumeric():
            return False
        if data[: -1] == "\n":
            self.line = data[: -1]
        else:
            self.line = data
        return True

    def _standardizeLine(self):
        """
        deleting all dots where are 4 and more in line
        """
        for _ in range(2):
            startPoint = self.line.find("....")
            endPoint = None
            for _ in range(startPoint, len(self.line)):
                if self.line[_] != ".":
                    endPoint = _
                    break
            self.line = self.line.replace(self.line[startPoint: endPoint], "-")
    
    def _getLogDate(self):
        date = self.line[:10]
        if date in self.db:
            pass
        else:
            self.db[date] = {}
        return date
    
    def _getLogPerson(self, date):
        # 28/10/2021 12:36:59:  Angela Martin-28.10.2021 12:36:53-CheckOut
        strt = self.line.find("  ")
        stp = self.line.find("-")
        person = self.line[strt + 2: stp]
        if person in self.db[date]:
            pass
        else:
            self.db[date][person] = {}
        self.db[date][person]["i"] = []
        self.db[date][person]["o"] = []
        return person
        
    def _getLogStatus(self, person):
        # print(self.line)
        strt = self.line.rfind("-") +1
        return self.line[strt:-1]
        # print(status)
        # input()
    
    def _getLogTime(self):
        strt = self.line.find("-")
        stp = self.line.rfind("-")
        strt = self.line.find(" ", strt, stp)
        return self.line[strt +1: stp]


if __name__ == "__main__":
    """
    дается старт программы ~ void main
    """
    reader = iawReader(file_namex)
    reader.startReader()