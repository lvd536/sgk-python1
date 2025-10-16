class Employee:
    BASE_SALARY = {
        'manager': 40000,
        'developer': 45000,
        'marketer': 30000

    }
    BASE_HOUR_SALARY = {
        'manager': 125,
        'developer': 150,
        'marketer': 100

    }
    REGION_MULTIPLIER = {
        "moscow": 1.2,
        "peter": 1.1,
        "other": 1
    }
    BASE_HOURS = 8
    def __init__(self, person, region, sales):
        self.job = person
        self.region = region
        self.sales = sales
        self.salary = self.BASE_SALARY[self.job] * self.REGION_MULTIPLIER[self.region]

class Manager(Employee):
    def __init__(self, person, region, sales):
        super().__init__(person, region, sales)
        if self.sales <= 100: self.salary = round(self.salary * 1.05)
        elif self.sales > 100 & self.sales <= 120: self.salary = round(self.salary * (self.salary / 100))
        elif self.sales > 120: self.salary = round(self.salary * 1.2)
        self.sales = sales
class Developer(Employee):
    def __init__(self, person, region, sales, hours, isTemp):
        super().__init__(person, region, sales)
        self.hours = hours
        self.isTemp = isTemp
        if not self.isTemp |  self.hours > self.BASE_HOURS & self.sales > 100: self.salary = round(self.salary * (self.salary / 100))
        else: self.salary = round(self.BASE_HOURS * self.BASE_HOUR_SALARY[self.job])
class Marketer(Employee):
    PROJECTS_PERCENT = 15
    def __init__(self, person, region, sales, hours, projectBudjet, isTemp):
        super().__init__(person, region, sales)
        self.hours = hours
        self.isTemp = isTemp
        if not self.isTemp |  self.hours > self.BASE_HOURS & self.sales > 100: self.salary = round(self.salary * (self.salary / 100))
        else: self.salary = round(self.BASE_HOURS * self.BASE_HOUR_SALARY[self.job])
        self.salary += projectBudjet * self.PROJECTS_PERCENT


def getPerson():
    person = input('Выберите должность (Manager Developer Marketer): ').lower()
    region = input('Выберите регион (Moscow | Peter | Other): ').lower()
    return {"person": person, "region": region}

def getPeople(personObj):
    if personObj["person"] == 'manager':
        return Manager(personObj["person"], personObj["region"], 250)
    if personObj["person"] == 'developer':
        return Developer(personObj["person"], personObj["region"], 250, 15, bool(1))
    if personObj["person"] == 'marketer':
        return Marketer(personObj["person"], personObj["region"], 150, 14, 750000, bool(0))

    print('Вы выбрали неверный вариант')
    return 0

manager = Manager('manager', 'moscow', 250)
marketer = Marketer('marketer', 'peter', 150, 14, 750000, bool(0))
dev = Developer('developer', 'other', 250, 15, bool(1))

person = getPeople(getPerson())

print("Зарплата програмно заданного менеджера: ", manager.salary)
print("Зарплата програмно заданного маркетолога: ", marketer.salary)
print("Зарплата програмно заданного прогера: ", dev.salary)
print("Зарплата вашего пользователя: ", person.salary)