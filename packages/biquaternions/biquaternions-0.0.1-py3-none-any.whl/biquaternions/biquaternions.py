import numpy
import pyquaternion
from pyquaternion import Quaternion
from dataclasses import dataclass

@dataclass
class dual_Num: # <--- Класс дуальных чисел
    polar = False  
    def __init__(self, *args, **kwargs): # <--- конструктор класса (мы можем по разному передавать значения)
        if len(args) == 1: # <--- если передан массив из пары чисел
            x = args
            self.a = x[0][0]
            self.b = x[0][1]
        else: 
            if ('r' in kwargs) and ('phi' in kwargs):
                x,y = kwargs.get('r'), kwargs.get('phi')
                self.r = x
                self.phi = y
                self.a = self.r
                self.b = self.phi*self.r
                self.polar = True
            else: # <--- если переданы 2 числа
                x,y = args
                self.a = x
                self.b = y     
                         
    def __abs__(self): # <--- перегрузка оператора abs: abs(a)
        return abs(self.a)
    
    def __neg__(self): # <--- перегрузка оператора - : -a 
        return dual_Num(-self.a, -self.b)
    
    def inv(self): # <--- сопряженное дуальное число
        return dual_Num(self.a, -self.b)   
    
    def __add__(self, b): # <--- перегрузка оператора +
        if type(b) is dual_Num:
            return dual_Num(self.a+b.a, self.b+b.b)
        else:
            return dual_Num(self.a+b, self.b) 
        
    def __sub__(self, b): # <--- перегрузка оператора -
        if type(b) is dual_Num:
            return dual_Num(self.a-b.a, self.b-b.b)
        else:
            return dual_Num(self.a-b, self.b) 
        
    def __mul__(self, b): # <--- перегрузка оператора *
        if type(b) is dual_Num and type(self) is dual_Num:
            return dual_Num(self.a*b.a, self.a*b.b + self.b*b.a)
        if isinstance(b, (int, float, numpy.float64)):
            return dual_Num(self.a*b, self.b*b)
        if isinstance(self, (int, float, numpy.float64)):
            return dual_Num(b.a*self, b.b*self)           
            
    def __str__(self): # <--- перегрузка оператора str для вывода
        if self.polar == False:
            if isinstance(self.a, (int, float, numpy.float64)):
                if self.b == 0.0:
                    return str(self.a)
                if self.b > 0.0:
                    return '{}+s*{}'.format(self.a, self.b)
                if self.b < 0.0:
                    return '{}-s*{}'.format(self.a, abs(self.b))
            else:
                return '({})+s*({})'.format(self.a, self.b)
        if self.polar == True:
            if self.r == 0:
                return str(0)
            if self.r == 1:
                return '1+s*{}'.format(self.phi)
            if self.r!=0:
                return '{}(1+s*{})'.format(self.r, self.phi)
            
    def __pow__(self, y): # <--- перегрузка оператора ** : a**n
        return dual_Num(self.a**y, y*self.a**(y-1)*self.b)
    
    def __iadd__(self, b): # <--- перегрузка оператора +=
        if type(b) is dual_Num:
            return dual_Num(self.a+b.a, self.b+b.b)
        else:
            return dual_Num(self.a+b, self.b)
        
    def __isub__(self, b): # <--- перегрузка оператора -=
        if type(b) is dual_Num:
            return dual_Num(self.a-b.a, self.b-b.b)
        else: 
            return dual_Num(self.a-b, self.b)
        
    def __imul__(self, b): # <--- перегрузка оператора *=
        if type(b) is dual_Num:
            return dual_Num(self.a*b.a, self.a*b.b + self.b*b.a)
        else:
            return dual_Num(self.a*b, self.b*b) 
        
    def __truediv__(self, b): # <--- перегрузка оператора /
        if type(b) is dual_Num:
            if b.a == 0:
                print("Нельзя")
                return False
            return dual_Num((self.a/b.a),((-self.a*b.b + self.b*b.a)/b.a**2))
        else:
            return dual_Num(self.a/b, self.b/b)
    def __itruediv__(self, b): # <--- перегрузка оператора /=
        if type(b) is dual_Num:
            if b.a == 0:
                print("Нельзя")
                return False
            return dual_Num((self.a/b.a),((-self.a*b.b + self.b*b.a)/b.a**2))
        else:
            return dual_Num(self.a/b, self.b/b)
    def __getitem__(self, i): # <--- перегрузка оператора [] a[]
            if i == 0:
                return self.a
            if i == 1:
                return self.b
