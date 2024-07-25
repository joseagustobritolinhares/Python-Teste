from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reddit')
layout =[
    [sg.Text('Usuario'),sg.Input(Key='Usuario')],
    [sg.Text('senha'),sg.Input(Key='senha',password_char='*')],
    [sg.Checkbox('Salvar informações de login')],
    [sg.Button('Entrar')]
]
janela = sg.Window('Tela de Login ', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break 
    if eventos == 'Entrar':
        if valores['usuario'] == 'augusto' and valores['senha'] == '123456': 
            print('bem vindo ao meu codigo python')