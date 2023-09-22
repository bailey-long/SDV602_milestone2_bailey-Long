import PySimpleGUI as sg
import subprocess
import sys

# Define dummy accounts (replace with your actual account information)
dummy_accounts = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "user3", "password": "password3"},
    {"username": "admin", "password": "admin"}
]

# Define the layout for the login screen
login_layout = [
    [sg.Text("Login")],
    [sg.Text("Username:", size=(10, 1)), sg.InputText(key="-USERNAME-", size=(20, 1), focus=True)],
    [sg.Text("Password:", size=(10, 1)), sg.InputText(key="-PASSWORD-", size=(20, 1), password_char="*")],
    [sg.Button("Login")]
]

# Create a function for the main screen
def main_screen(username):
    return [
        [sg.Text(f"Welcome, {username}!")],
        [sg.Button("Screen 1"), sg.Button("Screen 2"), sg.Button("Screen 3")],
        [sg.Button("Logout")]
    ]

# Create the main window
window = sg.Window("App", login_layout, resizable=True, finalize=True)

# Get the path to the Python interpreter within the virtual environment
python_exe = sys.executable

# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Login":
        username = values["-USERNAME-"]
        password = values["-PASSWORD-"]

        # Check if the entered username and password match any of the dummy accounts
        authenticated = False
        for account in dummy_accounts:
            if account["username"] == username and account["password"] == password:
                authenticated = True
                break

        if authenticated:
            window.close()
            main_window = sg.Window("App", main_screen(username), resizable=True)
            while True:
                event, values = main_window.read()

                if event == sg.WIN_CLOSED or event == "Logout":
                    main_window.close()
                    break
                elif event == "Screen 1":
                    subprocess.run([python_exe, "des-one.py", "--username", username])

                elif event == "Screen 2":
                    sg.popup("You are on Screen 2")
                elif event == "Screen 3":
                    sg.popup("You are on Screen 3")
        else:
            sg.popup_error("Invalid username or password")

# Close the main window
window.close()
