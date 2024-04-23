# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

from math import sqrt, pi
import turtle
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk

print("Розрахуйте S площу круга , та L довжину його кола ")
r = float(input("Введіть радіус кола R ? = "))
print("S Площа = %.2f" % (pi * r ** 2))
print("L Довжина = %.2f" % (2*pi * r ))
print ("Поки Ви звіряєте свій розв'язок, дана програма побудує Вам Ваше коло ")
print("У графічному сервісі\n1-Turtle\n2-Matplotlib\n3-Tkinter")
figure = input("Оберіть графічний сервіс : ")
if figure == '1':
    turtle.left(90)
    turtle.circle(r*37)
    turtle.hideturtle()
    style = ('Courier', 15, 'italic')
    turtle.write(" Turtle накреслила\n Вам ваше коло", font=style, align='left')
    turtle.title("Ваше коло")
    
elif figure == '2':
    plt.figure(figsize=(r+2,r+2))
    circle1=plt.Circle(xy=(0.0,0.0), radius= r, color='grey', linewidth=1,fill = False)
    fig = plt.gcf()
    ax = fig.gca()
    ax.add_patch(circle1)
    plt.xlim([-1.2*r,r+2])
    plt.ylim([-1.2*r,r+2])
    plt.savefig('circle2.png',dpi=600)
    plt.title('Ваше коло накреслене на координатній сітці')
    plt.show()

elif figure == '3':
    win = tk.Tk()
    win.title("Ваше коло накреслене в Tkinter")
    canvas = Canvas(width=r*2*37+50, height=r*2*37+50, bg='white')  
    canvas.pack(expand=YES, fill=BOTH)                
    canvas.create_oval(50, 50, r*2*37, r*2*37)
    mainloop()

else:
    print("Помилка введення ???")


