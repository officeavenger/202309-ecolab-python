
last_id=0

class Employee:
    def __init__(self, name,salary):
        global last_id
        last_id+=1
        self._id=last_id
        self._name=name
        self._salary=salary

    def info(self):
        return f'{type(self).__name__}\tId={self._id}\tName={self._name}\tSalary={self._salary}'
