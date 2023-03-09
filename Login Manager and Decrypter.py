import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
from cryptography.fernet import Fernet


# creates a dummy csv file for testing
def create_csv():
    headers = ['Service', 'Username', 'Password']
    test_logins = [['Hulu', 'Huluusername', 'Hulupassword'], ['Netflix', 'Netflixusername', 'Netflixpassword'], ['Disney+', 'Disney+username', 'Disney+password'], ['Amazon Prime', 'Amazonusername', 'Amazonpassword']]
    with open('test_login_info.csv', 'w', newline='') as login_file:
        csv_writer = csv.writer(login_file)
        csv_writer.writerow(headers)
        csv_writer.writerows(test_logins)

# generates and writes the crytography key to a key file on the desktop, !!Only use one time!!
def write_key():
    key = Fernet.generate_key()
    with open(r'C:\Users\zcoff\OneDrive\Desktop\key.key', "wb") as key_file:
        key_file.write(key)


# reads and returns the cryptography key
def load_key():
    with open(r'C:\Users\zcoff\OneDrive\Desktop\key.key', "rb") as key_file:
        key = key_file.read()
        return key


# grabs the returned key and saves it to the key variable, then creates the fer variable with the key that will be used to encrypt and decrypt the passwords
key = load_key()
fer = Fernet(key)


# variation on the function that creates the test login info csv, but corrected to encrypt the passwords
def write_test_csv():
    headers = ['Service', 'Username', 'Password']
    test_logins = [['Hulu', 'Huluusername', 'Hulupassword'], ['Netflix', 'Netflixusername', 'Netflixpassword'], ['Disney+', 'Disney+username', 'Disney+password'], ['Amazon Prime', 'Amazonusername', 'Amazonpassword']]
    
    for count in range(len(test_logins)):
        password = test_logins[count][2]
        encrypted_password = fer.encrypt(password.encode()).decode()
        test_logins[count][2] = encrypted_password


    with open('encrypt_test.csv', 'w', newline='') as login_file:
        csv_writer = csv.writer(login_file)
        csv_writer.writerow(headers)
        csv_writer.writerows(test_logins)


# reads the new encrypted password test info csv and returns the login list with decrypted passwords
def read_test():
        with open(r'C:\Users\zcoff\OneDrive\Desktop\CSVs\encrypt_test.csv', 'r') as login_file:
            corrected_login_file = csv.reader(login_file)
            login_list = []
            for line in corrected_login_file:
                login_list.append(line)
        
        for count in range(len(login_list)):
            if count == 0:
                continue
            else:
                password = login_list[count][2]
                decrypted_password = fer.decrypt(password.encode()).decode()
                login_list[count][2] = decrypted_password

        return login_list


# add app, when you hit the initial submit button, it loads a series of labels that show you the info you submitted, also loads the final yes and no button to actually submit the information to the csv
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

# add app, actually submits the login info to add it to the csv file
def add_are_you_sure_yes():
    new_service = add_frame_service_entry.get()
    new_username = add_frame_username_entry.get()
    new_password = add_frame_password_entry.get()
    new_login = [new_service, new_username, new_password]
    with open(r'C:\Users\zcoff\OneDrive\Desktop\CSVs\test_login_info.csv', 'a', newline='') as login_file:
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

# add app, removes the confirmation labels and resets the page, does not submit info to the csv file
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


# aquires only the list of services from the csv, used in multiple apps
def get_service_list():
    with open(r'C:\Users\zcoff\OneDrive\Desktop\CSVs\test_login_info.csv', 'r') as login_file:
        corrected_login_file = csv.reader(login_file)

        login_list = []
        for line in corrected_login_file:
            login_list.append(line)
        
        service_list = []
        for info in login_list[1:]:
            service_list.append(info[0])
    return service_list

# retrieve app, generates the username and password of the service selected from the combo box
def generate_info_button_commmand():
    with open(r'C:\Users\zcoff\OneDrive\Desktop\CSVs\test_login_info.csv', 'r') as login_file:
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

# used for all apps, returns you to the orignal app selection screen
def return_to_title_screen():
    retrieve_frame.grid_remove()
    add_frame.grid_remove()
    delete_frame.grid_remove()
    update_frame.grid_remove()
    checkbox_frame.pack()

# loads the selected app from the checked box, and gives you an error message if you try to load more than one
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
    elif update_var.get() == 1:
        checkbox_frame.pack_forget()
        update_frame.grid()

# delete app, is the final button to delete a service from the csv list, takes the selected service from the combo box, and deletes that from the csv file
def delete_login_from_csv():
    
    service_to_delete = delete_frame_selected_service.get()

    stored_logins = []
    with open(r'C:\Users\zcoff\OneDrive\Desktop\CSVs\test_login_info.csv', 'r', newline='') as login_file:
        csv_read = csv.reader(login_file)
        for row in csv_read:
            stored_logins.append(row)
    
    new_logins = []

    for row in stored_logins:
        if row[0] == service_to_delete:
            continue
        else:
            new_logins.append(row)

    with open(r'C:\Users\zcoff\OneDrive\Desktop\CSVs\test_login_info.csv', 'w', newline='') as login_file:
        csv_writer = csv.writer(login_file)
        csv_writer.writerows(new_logins)

    delete_frame_are_you_sure.grid_forget()
    delete_frame_no_button.grid_forget()
    delete_frame_yes_button.grid_forget()

