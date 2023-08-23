from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import webbrowser

#title
root = Tk()
root.geometry("1100x320")
root.resizable(0, 0)
root['bg'] = 'plum'
root.title('Language Translator')

title_style = ("Arial", 25, "bold")
label_style = ("Arial", 13, "bold")
input_style = ("Arial", 10)
button_style = ("Arial", 12, "bold")

# Create a custom gradient background for the title label
def create_gradient_label(parent, text, font, bg_color, fg_color1, fg_color2):
    label_frame = Frame(parent, bg=bg_color)
    label_frame.pack(pady=20, fill="both", expand=True)
    label = Label(label_frame, text=text, font=font, bg=bg_color, fg="black")  
    label.pack(side="top", pady=5)
    label.bind("<Configure>", lambda e: label.config(fg=fg_color1 if e.width > 400 else fg_color2))

# Create the gradient title label
create_gradient_label(root, "Language Translator", title_style, "plum", "white", "darkorchid")

# Navigation bar
navbar_frame = Frame(root, bg="darkorchid")
navbar_frame.pack(fill=X, padx=10, pady=5)

def navigate_to_about():
    output_txt.delete(1.0, END)
    output_txt.insert(END, "An overview of the Language Translator app. Discover its features, functionality, and purpose in simplifying language translation tasks. Welcome to a world of linguistic convenience.")

def navigate_to_help():
    output_txt.delete(1.0, END)
    output_txt.insert(END, "This is the Help page.\n\nIf you need assistance, please contact Ishita Choudhuri.")

def open_linkedin():
    webbrowser.open("https://www.linkedin.com/in/IshitaChoudhuri")

def send_email():
    webbrowser.open("mailto:ishitachoudhuri3@gmail.com")

# Styling for the buttons
button_style = ("Arial", 12, "bold")
button_bg = "darkorchid"
button_fg = "white"
button_padx = 15
button_pady = 8
hover_bg = "purple"  
hover_fg = "lightblue"   

about_button = Button(navbar_frame, text="About", font=button_style, bg=button_bg, fg=button_fg, command=navigate_to_about, activebackground=hover_bg, activeforeground=hover_fg)
about_button.pack(side="left", padx=button_padx, pady=button_pady)

help_button = Button(navbar_frame, text="Help", font=button_style, bg=button_bg, fg=button_fg, command=navigate_to_help, activebackground=hover_bg, activeforeground=hover_fg)
help_button.pack(side="left", padx=button_padx, pady=button_pady)

linkedin_button = Button(navbar_frame, text="LinkedIn", font=button_style, bg=button_bg, fg=button_fg, command=open_linkedin, activebackground=hover_bg, activeforeground=hover_fg)
linkedin_button.pack(side="right", padx=button_padx, pady=button_pady)

mail_button = Button(navbar_frame, text="Mail", font=button_style, bg=button_bg, fg=button_fg, command=send_email, activebackground=hover_bg, activeforeground=hover_fg)
mail_button.pack(side="right", padx=button_padx, pady=button_pady)

# Labels and entry for input and output text
Label(root, text="Enter your text here: ", font=label_style, bg="plum").place(x=165, y=80)
input_txt = Entry(root, width=65, font=input_style, background="cornsilk")
input_txt.place(x=40, y=130, height=30)
input_txt.get()
Label(root, text="Your translation goes here", font='arial 13 bold', bg="plum").place(x=780, y=80)
output_txt = Text(root, font='arial 10', height=5, wrap=WORD, padx=5, pady=5, width=50, background="cornsilk")
output_txt.place(x=700, y=130)

language = list(LANGUAGES.values())

style = ttk.Style()
style.theme_create("combostyle", parent="alt",
                   settings={"TCombobox":
                             {"configure":
                              {"selectbackground": "lightcyan",
                               "fieldbackground": "cornsilk",
                               "background": "white",
                               "bordercolor": "gray",
                               "darkcolor": "gray",
                               "lightcolor": "white",
                               "arrowcolor": "black"
                               }}}
                   )
style.theme_use("combostyle")

dest_lang = ttk.Combobox(root, values=language, width=22, font=input_style)
dest_lang.place(x=130, y=170)
dest_lang.set('Choose language')

def Translate():
    translator = Translator()
    translated = translator.translate(text=input_txt.get(), dest=dest_lang.get())
    output_txt.delete(1.0, END)
    output_txt.insert(END, translated.text)

trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='mediumseagreen', fg='white', activebackground='darkgreen', activeforeground='white', relief=FLAT)
trans_btn.place(x=510, y=210)

root.mainloop()
