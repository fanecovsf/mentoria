from entities import *
import datetime

#Parameters
#-------------------------------------------------------------------------------------------------------------------------------------
WORKER_LEVEL = [
    'JUNIOR',
    'MID_LEVEL',
    'SENIOR',
]

#Program
#-------------------------------------------------------------------------------------------------------------------------------------
department = Department(input("Enter department's name: "))

print("Enter worker's data:")

workerName = input('Name: ')

workerLevel = input('Level (JUNIOR, MID_LEVEL, SENIOR): ')

while workerLevel not in WORKER_LEVEL:
    workerLevel = input("This level doesn't exist. Try again: ")

workerSalary = input('Base salary (Only numbers): ')

worker = Worker(workerName, workerLevel, workerSalary, department)

print('')

contractQty = input('How many contracts to this worker? ')

for i in range(int(contractQty)):
    print(f"Enter contract {i+1} data:")
    contractDate = input('Date (dd/mm/yyyy): ')
    contractValue = input('Value per hour: ')
    contractDuration = input('Duration (hours): ')

    formattedDate = datetime.datetime.strptime(contractDate, "%d/%m/%Y")
    formattedDate = datetime.date.strftime(formattedDate, "%d/%m/%Y")

    contract = HourContract(formattedDate, contractValue, contractDuration)

    worker.addContract(contract)


#View income
dateIncome = input('Enter month and year to calculate income (mm/yyyy): ')

month = dateIncome.split('/')[0]
year = dateIncome.split('/')[1]

baseSalary = worker.baseSalary

for contract in worker.contracts:
    if month == contract.getMonth() and year == contract.getYear():
        baseSalary += contract.totalValue()


print(f"Name: {worker.name}")
print(f"Department: {worker.department}")
print(f"Income for {dateIncome}: {baseSalary}")




