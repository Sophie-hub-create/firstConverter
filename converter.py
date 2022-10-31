from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50, bg='#e2979c')


my_label2= Label(text='Pleaser enter the Miles you want to convert', font=("Uni Sans", 14, 'bold'), bg='#e2979c')
my_label2.grid(columnspan=2, row=0)
my_label2.config(pady=30)

entry = Entry(width=15, highlightbackground='#e2979c')

entry.grid(column=0, row=1)

my_label=Label(text="Miles", font=("Uni Sans", 12),bg='#e2979c')
my_label.config(padx=100)
my_label.grid(column=0, row=2)
my_label.config(pady=30)

my_label3=Label(text="is equal to", font=("Uni Sans", 12),bg='#e2979c')
my_label3.config(padx=100)
my_label3.grid(column = 1, row=2)
my_label3.config(pady=30)

my_label4=Label(font=("Uni Sans", 12), bg='#e2979c')
my_label4.config(padx=100)
my_label4.grid(columnspan = 2, row=3)
my_label4.config(pady=30)

def conversion():
    result = round(float(entry.get() or 0)*1.609,2)
    my_label4.config(text = f"{result} Km")



button = Button(text="Calculate", font=("Uni Sans", 12), highlightbackground='#e2979c',command=conversion)
button.grid(column=1, row=1)

window.mainloop()