"""
Started June 29th, 2018...
Version 1; sucked ass and was poorly written by me. Replaced by version 2.
Version 2 (below); includes updated menu, message history, a scroll bar, more functionality, and cleaner code. 
"""
# Important code, totally not fuckable.
from tkinter import *
m_win = Tk(className = " Chatbox App")
m_win.resizable(False, False)
""" Fuckable code below... """
# Login Window
def do_login():
    # Window Creation, naming, and resize availability.
    login = Toplevel(m_win, width = 80, height = 40)
    login.title("Login")
    login.resizable(False, False)
    Label(login, text="Enter a name:").grid(row = 1) # Label creation, left.
    usernameGet = Entry(login) # Creates entry and assigns to var.
    usernameGet.grid(row = 1, column = 1) # Places entry in the middle.
    # Checks name; if good, closes login window.
    def login_ok():
        global name
        name = usernameGet.get()
        if name != "":
            login.destroy()
    usernameGet.bind('<Return>', lambda e: login_ok())
    Button(login, text="Ok", command = login_ok).grid(row = 1, column = 2) # Makes button that uses the login function, sets it to the right.
    # Brings login window to front; User cannot focus on main window, must focus this one.
    login.grab_set()
    login.focus_set()
    usernameGet.focus_set()
    login.lift()
# Main Window, ordered top down, left to right; starting with the menu and menu items.
menu_bar = Menu(m_win) # Defines the 'menu_bar' variable as a menu belonging to the main window
m_win.config(menu = menu_bar) # Adds the variable 'menu_bar' to the m_win, main window.
app_menu = Menu(menu_bar, tearoff = 0) # Defines the 'app_menu' variable as a menu belonging to the menu bar.
user_menu = Menu(menu_bar, tearoff = 0) # Defines the 'user_menu' variable as a menu belonging to the menu bar.
def clear_msg_hist(): # Function that clears the message box.
    msg_history.configure(state = NORMAL)
    msg_history.delete('1.0', 'end')
    msg_history.configure(state = DISABLED)
    msg_history.see('end')
def change_username(): # Change username function; modified copy-paste of login function.
    change_name = Toplevel(m_win, width = 80, height = 40)
    change_name.title("Change Username")
    change_name.resizable(False, False)
    Label(change_name, text="Enter a name:").grid(row = 1)
    usernameGet = Entry(change_name)
    usernameGet.grid(row = 1, column = 1)
    def name_change_ok():
        global name
        name = usernameGet.get()
        if name != "":
            change_name.destroy()
    def cancel_name_change():
        change_name.destroy()
    usernameGet.bind('<Return>', lambda e: name_change_ok())
    Button(change_name, text = "Ok", command = name_change_ok).grid(row = 1, column = 2)
    Button(change_name, text = "Cancel", command = cancel_name_change).grid(row = 1, column = 3)
app_menu.add_command(label = 'Clear Chat', command = clear_msg_hist) # Adds a menu option to the app_menu; makes it able to clear the chat log.
app_menu.add_command(label = 'Exit', command = m_win.quit) # Adds a menu option to the app_menu; makes it able to exit the program.
user_menu.add_command(label = 'Change Name', command = change_username) # Adds a menu option to the user_menu; makes it able to change username.
menu_bar.add_cascade(label = 'App', menu = app_menu) # Adds the app_menu variable to the menu_bar menu and makeks it usable.
menu_bar.add_cascade(label = 'User', menu = user_menu) # Adds the user_menu variable to the menu_bar menu and makeks it usable.
# Message history and scrollbar.
msg_history = Text(m_win, font = 'TkDefaultFont', state = DISABLED)
msg_history.grid(row = 0, sticky='nsew')
scroller = Scrollbar(m_win, command = msg_history.yview)
scroller.grid(row = 0, column = 1, sticky = 'ns')
msg_history.config(yscrollcommand = scroller.set)
# Makes the bold_font (Used in the 'clearandsend' function) and configures the tags of 'msg_history' with it.
from tkinter.font import Font
bold_font = Font(font='TkDefaultFont')
bold_font.configure(weight='bold')
msg_history.tag_config('name', font = bold_font)
# Textbox.
msg_box = Entry(m_win)
msg_box.grid(row=1, sticky='ew')
# Send line function, key binding for send, and send button.
exit_cognates = ['Exit', 'exit', 'Quit', 'quit']
kenobi_cognates = ['Hello there!', 'hello there!', 'Allo there!',
'allo there!', 'Ello there!', 'ello there!']
windu_cognates = ["You're under arrest, Chancellor!", "you're under arrest, chancellor!",
"The senate will decide your fate!", "the senate will decide your fate!"]
palpatine_cognates = ["Kill him!", "kill him!"]
def clearandsend():
    msg = msg_box.get()
    msg_box.delete(0, 'end')
    if msg == "Clear" or msg == "clear":
        clear_msg_hist()
    elif msg in exit_cognates:
        m_win.quit()
    elif msg in kenobi_cognates:
        msg_history.configure(state = NORMAL)
        msg_history.insert('end', f'{name}: ', 'name')
        msg_history.insert('end', f'{msg}\n')
        msg_history.insert('end', 'General Grievous: ', 'name')
        msg_history.insert('end', 'General Kenobi!\n')
        msg_history.configure(state = DISABLED)
        msg_history.see('end')
    elif msg in windu_cognates:
        msg_history.configure(state = NORMAL)
        msg_history.insert('end', f'{name}: ', 'name')
        msg_history.insert('end', f'{msg}\n')
        msg_history.insert('end', 'Sheev Palpatine: ', 'name')
        msg_history.insert('end', 'I am the Senate!\n')
        msg_history.configure(state = DISABLED)
        msg_history.see('end')
    elif msg in palpatine_cognates:
        msg_history.configure(state = NORMAL)
        msg_history.insert('end', f'{name}: ', 'name')
        msg_history.insert('end', f'{msg}\n')
        msg_history.insert('end', 'Sheev Palpatine: ', 'name')
        msg_history.insert('end', 'Dew it!\n')
        msg_history.configure(state = DISABLED)
        msg_history.see('end')
    elif msg != "":
        msg_history.configure(state = NORMAL)
        msg_history.insert('end', f'{name}: ', 'name')
        msg_history.insert('end', f'{msg}\n')
        msg_history.configure(state = DISABLED)
        msg_history.see('end')
msg_box.bind('<Return>', lambda f: clearandsend())
msg_send = Button(m_win, text = "Send", command = clearandsend)
msg_send = msg_send.grid(row = 1, column = 1)
# Code that runs the program.
m_win.after(1, do_login)
msg_box.focus_set()
m_win.grid_columnconfigure(1, weight=1)
m_win.grid_rowconfigure(0,weight=1)
m_win.mainloop()

# Things to fix...
    # Scrollbar is too thin; have to make it wider. Perhaps `fill()` would work?
# Features to add...
    # Ability to add images, gifs, etc.
    # Save chat logs and user info like avatar, name, etc.
    # Make it look beauty
    # Network capability