import tkinter as tk
import math


class ScientificCalculator:

    def __init__(self, root):
        self.root = root

        self.root.title("Scientific Calculator")
        self.root.geometry("520x500")
        self.root.resizable(False, False)
        self.root.configure(bg="white")

        self.expression = ""

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 18, "bold"),
            bg="black",
            fg="white",
            justify="right",
            bd=10
        )

        self.display.grid(
            row=0,
            column=0,
            columnspan=8,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.create_buttons()


    def update_display(self, value):
        self.expression += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)


    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)


    def delete(self):
        self.expression = self.expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)


    def calculate(self):
        try:
            result = eval(
                self.expression,
                {"__builtins__": None},
                {
                    "sqrt": math.sqrt,
                    "sin": math.sin,
                    "cos": math.cos,
                    "tan": math.tan,
                    "log": math.log,
                    "log10": math.log10,
                    "pi": math.pi,
                    "e": math.e
                }
            )

            self.expression = str(result)

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)

        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""


    def scientific(self, operation):

        try:

            value = float(self.display.get())

            if operation == "sqrt":
                result = math.sqrt(value)

            elif operation == "sin":
                result = math.sin(math.radians(value))

            elif operation == "cos":
                result = math.cos(math.radians(value))

            elif operation == "tan":
                result = math.tan(math.radians(value))

            elif operation == "asin":
                result = math.degrees(math.asin(value))

            elif operation == "acos":
                result = math.degrees(math.acos(value))

            elif operation == "atan":
                result = math.degrees(math.atan(value))

            elif operation == "sinh":
                result = math.sinh(value)

            elif operation == "cosh":
                result = math.cosh(value)

            elif operation == "tanh":
                result = math.tanh(value)

            elif operation == "log":
                result = math.log(value)

            elif operation == "log10":
                result = math.log10(value)


            self.expression = str(result)

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)


        except:

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")



    def create_buttons(self):

        buttons = [

            ("7",1,0),("8",1,1),("9",1,2),
            ("/",1,3),("C",1,4),

            ("4",2,0),("5",2,1),("6",2,2),
            ("*",2,3),("⌫",2,4),

            ("1",3,0),("2",3,1),("3",3,2),
            ("-",3,3),("sqrt",3,4),

            ("0",4,0),(".",4,1),
            ("+",4,2),("=",4,3),
            ("(",4,4),(")",4,5),

            ("sin",5,0),
            ("cos",5,1),
            ("tan",5,2),
            ("log",5,3),
            ("ln",5,4),

            ("asin",6,0),
            ("acos",6,1),
            ("atan",6,2),
            ("sinh",6,3),
            ("cosh",6,4),
            ("tanh",6,5),

            ("π",7,0),
            ("e",7,1),
            ("log10",7,2)

        ]


        for text,row,col in buttons:

            if text == "=":

                command = self.calculate

            elif text == "C":

                command = self.clear

            elif text == "⌫":

                command = self.delete


            elif text in [
                "sqrt","sin","cos","tan",
                "asin","acos","atan",
                "sinh","cosh","tanh",
                "log","log10","ln"
            ]:

                command = lambda x=text:self.scientific(x)


            elif text == "π":

                command = lambda:self.update_display(math.pi)


            elif text == "e":

                command = lambda:self.update_display(math.e)


            else:

                command = lambda x=text:self.update_display(x)


            button = tk.Button(
                self.root,
                text=text,
                width=6,
                height=2,
                font=("Arial",12,"bold"),
                command=command
            )

            button.grid(
                row=row,
                column=col,
                padx=3,
                pady=3
            )



if __name__ == "__main__":

    root = tk.Tk()

    calculator = ScientificCalculator(root)

    root.mainloop()