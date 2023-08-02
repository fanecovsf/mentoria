
#Worker
#-------------------------------------------------------------------------------------------------------------------------------------
class Worker:
    def __init__(self, name, level, baseSalary, department):
        self.name = name
        self.level = level
        self.baseSalary = float(baseSalary)
        self.contracts = []
        self.department = department

    def __str__(self):
        formattedSalary = "{:.2f}".format(self.baseSalary)
        return f'Name: {self.name} | Level: {self.level} | Base salary: R${formattedSalary} | Contracts: {self.contracts}'

    
    #Métodos
    def addContract(self, contract):
        self.contracts.append(contract)

    def removeContract(self, contract):
        self.contracts.remove(contract)


#Department
#-------------------------------------------------------------------------------------------------------------------------------------
class Department:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


#HourContract
#-------------------------------------------------------------------------------------------------------------------------------------
class HourContract:
    def __init__(self, date, valuePerHour, hours):
        self.date = date
        self.valuePerHour = valuePerHour
        self.hours = hours

    def __str__(self) -> str:
        return f"Date: {self.date} | Value per hour: {self.valuePerHour} | Hours: {self.hours}"
    
    #Métodos
    def totalValue(self):
        return float(self.valuePerHour) * float(self.hours)
    
    def getMonth(self):
        return str(self.date).split('/')[1]
    
    def getYear(self):
        return str(self.date).split('/')[2]
