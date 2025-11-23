from customtkinter import *
import tkinter.messagebox as messagebox
from PIL import Image, ImageDraw, ImageFont

image_font = ImageFont.load_default(53)


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1280x1280')
        self.resizable(False, False)
        self.title("Лонг Айленд")
        font=CTkFont(family="Arial", size=53)
        self.sign = None
        self.first_num = None
        self.second_num = None
        self.error_window = None


        self.bg_image = CTkImage(light_image=Image.open("/home/egor/Python/gui/calc.png"), size=(1280, 1280))
        self.bg_label = CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.pack(fill="both", expand=True)


        self.button1 = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text="1", text_color="#006e8c", anchor="center", font=font,
                                command=self.button1_click)
        self.button1.place(x=450, y=822)


        self.button2 = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text="2", text_color="#006e8c", anchor="center", font=font,
                                command=self.button2_click)
        self.button2.place(x=562, y=822)


        self.button3 = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text="3", text_color="#006e8c", anchor="center", font=font,
                                command=self.button3_click)
        self.button3.place(x=673, y=822)


        self.button4 = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text="4", text_color="#006e8c", anchor="center", font=font,
                                command=self.button4_click)
        self.button4.place(x=450, y=698)



        image = Image.new("RGBA", (82, 82), (133, 162, 180, 255))
        draw = ImageDraw.Draw(image)
        draw.ellipse([0, 0, 80, 80], fill=(0, 92, 126, 255))
        draw.text((25, 5), text="5", fill=(212, 158, 94, 255), font=image_font)
        ctk_image = CTkImage(light_image=image, size=(70, 70))


        self.button5 = CTkLabel(self, image=ctk_image, text="")
        self.button5.place(x=559, y=698)
        self.button5.bind("<Button-1>", lambda e: self.button5_click())


        self.button6 = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text="6", text_color="#006e8c", anchor="center", font=font,
                                command=self.button6_click)
        self.button6.place(x=673, y=698)


        self.button7 = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text="7", text_color="#006e8c", anchor="center", font=font,
                                command=self.button7_click)
        self.button7.place(x=450, y=575)


        self.button8 = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text="8", text_color="#006e8c", anchor="center", font=font,
                                command=self.button8_click)
        self.button8.place(x=562, y=575)


        self.button9 = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text="9", text_color="#006e8c", anchor="center", font=font,
                                command=self.button9_click)
        self.button9.place(x=673, y=575)


        self.button0 = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text="0", text_color="#006e8c", anchor="center", font=font,
                                command=self.button0_click)
        self.button0.place(x=562, y=930)


        self.point_button = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text=".", text_color="#006e8c", anchor="center", font=font,
                                command=self.point_button_click)
        self.point_button.place(x=673, y=930)


        image = Image.new("RGBA", (82, 82), (133, 162, 180, 255))
        draw = ImageDraw.Draw(image)
        draw.ellipse([0, 0, 80, 80], fill=(0, 92, 126, 255))
        draw.text((27, 5), text="+", fill=(212, 158, 94, 255), font=image_font)
        ctk_image = CTkImage(light_image=image, size=(70, 70))


        self.plus_button = CTkLabel(self, image=ctk_image, text="")
        self.plus_button.place(x=763, y=822)
        self.plus_button.bind("<Button-1>", lambda e: self.plus_button_click())


        image = Image.new("RGBA", (85, 85), (133, 162, 180, 255))
        draw = ImageDraw.Draw(image)
        draw.ellipse([0, 0, 80, 80], fill=(0, 92, 126, 255))
        draw.text((35, 5), text="-", fill=(212, 158, 94, 255), font=image_font)
        ctk_image = CTkImage(light_image=image, size=(70, 70))


        self.minus_button = CTkLabel(self, image=ctk_image, text="")
        self.minus_button.place(x=765, y=697)
        self.minus_button.bind("<Button-1>", lambda e: self.minus_button_click())


        image = Image.new("RGBA", (80, 80), (133, 162, 180, 255))
        draw = ImageDraw.Draw(image)
        draw.ellipse([0, 0, 80, 80], fill=(0, 92, 126, 255))
        draw.text((30, 3), text="x", fill=(212, 158, 94, 255), font=image_font)
        ctk_image = CTkImage(light_image=image, size=(70, 70))


        self.mult_button = CTkLabel(self, image=ctk_image, text="")
        self.mult_button.place(x=765, y=578)
        self.mult_button.bind("<Button-1>", lambda e: self.mult_button_click())


        image = Image.new("RGBA", (80, 80), (133, 162, 180, 255))
        draw = ImageDraw.Draw(image)
        draw.ellipse([0, 0, 80, 80], fill=(0, 92, 126, 255))
        draw.text((30, 3), text="/", fill=(212, 158, 94, 255), font=image_font)
        ctk_image = CTkImage(light_image=image, size=(70, 70))


        self.div_button = CTkLabel(self, image=ctk_image, text="")
        self.div_button.place(x=762, y=461)
        self.div_button.bind("<Button-1>", lambda e: self.div_button_click())


        image = Image.new("RGBA", (80, 80), (133, 162, 180, 255))
        draw = ImageDraw.Draw(image)
        draw.ellipse([0, 0, 80, 80], fill=(0, 92, 126, 255))
        draw.text((27, 5), text="=", fill=(212, 158, 94, 255), font=image_font)
        ctk_image = CTkImage(light_image=image, size=(70, 70))


        self.eq_button = CTkLabel(self, image=ctk_image, text="")
        self.eq_button.place(x=767, y=940)
        self.eq_button.bind("<Button-1>", lambda e: self.eq_button_click())


        self.change_sign_button = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text="+/-", text_color="#006e8c", anchor="center", font=font,
                                command=self.change_sign_click)
        self.change_sign_button.place(x=562, y=461)


        self.clear_all_button = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text="AC", text_color="#006e8c", anchor="center", font=font,
                                command=self.clear_all_click)
        self.clear_all_button.place(x=450, y=461)


        self.root_button = CTkButton(self, width=70, height=70, corner_radius=0, fg_color="#85a2b4",
                                 hover_color="#85a2b4", border_color="#85a2b4",
                                text="⎷", text_color="#006e8c", anchor="center", font=font,
                                command=self.root_button_click)
        self.root_button.place(x=673, y=461)


        self.bind("<Key>", self.on_key_press)


        entry_font=CTkFont(family="Arial", size=25)
        self.text = StringVar()
        self.entry_field = CTkLabel(self, textvariable=self.text, width=300, height=100,
                                    font=entry_font, justify="right", anchor="e",
                                    fg_color="transparent")
        self.entry_field.place(x=480, y=274)


    def button1_click(self):
        self.text.set(self.text.get() + "1")


    def button2_click(self):
        self.text.set(self.text.get() + "2")


    def button3_click(self):
        self.text.set(self.text.get() + "3")


    def button4_click(self):
        self.text.set(self.text.get() + "4")


    def button5_click(self):
        self.text.set(self.text.get() + "5")


    def button6_click(self):
        self.text.set(self.text.get() + "6")


    def button7_click(self):
        self.text.set(self.text.get() + "7")


    def button8_click(self):
        self.text.set(self.text.get() + "8")


    def button9_click(self):
        self.text.set(self.text.get() + "9")


    def button0_click(self):
        self.text.set(self.text.get() + "0")
    

    def point_button_click(self):
        if self.text.get() and "." not in self.text.get():
            self.text.set(self.text.get() + ".")
    

    def plus_button_click(self):
        if not self.sign and self.text.get():
            self.first_num = self.text.get()
            self.text.set("")
            self.sign = "+"
    

    def minus_button_click(self):
        if not self.sign and self.text.get():
            self.first_num = self.text.get()
            self.text.set("")
            self.sign = "-"
    

    def div_button_click(self):
        if not self.sign and self.text.get():
            self.first_num = self.text.get()
            self.text.set("")
            self.sign = "/"        
    

    def mult_button_click(self):
        if not self.sign and self.text.get():
            self.first_num = self.text.get()
            self.text.set("")
            self.sign = "*"
    

    def root_button_click(self):
        if not self.sign and self.text.get():


            self.first_num = self.text.get()


            if "." in self.first_num:
                self.first_num = float(self.first_num)
            else:
                self.first_num = int(self.first_num)


            if self.first_num >= 0:
                result = self.first_num ** 0.5
                self.first_num = result
                self.second_num = None
                self.text.set(str(result))
                self.sign = None
            else:
                if self.error_window is None or not self.error_window.winfo_exists():
                    self.error_window = RootErrorWindow()
                else:
                    self.error_window.focus()
                    self.first_num = None
                    self.text.set("")
    

    def eq_button_click(self):
        if isinstance(self.first_num, str):
            self.second_num = self.text.get()


            if "." in self.first_num:
                self.first_num = float(self.first_num)
            else:
                self.first_num = int(self.first_num)
            

            if "." in self.second_num:
                self.second_num = float(self.second_num)
            else:
                self.second_num = int(self.second_num)
            

            if self.sign == "+":
                result = self.first_num + self.second_num
                self.first_num = result
                self.second_num = None
                self.text.set(str(result))
                self.sign = None
            

            if self.sign == "-":
                result = self.first_num - self.second_num
                self.first_num = result
                self.second_num = None
                self.text.set(str(result))
                self.sign = None
            

            if self.sign == "*":
                result = self.first_num * self.second_num
                self.first_num = result
                self.second_num = None
                self.text.set(str(result))
                self.sign = None
            

            if self.sign == "/":
                try:
                    result = self.first_num / self.second_num
                    self.first_num = result
                    self.second_num = None
                    self.text.set(str(result))
                    self.sign = None
                except ZeroDivisionError:
                    if self.error_window is None or not self.error_window.winfo_exists():
                        self.error_window = DivisionErrorWindow()
                    else:
                        self.error_window.focus()
                    self.first_num = None
                    self.sign = None
                    self.second_num = None
                    self.text.set("")
    

    def change_sign_click(self):
        if self.text.get():
            num = self.text.get()
            if num.startswith("-"):
                self.text.set(num[1:])
            else:
                self.text.set("-" + num)
    

    def clear_all_click(self):
        self.text.set("")
        self.first_num = None
        self.second_num = None
        self.sign = None

    
    def on_key_press(self, event):
        if event.char in '0123456789':
            digit = event.char
            getattr(self, f'button{digit}_click', lambda: None)()
        elif event.char == "+":
            self.plus_button_click()
        elif event.char == "-":
            self.minus_button_click()
        elif event.char == "*":
            self.mult_button_click()
        elif event.char == "/":
            self.div_button_click()
        elif event.char == "=" or event.keysym == "Return":
            self.eq_button_click()
        elif event.char == ".":
            self.point_button_click()
        elif event.keysym == "Escape":
            self.clear_all_click()
        


class DivisionErrorWindow(CTkToplevel):
    def __init__(self):
        super().__init__()
        font=CTkFont(family="Arial", size=20)
        self.geometry("850x100")
        self.title("Ошибка!")
        self.label = CTkLabel(self, text="Делить на ноль нельзя! Иди учи математику!", font=font)
        self.label.pack(padx=20, pady=20)


class RootErrorWindow(CTkToplevel):
    def __init__(self):
        super().__init__()
        font=CTkFont(family="Arial", size=15)
        self.geometry("900x100")
        self.title("Ошибка!")
        self.label = CTkLabel(self, text="Извлекать корень из отрицательного числа нельзя! Иди учи математику!", font=font)
        self.label.pack(padx=20, pady=20)
        
                           

app = App()
app.mainloop()