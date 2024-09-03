from tkinter import *
from tkinter.ttk import Combobox
from dotenv import load_dotenv
import os
import currencyapicom

load_dotenv(override=True)
CURRENCY_API_KEY = os.getenv('CURRENCY_API_KEY')

# google მონაცემებია
currency_dict={"GEL_TO_USD": 0.3717, "GEL_TO_EUR": 0.3359, "GEL_TO_GBP": 0.2827, "USD_TO_GBP": 0.7624,
               "USD_TO_EUR": 0.9062, "USD_TO_GEL": 2.6900, "EUR_TO_GBP": 0.8414, "EUR_TO_GEL": 2.9775,
               "EUR_TO_USD": 1.1036, "GBP_TO_USD": 1.3116, "GBP_TO_EUR": 1.1885, "GBP_TO_GEL": 3.5383}

root = Tk()
root.title("Currency Converter")
root.config(bg="#6A9C89")

currency_list = ["USD", "GEL", "EUR", "GBP"]

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_offset = screen_width // 2 - 300 // 2
y_offset = screen_height // 2 - 200 // 2

root.geometry(f"300x200+{x_offset}+{y_offset}")

title_label = Label(root, bg="#6A9C89", text="Currency Converter", fg="#E9EFEC", font=("Arial", 20, "bold"))
title_label.grid(column=0, row=0, columnspan=2)

from_container = Frame(root, bg="#16423C")
to_container = Frame(root, bg="#16423C")

from_container.grid(row=1, column=0)
to_container.grid(row=2, column=0)

value_to_convert_input = Entry(from_container, width=25, bg="#C4DAD2", justify='center', fg="#16423C")
value_to_convert_input.pack(side="left")

get_curr_list = Combobox(from_container, values=currency_list)
get_curr_list.pack(side="left")

converted_label = Label(to_container, bg="#C4DAD2",fg="#16423C", text="Converted Value", width=21)
converted_label.pack(side="left")

to_curr_list = Combobox(to_container, values=currency_list)
to_curr_list.pack(side="left")

def convert_func():
    value_to_convert = int(value_to_convert_input.get())
    get_curr = get_curr_list.get()
    to_curr = to_curr_list.get()

    # ჰარდკოდინგით
    # converted_value = currency_dict[f'{get_curr.upper()}_TO_{to_curr.upper()}'] * value_to_convert
    # converted_label.config(text=f"{converted_value:.2f}")

    # currency api გამოყენებით

    client = currencyapicom.Client(CURRENCY_API_KEY)
    result = client.latest(get_curr, currencies=[to_curr])

    curr = result["data"][to_curr]["value"]
    converted = value_to_convert*curr
    converted_label.config(text=f'{converted:.2f}')

def clear_func():
    get_curr_list.set("")
    to_curr_list.set("")
    value_to_convert_input.delete(0, END)
    converted_label.config(text="Converted Value")

convert_button = Button(root, text="Convert", bg="#16423C", command=convert_func, fg="#E9EFEC")
convert_button.grid(row=3, column=0)

clear_button = Button(root, text="Clear", bg="#16423C", command=clear_func, fg="#E9EFEC")
clear_button.grid(row=4, column=0)

root.mainloop()
