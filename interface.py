import PySimpleGUI as sg
from app import maps

cidades_cadastradas = ['Curitiba/PR', 'Londrina/PR', 'União da Vitória/PR', 'Foz do Iguaçu/PR', 'Joinville/SC', 'Chapecó/SC', 'Porto Alegre/RS', 'Uruguaiana/RS', 'Pelotas/RS']

layout = [
    [sg.Text('Selecione a cidade de origem:')],
    [sg.Combo(cidades_cadastradas, key='origem')],
    [sg.Text('Selecione a cidade de destino:')],
    [sg.Combo(cidades_cadastradas, key='destino')],
    [sg.Button('Gerar Caminho')],
]

window = sg.Window('Seleção de Cidades', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Gerar Caminho':
        cidade_origem = values['origem']
        cidade_destino = values['destino']

        if cidade_origem and cidade_destino:
            maps(cidade_origem, cidade_destino)
            
        else:
            print('Por favor, selecione cidade de origem e destino.')

window.close()