@dataclass
class dual_Quaternion(dual_Num): # <--- Класс дуальных кватернионов
    def __init__(self, *args, **kwargs): # <--- конструктор класса (мы можем передавать значения как ввиде пары кватернионов так и ввиде 4 дуальных чисел)
        if len(args)==4:
            _a,_b,_c,_d = args
            self.q = [_a,_b,_c,_d]
            self.a = _a
            self.b = _b
            self.c = _c
            self.d = _d
        
        if len(args)==2:
            l_1, l_2 = args
            self.q = [l_1, l_2]
            self.a = l_1
            self.b = l_2
            
    def __str__(self): # <--- перегрузка оператора str для вывода
        if len(self.q) == 4:
            return '({})+({})*i+({})*j+({})*k'.format(self.a, self.b, self.c, self.d)
        if len(self.q) == 2:
            return '({})+s({})'.format(self.a, self.b)
        
    def __sub__(self, b): # <--- перегрузка оператора -
        if type(b) is dual_Quaternion:
            if len(self.q) == 4:
                return dual_Quaternion(self.a-b.a, self.b-b.b, self.c-b.c, self.d-b.d)
            if len(self.q) == 2:
                return dual_Quaternion(self.a-b.a, self.b-b.b)
        elif type(b) is dual_Num:
            if len(self.q) == 4:
                return dual_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return dual_Quaternion(self.a-b.a, self.b-b.b)
        else:
            if len(self.q) == 4:
                return dual_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return dual_Quaternion(self.a-b, self.b)
            
    def __isub__(self, b): # <--- перегрузка оператора -=
        if type(b) is dual_Quaternion:
            if len(self.q) == 4:
                return dual_Quaternion(self.a-b.a, self.b-b.b, self.c-b.c, self.d-b.d)
            if len(self.q) == 2:
                return dual_Quaternion(self.a-b.a, self.b-b.b)
        elif type(b) is dual_Num:
            if len(self.q) == 4:
                return dual_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return dual_Quaternion(self.a-b.a, self.b-b.b)
        else:
            if len(self.q) == 4:
                return dual_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return dual_Quaternion(self.a-b, self.b)
            
    def __add__(self, b): # <--- перегрузка оператора +
        if type(self) is dual_Quaternion and type(b) is dual_Quaternion:
            if len(self.q) == 4:
                return dual_Quaternion(self.a+b.a, self.b+b.b, self.c+b.c, self.d+b.d)
            if len(self.q) == 2:
                return dual_Quaternion(self.a+b.a, self.b+b.b)
        if type(b) is dual_Num:
            if len(self.q) == 4:
                return dual_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return dual_Quaternion(self.a+b.a, self.b+b.b)
        if type(self) is dual_Num:
            if len(b.q) == 4:
                return dual_Quaternion(b.a+self, b.b, b.c, b.d)
            if len(b.q) == 2:
                return dual_Quaternion(b.a+self.a, b.b+self.b)      
        if type(self) is dual_Quaternion:
            if len(self.q) == 4:
                return dual_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return dual_Quaternion(self.a+b, self.b)
        if type(b) is dual_Quaternion:
            if len(b.q) == 4:
                return dual_Quaternion(b.a+self, b.b, b.c, b.d)
            if len(b.q) == 2:
                return dual_Quaternion(b.a+self, b.b)
            
    def __iadd__(self, b): # <--- перегрузка оператора +=
        if type(b) is dual_Quaternion:
            if len(self.q) == 4:
                return dual_Quaternion(self.a+b.a, self.b+b.b, self.c+b.c, self.d+b.d)
            if len(self.q) == 2:
                return dual_Quaternion(self.a+b.a, self.b+b.b)
        elif type(b) is dual_Num:
            if len(self.q) == 4:
                return dual_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return dual_Quaternion(self.a+b.a, self.b+b.b)
        else:
            if len(self.q) == 4:
                return dual_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return dual_Quaternion(self.a+b, self.b)
            
    def __mul__(self, b):# <--- перегрузка оператора *
        if type(self) is dual_Quaternion and type(b) is dual_Quaternion:
            if type(b) is dual_Quaternion:
                if len(self.q) == 2 and len(b.q)==2:
                    return dual_Quaternion(self.a*b.a, self.a*b.b + self.b*b.a)
                if len(self.q) == 4 and len(b.q)==4:
                    _a = self.a
                    _b = self.b
                    _c = self.c
                    _d = self.d
                    return dual_Quaternion(-b.b * _b - b.c * _c - b.d * _d + b.a * _a,
                     b.b * _a + b.c * _d + b.d * _c - b.a * _b,
                     b.b * _d - b.c * _a + b.d * _b + b.a *_c,
                     -b.b * _c + b.c * _b + b.d * _a + b.a *_d)
                else:
                    print('Приведите к единому типу')    
                    return self
        if type(self) is dual_Quaternion:
                if len(self.q) == 2:
                    return dual_Quaternion(b*self.a, b*self.b)
                if len(self.q) == 4:
                    _a = self.a
                    _b = self.b
                    _c = self.c
                    _d = self.d
                    _a*=b
                    _b*=b
                    _c*=b
                    _d*=b
                    return dual_Quaternion(_a, _b, _c, _d) 
        if type(b) is dual_Quaternion:
                if len(b.q) == 2:
                    return dual_Quaternion(self*b.a, self*b.b)
                if len(b.q) == 4:
                    b.a*=self
                    b.b*=self
                    b.c*=self
                    b.d*=self
                    return dual_Quaternion(b.a, b.b, b.c, b.d)  
              
    def __imul__(self, b): # <--- перегрузка оператора *=
        if type(b) is dual_Quaternion:
            if len(self.q) == 2 and len(b.q)==2:
                return dual_Quaternion(self.a*b.a, self.a*b.b + self.b*b.a)
            elif len(self.q) == 4 and len(b.q)==4:
                return dual_Quaternion(-b.b * self.b - b.c * self.c - b.d * self.d + b.a * self.a,
                     b.b * self.a + b.c * self.d - b.d * self.c + b.a * self.b,
                     -b.b * self.d + b.c * self.a + b.d * self.b + b.a *self.c,
                     b.b * self.c - b.c * self.b + b.d * self.a + b.a *self.d)
            else:
                print('Приведите к единому типу')    
                return self
        else:
            if len(self.q) == 2:
                return dual_Quaternion(b*self.a, b*self.b)
            if len(self.q) == 4:
                return dual_Quaternion(b*self.a, b*self.b, b*self.c, b*self.d)
            
    def to_quaternions(self): # <--- перевод в кватернионы 
        _a = Quaternion(self.a.a, self.b.a, self.c.a, self.d.a)
        _b = Quaternion(self.a.b, self.b.b, self.c.b, self.d.b)
        return dual_Quaternion(_a, _b)
    
    def to_dual_num(self): # <--- перевод в дуальные числа из пары кватернионов
        _a = dual_Num(self.a[0], self.b[0])
        _b = dual_Num(self.a[1], self.b[1])
        _c = dual_Num(self.a[2], self.b[2])
        _d = dual_Num(self.a[3], self.b[3])
        return dual_Quaternion(_a, _b, _c, _d)
    
    def __neq__(self): # <--- перегрузка оператора - : -a
        if self.q == 2:
            return dual_Quaternion(-self.a, -self.b)
        
    def inv(self): # <--- сопряженный элемент
        if len(self.q) == 2:
            return dual_Quaternion(self.a.conjugate, self.b.conjugate)
        if len(self.q) == 4:
            return dual_Quaternion(self.a.inv(), self.b.inv(), self.c.inv(), self.d.inv())
        
    def __abs__(self): # <--- перегрузка оператора модуля abs(a)
        if len(self.q) == 2:
            return dual_Num((self*self.inv()).a[0], (self*self.inv()).b[0])
        if len(self.q) == 4:
            t = self
            t = t.to_quaternions()
            return dual_Num((t*t.inv()).a[0], (t*t.inv()).b[0]) 
        
    def __getitem__(self, i): # <--- перегрузка оператора [] a[]
        if len(self.q) == 2:
            if i == 0:
                return self.a
            if i == 1:
                return self.b
        if len(self.q) == 4:
            if i == 0:
                return self.a
            if i == 1:
                return self.b
            if i == 2:
                return self.c
            if i == 3:
                return self.d

