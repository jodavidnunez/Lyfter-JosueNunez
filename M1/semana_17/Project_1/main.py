from GUI import create_main_window

try:
    if __name__ == "__main__":
        create_main_window()
except KeyboardInterrupt:
    print(f'\n-E-(GUI.py:create_main_window): Manual interruption by user.')