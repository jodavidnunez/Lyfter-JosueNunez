from menu import menu


try:
    if __name__ == "__main__":
        menu()
except KeyboardInterrupt:
    print(f'\n-E-(main.py:main): Manual interruption by user.')