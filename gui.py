import tkinter as tk
from tkinter import messagebox

class PolygonAreaCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Polygon Area Calculator")

        self.label_width = tk.Label(master, text="Width:")
        self.label_width.grid(row=0, column=0)

        self.entry_width = tk.Entry(master)
        self.entry_width.grid(row=0, column=1)

        self.label_height = tk.Label(master, text="Height:")
        self.label_height.grid(row=1, column=0)

        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=1, column=1)

        self.button_calculate = tk.Button(master, text="Calculate Area", command=self.calculate_area)
        self.button_calculate.grid(row=2, columnspan=2)

    def calculate_area(self):
        try:
            width = float(self.entry_width.get())
            height = float(self.entry_height.get())
            area = width * height
            messagebox.showinfo("Area", f"The area of the polygon is {area}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for width and height.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PolygonAreaCalculatorGUI(root)
    root.mainloop()
