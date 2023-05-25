import pathlib
import PySimpleGUI as sg


def make_window():
    # cwd = pathlib.Path.cwd()
    home = pathlib.Path.home()

    window_title = "Validate Stems"
    text_width = 30
    text_height = 1

    init_dir = home

    sg.theme("DarkBlack")

    # top_left_column = [
    #     [sg.Text("Select folder with stems:", size=(text_width, text_height))],
    # ]

    # top_right_column = [
    #     [sg.FolderBrowse(initial_folder=init_dir)],
    # ]

    # bottom_left_column = [
    #     [
    #         sg.Text(
    #             "Select operation to perform\non silent stems:", size=(text_width, 2)
    #         )
    #     ],
    # ]

    # bottom_right_column = [
    #     # [sg.Radio('Move stems to their own folder',  'OPERATION', default=True,  key='-MOVE-')],
    #     # [sg.Radio('Don\'t move, and instead rename', 'OPERATION', default=False, key='-RENAME-')],
    #     [sg.Radio("Rename", "OPERATION", default=True, key="-RENAME-")],
    #     [sg.Radio("Move", "OPERATION", default=False, key="-MOVE-")],
    # ]

    layout = [
        # [
        #     sg.Col(top_left_column, element_justification="left", key="-T_L_COL-"),
        #     sg.Col(top_right_column, element_justification="right", key="-T_R_COL-"),
        # ],
        # [
        #     sg.Col(bottom_left_column, element_justification="left", key="-B_L_COL-"),
        #     sg.Col(bottom_right_column, element_justification="left", key="-B_R_COL-"),
        # ],
        [sg.HorizontalSeparator()],
        [
            sg.OK(),
            sg.Exit(),
        ],
    ]

    window = sg.Window(window_title, layout, resizable=False, finalize=True)

    return window

