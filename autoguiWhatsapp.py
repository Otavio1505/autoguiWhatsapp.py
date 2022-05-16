import time
import pyautogui as p
print('='*30,'TRANSMISSOR DE MENSAGEM WHATSAPP','='*30)
print('Enviar mensagem para:')
print('[1] Contato único\n'
      '[2] Contatos múltiplos')
print()
choice = int(input('Escolha a opção de destinatário da mensagem: '))

if choice == 1:
    contato = str(input('Contato: '))
    mensagem = str(input('Mensagem: '))
    p.alert('Iniciando o programa.')
    p.hotkey('win','d')
    time.sleep(1)
    p.write('Microsoft Edge')
    time.sleep(0.5)
    p.press('enter')
    time.sleep(1)
    p.hotkey('win','up')
    time.sleep(3)
    p.write('https://web.whatsapp.com/')
    p.press(['enter'])
    time.sleep(8)

    time.sleep(0.5)
    p.click('zap1.png')
    time.sleep(0.5)
    p.write(f'{contato}') #<-- Basta digitar o nome do contato para que seja destinado o macro
    time.sleep(0.5)
    p.press('enter')
    time.sleep(0.5)

    p.write(f'{mensagem}') #digita e envia a mensagem para o contato
    p.press('enter')
    time.sleep(2)
    p.alert('Programa encerrado')
if choice == 2:
    nc = int(input('Digite a quantidade de contatos destinatários: '))
    contato = []
    print()
    print('[Digite o nome do contato sem a presença de acentuações]')
    print()
    for c in range(nc):
        contato.append(input(f'Contato [{c+1}]: '))

    mensagem = str(input('Mensagem: '))
    p.alert('Iniciando o programa.')
    for c in range(nc):
        if c ==0:
            p.hotkey('win', 'd')
            time.sleep(1)
            p.write('Microsoft Edge')
            time.sleep(1)
            p.press('enter')
            time.sleep(1)
            p.hotkey('win', 'up')
            time.sleep(4)
            p.write('https://web.whatsapp.com/')
            p.press(['enter'])
            time.sleep(8)

            time.sleep(0.5)
            p.click('zap1.png')
            time.sleep(0.5)
            p.write(f'{contato[c]}')  # <-- Basta digitar o nome do contato para que seja destinado o macro
            time.sleep(0.5)
            p.press('enter')
            time.sleep(0.5)

            p.write(f'{mensagem}')  # digita e envia a mensagem para o contato
            p.press('enter')
            p.press(['esc','esc'])

        elif c > 0:
            time.sleep(0.5)
            p.click('zap1.png')
            time.sleep(0.5)
            p.write(f'{contato[c]}')  # <-- Basta digitar o nome do contato para que seja destinado o macro
            time.sleep(0.5)
            p.press('enter')
            time.sleep(0.5)

            p.write(f'{mensagem}')  # digita e envia a mensagem para o contato
            p.press('enter')
            time.sleep(1)
            p.press(['esc', 'esc'])

time.sleep(2)
p.alert('Programa encerrado')