# delete app, the first delete service info button, which loads the actual delete button and confirmation info
def intial_delete_button():
    delete_frame_are_you_sure.grid(row=5, column=1, pady=20, padx=30)
    delete_frame_no_button.grid(row=6, column=1)
    delete_frame_yes_button.grid(row=7, column=1)

# delete app, resets the delete page if you choose no to go ahead with deletion 
def delete_no_go_back():
    delete_frame_are_you_sure.grid_forget()
    delete_frame_no_button.grid_forget()
    delete_frame_yes_button.grid_forget()

# update app, is the initial update button, that when pressed, loads the confirmation labels and the actual yes and no buttons
def update_button():
    update_frame_correct_label.grid(row=8, column=1)
    update_frame_confirm_label.grid(row=9, column=1)
    update_frame_yes_button.grid(row=10, column=1)
    update_frame_no_button.grid(row=11, column=1)

    update_frame_confirm_label['text'] = 'New ' + update_frame_what_combobox.get() + ': ' + update_frame_new_entry.get()

# update app, resets the update app if you do not decide to go ahead with updating the info
def update_no_button():
    update_frame_correct_label.grid_remove()
    update_frame_confirm_label.grid_remove()
    update_frame_yes_button.grid_remove()
    update_frame_no_button.grid_remove()

# update app, the actual update info button after youve seen the confirmation labels
def update_yes_button():

    stored_logins = []

    with open(r'C:\Users\zcoff\OneDrive\Desktop\CSVs\test_login_info.csv', 'r', newline='') as login_file:
        csv_read = csv.reader(login_file)
        for row in csv_read:
            stored_logins.append(row)
    
    new_logins = []
    
    stored_service = ''
    stored_username = ''
    stored_password = ''

    for row in stored_logins:
        if row[0] == update_frame_service_combobox.get():
            stored_service = row[0]
            stored_username = row[1]
            stored_password = row[2]
            continue
        else:
            new_logins.append(row)

    if update_frame_what_combobox.get() == 'Password':
        new_login_row = [stored_service, stored_username, update_frame_new_entry.get()]
    elif update_frame_what_combobox.get() == 'Username':
        new_login_row = [stored_service, update_frame_new_entry.get(), stored_password]
    elif update_frame_what_combobox.get() == 'Service':
        new_login_row = [update_frame_new_entry.get(), stored_username, stored_password]
    
    new_logins.append(new_login_row)

    with open(r'C:\Users\zcoff\OneDrive\Desktop\CSVs\test_login_info.csv', 'w', newline='') as login_file:
        csv_writer = csv.writer(login_file)
        csv_writer.writerows(new_logins)

    
    

    


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

update_frame = tk.Frame(master=login_app, borderwidth=5, relief='solid')

update_frame_title_label = tk.Label(master=update_frame, text='Update Login Info', font=('Arial Bold', 25))
update_frame_wherefrom_label = tk.Label(master=update_frame, text='What do you need to update?')
update_frame_what_combobox = ttk.Combobox(master=update_frame, values=['Service', 'Username', 'Password'])
update_frame_from_lable = tk.Label(master=update_frame, text='For which Service?')
update_frame_service_combobox = ttk.Combobox(master=update_frame)
update_frame_service_combobox['values'] = get_service_list()
update_frame_enter_new_label = tk.Label(master=update_frame, text='Enter new Service/Username/Password:')
update_frame_new_entry = tk.Entry(master=update_frame, width=30)
update_frame_update_info_button = tk.Button(master=update_frame,text='Update Info:')
update_frame_titlescreen_button = tk.Button(master=update_frame,text='Return to Title Screen')
update_frame_correct_label = tk.Label(master=update_frame, text='Does this look correct?')
update_frame_confirm_label = tk.Label(master=update_frame, text='New Password: Password')
update_frame_yes_button = tk.Button(master=update_frame, text='Yes')
update_frame_no_button = tk.Button(master=update_frame, text='No')
update_frame_placeholder = tk.Frame(master=update_frame)


update_frame_title_label.grid(row=0, column=1, padx=100)
update_frame_wherefrom_label.grid(row=1, column=1)
update_frame_what_combobox.grid(row=2, column=1)
update_frame_from_lable.grid(row=3, column=1)
update_frame_service_combobox.grid(row=4, column=1)
update_frame_enter_new_label.grid(row=5, column=1)
update_frame_new_entry.grid(row=6, column=1)
update_frame_update_info_button.grid(row=7, column=1)
update_frame_titlescreen_button.grid(row=0, column=0)
update_frame_placeholder.grid(row=0, column=2, padx=56)




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
update_frame_titlescreen_button['command'] = return_to_title_screen
update_frame_update_info_button['command'] = update_button
update_frame_no_button['command'] = update_no_button
update_frame_yes_button['command'] = update_yes_button

login_app.mainloop()
