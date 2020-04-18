from datetime import date, timedelta


class Employee:
    def __init__(self, name, surname, mail, salary):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.salary = salary

    def work(self):
        return '{} comes to the office!\n'.format(self.name)

    def check_salary(self):
        now = date.today()
        month_start = date(now.year, now.month, 1)
        weekend = [5, 6]
        diff = (now - month_start).days+1
        day_count = 0
        for day in range(diff):
            if(month_start + timedelta(day)).weekday() not in weekend:
                day_count += 1
        return '{} earned {} UAH for {} days.'.format(self.name, day_count * self.salary, day_count)

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __ne__(self, other):
        return self.salary != other.salary


class Recruiter (Employee):
    def __init__(self, name, surname, mail, salary, hired_this_month):
        super().__init__(name, surname, mail, salary)
        self.hired_this_month = hired_this_month

    def work(self):
        recruiter_work = super().work()[:-2]
        return recruiter_work + " and start codding."

    def __str__(self):
        return "{}: {} {}".format(self.__class__.__name__, self.name, self.surname)


class Programmer (Employee):
    def __init__(self, name, surname, mail, salary, tech_stack, closed_this_month):
        super().__init__(name, surname, mail, salary)
        self.tech_stack = tech_stack
        self.closed_this_month = closed_this_month

    def work(self):
        programmer_work = super().work()[:-2]
        return programmer_work + " and start hiring."

    def __str__(self):
        return "{}: {} {}".format(self.__class__.__name__, self.name, self.surname)

    def __lt__(self, other):
        print("LT")
        return len(self.tech_stack) < len(other.tech_stack)

    def __gt__(self, other):
        print("GT")
        return len(self.tech_stack) > len(other.tech_stack)

    def __eq__(self, other):
        print("EQ")
        return len(self.tech_stack) == len(other.tech_stack)

    def __le__(self, other):
        print("LE")
        return len(self.tech_stack) <= len(other.tech_stack)

    def __ge__(self, other):
        print("GE")
        return len(self.tech_stack) >= len(other.tech_stack)

    def __ne__(self, other):
        print("NE")
        return len(self.tech_stack) != len(other.tech_stack)
    
    def alpha_p(self, other):
        for i in self.tech_stack:
            if i not in other.tech_stack:
                other.tech_stack.append(i)
        return 'Alpha-programmer`s tech stack: {}.\n' \
               'Alpha-programmer closed this month: {}.'\
            .format(other.tech_stack, self.closed_this_month + other.closed_this_month)


person1 = Programmer("Ivan", "Ivanov", "Ivanov@gmail.com", 450, ["python", "C", "C++", "Java"], 5)
person2 = Programmer("Semen", "Semenov", "Semenov@gmail.com", 500, ["Ruby", "PHP", "Java"], 8)
person3 = Recruiter("Petr", "Petrov", "Petrov@gmail.com", 250, 10)
person4 = Recruiter("Daniil", "Daniilov", "Daniilov@gmail.com", 300, 15)
