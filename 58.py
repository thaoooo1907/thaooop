# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:37:56 2024

@author: ADMIN
"""

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_monthly_salary(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def __str__(self):
        return f"Mã NV: {self.emp_id}, Họ tên: {self.name}, Lương cơ bản: {self.basic_salary}, Lương hằng tháng: {self.calculate_monthly_salary()}"


class OfficeEmployee(Employee):
    def __init__(self, emp_id, name, basic_salary, working_days):
        super().__init__(emp_id, name, basic_salary)
        self.working_days = working_days

    def calculate_monthly_salary(self):
        return self.basic_salary + self.working_days * 150000


class SalesEmployee(Employee):
    def __init__(self, emp_id, name, basic_salary, products_sold):
        super().__init__(emp_id, name, basic_salary)
        self.products_sold = products_sold

    def calculate_monthly_salary(self):
        return self.basic_salary + self.products_sold * 18000


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        if len(self.employees) < 300:
            self.employees.append(employee)

    def display_employees(self):
        for emp in self.employees:
            print(emp)

    def find_employee_by_id(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    def get_highest_salary_employee(self):
        if not self.employees:
            return None
        return max(self.employees, key=lambda emp: emp.calculate_monthly_salary())

    def get_lowest_sales_employee(self):
        sales_employees = [emp for emp in self.employees if isinstance(emp, SalesEmployee)]
        if not sales_employees:
            return None
        return min(sales_employees, key=lambda emp: emp.calculate_monthly_salary())
if __name__ == "__main__":
    manager = EmployeeManager()

    manager.add_employee(OfficeEmployee("NV001", "Nguyen Van A", 5000000, 20))
    manager.add_employee(SalesEmployee("NV002", "Tran Thi B", 4000000, 50))
    manager.add_employee(OfficeEmployee("NV003", "Le Van C", 6000000, 22))
    manager.add_employee(SalesEmployee("NV004", "Pham Thi D", 4500000, 30))
    manager.add_employee(SalesEmployee("NV005", "Vo Van E", 4800000, 10))
    print("Danh sách nhân viên:")
    manager.display_employees()
    print("\nTìm nhân viên theo mã 'NV002':")
    employee = manager.find_employee_by_id('NV002')
    if employee:
        print(employee)
    else:
        print("Không tìm thấy nhân viên.")

    print("\nNhân viên có lương hằng tháng cao nhất:")
    highest_salary_employee = manager.get_highest_salary_employee()
    if highest_salary_employee:
        print(highest_salary_employee)
    print("\nNhân viên bán hàng có lương hằng tháng thấp nhất:")
    lowest_sales_employee = manager.get_lowest_sales_employee()
    if lowest_sales_employee:
        print(lowest_sales_employee)
