import math
import cmath as m
import tkinter as tk
import copy


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def get(self):
        return self.__x,self.__y
    def set(self,x1):
        self.__x=x1

class Figure:
    def __init__(self, A, B):
        self.x1,self.y1 = copy.deepcopy(A.get())
        self.x2,self.y2 = copy.deepcopy(B.get())

    def draw(self):
        stroka=''
        data = [['⭔'] * 40 for i in range(40)]
        for i in range(40):
            for j in range(40):
                if (i == self.x1 and j == self.y1) or (i == self.x2 and j == self.y2):
                    data[i][j] = '⭓'
        for i in range(len(data)):  # строка
            for j in range(len(data[i])):  # строка
                # print(len(data[i]))
                stroka += data[i][j]
                if j == len(data[i])-1:
                    stroka += '\n'
        for i in range(40):
            for j in range(40):
                print(data[i][j], end='')
            print('')
        return stroka

    def figure_square(self):
         pass

class Rectangle(Figure):
    def __init__(self, A, D):
        self.x1, self.y1 = copy.deepcopy(A.get())
        self.x2, self.y2 = copy.deepcopy(D.get())

    def draw(self):
        stroka=''
        data = [['⭔'] * 40 for i in range(40)]
        for i in range(40):
            for j in range(40):
                if (self.y1 <= i <= self.y2) and (self.x1 <= j <= self.x2):
                    data[i][j] = '⭓'
        for i in range(len(data)):  # строка
            for j in range(len(data[i])):  # строка
                # print(len(data[i]))
                 stroka += data[i][j]
                 if j == len(data[i])-1:
                        stroka += '\n'
        for i in range(40):
            for j in range(40):
                print(data[i][j], end='')
            print('')
        return stroka

    def move_left(self):
        self.x1=self.x1-1
        self.x2=self.x2-1
        self.draw()
    def move_right(self):
        self.x1=self.x1+1
        self.x2=self.x2+1
        self.draw()
    def move_up(self):
        self.y1=self.y1-1
        self.y2=self.y2-1
        self.draw()
    def move_down(self):
        self.y1 = self.y1 + 1
        self.y2 = self.y2+ 1
        self.draw()

    @property
    def figure_square(self):
        a = (self.x2 - self.x1)
        b = (self.y2 - self.y1)
        return a * b


class Triangle(Figure):
    def __init__(self, A, B, C):
        self.x1,self.y1 = copy.deepcopy(A.get())
        self.x2,self.y2 = copy.deepcopy(B.get())
        self.x3,self.y3 = copy.deepcopy(C.get())

    def line(self, x_1, y_1, x_2, y_2):
        return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

    def square(self, x1, y1, x2, y2, x3, y3):
        a, b, c = self.line(x1, y1, x2, y2), self.line(x1, y1, x3, y3), self.line(x2, y2, x3, y3)
        p = (a + b + c) / 2
        return m.sqrt(p * (p - a) * (p - b) * (p - c))

    @property
    def figure_square(self):
        a = math.floor(math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2))
        b = math.floor(math.sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2))
        c = math.floor(math.sqrt((self.x3 - self.x1) ** 2 + (self.y2 - self.y1) ** 2))
        p = (a + b + c) / 2
        return m.sqrt(math.sqrt(p * (p - a) * (p - b) * (p - c)))

    def in_or_out(self, x, y):
        self.x = x - 1
        self.y = y - 1
        sqr1 = self.square(self.x1, self.y1, self.x2, self.y2, self.x, self.y)
        sqr2 = self.square(self.x1, self.y1, self.x3, self.y3, self.x, self.y)
        sqr3 = self.square(self.x2, self.y2, self.x3, self.y3, self.x, self.y)
        sqr_whole = self.square(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)
        if (abs(sqr_whole - sqr1 - sqr2 - sqr3) <= 0.0001):
            return True
        else:
            return False

    def draw(self):
        data = [['⭔'] * 40 for i in range(40)]
        stroka=''
        for i in range(40):
            for j in range(40):
                if self.in_or_out(i, j):
                    data[i][j] = '⭓'
        for i in range(len(data)):  # строка
            for j in range(len(data[i])):  # строка
                # print(len(data[i]))
                stroka += data[i][j]
                if j == len(data[i])-1:
                    stroka += '\n'
        for i in range(40):
            for j in range(40):
                print(data[i][j], end='')
            print('')
        return stroka
    def move_up(self):
        self.x1 = self.x1-1
        self.x2 = self.x2-1
        self.x3 = self.x3-1
        self.draw()
    def move_down(self):
        self.x1 = self.x1 + 1
        self.x2 = self.x2 + 1
        self.x3 = self.x3 + 1
        self.draw()
    def move_left(self):
        self.y1 = self.y1 - 1
        self.y2 = self.y2 - 1
        self.y3 = self.y3 -1
        self.draw()
    def move_right(self):
        self.y1 = self.y1 + 1
        self.y2 = self.y2 + 1
        self.y3 = self.y3 + 1
        self.draw()

