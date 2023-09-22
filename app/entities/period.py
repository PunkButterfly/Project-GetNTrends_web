from enum import Enum



class Period(Enum):

    def __init__(self, days_number, description):
        self.days_number = days_number
        self.description = description

    DAY = (1, "День")
    WEEK = (7, "Неделя")
    MONTH = (30, "Месяц")
    YEAR = (365, "Год")
