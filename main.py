import random
import tkinter as tk

#
clicks = 1
number = 0
number1 = 1
#
press_return = True
#
root = tk.Tk()
root.title("Homework Shag")
root.geometry('600x600')
root.resizable(width=False, height=False)
root.iconbitmap("alien.ico")
#
label = tk.Label(root, text=" Нажимай на кнопку и создаться случайное число", font=('Arial', '17', 'bold'), bg='pink',
                 fg='red', width=1000)
label_1 = tk.Label(root, text=f'Ваше число: {str(number)}', font=('Arial, 20'), bg='pink', fg='red', width=1000,
                   height=1000)
label_2 = tk.Label(root, bg='pink', fg='red', width=1000, height=3)
label_3 = tk.Label(root, bg='pink', fg='red', width=1000, height=3)


#
def alive():
    global number
    global clicks
    global press_return
    if clicks == 1:
        number = random.randint(0, 10)
        label_1.config(text='Ваше случайное число :' + str(number))
        label.config(text='Программа успешно работает! ')
        press_return = True
        return False
    else:
        return True


#
def alive2():
    global clicks
    global press_return
    global number
    global number1
    global label_1
    if clicks == 1:
        number1 = number * 2
        number = number + number
        label_1.config(text=f"Ваше умноженное  число: " + str(number1))
        press_return = True
        return False
    else:
        return True


#
def alive3():
    global clicks
    global press_return
    global number
    global number1
    global label_1
    if clicks == 1:
        number = 0
        label_1.config(text=f"Ваше число успешно обнулилось : " + str(number))
        label.config(text='Нажимай на кнопку и создаться случайное число ')
        press_return = True
        return False
    else:
        return True


#
def click_button_act3():
    global clicks
    if alive3():
        clicks += 1


#
def click_button_act2():
    global clicks
    if alive2():
        clicks += 1


#
def click_button_act():
    global clicks
    if alive():
        clicks += 1


if 3 > 2:
    ddd
#
click_button = tk.Button(root, text='Запустить случайное число', font=('Arial', '9', 'bold'), bg='pink', fg='red',
                         width=100, height=7, command=click_button_act)
click_button1 = tk.Button(root, text='Умножить на 2', font=('Arial', '9', 'bold'), bg='pink', fg='red', width=100,
                          height=7, command=click_button_act2)
click_button2 = tk.Button(root, text='удалить число', font=('Arial', '9', 'bold'), bg='pink', fg='red', width=100,
                          height=7, command=click_button_act3)
#
label_2.pack()
click_button_act()
label.pack()
label_3.pack()
click_button.pack()
click_button1.pack()
click_button2.pack()
label_1.pack()
root.mainloop()
