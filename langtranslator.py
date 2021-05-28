from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# create a display window
root=Tk()
root.geometry('1080x500')
root.config(bg='ghost white')
root.title("Parul--Language Translator")
root.iconbitmap(r"C:\Users\Parul Gupta\Desktop\python\translator.ico")
Label(root, text = "LANGUAGE TRANSLATOR", font="arial 20 bold", bg="white smoke").pack()
Label(root, text="Parul Project", font="arial 20 bold", bg="white smoke", width="20").pack(side='bottom')

# input-output text widget
Label(root, text="Enter Text", font="arial 13 bold", bg="white smoke").place(x=200, y=60)
inputText=Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
inputText.place(x=30, y=100)

Label(root, text="Output", font="arial 13 bold", bg="white smoke").place(x=780, y=60)
outputText=Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
outputText.place(x=600, y=100)

# combobox to select language
language=list(LANGUAGES.values())
input_lang=ttk.Combobox(root, values=language, width=22)
input_lang.place(x=20, y=60)
input_lang.set('choose input language')

output_lang=ttk.Combobox(root, values=language, width=22)
output_lang.place(x=890, y=60)
output_lang.set('choose output language')

def translate():
	translator=Translator()
	translated=translator.translate(text=inputText.get(1.0, END), src=input_lang.get(), dest=output_lang.get())
	outputText.delete(1.0, END)
	outputText.insert(END, translated.text)

# translate button
trans_btn=Button(root, text="Translate", font='arial 12 bold', pady=5, command=translate, bg='royal blue1', activebackground='skyblue')
trans_btn.place(x=490, y=180)
root.mainloop()


