from tkinter import *
from tkinter.ttk import Combobox
# import requests

# თუ სხვა API-ს ვიყენებთ (პ.ს. აღარ ვაჩენ გასაღებს რადგან ჰარდკოდინგის ვარიანტიც მიწერია ქვემოთ)

# from dotenv import load_dotenv
# import os
# import currencyapicom
#
# load_dotenv(override=True)
# CURRENCY_API_KEY = os.getenv('CURRENCY_API_KEY')


# google მონაცემებია without API
currency_dict={"GEL_TO_USD": 0.3717, "GEL_TO_EUR": 0.3359, "GEL_TO_GBP": 0.2827, "USD_TO_GBP": 0.7624,
               "USD_TO_EUR": 0.9062, "USD_TO_GEL": 2.6900, "EUR_TO_GBP": 0.8414, "EUR_TO_GEL": 2.9775,
               "EUR_TO_USD": 1.1036, "GBP_TO_USD": 1.3116, "GBP_TO_EUR": 1.1885, "GBP_TO_GEL": 3.5383}

root = Tk()
root.title("კონვერტაცია")
root.config(bg="#6A9C89")

currency_list = ["USD", "GEL", "EUR", "GBP"]

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_offset = screen_width // 2 - 320 // 2
y_offset = screen_height // 2 - 200 // 2

root.geometry(f"320x200+{x_offset}+{y_offset}")

title_label = Label(root, bg="#6A9C89", text="ვალუტის კონვერტაცია", fg="#E9EFEC", font=("Arial", 20, "bold"))
title_label.grid(column=0, row=0, columnspan=2)

from_container = Frame(root, bg="#16423C")
to_container = Frame(root, bg="#16423C")

from_container.grid(row=1, column=0, padx=10)
to_container.grid(row=2, column=0, padx=11)

value_to_convert_input = Entry(from_container, width=25, bg="#C4DAD2", justify='center', fg="#16423C")
value_to_convert_input.insert(0, "შეიყვანეთ თანხა")
value_to_convert_input.focus()
value_to_convert_input.pack(side="left")

get_curr_list = Combobox(from_container, values=currency_list)
get_curr_list.pack(side="left")

converted_label = Label(to_container, bg="#E9EFEC",fg="#16423C", text="შედეგი", width=21)
converted_label.pack(side="left")

to_curr_list = Combobox(to_container, values=currency_list)
to_curr_list.pack(side="left")

def convert_func():
    value_to_convert = float(value_to_convert_input.get())
    get_curr = get_curr_list.get().upper()
    to_curr = to_curr_list.get().upper()

    if get_curr in currency_list and to_curr in currency_list:
        #---------------------- ჰარდკოდინგით ----------------------------------------------------------#
        converted_value = currency_dict[f'{get_curr.upper()}_TO_{to_curr.upper()}'] * value_to_convert
        converted_label.config(text=f"{converted_value:.2f}")
        #----------------------------------------------------------------------------------------------#

        #---------- currency api გამოყენებით --------------------#
        # client = currencyapicom.Client(CURRENCY_API_KEY)
        # result = client.latest(get_curr, currencies=[to_curr])
        #
        # curr = result["data"][to_curr]["value"]
        # converted = value_to_convert*curr
        # converted_label.config(text=f'{converted:.2f}')
        #------------------------------------------------------#

    else:
        clear_func()
        raise ValueError

def clear_func():
    get_curr_list.set("")
    to_curr_list.set("")
    value_to_convert_input.delete(0, END)
    value_to_convert_input.insert(0, "შეიყვანეთ თანხა")
    converted_label.config(text="შედეგი")

convert_button = Button(root, text="კონვერტაცია", bg="#16423C", width=20, command=convert_func, fg="#E9EFEC")
convert_button.grid(row=3, column=0, padx=20, pady=20)

clear_button = Button(root, text="გასუფთავება", bg="#16423C", width=20, command=clear_func, fg="#E9EFEC")
clear_button.grid(row=4, column=0)

root.mainloop()

# თუ ეროვნული ბანკის მონაცემებს ვიყენებთ მაინც ჰარდკოდინგი გამოდის, რადგან ვერ ვიპოვე ლარის გარდა სხვა
# ვალუტების რეითები

# url = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/ka/json/"
#
# data = requests.get(url, params={"currencies": ["USD", "GBP", "EUR"]})
# data.raise_for_status()
# data = data.json()
#
# USD_TO_GEL = data[0]["currencies"][0]["rate"]
# GBP_TO_GEL = data[0]["currencies"][1]["rate"]
# EUR_TO_GEL = data[0]["currencies"][2]["rate"]
#
# USD_TO_GBP = round(USD_TO_GEL / GBP_TO_GEL, 4)
# USD_TO_EUR = round(USD_TO_GEL / EUR_TO_GEL, 4)
#
# EUR_TO_USD = round(EUR_TO_GEL / USD_TO_GEL, 4)
# EUR_TO_GBP = round(EUR_TO_GEL / GBP_TO_GEL, 4)
#
# GBP_TO_USD = round(GBP_TO_GEL / USD_TO_GEL, 4)
# GBP_TO_EUR = round(GBP_TO_GEL / EUR_TO_GEL, 4)
#
# GEL_TO_USD = round(1/ USD_TO_GEL, 4)
# GEL_TO_GBP = round(1/ GBP_TO_GEL, 4)
# GEL_TO_EUR = round(1/ EUR_TO_GEL, 4)

# ამიტომ აღარ გავაგრძელე

# ---------------------------------------------------------------------------------------------- #


