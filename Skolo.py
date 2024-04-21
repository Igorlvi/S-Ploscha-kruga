# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

from math import sqrt, pi
import turtle
import matplotlib.pyplot as plt

print("Розрахуйте S площу круга , та L довжину його кола ")

r = float(input("Введіть радіус кола R ? = "))

print ("S круга = Пі(3.14)*(R в квадраті)")
print ("L кола = 2*Пі(3.14)*R ")
print("S Площа = %.2f" % (pi * r ** 2))
print("L Довжина = %.2f" % (2*pi * r ))
print ("Поки Ви звіряєте свій розв'язок із розв'язком даної програми, черепашка та matplotlib накреслили Вам ваше коло . Знайдіть їх у себе на моніторі.")


# turtle
turtle.left(90)
turtle.circle(r*37)
turtle.hideturtle()
style = ('Courier', 15, 'italic')
turtle.write(" Turtle накреслила\n Вам ваше коло", font=style, align='left')
turtle.title('Ваше коло')
# matplotlib
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
