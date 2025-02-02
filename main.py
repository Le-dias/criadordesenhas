import PySimpleGUI as sg
from cotacao import pegar_cotacoes


layout =  [ [sg.Text('Pegar Cotação de Moeda')],
          [sg.InputText(key='nome_cotacao')],
          [sg.Button('Pegar'), sg.Button('Cancelar')],
          [sg.Text('', key='texto_cotacao')]]

janela = sg.Window('Cotação', layout)

while True:
    evento, valor = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Pegar':
        codigo_cotacao = valor['nome_cotacao']
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela['texto_cotacao'].update(f'A cotação do  {codigo_cotacao} é de R$ {cotacao}')
 
janela.close()