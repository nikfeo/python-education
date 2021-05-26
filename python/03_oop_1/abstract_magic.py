from abc import ABC, abstractmethod


class Builder(ABC):
    devices = []
    speciality = None

    def __init__(self, name: str, salary: int, experience: str):
        self.name = name
        self.salary = salary
        self.experience = experience

    def __len__(self):
        return len(self.devices)

    @abstractmethod
    def do_work(self):
        ...

    @abstractmethod
    def drink(self):
        print('Drink vodka')

    @abstractmethod
    def calculate_estimate(self):
        print('Make an estimate and multiply by three')


class Plumber(Builder):

    def __init__(self, name: str, salary: int, experience: str):
        super().__init__(name, salary, experience)
        self.speciality = 'Plumber'

    def do_work(self):
        print(f'{self.speciality} {self.name} laid and connected sewer and water pipes')

    def drink(self):
        print(f'{self.speciality}s usually drink vodka very hard')

    def calculate_estimate(self):
        super().calculate_estimate()


class Electrician(Builder):

    def __init__(self, name: str, salary: int, experience: str):
        super().__init__(name, salary, experience)
        self.speciality = 'Electrician'

    def do_work(self):
        print(f'{self.speciality} {self.name} made electrical wiring and connect lamps')

    def drink(self):
        print(f'{self.speciality}s do not drink alcohol, electric shock is not a joke')

    def calculate_estimate(self):
        super().calculate_estimate()


class Handyman(Builder):
    devices = ['saw', 'hummer']

    def __init__(self, name: str, salary: int, experience: str):
        super().__init__(name, salary, experience)
        self.speciality = 'Handyman'

    def calculate_estimate(self):
        print('I have no idea how to make an estimate')

    def drink(self):
        super().drink()

    def do_work(self):
        super().do_work()


class Foreman(Builder):
    new_brigade = {}

    def __init__(self, name: str, salary: int, experience: str):
        super().__init__(name, salary, experience)
        self.speciality = 'Foreman'

    def __getitem__(self, spec_name: str):
        return f'{spec_name} is {self.new_brigade[spec_name]} in {self.name}\'s brigade'

    def __delitem__(self, spec_name: str):
        del self.new_brigade[spec_name]
        print(f'{spec_name} was fired')

    def show_available_specialists(self):
        for key in self.new_brigade:
            print(f'{key} ---> {self.new_brigade[key]}')

    def do_work(self):
        print('Builds anything, just not with his own hands')

    def drink(self):
        print(f'{self.speciality}s drinks cognac, because they can')

    def hire_specialist(self, specialist_obj: Builder):
        self.new_brigade[specialist_obj.name] = specialist_obj.speciality

    def calculate_estimate(self):
        print('Make an estimate and multiply by three, than add 20%')


if __name__ == "__main__":

    alex_foreman = Foreman('Sasha', 1500, '10 years')
    stas_electr = Electrician('Stas', 1000, '3 years')
    andrew_plumber = Plumber('Andrew', 800, '5 years')
    kostya_handy = Handyman('Kostya', 300, '1 year')

    alex_foreman.hire_specialist(stas_electr)
    alex_foreman.hire_specialist(andrew_plumber)
    alex_foreman.hire_specialist(kostya_handy)
    print(f'{kostya_handy.speciality} {kostya_handy.name} has {len(kostya_handy)} devices')
    print(alex_foreman.new_brigade)

    print(alex_foreman['Stas'])
    del alex_foreman['Stas']
    print(alex_foreman.new_brigade)
    alex_foreman.show_available_specialists()
