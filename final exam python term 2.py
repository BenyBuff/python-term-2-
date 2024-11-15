class Square:  
    def __init__(self, side_length):  
        """مقداردهی اولیه با طول ضلع مربع."""  
        self.side_length = side_length  

    def area(self):  
        """محاسبه مساحت مربع."""  
        return self.side_length ** 2  

# مثال استفاده از کلاس  
square = Square(4)  # ایجاد یک مربع با طول ضلع 4  
print("مساحت مربع:", square.area())  # چاپ مساحت مربع
