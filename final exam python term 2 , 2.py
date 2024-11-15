import turtle

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def draw(self):
        turtle.penup()
        turtle.goto(-self.side_length / 2, -self.side_length / 2)  # مرکز شکل در وسط صفحه قرار می‌گیرد
        turtle.pendown()
        for _ in range(4):
            turtle.forward(self.side_length)
            turtle.left(90)
        turtle.done()

# نمونه‌سازی و استفاده از کلاس
square = Square(100)  # اندازه ضلع مربع
print("مساحت مربع:", square.area())  # محاسبه و نمایش مساحت
square.draw()  # رسم مربع
