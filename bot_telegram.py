import telebot

# Tenho que colocar em um .env
CHAVE_API = "6566152384:AAH4BEDjifnavWLPJNkNKAmKamirU6iFf3E"

bot = telebot.TeleBot(CHAVE_API)

Estoques = {"Hamburguer": 100, "Pizza": 250, "Sobremesa":25, "Salada":10}

agradecimento = "Agradecemos Pela Preferência!"

# Função para encerrar
@bot.message_handler(commands=["encerrar"])
def encerrar(msg):
    bot.reply_to(msg, agradecimento)

# Função para pedir pizza
@bot.message_handler(commands=["pizza"])
def pizza(msg):
    if Estoques["Pizza"] < 1:
        bot.reply_to(msg,f"Infelizmente nosso estoque de {msg.text[1:]} está vazio. :(\n Clique aqui em /iniciar para escolher outro pedido.\n Ou aqui em /encerrar para encerrar o pedido.")
        return

    bot.reply_to(msg,"Entendido! Nosso cozinheiro já foi avisado.\nTempo de espera é de 30 minutos.\n" + agradecimento)

    Estoques["Pizza"] -= 1

# Função para pedir hamburguer
@bot.message_handler(commands=["hamburguer"])
def hamburguer(msg):
    if Estoques["Hamburguer"] < 1:
        bot.reply_to(msg,f"Infelizmente nosso estoque de {msg.text[1:]} está vazio. :(\n Clique aqui em /iniciar para escolher outro pedido.\n Ou aqui em /encerrar para encerrar o pedido.")
        return

    bot.reply_to(msg,"Entendido! Nosso cozinheiro já foi avisado. Saindo o Melhor hamburguer já feito.\nTempo de espera é de 15 minutos.\n" + agradecimento)

    Estoques["Hamburguer"] -= 1

# Função para pedir sobremesa
@bot.message_handler(commands=["sobremesa"])
def sobremesa(msg):
    if Estoques["Sobremesa"] < 1:
        bot.reply_to(msg,f"Infelizmente nosso estoque de {msg.text[1:]} está vazio. :(\n Clique aqui em /iniciar para escolher outro pedido.\n Ou aqui em /encerrar para encerrar o pedido.")
        return

    bot.reply_to(msg,"Entendido! A sobremesa já está pronta.\n" + agradecimento)

    Estoques["Sobremesa"] -= 1

# Função para pedir salada
@bot.message_handler(commands=["salada"])
def salada(msg):
    if Estoques["Salada"] < 1:
        bot.reply_to(msg,f"Infelizmente nosso estoque de {msg.text[1:]} está vazio. :(\n Clique aqui em /iniciar para escolher outro pedido.\n Ou aqui em /encerrar para encerrar o pedido.")
        return
    
    bot.reply_to(msg,"Entendido! Nosso cozinheiro já foi avisado. Saindo a Melhor Salada do mundo.\nTempo de espera é de 5 minutos.\n" + agradecimento)

    Estoques["Salada"] -= 1


# Função para opção1
@bot.message_handler(commands=["opcao1"])
def opcao1(msg):
   texto = """
    O que voçê deseja? (Clique em uma opção)
    /pizza Pizza
    /hamburguer Hamburguer
    /sobremesa Sobremesa
    /salada Salada"""
   bot.send_message(msg.chat.id, texto)

# Função para opção2
@bot.message_handler(commands=["opcao2"])
def opcao2(msg):
    bot.send_message(msg.chat.id, "Para enviar uma reclamação, envie um e-mail para:\n loremimpsum@gmail.com \nOu entre em contato com o nosso suporte em:\n 99 91234-5678")

# Função para opção3
@bot.message_handler(commands=["opcao3"])
def opcao3(msg):
    bot.send_message(msg.chat.id, "Valeu! O cozinheiro mandou um abraço de volta")

# Função padrão
def verificar(msg):
    return True

@bot.message_handler(func=verificar)
def responder(msg):
    texto = """
Escolha uma opção para continuar (Clique no item:)
        /opcao1 Fazer um pedido
        /opcao2 Fazer uma reclamação
        /opcao3 Mandar um abraço para o cozinheiro
OBS: Responder qualquer outra mensagem não vai funcionar, clique em uma das opções"""

    bot.reply_to(msg, texto)

# Função para o bot continuar rodando
bot.polling()