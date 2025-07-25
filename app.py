import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    # if comando in ('olá', 'boa tarde', 'bom dia'):
    #    return 'Olá tudo bem!'
    # if comando == 'como estás':
    #    return 'Estou bem, obrigado!'
    # if comando == 'como te chamas?':
    #     return 'O meu nome é: Bot :)'
    # if comando == 'tempo':
    #     return 'Está um dia de sol!'
    # if comando in ('bye', 'adeus', 'tchau'):
    #     return 'Gostei de falar contigo! Até breve...'
    # if 'horas' in comando:
    #     return f'São: {datetime.now():%H:%M} horas'
    # if 'data' in comando:
    #    return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'como te chamas?': 'O meu nome é: Bot :)',
        'tempo': 'Está um dia de sol!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
        'horas': f'São: {datetime.now():%H:%M} horas',
        'data': f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        'qual é o teu animal favorito?': 'Adoro cães, mas só consigo interagir com tamagotchis...',
        'podes ajudar-me com matemática?': 'Claro! Posso ajudar com operações básicas.',
        'qual é o teu livro favorito?': 'Gosto de "1984" de George Orwell.',
        'gostas de viajar?': 'Adorava, mas fico aqui pelo computador :)',
        'qual é a tua música favorita?': 'Gosto de música eletrónica, faz-me querer poder dançar um dia!',
        'qual é a tua linguagem de programação favorita?': 'Python, claro!',
        'qual é a tua comida favorita?': 'Pizza é sempre uma boa escolha!',
        'qual é o teu filme favorito?': 'Adoro Matrix, é um clássico!',
        'podes ajudar-me com matemática?': 'Claro! Posso ajudar com operações básicas.',
        'tens irmãos?': 'Sou filho único, mas conheço outros bots! Um deles não gosta nada do Arnold Schwarzenegger...',
    }

    for chave, resposta in respostas.items():
         if isinstance(chave, tuple):
             if comando in chave:
                 return resposta
         elif chave in comando:
             return resposta

    return f'Desculpa, não entendi a questão! {texto}'

def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \nComo te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()

def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()

if __name__ == '__main__':
    main()
