import os
import PySimpleGUI as sg


def notify(message):
    sg.Popup(message)

def main():
    layout = [
        [sg.Text('Choose a background picture:')],
        [sg.Input(), sg.FileBrowse()],
        [sg.Button('Change Background', key='--change--'), sg.Button('Exit', key='--exit--')],
        [sg.Text('Background Changer Python')]
    ]

    window = sg.Window('Background Changer Python', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '--change--':
            command = "gsettings set org.gnome.desktop.background picture-uri file:" + values[0]
            os.system(command)
            window.hide()
            notify('Background changed successfully!')
            window.UnHide()
        elif event == '--exit--':
            break


if __name__ == '__main__':
    main()