@dataclass
class ordinary_Quaternion: # <--- Класс ординарных кватернионов
    def __init__(self, *args, **kwargs): # <--- конструктор класса (мы можем передавать значения как ввиде пары кватернионов так и ввиде 4 дуальных чисел)
        if len(args)==4:
            _a,_b,_c,_d = args
            self.q = [_a,_b,_c,_d]
            self.a = _a
            self.b = _b
            self.c = _c
            self.d = _d
        
        if len(args)==2:
            l_1, l_2 = args
            self.q = [l_1, l_2]
            self.a = l_1
            self.b = l_2
            
    def __str__(self): # <--- перегрузка оператора str для вывода
        if len(self.q) == 4:
            return '({})+({})*i+({})*j+({})*k'.format(self.a, self.b, self.c, self.d)
        if len(self.q) == 2:
            return '({})+s({})'.format(self.a, self.b)
        
    def __sub__(self, b): # <--- перегрузка оператора -
        if type(b) is ordinary_Quaternion:
            if len(self.q) == 4:
                return ordinary_Quaternion(self.a-b.a, self.b-b.b, self.c-b.c, self.d-b.d)
            if len(self.q) == 2:
                return ordinary_Quaternion(self.a-b.a, self.b-b.b)
        elif type(b) is complex:
            if len(self.q) == 4:
                return ordinary_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return ordinary_Quaternion(self.a-b.a, self.b-b.b)
        else:
            if len(self.q) == 4:
                return ordinary_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return ordinary_Quaternion(self.a-b, self.b)
            
    def __isub__(self, b): # <--- перегрузка оператора -=
        if type(b) is ordinary_Quaternion:
            if len(self.q) == 4:
                return ordinary_Quaternion(self.a-b.a, self.b-b.b, self.c-b.c, self.d-b.d)
            if len(self.q) == 2:
                return ordinary_Quaternion(self.a-b.a, self.b-b.b)
        elif type(b) is complex:
            if len(self.q) == 4:
                return ordinary_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return ordinary_Quaternion(self.a-b.a, self.b-b.b)
        else:
            if len(self.q) == 4:
                return ordinary_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return ordinary_Quaternion(self.a-b, self.b)
            
    def __add__(self, b): # <--- перегрузка оператора +
        if type(self) is ordinary_Quaternion and type(b) is ordinary_Quaternion:
            if len(self.q) == 4:
                return ordinary_Quaternion(self.a+b.a, self.b+b.b, self.c+b.c, self.d+b.d)
            if len(self.q) == 2:
                return ordinary_Quaternion(self.a+b.a, self.b+b.b)
        if type(b) is complex:
            if len(self.q) == 4:
                return ordinary_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return ordinary_Quaternion(self.a+b.a, self.b+b.b)
        if type(self) is complex:
            if len(b.q) == 4:
                return ordinary_Quaternion(b.a+self, b.b, b.c, b.d)
            if len(b.q) == 2:
                return ordinary_Quaternion(b.a+self.a, b.b+self.b)      
        if type(self) is ordinary_Quaternion:
            if len(self.q) == 4:
                return ordinary_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return ordinary_Quaternion(self.a+b, self.b)
        if type(b) is ordinary_Quaternion:
            if len(b.q) == 4:
                return ordinary_Quaternion(b.a+self, b.b, b.c, b.d)
            if len(b.q) == 2:
                return ordinary_Quaternion(b.a+self, b.b)
            
    def __iadd__(self, b): # <--- перегрузка оператора +=
        if type(b) is ordinary_Quaternion:
            if len(self.q) == 4:
                return ordinary_Quaternion(self.a+b.a, self.b+b.b, self.c+b.c, self.d+b.d)
            if len(self.q) == 2:
                return ordinary_Quaternion(self.a+b.a, self.b+b.b)
        elif type(b) is complex:
            if len(self.q) == 4:
                return ordinary_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return ordinary_Quaternion(self.a+b.a, self.b+b.b)
        else:
            if len(self.q) == 4:
                return ordinary_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return ordinary_Quaternion(self.a+b, self.b)
            
    def __mul__(self, b):# <--- перегрузка оператора *
        if type(self) is ordinary_Quaternion and type(b) is ordinary_Quaternion:
            if type(b) is ordinary_Quaternion:
                if len(self.q) == 2 and len(b.q)==2:
                    return ordinary_Quaternion(self.a*b.a, self.a*b.b + self.b*b.a)
                if len(self.q) == 4 and len(b.q)==4:
                    _a = self.a
                    _b = self.b
                    _c = self.c
                    _d = self.d
                    return ordinary_Quaternion(-b.b * _b - b.c * _c - b.d * _d + b.a * _a,
                     b.b * _a + b.c * _d + b.d * _c - b.a * _b,
                     b.b * _d - b.c * _a + b.d * _b + b.a *_c,
                     -b.b * _c + b.c * _b + b.d * _a + b.a *_d)
                else:
                    print('Приведите к единому типу')    
                    return self
        if type(self) is ordinary_Quaternion:
                if len(self.q) == 2:
                    return ordinary_Quaternion(b*self.a, b*self.b)
                if len(self.q) == 4:
                    _a = self.a
                    _b = self.b
                    _c = self.c
                    _d = self.d
                    _a*=b
                    _b*=b
                    _c*=b
                    _d*=b
                    return ordinary_Quaternion(_a, _b, _c, _d) 
        if type(b) is ordinary_Quaternion:
                if len(b.q) == 2:
                    return ordinary_Quaternion(self*b.a, self*b.b)
                if len(b.q) == 4:
                    b.a*=self
                    b.b*=self
                    b.c*=self
                    b.d*=self
                    return ordinary_Quaternion(b.a, b.b, b.c, b.d)  
              
    def __imul__(self, b): # <--- перегрузка оператора *=
        if type(b) is ordinary_Quaternion:
            if len(self.q) == 2 and len(b.q)==2:
                return ordinary_Quaternion(self.a*b.a, self.a*b.b + self.b*b.a)
            elif len(self.q) == 4 and len(b.q)==4:
                return ordinary_Quaternion(-b.b * self.b - b.c * self.c - b.d * self.d + b.a * self.a,
                     b.b * self.a + b.c * self.d - b.d * self.c + b.a * self.b,
                     -b.b * self.d + b.c * self.a + b.d * self.b + b.a *self.c,
                     b.b * self.c - b.c * self.b + b.d * self.a + b.a *self.d)
            else:
                print('Приведите к единому типу')    
                return self
        else:
            if len(self.q) == 2:
                return ordinary_Quaternion(b*self.a, b*self.b)
            if len(self.q) == 4:
                return ordinary_Quaternion(b*self.a, b*self.b, b*self.c, b*self.d)
            
    def to_quaternions(self): # <--- перевод в кватернионы 
        _a = Quaternion(self.a.a, self.b.a, self.c.a, self.d.a)
        _b = Quaternion(self.a.b, self.b.b, self.c.b, self.d.b)
        return ordinary_Quaternion(_a, _b)
    
    def to_complex(self): # <--- перевод в дуальные числа из пары кватернионов
        _a = complex(self.a[0], self.b[0])
        _b = complex(self.a[1], self.b[1])
        _c = complex(self.a[2], self.b[2])
        _d = complex(self.a[3], self.b[3])
        return ordinary_Quaternion(_a, _b, _c, _d)
    
    def __neq__(self): # <--- перегрузка оператора - : -a
        if self.q == 2:
            return ordinary_Quaternion(-self.a, -self.b)
        
    def inv(self): # <--- сопряженный элемент
        if len(self.q) == 2:
            return ordinary_Quaternion(self.a.conjugate, self.b.conjugate)
        if len(self.q) == 4:
            return ordinary_Quaternion(self.a.inv(), self.b.inv(), self.c.inv(), self.d.inv())
        
    def __abs__(self): # <--- перегрузка оператора модуля abs(a)
        if len(self.q) == 2:
            return complex((self*self.inv()).a[0], (self*self.inv()).b[0])
        if len(self.q) == 4:
            t = self
            t = t.to_quaternions()
            return complex((t*t.inv()).a[0], (t*t.inv()).b[0]) 
        
    def __getitem__(self, i): # <--- перегрузка оператора [] a[]
        if len(self.q) == 2:
            if i == 0:
                return self.a
            if i == 1:
                return self.b
        if len(self.q) == 4:
            if i == 0:
                return self.a
            if i == 1:
                return self.b
            if i == 2:
                return self.c
            if i == 3:
                return self.d