class Square(Rectangle):
    def __init__(self, A, D):
        self.x1,self.y1 = copy.deepcopy(A.get())
        self.x2,self.y2 = copy.deepcopy(D.get())
    def  move_left(self):
        self.x1=self.x1-1
        self.x2=self.x2-1
        self.draw()
    def move_right(self):
        self.x1=self.x1+1
        self.x2=self.x2+1
        return self.draw()
    def move_up(self):
        self.y1=self.y1-1
        self.y2=self.y2-1
        return self.draw()
    def move_down(self):
        self.y1 = self.y1 + 1
        self.y2 = self.y2 + 1
        return self.draw()

    def draw(self):
        return super().draw()
    @property
    def figure_square(self):
        a = math.floor((self.x1 - self.x2))
        return a * a


class Diamond:
    def __init__(self, A, B, C, D):
        self.x1,self.y1 = copy.deepcopy(A.get())
        self.x2,self.y2 = copy.deepcopy(B.get())
        self.x3,self.y3 = copy.deepcopy(C.get())
        self.x4,self.y4 = copy.deepcopy(D.get())

    def line(self, x_1, y_1, x_2, y_2):
        return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

    def square(self, x1, y1, x2, y2, x3, y3):
        a, b, c = self.line(x1, y1, x2, y2), self.line(x1, y1, x3, y3), self.line(x2, y2, x3, y3)
        p = (a + b + c) / 2
        return m.sqrt(p * (p - a) * (p - b) * (p - c))
    @property
    def figure_square(self):
        sqr_whole = self.square(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)
        return 2*sqr_whole

    def in_or_out(self, x, y):
        self.x = x - 1
        self.y = y - 1
        sqr1 = self.square(self.x1, self.y1, self.x2, self.y2, self.x, self.y)
        sqr2 = self.square(self.x1, self.y1, self.x3, self.y3, self.x, self.y)
        sqr3 = self.square(self.x2, self.y2, self.x3, self.y3, self.x, self.y)
        sqr_whole = self.square(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)
        if (abs(sqr_whole - sqr1 - sqr2 - sqr3) <= 0.0001):
            return True
        else:
            return False

    def draw(self):
        stroka=''
        data = [['⭔'] * 40 for i in range(40)]
        for i in range(40):
            for j in range(40):
                if self.in_or_out(i, j):
                    data[i][j] = '⭓'
        self.x3 = self.x4
        self.y3 = self.y4
        for i in range(len(data)):  # строка
            for j in range(len(data[i])):  # строка
                # print(len(data[i]))
                stroka += data[i][j]
                if j == len(data[i])-1:
                    stroka += '\n'
        for i in range(40):
            for j in range(40):
                print(data[i][j], end='')
            print('')
        return stroka
    def move_up(self):
        self.x1 = self.x1 - 1
        self.x2 = self.x2 - 1
        self.x3 = self.x3 - 1
        self.x4=self.x4-1
        self.draw()

    def move_down(self):
        self.x1 = self.x1 + 1
        self.x2 = self.x2 + 1
        self.x3 = self.x3 + 1
        self.x4 = self.x4 + 1
        self.draw()

    def move_left(self):
        self.y1 = self.y1 - 1
        self.y2 = self.y2 - 1
        self.y3 = self.y3 - 1
        self.y4 = self.y4 - 1
        self.draw()

    def move_right(self):
        self.y1 = self.y1 + 1
        self.y2 = self.y2 + 1
        self.y3 = self.y3 + 1
        self.y4 = self.y4 + 1
        self.draw()

class Window(object):
    def __int__(self,text,text1='',text2='',text3=''):
        self.text=text
        self.text1=text1
        self.text2=text2
        self.text3=text3
    @property
    def screen(self):
        windows=tk.Tk()
        windows=windows.title('Figures')
        return windows
    @staticmethod
    def draw_with_window(text,color1,color2):
        windows = tk.Tk()
        windows.title('Figures')
        windows= tk.Label(text=text,background=color2,foreground=color1).grid(row=0, column=1)
        return windows
    @staticmethod
    def draw_all_figures(fig1,fig2,fig3,fig4,color1,color2):
        x1=tk.Label(text=fig1,bg=color1,fg=color2,justify='left').grid(row=0,column=1)
        x2=tk.Label(text=fig2,bg=color1,fg=color2).grid(row=0,column=3)
        x3=tk.Label(text=fig3,bg=color1,fg=color2).grid(row=0,column=5)
        x4=tk.Label(text=fig4,bg=color1,fg=color2).grid(row=0,column=7)
        return x1,x2,x3,x4

w=Window()
a = Point(0,0)
b = Point(20, 30)
c = Point(30, 10)
d = Point(40, 40)
answ=Square(a,b)
# w.draw_with_window(answ.draw(),'purple','grey')
answ2=Rectangle(a,b)
answ3=Diamond(a,b,c,d)
answ1=Triangle(a,b,c)
print(answ1.move_down())
x=answ.draw()
y=answ1.draw()
z=answ2.draw()
c=answ3.draw()
w.draw_all_figures(x,y,z,c,'darkcyan','yellow')
lst = [answ, answ1, answ2,answ3]

class Shape(object):
    def __init__(self, lst):
        self.lst = lst

    def draw_all(self):
        for el in lst:
            el.draw()
            print('XXX')

    def all_square(self):
        lst1 = []
        for el in lst:
            lst1.append(el.figure_square)
        return sum(lst1)


sh = Shape(lst)
print(sh.draw_all())
print(sh.all_square())
tk.mainloop()
