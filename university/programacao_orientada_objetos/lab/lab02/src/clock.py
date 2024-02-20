class NumberDisplay:
    '''
     __limit
     __value
    '''

    def __init__(self, rollOverLimit):
        self.__limit = rollOverLimit
        self.__value = 0

    def increment(self):
        self.__value = (self.__value + 1) % self.__limit

    def getDisplayValue(self):
        if self.__value < 10:
            return f'0{str(self.__value)}'
        else:
            return f'{str(self.__value)}'

    def getValue(self):
        return self.__value

    def setValue(self, replacementValue):
        if replacementValue < self.__limit:
            self.__value = replacementValue
        else:
            while (replacementValue >= self.__limit):
                replacementValue = replacementValue - self.__limit

            self.__value = replacementValue


class ClockDisplay:
    '''
     __hours
     __minutes
     __seconds
     __displyString
    '''

    def __init__(self):
        self.__hours = NumberDisplay(24)
        self.__minutes = NumberDisplay(60)
        self.__seconds = NumberDisplay(60)
        self.__updateDisplay()

    def timeTick(self):
        self.__seconds.increment()

        if self.__seconds.getValue() == 0:
            self.__minutes.increment()

            if self.__minutes.getValue() == 0:
                self.__hours.increment()

        self.__updateDisplay()

    def __updateDisplay(self):
        self.__displayString = f'{self.__hours.getDisplayValue()}:{self.__minutes.getDisplayValue()}:{self.__seconds.getDisplayValue()}'

    def getTime(self):
        return self.__displayString

    def setTime(self, hours, minutes, seconds):
        self.__hours.setValue(hours)
        self.__minutes.setValue(minutes)
        self.__seconds.setValue(seconds)
        self.__updateDisplay()
