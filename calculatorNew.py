from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import Tk, StringVar
window = Tk()
window.geometry("300x400")  # Increased window size
window.title("Calculator")
window.resizable(False, False)

result = ""

def press(num):
    global result
    result = result + str(num)
    equation.set(result)

def clear():
    global result
    result = ""
    equation.set("")

equation = StringVar()

def equalpress():
    try:
        global result
        total = str(eval(result))
        equation.set(total)
        result = ""
    except:
        equation.set(' Not Valid')
        result = ""

entry = ttk.Entry(window, width=15, font=("Arial", 24), textvariable=equation, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


btn_width = 6
btn_height = 3

ttk.Button(window, width=btn_width, text="1", command=lambda: press(1)).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(window, width=btn_width, text="2", command=lambda: press(2)).grid(row=1, column=1, padx=5, pady=5)
ttk.Button(window, width=btn_width, text="3", command=lambda: press(3)).grid(row=1, column=2, padx=5, pady=5)
ttk.Button(window, width=btn_width, text="+", command=lambda: press("+")).grid(row=1, column=3, padx=5, pady=5)

ttk.Button(window, width=btn_width, text="4", command=lambda: press(4)).grid(row=2, column=0, padx=5, pady=5)
ttk.Button(window, width=btn_width, text="5", command=lambda: press(5)).grid(row=2, column=1, padx=5, pady=5)
ttk.Button(window, width=btn_width, text="6", command=lambda: press(6)).grid(row=2, column=2, padx=5, pady=5)
ttk.Button(window, width=btn_width, text="-", command=lambda: press("-")).grid(row=2, column=3, padx=5, pady=5)

ttk.Button(window, width=btn_width, text="7", command=lambda: press(7)).grid(row=3, column=0, padx=5, pady=5)
ttk.Button(window, width=btn_width, text="8", command=lambda: press(8)).grid(row=3, column=1, padx=5, pady=5)
ttk.Button(window, width=btn_width, text="9", command=lambda: press(9)).grid(row=3, column=2, padx=5, pady=5)
ttk.Button(window, width=btn_width, text="*", command=lambda: press("*")).grid(row=3, column=3, padx=5, pady=5)

ttk.Button(window, width=btn_width, text="0", command=lambda: press(0)).grid(row=4, column=0, padx=5, pady=5)
ttk.Button(window, width=btn_width, text="Clear", command=clear).grid(row=4, column=1, padx=5, pady=5)
ttk.Button(window, width=btn_width, text="=", command=equalpress).grid(row=4, column=2, padx=5, pady=5)
ttk.Button(window, width=btn_width, text="/", command=lambda: press("/")).grid(row=4, column=3, padx=5, pady=5)

ttk.Button(window, width=btn_width, text=".", command=lambda: press(".")).grid(row=5, column=0, padx=5, pady=5)
footer = ttk.Label(window, text="created by thanos katsifis", font=("Segoe UI", 9, "italic"))
footer.grid(column=0, row=8, columnspan=6, pady=(10, 0))
window.mainloop()