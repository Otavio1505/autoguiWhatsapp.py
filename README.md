# autoguiWhatsapp.py
Automação capaz de enviar a mesma mensagem para um ou vários contatos ao mesmo tempo.

# Sobre o Projeto
Projeto pessoal, desenvolvido após aprendizados sobre a biblioteca PyAutoGui. A utilidade do programa permite enviar a mesma mensagem para um ou vários contatos ao mesmo tempo. De forma automática o 'bot' irá abrir o site: https://web.whatsapp.com/ e irá entrar em uma estrutura de repetição que filtrará os nomes dos contatos em sua 'Lista de contatos' no Whatsapp e o enviará a mensagem. Caso o usuário deseje enviar a mesma mensagem para Contatos Múltiplos, a cada mensagem enviada, o laço se repetirá até que a mensagem tenha sido enviada para todos os contatos desejados pelo usuário.

# Como funciona?
Primeiramente, o programa fará uso do import da biblioteca: PyAutoGui, que será responsável pela automação, juntamente com o import da biblioteca: Time, que auxiliará a automação, sinalizando os momentos de pause/espera naturais entre os comandos.

Ao iniciar o programa, será aberto um Menu interativo com o usuário, na qual o usuário deverá indicar, se ele deseja enviar uma mensagem para um Contato Único, ou Contatos Múltiplos. 

![a](https://user-images.githubusercontent.com/84475339/168650992-044a2d70-7c11-41b0-b52b-1f5e323010b6.png)

Caso seja informado a preferência por Contato Único, será aberto apenas 2 inputs, onde o usuário precisará informar o nome do Contato (primeiro input) e a mensagem que deseja enviar (segundo input)

![a](https://user-images.githubusercontent.com/84475339/168651145-9b2a5935-93c6-4d35-83f0-43750743449f.png)

Se o usuário desejar enviar mensagens para Contatos Múltiplos, será aberto um input alternativo, na qual o usuário deverá inserir a quantidade de contatos destinatários, havendo assim um entendimento do programa, de quantos inputs de contatos, deverão ser abertos. Após o usuário informar a quantidade de contatos destinatários e preencher os inputs de contato, será aberto o input de mensagem onde o usuário deverá preencher o campo com a mensagem que deseja enviar aos contatos.

![a](https://user-images.githubusercontent.com/84475339/168652440-185948dc-db0e-49f9-9572-86da3e7c9d66.png)

Após a confirmação destes inputs, o programa dará início ao processo de automação, que será compostos por 4 passos.

1. O programa abrirá a Área de Trabalho, e através do botão Windows, abrirá o navegador.

2. Com o navegador aberto, o programa irá acessar a URL: https://web.whatsapp.com. (É necessário que haja o login automático na conta do remetente das mensagens).

3. Na tela inicial do site, o mouse de forma automática irá localizar e abrir a 'Lista de contatos' e irá pesquisar pelo nome de contato inserido no input antes do início da automação.

4. Com o contato localizado, a conversa será aberta e a mensagem (informada no input) será escrita e enviada.

Caso o usuário tenha informado que deseja Contatos Múltiplos, os 3 passos inicias serão feitos apenas uma vez, havendo a repetição apenas para o Passo 4, que irá se repetir conforme a quantidade de contatos que o usuário deseja enviar.

# Saída

1. Saída para: Contato Único

![contatouni auto](https://user-images.githubusercontent.com/84475339/168656823-664d4903-eb51-4839-8e67-bcb0ed453d77.png)

2. Saída para: Contatos Múltiplos

![multicontatos auto](https://user-images.githubusercontent.com/84475339/168656288-5682bf6e-2505-45ee-83db-3d6782f5bf42.png)

