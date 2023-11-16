import tkinter as tk # to simplfy the call of the module we named him(tk)
from math import* # to call all the function of the math module 
window= tk.Tk()
window.geometry("300x400")# make dimension for our window 
window.title("Python Calculator")# make a title for the window

textbox=tk.Text(window, height=4, font=("Arial",16))# create the textbox and defind his position in the screen
textbox.insert(tk.END, "")#insert nothing in the textbox
textbox.pack(padx=10,pady=5)# run the function , select the distnace between the textbox and the boards


def clear():#"clear" function for clear the texbox
     textbox.delete("1.0", tk.END)

def cnvt_2_10():#to convert a binary number to decimal
    n = textbox.get("1.0", tk.END).strip()  # Get the text and remove any trailing whitespace
    
    binary_set = {'0', '1'}
    bina = set(str(n)) <= binary_set
    
    if bina:   
        result = int(n, 2)  # Convert the binary number n
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, result)
    else:# if the user enter a decimal number
        result = "Error, write a binary ...! "
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, result)

   
def cnvt_10_2():# to convert a decimal number to binary number  
    decNum=textbox.get("1.0", tk.END)
    result=bin(int(decNum))[2:]
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, result)

def press_pi():#to insert the constant Pi 
    
    textbox.insert(tk.END,float(pi))

def press(x):# we use this function to insert any string in the textbox
    
    textbox.insert(tk.END,x)


button1 = tk.Button(window, text="√", font=("Arial", 10, "bold"),command=lambda:press("sqrt(" ) )#create the button and write a text on it
button1.pack()# Add the button to the window
button1.place(x=0, y=340, width=60, height=60)#Place the button

button2 = tk.Button(window, text="0", font=("Arial", 10, "bold"),command=lambda: press(0))#create the button and write a text on it
button2.pack()# Add the button to the window
button2.place(x=60, y=340, width=60, height=60)#Place the button

button3 = tk.Button(window, text=".", font=("Arial", 10, "bold"),command=lambda: press("."))#create the button and write a text on it
button3.pack()# Add the button to the window
button3.place(x=120, y=340, width=60, height=60)#Place the button

button4 = tk.Button(window, text="+", font=("Arial", 10, "bold"),command=lambda: press("+"))#create the button and write a text on it
button4.pack()# Add the button to the window
button4.place(x=180, y=340, width=60, height=60)#Place the button

button5 = tk.Button(window, text="-", font=("Arial", 10, "bold"),command=lambda: press("-"))#create the button and write a text on it
button5.pack()# Add the button to the window
button5.place(x=240, y=340, width=60, height=60)#Place the button

button6 = tk.Button(window, text="7", font=("Arial", 10, "bold"),command=lambda: press(7))#create the button and write a text on it
button6.pack()# Add the button to the window
button6.place(x=0, y=280, width=60, height=60)#Place the button

button7 = tk.Button(window, text="8", font=("Arial", 10, "bold"),command=lambda: press(8))#create the button and write a text on it
button7.pack()# Add the button to the window
button7.place(x=60, y=280, width=60, height=60)#Place the button

button8 = tk.Button(window, text="9", font=("Arial", 10, "bold"),command=lambda: press(9))#create the button and write a text on it
button8.pack()# Add the button to the window
button8.place(x=120, y=280, width=60, height=60)#Place the button

button9 = tk.Button(window, text="/", font=("Arial", 10, "bold"),command=lambda: press("/"))#create the button and write a text on it
button9.pack()# Add the button to the window
button9.place(x=180, y=280, width=60, height=60)#Place the button

button10 = tk.Button(window, text="x", font=("Arial", 10, "bold"),command=lambda: press("*"))#create the button and write a text on it
button10.pack()# Add the button to the window
button10.place(x=240, y=280, width=60, height=60)#Place the button

button11 = tk.Button(window, text="4", font=("Arial", 10, "bold"),command=lambda: press(4))#create the button and write a text on it
button11.pack()# Add the button to the window
button11.place(x=0, y=220, width=60, height=60)#Place the button

button12 = tk.Button(window, text="5", font=("Arial", 10, "bold"),command=lambda: press(5))#create the button and write a text on it
button12.pack()# Add the button to the window
button12.place(x=60, y=220, width=60, height=60)#Place the button

button13 = tk.Button(window, text="6", font=("Arial", 10, "bold"),command=lambda: press(6))#create the button and write a text on it
button13.pack()# Add the button to the window
button13.place(x=120, y=220, width=60, height=60)#Place the button