@dataclass
class hyperbolic_Num: # <--- Класс дуальных чисел
    polar = False  
    def __init__(self, *args, **kwargs): # <--- конструктор класса (мы можем по разному передавать значения)
        if len(args) == 1: # <--- если передан массив из пары чисел
            x = args
            self.a = x[0][0]
            self.b = x[0][1]
        else: 
            if ('r' in kwargs) and ('phi' in kwargs):
                x,y = kwargs.get('r'), kwargs.get('phi')
                self.r = x
                self.phi = y
                self.a = self.r
                self.b = self.phi*self.r
                self.polar = True
            else: # <--- если переданы 2 числа
                x,y = args
                self.a = x
                self.b = y     
                         
    def __abs__(self): # <--- перегрузка оператора abs: abs(a)
        return abs(self.a)
    
    def __neg__(self): # <--- перегрузка оператора - : -a 
        return hyperbolic_Num(-self.a, -self.b)
    
    def inv(self): # <--- сопряженное дуальное число
        return hyperbolic_Num(self.a, -self.b)   
    
    def __add__(self, b): # <--- перегрузка оператора +
        if type(b) is hyperbolic_Num:
            return hyperbolic_Num(self.a+b.a, self.b+b.b)
        else:
            return hyperbolic_Num(self.a+b, self.b) 
        
    def __sub__(self, b): # <--- перегрузка оператора -
        if type(b) is hyperbolic_Num:
            return hyperbolic_Num(self.a-b.a, self.b-b.b)
        else:
            return hyperbolic_Num(self.a-b, self.b) 
        
    def __mul__(self, b): # <--- перегрузка оператора *
        if type(b) is hyperbolic_Num and type(self) is hyperbolic_Num:
            return hyperbolic_Num(self.a*b.a+self.b*b.b, self.a*b.b + self.b*b.a)
        if isinstance(b, (int, float, numpy.float64)):
            return hyperbolic_Num(self.a*b, self.b*b)
        if isinstance(self, (int, float, numpy.float64)):
            return hyperbolic_Num(b.a*self, b.b*self)           
            
    def __str__(self): # <--- перегрузка оператора str для вывода
        if self.polar == False:
            if isinstance(self.a, (int, float, numpy.float64)):
                if self.b == 0.0:
                    return str(self.a)
                if self.b > 0.0:
                    return '{}+s*{}'.format(self.a, self.b)
                if self.b < 0.0:
                    return '{}-s*{}'.format(self.a, abs(self.b))
            else:
                return '({})+s*({})'.format(self.a, self.b)
        if self.polar == True:
            if self.r == 0:
                return str(0)
            if self.r == 1:
                return '1+s*{}'.format(self.phi)
            if self.r!=0:
                return '{}(1+s*{})'.format(self.r, self.phi)
            
    def __pow__(self, y): # <--- перегрузка оператора ** : a**n
        return hyperbolic_Num(self.a**y, y*self.a**(y-1)*self.b)
    
    def __iadd__(self, b): # <--- перегрузка оператора +=
        if type(b) is hyperbolic_Num:
            return hyperbolic_Num(self.a+b.a, self.b+b.b)
        else:
            return hyperbolic_Num(self.a+b, self.b)
        
    def __isub__(self, b): # <--- перегрузка оператора -=
        if type(b) is hyperbolic_Num:
            return hyperbolic_Num(self.a-b.a, self.b-b.b)
        else: 
            return hyperbolic_Num(self.a-b, self.b)
        
    def __imul__(self, b): # <--- перегрузка оператора *=
        if type(b) is hyperbolic_Num:
            return hyperbolic_Num(self.a*b.a, self.a*b.b + self.b*b.a)
        else:
            return hyperbolic_Num(self.a*b, self.b*b) 
        
    def __truediv__(self, b): # <--- перегрузка оператора /
        if type(b) is hyperbolic_Num:
            if b.a == 0:
                print("Нельзя")
                return False
            return hyperbolic_Num((self.a/b.a),((-self.a*b.b + self.b*b.a)/b.a**2))
        else:
            return hyperbolic_Num(self.a/b, self.b/b)
    def __itruediv__(self, b): # <--- перегрузка оператора /=
        if type(b) is hyperbolic_Num:
            if b.a == 0:
                print("Нельзя")
                return False
            return hyperbolic_Num((self.a/b.a),((-self.a*b.b + self.b*b.a)/b.a**2))
        else:
            return hyperbolic_Num(self.a/b, self.b/b)
    def __getitem__(self, i): # <--- перегрузка оператора [] a[]
            if i == 0:
                return self.a
            if i == 1:
                return self.b

