# class KlasaBazowa:
#     pass
# class KlasaPochodna(KlasaBazowa):
#     pass

# class KontoBankowe:
#     def __init__(self, nazwa, stan=0):
#         self.nazwa = nazwa
#         self.stan = stan
#
#     def info(self):
#         print("nazwa:", self.nazwa)
#         print("stan:", self.stan)
#
#     def wyplac(self, ilosc):
#         self.stan -= ilosc
#
#     def wplac(self, ilosc):
#         self.stan += ilosc
#
#
# class KontoDebetowe(KontoBankowe):
#     def __init__(self, nazwa, stan=0, limit=0):
#         super().__init__(nazwa, stan)
#         self.limit = limit
#
#     def wyplac(self, ilosc):
#         """Jeżeli stan konta po operacji przekroczyłby limit, przerwij."""
#         if (self.stan - ilosc) < (-self.limit):
#             print("Brak srodkow na koncie")
#         else:
#             super().wyplac(ilosc)
#
# account = KontoDebetowe("Jan Nowak", 0, 1000)
# account.info()
# account.wplac(500)
# account.info()
# account.wyplac(2000)
# account.info()

# class A:
#     """Rodzic pierwszy"""
#
#     def __init__(self):
#         super().__init__()
#         self.a = "A"
#
#     def fa(self):
#         print("a:", self.a)
#
#
# class B:
#     """Rodzic drugi"""
#
#     def __init__(self):
#         super().__init__()
#         self.b = "B"
#
#     def fb(self):
#         print("b:", self.b)
#
#
# class Pochodna(B, A):
#     """Dziecko"""
#
#     def __init__(self):
#         super().__init__()

# import math
# class Figura:
#     def obwod(self):  # L
#         """Obliczanie obwodu."""
#         raise NotImplementedError
#
#     def pole(self):  # S/P
#         """Obliczanie pola powierzchni."""
#         raise NotImplementedError
#
# class Circle(Figura):
#     def __init__(self, r):
#         self.r = r
#     def obwod(self):
#         perimeter = round(2*math.pi*self.r, 2)
#         return perimeter
#     def pole(self):
#         area = round(math.pi*self.r**2, 2)
#         return area
# circle1 = Circle(5)
# print('Obwód koła:', circle1.obwod())
# print('Obwód koła:', circle1.pole())
#
# class TriangleEquilateral(Figura):
#     def __init__(self, a):
#         self.a = a
#     def obwod(self):
#         return round(3*self.a, 2)
#     def pole(self):
#         return round((self.a*math.sqrt(3))/4, 2)
#
# t1 = TriangleEquilateral(3.5)
# print('Obwód trójkąta równobocznego:', t1.obwod())
# print('Obwód trójkąta równobocznego:', t1.pole())
#
# class Rectangle(Figura):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def obwod(self):
#         return round(2*(self.a+self.b), 2)
#     def pole(self):
#         return round(self.a * self.b, 2)
# r1 = Rectangle(4,8)
# print('Pole prostokata:', r1.obwod())
# print('Obwód prostokąta:', r1.pole())
#
# class Square(Rectangle):
#     def __init__(self, a):
#         super().__init__(a,a)
#
# sq1 = Square(8)
# print('Obwód kwadratu:', sq1.obwod())
# print('Obwód kwadratu:', sq1.pole())
#
# class Diamond(Figura):
#     def __init__(self, a, b, h):
#         self.a, self.b, self.h = a, b, h
#     def obwod(self):
#         return round((2*self.a) + (2*self.b), 2)
#     def pole(self):
#         return round(self.a*self.h, 2)
# d1 = Diamond(2, 3, 4.5)
# print('Obwód równoległoboku:', d1.obwod())
# print('Pole równoległoboku:', d1.pole())
#
# class Diamond(Rectangle):
#     def __init__(self,a , b, h):
#         Rectangle.__init__(self, a, b)
#         self.h = h
#     def pole(self):
#         return round(self.a*self.h, 2)
#
# d2 = Diamond(2, 3, 4.5)
# print('Obwód równoległoboku:', d2.obwod())
# print('Pole równoległoboku:', d2.pole())
#
# class RectangularTrapezoid(Figura):
#     def __init__(self, a, b, h):
#         self.a, self.b, self.h = a, b, h
#         base = a-b
#         self.c = math.sqrt(h**2+base**2)
#     def obwod(self):
#         return self.a+self.b+self.h+self.c
#     def pole(self):
#         return ((self.a+self.b)/2)*self.h
# rt1 = RectangularTrapezoid(2, 4, 3)
# print('Obwód trapezu prostokątnego:', rt1.obwod())
# print('Pole trapezu prostokątnego:', rt1.pole())


# class Vehicle:
#     color = 'biały,'
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
# class Bus(Vehicle):
#     pass
# class Car(Vehicle):
#     pass
#
# school_bus = Bus('Szkolne Volvo', 180, 12000)
# car1 = Car('Audi Q5', 240, 18000)
# car2 = Car('Mitsubishi Colt', 210, 240000)
# for vehicle in [school_bus, car1, car2]:
#     print('Kolor:',Vehicle.color,'Nazwa pojazdu:', vehicle.name,',', 'Prędkość:', vehicle.max_speed,',', 'Przebieg:', vehicle.mileage)

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#     def fare(self):
#         return super().fare()*1.1
#
# school_bus = Bus("Szkolne Volvo", 12, 50)
# print("Całkowita opłata za przejazd autobusem wynosi:", school_bus.fare())
# # Całkowita opłata za przejazd autobusem wynosi: 5000

class Rectangle:
    def __init__(self, length , width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2*(self.length + self.width)

    def area(self):
        return (self.length * self.width)

    def display(self):
        print(f'Długość: {self.length}, Szerokość: {self.width}, Obwód: {self.perimeter()}, Obszar: {self.area()}')
rectangle1 = Rectangle(10, 20)
rectangle1.display()
class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height
    def volume(self):
            return Rectangle.area(self) * self.height
    def display(self):
            print(f'Długość: {self.length}, Szerokość: {self.width}, Objętość: {self.volume()}')

parallelepipede1 = Parallelepipede(10, 15, 30)
parallelepipede1.display()

