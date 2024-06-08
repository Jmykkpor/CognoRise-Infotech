"""
    This module uses the eval function to evaluate the string of mathematical operations that will be inputted in the text section of the 
    gui that opens when the code runs. The delete_last function takes out the lat element that was inputted. A text or number cannot 
    be manually inputted into the text section.Input must be made from thr buttons on the gui that appears
"""

import tkinter as tk


calculation = ""


def add_to_calculation(symb):
    global calculation
    calculation += str(symb)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    except:
        clear()
        text_result.insert(1.0, "Error")


def clear():
    global calculation
    calculation= ""
    text_result.delete(1.0, "end")

def delete_last():
    global calculation
    calculation= calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


master= tk.Tk()
master.title("Calculator")
master.geometry("280x315")

text_result= tk.Text(master, height=2, width= 15, font= ("Arial", 24))
text_result.grid(columnspan=5)

btn_1= tk.Button(master, text="1", command= lambda: add_to_calculation(1), width= 5 , font= ("Arial",14))
btn_1.grid(row= 2, column=1)
btn_2= tk.Button(master, text="2", command= lambda: add_to_calculation(2), width= 5 , font= ("Arial",14))
btn_2.grid(row= 2, column=2)
btn_3= tk.Button(master, text="3", command= lambda: add_to_calculation(3), width= 5 , font= ("Arial",14))
btn_3.grid(row= 2, column=3)
btn_4= tk.Button(master, text="4", command=lambda: add_to_calculation(4), width= 5 , font= ("Arial",14))
btn_4.grid(row= 3, column=1)
btn_5= tk.Button(master, text="5", command= lambda: add_to_calculation(5), width= 5 , font= ("Arial",14))
btn_5.grid(row= 3, column=2)
btn_6= tk.Button(master, text="6", command= lambda: add_to_calculation(6), width= 5 , font= ("Arial",14))
btn_6.grid(row= 3, column=3)
btn_7= tk.Button(master, text="7", command= lambda: add_to_calculation(7), width= 5 , font= ("Arial",14))
btn_7.grid(row= 4, column=1)
btn_8= tk.Button(master, text="8", command= lambda: add_to_calculation(8), width= 5 , font= ("Arial",14))
btn_8.grid(row= 4, column=2)
btn_9= tk.Button(master, text="9", command= lambda: add_to_calculation(9), width= 5 , font= ("Arial",14))
btn_9.grid(row= 4, column=3)
btn_0= tk.Button(master, text="0", command= lambda: add_to_calculation(0), width= 5 , font= ("Arial",14))
btn_0.grid(row= 5, column=2)

btn_plus= tk.Button(master, text="+", command= lambda: add_to_calculation("+"), width= 5 , font= ("Arial",14))
btn_plus.grid(row= 2, column=4)
btn_sub= tk.Button(master, text="-", command= lambda: add_to_calculation("-"), width= 5 , font= ("Arial",14))
btn_sub.grid(row= 3, column=4)
btn_mult= tk.Button(master, text="*", command= lambda: add_to_calculation("*"), width= 5 , font= ("Arial",14))
btn_mult.grid(row= 4, column=4)
btn_div= tk.Button(master, text="/", command= lambda: add_to_calculation("/"), width= 5 , font= ("Arial",14))
btn_div.grid(row= 5, column=4)
btn_open= tk.Button(master, text="(", command= lambda: add_to_calculation("("), width= 5 , font= ("Arial",14))
btn_open.grid(row= 5, column=1)
btn_close= tk.Button(master, text=")", command= lambda: add_to_calculation(")"), width= 5 , font= ("Arial",14))
btn_close.grid(row= 5, column=3)

btn_clear= tk.Button(master, text="C", command=clear, width= 11 , font= ("Arial",14))
btn_clear.grid(row= 6, column= 1,columnspan=2)
btn_del_one= tk.Button(master, text="Del", command= delete_last, width= 11 , font= ("Arial",14))
btn_del_one.grid(row= 6, column= 3,columnspan=2)
btn_equal= tk.Button(master, text="=", command= evaluate_calculation , width= 24, font= ("Arial",14))
btn_equal.grid(row= 7, columnspan=5,padx= 2, pady=1)

master.mainloop()