import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv



def create_csv():
    headers = ['Service', 'Username', 'Password']
    test_logins = [['Hulu', 'Huluusername', 'Hulupassword'], ['Netflix', 'Netflixusername', 'Netflixpassword'], ['Disney+', 'Disney+username', 'Disney+password'], ['Amazon Prime', 'Amazonusername', 'Amazonpassword']]
    with open('test_login_info.csv', 'w', newline='') as login_file:
        csv_writer = csv.writer(login_file)
        csv_writer.writerow(headers)
        csv_writer.writerows(test_logins)


def submit_login_command():
    add_frame_confirm_label.grid(row=4, column=1)
    add_frame_service_confirm.grid(row=5, column=1)
    add_frame_username_confirm.grid(row=6, column=1)
    add_frame_password_confirm.grid(row=7, column=1)
    add_frame_confirm_no_button.grid(row=8, column=1)
    add_frame_confirm_yes_button.grid(row=9, column=1)

    new_service = add_frame_service_entry.get()
    new_username = add_frame_username_entry.get()
    new_password = add_frame_password_entry.get()

    add_frame_service_confirm['text'] = 'Service:    ' + new_service
    add_frame_username_confirm['text'] = 'Username:    ' + new_username
    add_frame_password_confirm['text'] = 'Password:    ' + new_password


def add_are_you_sure_yes():
    new_service = add_frame_service_entry.get()
    new_username = add_frame_username_entry.get()
    new_password = add_frame_password_entry.get()
    new_login = [new_service, new_username, new_password]
    with open('test_login_info.csv', 'a', newline='') as login_file:
        csv_writer = csv.writer(login_file)
        csv_writer.writerow(new_login)
    add_frame_service_entry.delete(0, tk.END)
    add_frame_username_entry.delete(0, tk.END)
    add_frame_password_entry.delete(0, tk.END)

    add_frame_confirm_label.grid_remove()
    add_frame_service_confirm.grid_remove()
    add_frame_username_confirm.grid_remove()
    add_frame_password_confirm.grid_remove()
    add_frame_confirm_no_button.grid_remove()
    add_frame_confirm_yes_button.grid_remove()


def add_are_you_sure_no():
    add_frame_confirm_label.grid_remove()
    add_frame_service_confirm.grid_remove()
    add_frame_username_confirm.grid_remove()
    add_frame_password_confirm.grid_remove()
    add_frame_confirm_no_button.grid_remove()
    add_frame_confirm_yes_button.grid_remove()

    add_frame_service_entry.delete(0, tk.END)
    add_frame_username_entry.delete(0, tk.END)
    add_frame_password_entry.delete(0, tk.END)


def delete_login_from_csv(service_to_delete):
    
    stored_logins = []
    with open('test_login_info.csv', 'r', newline='') as login_file:
        csv_read = csv.reader(login_file)
        for row in csv_read:
            stored_logins.append(row)
    
    new_logins = []

    for row in stored_logins:
        if row[0] == service_to_delete:
            continue
        else:
            new_logins.append(row)

    with open('test_login_info.csv', 'w', newline='') as login_file:
        csv_writer = csv.writer(login_file)
        csv_writer.writerows(new_logins)
    

def get_service_list():
    with open('test_login_info.csv', 'r') as login_file:
        corrected_login_file = csv.reader(login_file)

        login_list = []
        for line in corrected_login_file:
            login_list.append(line)
        
        service_list = []
        for info in login_list[1:]:
            service_list.append(info[0])
    return service_list


def generate_info_button_commmand():
    with open('test_login_info.csv', 'r') as login_file:
        corrected_login_file = csv.reader(login_file)
        login_list = []
        for line in corrected_login_file:
            login_list.append(line)

        retrieve_frame_selected_service = retrieve_frame_service_combobox.get()

        for info in login_list:
            if info[0] == retrieve_frame_selected_service:
                username = info[1]
                password = info[2]

        retrieve_frame__return_username_label['text'] = username
        retrieve_frame_return_password_label['text'] = password


def return_to_title_screen():
    retrieve_frame.grid_remove()
    add_frame.grid_remove()
    delete_frame.grid_remove()
    checkbox_frame.pack()


def checkbox_button_command():
    total_checks = retrieve_var.get() + add_var.get() + delete_var.get() + update_var.get()
    if total_checks > 1:
        checkbox_warning_label.grid(row=5, column=0)
    elif retrieve_var.get() == 1:
        checkbox_frame.pack_forget()
        retrieve_frame.grid()
    elif add_var.get() == 1:
        checkbox_frame.pack_forget()
        add_frame.grid()
    elif delete_var.get() == 1:
        checkbox_frame.pack_forget()
        delete_frame.grid()