@dataclass
class hyperbolic_Quaternion: # <--- Класс дуальных кватернионов
    def __init__(self, *args, **kwargs): # <--- конструктор класса (мы можем передавать значения как ввиде пары кватернионов так и ввиде 4 дуальных чисел)
        if len(args)==4:
            _a,_b,_c,_d = args
            self.q = [_a,_b,_c,_d]
            self.a = _a
            self.b = _b
            self.c = _c
            self.d = _d
        
        if len(args)==2:
            l_1, l_2 = args
            self.q = [l_1, l_2]
            self.a = l_1
            self.b = l_2
            
    def __str__(self): # <--- перегрузка оператора str для вывода
        if len(self.q) == 4:
            return '({})+({})*i+({})*j+({})*k'.format(self.a, self.b, self.c, self.d)
        if len(self.q) == 2:
            return '({})+s({})'.format(self.a, self.b)
        
    def __sub__(self, b): # <--- перегрузка оператора -
        if type(b) is hyperbolic_Quaternion:
            if len(self.q) == 4:
                return hyperbolic_Quaternion(self.a-b.a, self.b-b.b, self.c-b.c, self.d-b.d)
            if len(self.q) == 2:
                return hyperbolic_Quaternion(self.a-b.a, self.b-b.b)
        elif type(b) is hyperbolic_Num:
            if len(self.q) == 4:
                return hyperbolic_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return hyperbolic_Quaternion(self.a-b.a, self.b-b.b)
        else:
            if len(self.q) == 4:
                return hyperbolic_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return hyperbolic_Quaternion(self.a-b, self.b)
            
    def __isub__(self, b): # <--- перегрузка оператора -=
        if type(b) is hyperbolic_Quaternion:
            if len(self.q) == 4:
                return hyperbolic_Quaternion(self.a-b.a, self.b-b.b, self.c-b.c, self.d-b.d)
            if len(self.q) == 2:
                return hyperbolic_Quaternion(self.a-b.a, self.b-b.b)
        elif type(b) is hyperbolic_Num:
            if len(self.q) == 4:
                return hyperbolic_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return hyperbolic_Quaternion(self.a-b.a, self.b-b.b)
        else:
            if len(self.q) == 4:
                return hyperbolic_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return hyperbolic_Quaternion(self.a-b, self.b)
            
    def __add__(self, b): # <--- перегрузка оператора +
        if type(self) is hyperbolic_Quaternion and type(b) is hyperbolic_Quaternion:
            if len(self.q) == 4:
                return hyperbolic_Quaternion(self.a+b.a, self.b+b.b, self.c+b.c, self.d+b.d)
            if len(self.q) == 2:
                return hyperbolic_Quaternion(self.a+b.a, self.b+b.b)
        if type(b) is hyperbolic_Num:
            if len(self.q) == 4:
                return hyperbolic_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return hyperbolic_Quaternion(self.a+b.a, self.b+b.b)
        if type(self) is hyperbolic_Num:
            if len(b.q) == 4:
                return hyperbolic_Quaternion(b.a+self, b.b, b.c, b.d)
            if len(b.q) == 2:
                return hyperbolic_Quaternion(b.a+self.a, b.b+self.b)      
        if type(self) is hyperbolic_Quaternion:
            if len(self.q) == 4:
                return hyperbolic_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return hyperbolic_Quaternion(self.a+b, self.b)
        if type(b) is hyperbolic_Quaternion:
            if len(b.q) == 4:
                return hyperbolic_Quaternion(b.a+self, b.b, b.c, b.d)
            if len(b.q) == 2:
                return hyperbolic_Quaternion(b.a+self, b.b)
            
    def __iadd__(self, b): # <--- перегрузка оператора +=
        if type(b) is hyperbolic_Quaternion:
            if len(self.q) == 4:
                return hyperbolic_Quaternion(self.a+b.a, self.b+b.b, self.c+b.c, self.d+b.d)
            if len(self.q) == 2:
                return hyperbolic_Quaternion(self.a+b.a, self.b+b.b)
        elif type(b) is hyperbolic_Num:
            if len(self.q) == 4:
                return hyperbolic_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return hyperbolic_Quaternion(self.a+b.a, self.b+b.b)
        else:
            if len(self.q) == 4:
                return hyperbolic_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return hyperbolic_Quaternion(self.a+b, self.b)
            
    def __mul__(self, b):# <--- перегрузка оператора *
        if type(self) is hyperbolic_Quaternion and type(b) is hyperbolic_Quaternion:
            if type(b) is hyperbolic_Quaternion:
                if len(self.q) == 2 and len(b.q)==2:
                    return hyperbolic_Quaternion(self.a*b.a, self.a*b.b + self.b*b.a)
                if len(self.q) == 4 and len(b.q)==4:
                    _a = self.a
                    _b = self.b
                    _c = self.c
                    _d = self.d
                    return hyperbolic_Quaternion(-b.b * _b - b.c * _c - b.d * _d + b.a * _a,
                     b.b * _a + b.c * _d + b.d * _c - b.a * _b,
                     b.b * _d - b.c * _a + b.d * _b + b.a *_c,
                     -b.b * _c + b.c * _b + b.d * _a + b.a *_d)
                else:
                    print('Приведите к единому типу')    
                    return self
        if type(self) is hyperbolic_Quaternion:
                if len(self.q) == 2:
                    return hyperbolic_Quaternion(b*self.a, b*self.b)
                if len(self.q) == 4:
                    _a = self.a
                    _b = self.b
                    _c = self.c
                    _d = self.d
                    _a*=b
                    _b*=b
                    _c*=b
                    _d*=b
                    return hyperbolic_Quaternion(_a, _b, _c, _d) 
        if type(b) is hyperbolic_Quaternion:
                if len(b.q) == 2:
                    return hyperbolic_Quaternion(self*b.a, self*b.b)
                if len(b.q) == 4:
                    b.a*=self
                    b.b*=self
                    b.c*=self
                    b.d*=self
                    return hyperbolic_Quaternion(b.a, b.b, b.c, b.d)  
              
    def __imul__(self, b): # <--- перегрузка оператора *=
        if type(b) is hyperbolic_Quaternion:
            if len(self.q) == 2 and len(b.q)==2:
                return hyperbolic_Quaternion(self.a*b.a, self.a*b.b + self.b*b.a)
            elif len(self.q) == 4 and len(b.q)==4:
                return hyperbolic_Quaternion(-b.b * self.b - b.c * self.c - b.d * self.d + b.a * self.a,
                     b.b * self.a + b.c * self.d - b.d * self.c + b.a * self.b,
                     -b.b * self.d + b.c * self.a + b.d * self.b + b.a *self.c,
                     b.b * self.c - b.c * self.b + b.d * self.a + b.a *self.d)
            else:
                print('Приведите к единому типу')    
                return self
        else:
            if len(self.q) == 2:
                return hyperbolic_Quaternion(b*self.a, b*self.b)
            if len(self.q) == 4:
                return hyperbolic_Quaternion(b*self.a, b*self.b, b*self.c, b*self.d)
            
    def to_quaternions(self): # <--- перевод в кватернионы 
        _a = Quaternion(self.a.a, self.b.a, self.c.a, self.d.a)
        _b = Quaternion(self.a.b, self.b.b, self.c.b, self.d.b)
        return hyperbolic_Quaternion(_a, _b)
    
    def to_hyperbolic_num(self): # <--- перевод в дуальные числа из пары кватернионов
        _a = hyperbolic_Num(self.a[0], self.b[0])
        _b = hyperbolic_Num(self.a[1], self.b[1])
        _c = hyperbolic_Num(self.a[2], self.b[2])
        _d = hyperbolic_Num(self.a[3], self.b[3])
        return hyperbolic_Quaternion(_a, _b, _c, _d)
    
    def __neq__(self): # <--- перегрузка оператора - : -a
        if self.q == 2:
            return hyperbolic_Quaternion(-self.a, -self.b)
        
    def inv(self): # <--- сопряженный элемент
        if len(self.q) == 2:
            return hyperbolic_Quaternion(self.a.conjugate, self.b.conjugate)
        if len(self.q) == 4:
            return hyperbolic_Quaternion(self.a.inv(), self.b.inv(), self.c.inv(), self.d.inv())
        
    def __abs__(self): # <--- перегрузка оператора модуля abs(a)
        if len(self.q) == 2:
            return hyperbolic_Num((self*self.inv()).a[0], (self*self.inv()).b[0])
        if len(self.q) == 4:
            t = self
            t = t.to_quaternions()
            return hyperbolic_Num((t*t.inv()).a[0], (t*t.inv()).b[0]) 
        
    def __getitem__(self, i): # <--- перегрузка оператора [] a[]
        if len(self.q) == 2:
            if i == 0:
                return self.a
            if i == 1:
                return self.b
        if len(self.q) == 4:
            if i == 0:
                return self.a
            if i == 1:
                return self.b
            if i == 2:
                return self.c
            if i == 3:
                return self.d

a = hyperbolic_Num(1,4)
b = hyperbolic_Num([2,3])
c = hyperbolic_Num(3,2)
d = hyperbolic_Num(4,1)
l1 = Quaternion(1,2,3,4)
l2 = Quaternion(4,3,2,1)
v1 = hyperbolic_Quaternion(l1,l2)
v2 = hyperbolic_Quaternion(l2, l1)


print("v1 = ", v1, "\n", "v2 = ", v2)
print("v1+v2 =", v1+v2)
print("v1*v2 = ", v1*v2)
print("v1*2 = ", v1*2)
print("v1 + ", v1+2)
print("|v1| = ", abs(v1))
v1 = dual_Quaternion(a,b,c,d)
v2 = dual_Quaternion(d,c,b,a)

print(complex(1,1))

print("v1 = ", v1,"\n", "v2 = ", v2)
print("v1+v2 =", v1+v2)
print("v1*v2 = ", v1*v2)
print("v1*2 = ", v1*2)
print("v1 + ", v1+2)
print("|v1| = ", abs(v1))