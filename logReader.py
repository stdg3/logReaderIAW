from pprint import pprint
from datetime import datetime
import json

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
        self.dataFromCurrentLine = None # dinamic types: str-list...
        self.db = {}
        self.performace = {}

    def startReader(self):
        """
        method's name start without "_" char, it's mean safety call
        starting read file, by "with" operator to autoClose file
        """
        with open(self.file_name, "r", encoding="utf8") as file:
            for raw_line in file:
                """
                get every line
                """
                if self._isCorrectLine(raw_line): # if in line has no err msg
                    self._deleteDots() # first deelte dots
                    self._someRegex() # create prety data from line
                    self._createDic() # tranform line to dictionary

        self._deleteMistakesInCheck() # с удалением последний день онуляется если не имеет чекОута
        # pprint(self.db)
        self._calculatePerformance() # расчеты времени
        # pprint(self.performace)
        self._exportJson()

    def _exportJson(self):
        with open("data.json", "w") as fp:
            json.dump(self.performace, fp, sort_keys=True, indent=4)
        
        

    def _isCorrectLine(self, data) -> bool:
        """
        if line has no data about check-IN/OUT return false for getting next line immediately
        """
        checkIndex = data.find("  ")
        if data[checkIndex + 2].isnumeric():
            return False
        self.dataFromCurrentLine = data
        return True

    def _deleteDots(self):
        """
        deleting all dots where are 4 and more in line
        """
        for _ in range(2):
            startPoint = self.dataFromCurrentLine.find("....")
            endPoint = None
            for _ in range(startPoint, len(self.dataFromCurrentLine)):
                if self.dataFromCurrentLine[_] != ".":
                    endPoint = _
                    break
            self.dataFromCurrentLine = self.dataFromCurrentLine.replace(self.dataFromCurrentLine[startPoint: endPoint], "|")
    
    def _someRegex(self):
        """
        line to list [] with regex cases
        """
        if "\n" in self.dataFromCurrentLine:
            self.dataFromCurrentLine = self.dataFromCurrentLine.replace("\n", "")
        self.dataFromCurrentLine = self.dataFromCurrentLine.replace("  ", "|")
        self.dataFromCurrentLine = self.dataFromCurrentLine.replace(" ", "|")
        self.dataFromCurrentLine = self.dataFromCurrentLine.split("|")


    def _createDic(self):
        """
        transform line to dic with useful data, 
        structure be like :
        ["name", "surname", "checkDate", "checkTime", "action"]
        """
        self.dataFromCurrentLine = [self.dataFromCurrentLine[_] for _ in range(2, len(self.dataFromCurrentLine))]
        # self.dataFromCurrentLine = [self.dataFromCurrentLine[4], self.dataFromCurrentLine[5], self.dataFromCurrentLine[2], self.dataFromCurrentLine[3], self.dataFromCurrentLine[6]]
        # print(self.dataFromCurrentLine)
        person = self.dataFromCurrentLine[0] + " "+  self.dataFromCurrentLine[1]

        """if data not in DB alter it -> for all levels step by step"""
        if self.dataFromCurrentLine[2] not in self.db:
            self.db[self.dataFromCurrentLine[2]] = {}
        
        if person not in self.db[self.dataFromCurrentLine[2]]:
            self.db[self.dataFromCurrentLine[2]][person] = {}
            self.db[self.dataFromCurrentLine[2]][person]["i"] = []
            self.db[self.dataFromCurrentLine[2]][person]["o"] = []
        
        """add time just HH:MM
        ['Pam Beesly': 'i': ['07:25:34', '07:25:35', '12:26:34'], 
                'o': ['11:56:55', '16:23:46']]
        """
        checkTimeHourAndMin = self.dataFromCurrentLine[3][:-3]
        if self.dataFromCurrentLine[4] == "CheckIn" and checkTimeHourAndMin not in self.db[self.dataFromCurrentLine[2]][person]["i"]:
            self.db[self.dataFromCurrentLine[2]][person]["i"].append(checkTimeHourAndMin)
        
        elif self.dataFromCurrentLine[4] == "CheckOut" and checkTimeHourAndMin not in self.db[self.dataFromCurrentLine[2]][person]["o"]:
            self.db[self.dataFromCurrentLine[2]][person]["o"].append(checkTimeHourAndMin)
    
    def _deleteMistakesInCheck(self):
        """
        не нужные стампы        
        """
        innerTimes = []
        outTimes = []
        for dateKey,dateValue in self.db.items():
            for person,chekedTimes in dateValue.items():
                # status = None # i/o
                # timexStamps = None # list
                for status, timexStamps in chekedTimes.items():
                    if status=="i":
                        innerTimes = timexStamps
                    outTimes=timexStamps
                
                innerCounter = len(innerTimes)
                outCounter = len(outTimes)


                """
                чистим оут стампы беря за реферанс инпут
                25 'Meredith Palme': {'i': ['09:33:53'],
                    'o': ['13:55:23', '17:29:19', '20:30:55']
                """
                if innerCounter < outCounter:
                    newOutStampList = self._clearOutStamps(innerCounter, outTimes)
                    self.db[dateKey][person]["o"]=newOutStampList
                
                
                """
                чистим инпуты с точностью до наоборот
                26 'Michael Scott': {'i': ['06:41:29', '12:45:57'],
                    'o': ['16:46:11']},
                """
                if innerCounter > outCounter:
                    newInnerStampList = self._clearInStamps(outCounter, innerTimes)
                    self.db[dateKey][person]["i"]=newInnerStampList
                # print(person, innerTimes, outTimes, len(outTimes))

    def _calculatePerformance(self):
        # acces to data
        for dateKey, dateValue in self.db.items():
            for person, stamps in dateValue.items():
                innerTimes, outTimes = [], []
                worked = datetime.strptime("00:00", '%H:%M')
                for status, timexStamps in stamps.items():
                    if status=="i":
                        innerTimes = timexStamps
                    outTimes=timexStamps
                    # done, readed
                """loop: столько сколько имеется стампов
                из-за того что не закрытые стампы в учет не берутsя 
                кол-во стампов в arrayВходов и arrayВыходов будут равны по длине 
                преобразовываем в тайм структуру и дальше математика
                """ 
                for _ in range(len(innerTimes)):                    
                    timeInput = datetime.strptime(innerTimes[_], '%H:%M')
                    timeOutput = datetime.strptime(outTimes[_], '%H:%M')
                    worked += timeOutput-timeInput
                
                """
                новый словарь для оценки юзеров

                """
                if dateKey not in self.performace:
                    self.performace[dateKey] = {}
                if person not in self.performace[dateKey]:
                    i,o= "@work", "@work"
                    if innerTimes:
                        i = innerTimes[0]
                        o = outTimes[-1]
                    
                    pausedTime = datetime.strptime("00:00", '%H:%M')
                    if len(innerTimes) >= 2:
                        """
                        if person has more 2 stamp значит был простой
                        """
                        pausedTime = self._getBreaks(innerTimes, outTimes)

                    """
                    вычисления для сверх урочных, передаем сколько юзер работал, по графику рабоцхего места просто отнимаем"""
                    overTime = self._getOvertime(worked)
                    
                    # пресуем все в оценочный словарь
                    self.performace[dateKey][person] = {
                        "CheckIn": i,
                        "CheckOut": o,
                        "Worked": f"{worked.hour}:{worked.minute}",
                        "Break time": f"{pausedTime.hour}:{pausedTime.minute}",
                        "Over time": f"0:0"
                        }
                    # если переработки нет то во избежании none записей проверяем 
                    if overTime:
                       self.performace[dateKey][person]["Over time"] = f"{overTime.hour}:{overTime.minute}"

    def _getBreaks(self, checkInTimes, checkOutTimes):
        """ in -> [0] [1] [2]
            out-> [3] [4] [5]
            берем [1][3] отнимаем и имеем сколько была пауза
            дальше идем на искосок до len -1 случаев
        """
        pausedTime = datetime.strptime("00:00", '%H:%M')
        for _ in range(len(checkInTimes) - 1):
            timeInput = datetime.strptime(checkInTimes[_+1], '%H:%M')
            timeOutput = datetime.strptime(checkOutTimes[_], '%H:%M')
            pausedTime += timeInput - timeOutput
        return pausedTime

    def _getOvertime(self, workedHours):
        """"
        если отработнно больше 8.30 часов возвращается %H.%M от отработанного
        преобразования и вычитание времени 
        """
        startHour, endHour = "08:00", "16:30"
        standardWorkHour= datetime.strptime(endHour, '%H:%M') -datetime.strptime(startHour, '%H:%M')

        standardWorkHour = datetime.strptime(f"1900-01-01 {standardWorkHour}", '%Y-%m-%d %H:%M:%S')

        if workedHours>standardWorkHour:
            a = workedHours - standardWorkHour
            return datetime.strptime(f"1900-01-01 {workedHours - standardWorkHour}", '%Y-%m-%d %H:%M:%S')
            
    def _clearOutStamps(self, innerCounter, outTimes):
        """
        если длина аррая отличается по входам и выходам юзера то идем на сокращение в оутах оставляем последний выход  
        """
        __ = -1
        newOutes = []
        for _ in range(innerCounter):
            newOutes.append(outTimes[__])
            __ -=1
        return newOutes

    def _clearInStamps(self, outCounter, innerTimes):
        """
        и во входах оставляем первый вход
        таким образом не берем ложные входы выходы в середине
        """
        __ = 0
        newInners = []
        for _ in range(outCounter):
            newInners.append(innerTimes[__])
            __ += 1
        return newInners

    """
    код изначально не имел регекс конструкций - соответственно здесь костыли)

    def _getLogDate(self):
        date = self.dataFromCurrentLine[:10]
        if date in self.db:
            pass
        else:
            self.db[date] = {}
        return date
    
    def _getLogPerson(self, date):
        # 28/10/2021 12:36:59:  Angela Martin-28.10.2021 12:36:53-CheckOut
        strt = self.dataFromCurrentLine.find("  ")
        stp = self.dataFromCurrentLine.find("-")
        person = self.dataFromCurrentLine[strt + 2: stp]
        if person in self.db[date]:
            pass
        else:
            self.db[date][person] = {}
        self.db[date][person]["i"] = []
        self.db[date][person]["o"] = []
        return person
        
    def _getLogStatus(self, person):
        # print(self.dataFromCurrentLine)
        strt = self.dataFromCurrentLine.rfind("-") +1
        return self.dataFromCurrentLine[strt:-1]
        # print(status)
        # input()
    
    def _getLogTime(self):
        strt = self.dataFromCurrentLine.find("-")
        stp = self.dataFromCurrentLine.rfind("-")
        strt = self.dataFromCurrentLine.find(" ", strt, stp)
        return self.dataFromCurrentLine[strt +1: stp]
    """

if __name__ == "__main__":
    """
    дается старт программы ~ void main
    """
    reader = iawReader(file_namex)
    reader.startReader()
    # старт функция отличается наименованием, а точнее отсутсвует ниж подчеркивание, таким образом при передачи класса другой разработчик будет знать какие методы не вызывать на прямую