button14 = tk.Button(window, text="x^y", font=("Arial", 10, "bold"),command=lambda: press("**"))#create the button and write a text on it
button14.pack()# Add the button to the window
button14.place(x=180, y=220, width=60, height=60)#Place the button

button15 = tk.Button(window, text="x^-1", font=("Arial", 10, "bold"),command=lambda:press("**-1"))#create the button and write a text on it
button15.pack()# Add the button to the window
button15.place(x=240, y=220, width=60, height=60)#Place the button

button16 = tk.Button(window, text="1", font=("Arial", 10, "bold"),command=lambda: press(1))#create the button and write a text on it
button16.pack()# Add the button to the window
button16.place(x=0, y=160, width=60, height=60)#Place the button

button17 = tk.Button(window, text="2", font=("Arial", 10, "bold"),command=lambda: press(2))#create the button and write a text on it
button17.pack()# Add the button to the window
button17.place(x=60, y=160, width=60, height=60)#Place the button

button18 = tk.Button(window, text="3", font=("Arial", 10, "bold"),command=lambda: press(3))#create the button and write a text on it
button18.pack()# Add the button to the window
button18.place(x=120, y=160, width=60, height=60)#Place the button

button19 = tk.Button(window, text="(", font=("Arial", 10, "bold"),command=lambda:press('('))#create the button and write a text on it
button19.pack()# Add the button to the window
button19.place(x=180, y=160, width=60, height=60)#Place the button

button20 = tk.Button(window, text=")", font=("Arial", 10, "bold"),command=lambda :press(')') )#create the button and write a text on it
button20.pack()# Add the button to the window
button20.place(x=240, y=160, width=60, height=60)#Place the button

button21 = tk.Button(window, text="ln(x)", font=("Arial", 10, "bold"),command=lambda : press("log("))#create the button and write a text on it
button21.pack()# Add the button to the window
button21.place(x=0, y=100, width=60, height=60)#Place the button

button22 = tk.Button(window, text="exp(x)", font=("Arial", 10, "bold"),command=lambda:press("exp("))#create the button and write a text on it
button22.pack()# Add the button to the window
button22.place(x=60, y=100, width=60, height=60)#Place the button

button23 = tk.Button(window, text="sin(x)", font=("Arial", 10, "bold"),command=lambda:press("sin("))#create the button and write a text on it
button23.pack()# Add the button to the window
button23.place(x=120, y=100, width=60, height=60)#Place the button

button24 = tk.Button(window, text="cos(x)", font=("Arial", 10, "bold"),command=lambda:press("cos("))#create the button and write a text on it
button24.pack()# Add the button to the window
button24.place(x=180, y=100, width=60, height=60)#Place the button

button25 = tk.Button(window, text="tan(x)", font=("Arial", 10, "bold"),command=lambda:press("tan("))#create the button and write a text on it
button25.pack()# Add the button to the window
button25.place(x=240, y=100, width=60, height=60)#Place the button

button26 = tk.Button(window, text="()2-->()10", font=("Arial", 10, "bold"),command=lambda:cnvt_2_10())#create the button and write a text on it
button26.pack()# Add the button to the window
button26.place(x=0, y=60, width=60, height=40)#Place the button

button27 = tk.Button(window, text="()10-->()2", font=("Arial", 10, "bold"),command=lambda:cnvt_10_2())#create the button and write a text on it
button27.pack()# Add the button to the window
button27.place(x=60, y=60, width=60, height=40)#Place the button

button28= tk.Button(window, text="Pi", font=("Arial", 10, "bold"),command=lambda:press_pi())#create the button and write a text on it
button28.pack()# Add the button to the window
button28.place(x=120, y=60, width=60, height=40)#Place the button

button29= tk.Button(window, text="AC", font=("Arial", 10, "bold"),command=lambda:clear())#create the button and write a text on it
button29.pack()# Add the button to the window
button29.place(x=180, y=60, width=60, height=40)#Place the button

def equals():#the most important function in the program ,that calculate the the operation of the textbox
    try:
        result = eval(textbox.get("1.0", tk.END))
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, str(result))
    except Exception as e:
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, "Error: " + str(e))

equals_button = tk.Button(window, text="=", font=("Arial", 10, "bold"), command=equals)#create the button of "=" 
equals_button.pack()#add the button to the window
equals_button.place(x=240, y=60, width=60, height=40)



window.mainloop()# Run the window