import csv





def create_csv():
    headers = ['Service', 'Username', 'Password']
    test_logins = [['Hulu', 'Huluusername', 'Hulupassword'], ['Netflix', 'Netflixusername', 'Netflixpassword'], ['Disney+', 'Disney+username', 'Disney+password']]
    with open('test_login_info.csv', 'w', newline='') as login_file:
        csv_writer = csv.writer(login_file)
        csv_writer.writerow(headers)
        csv_writer.writerows(test_logins)





def take_logins(service, username, password):
    new_login_info = [service, username, password]
    with open('test_login_info.csv', 'a', newline='') as login_file:
        csv_writer = csv.writer(login_file)
        csv_writer.writerow(new_login_info)

create_csv()



with open('test_login_info.csv', 'r') as login_file:
    corrected_login_file = csv.reader(login_file)

    for line in corrected_login_file:
        print(line[1])

    