def delete_login_from_csv():
    
    service_to_delete = delete_frame_selected_service.get()

    stored_logins = []
    with open('test_login_info.csv', 'r', newline='') as login_file:
        csv_read = csv.reader(login_file)
        for row in csv_read:
            stored_logins.append(row)
    
    new_logins = []

    for row in stored_logins:
        if row[0] == service_to_delete:
            continue
        else:
            new_logins.append(row)

    with open('test_login_info.csv', 'w', newline='') as login_file:
        csv_writer = csv.writer(login_file)
        csv_writer.writerows(new_logins)

    delete_frame_are_you_sure.grid_forget()
    delete_frame_no_button.grid_forget()
    delete_frame_yes_button.grid_forget()


def intial_delete_button():
    delete_frame_are_you_sure.grid(row=5, column=1, pady=20, padx=30)
    delete_frame_no_button.grid(row=6, column=1)
    delete_frame_yes_button.grid(row=7, column=1)


def delete_no_go_back():
    delete_frame_are_you_sure.grid_forget()
    delete_frame_no_button.grid_forget()
    delete_frame_yes_button.grid_forget()


# MASTER
login_app = tk.Tk()
login_app.title("Login Storage and Decrypter")
#login_app.resizable(width=False, height=False)
#login_app.geometry('1000x600')



# APP SELECTION CHECK BOX

checkbox_frame = tk.Frame(master=login_app)

retrieve_var = tk.IntVar()
add_var = tk.IntVar()
delete_var = tk.IntVar()
update_var = tk.IntVar()

retrieve_checkbox = tk.Checkbutton(master=checkbox_frame, text='Retrieve Login Data', variable=retrieve_var, font=('Arial Bold', 15), padx=30, offvalue=0, onvalue=1)
add_checkbox = tk.Checkbutton(master=checkbox_frame, text='Add Login Data', variable=add_var, font=('Arial Bold', 15), padx=30, offvalue=0, onvalue=1)
delete_checkbox = tk.Checkbutton(master=checkbox_frame, text='Delete Login Data', variable=delete_var, font=('Arial Bold', 15), padx=30, offvalue=0, onvalue=1)
update_checkbox = tk.Checkbutton(master=checkbox_frame, text='Update Login Data', variable=update_var, font=('Arial Bold', 15), padx=30, offvalue=0, onvalue=1)
checkbox_button = tk.Button(master=checkbox_frame, text="Go to checked box:")
checkbox_warning_label = tk.Label(master=checkbox_frame, text='Please only select one checkbox!', font=('Arial Bold', 25))

checkbox_frame.pack()
retrieve_checkbox.grid(row=0, column=0, sticky='w')
add_checkbox.grid(row=1, column=0, sticky='w')
delete_checkbox.grid(row=2, column=0, sticky='w')
update_checkbox.grid(row=3, column=0, sticky='w')
checkbox_button.grid(row=4, column=0)



# RETRIEVE APP

retrieve_frame = tk.Frame(master=login_app)
retrieve_frame['borderwidth'] = 5
retrieve_frame['relief'] = 'solid'

retrieve_frame_selected_service = tk.StringVar()
retrieve_frame_service_combobox = ttk.Combobox(master=retrieve_frame, textvariable=retrieve_frame_selected_service)
retrieve_frame_service_combobox['state'] = 'readonly'
retrieve_frame_service_combobox['values'] = get_service_list()

retrieve_frame_title_label = tk.Label(master=retrieve_frame, text="Retrieve Login", font=('Arial', 25))
retrieve_frame_username_label = tk.Label(master=retrieve_frame, text="Username:", font=('Arial', 11))
retrieve_frame_password_label = tk.Label(master=retrieve_frame, text="Password:", font=('Arial', 11))
retrieve_frame__return_username_label = tk.Label(master=retrieve_frame, text="Username Placeholder", font=('Arial Bold', 15))
retrieve_frame_return_password_label = tk.Label(master=retrieve_frame, text="Password Placeholder", font=('Arial Bold', 15))
retrieve_frame_generate_button = tk.Button(master=retrieve_frame, text="<--- Generate Info --->", command=generate_info_button_commmand)
retrieve_frame_chooseservice_label = tk.Label(master=retrieve_frame, text="Choose Service:", font=('Arial', 13))
retrieve_frame_titlescreen_button = tk.Button(master=retrieve_frame, text='Return to Title Screen')


retrieve_frame_title_label.grid(row=0, column=1, pady=5)
retrieve_frame_titlescreen_button.grid(row=0, column=0, sticky='w')
retrieve_frame_chooseservice_label.grid(row=1, column=1, pady=5)
retrieve_frame_service_combobox.grid(row=2, column=1, pady=5)
retrieve_frame_password_label.grid(row=3, column=2)
retrieve_frame_return_password_label.grid(row=4, column=2, padx=20)
retrieve_frame_username_label.grid(row=3, column=0)
retrieve_frame__return_username_label.grid(row=4, column=0, padx=20)
retrieve_frame_generate_button.grid(row=4, column=1)


# ADD INFO APP

add_frame = tk.Frame(master=login_app, borderwidth=5, relief='solid')

add_frame_title_label = tk.Label(master=add_frame, text="Add Login", font=('Arial', 25))
add_frame_service_label = tk.Label(master=add_frame, text='Enter Service:', font=('Arial', 13))
add_frame_username_label = tk.Label(master=add_frame, text='Enter Username:', font=('Arial', 13))
add_frame_password_label = tk.Label(master=add_frame, text='Enter Password:', font=('Arial', 13))
add_frame_service_entry = tk.Entry(master=add_frame, width=30)
add_frame_username_entry = tk.Entry(master=add_frame, width=30)
add_frame_password_entry = tk.Entry(master=add_frame, width=30)
add_frame_titlescreen_button = tk.Button(master=add_frame, text='Return to Title Screen')
add_frame_submit_button = tk.Button(master=add_frame, text='Submit Login Information')
add_frame_confirm_label = tk.Label(master=add_frame, text='Does this look correct?', font=('Arial Bold', 20))
add_frame_service_confirm = tk.Label(master=add_frame, font=('Arial Bold', 16), text='test')
add_frame_username_confirm = tk.Label(master=add_frame, font=('Arial Bold', 16), text='test')
add_frame_password_confirm = tk.Label(master=add_frame, font=('Arial Bold', 16), text='test')
add_frame_confirm_yes_button = tk.Button(master=add_frame, text='YES, Submit New Login')
add_frame_confirm_no_button = tk.Button(master=add_frame, text='NO, Go back')

add_frame_title_label.grid(row=0, column=1, pady=20)
add_frame_titlescreen_button.grid(row=0, column=0, sticky='nw')
add_frame_service_label.grid(row=1, column=0)
add_frame_username_label.grid(row=1, column=1)
add_frame_password_label.grid(row=1, column=2)
add_frame_service_entry.grid(row=2, column=0, padx=20)
add_frame_username_entry.grid(row=2, column=1, padx=20)
add_frame_password_entry.grid(row=2, column=2, padx=20)
add_frame_submit_button.grid(row=3, column=1, pady=30)


# DELETE INFO APP

delete_frame = tk.Frame(master=login_app, borderwidth=5, relief='solid')

delete_frame_title_label = tk.Label(master=delete_frame, text="Delete Login", font=('Arial', 25), padx=100, pady=15)
delete_frame_chooseservice_label = tk.Label(master=delete_frame, text="Choose Service to Delete:", font=('Arial', 13))

delete_frame_selected_service = tk.StringVar()
delete_frame_service_combobox = ttk.Combobox(master=delete_frame, textvariable=delete_frame_selected_service)
delete_frame_service_combobox['state'] = 'readonly'
delete_frame_service_combobox['values'] = get_service_list()

delete_frame_submit_button = ttk.Button(master=delete_frame, text='Delete this service from list')
delete_frame_yes_button = ttk.Button(master=delete_frame, text='Confirm Delete')
delete_frame_no_button = ttk.Button(master=delete_frame, text='No, go back')
delete_frame_titlescreen_button = tk.Button(master=delete_frame, text='Return to Title Screen')
delete_frame_are_you_sure = tk.Label(master=delete_frame, text='Are you sure you want to delete this login?', font=('Arial Bold', 20))
delete_frame_placeholder = tk.Frame(master=delete_frame)


delete_frame_title_label.grid(row=0, column=1)
delete_frame_titlescreen_button.grid(row=0, column=0, sticky='w')
delete_frame_placeholder.grid(row=0, column=2, sticky='e', padx=56)
delete_frame_title_label.grid(row=1, column=1)
delete_frame_chooseservice_label.grid(row=2, column=1)
delete_frame_service_combobox.grid(row=3, column=1)
delete_frame_submit_button.grid(row=4, column=1, pady=15)


# UPDATE INFO APP



# buttons that must come at the end so that all varialbes exist
checkbox_button['command'] = checkbox_button_command
retrieve_frame_titlescreen_button['command'] = return_to_title_screen
add_frame_titlescreen_button['command'] = return_to_title_screen
add_frame_submit_button['command'] = submit_login_command
add_frame_confirm_no_button['command'] = add_are_you_sure_no
add_frame_confirm_yes_button['command'] = add_are_you_sure_yes
delete_frame_submit_button['command'] = intial_delete_button
delete_frame_no_button['command'] = delete_no_go_back
delete_frame_yes_button['command'] = delete_login_from_csv
delete_frame_titlescreen_button['command'] = return_to_title_screen


login_app.mainloop()
