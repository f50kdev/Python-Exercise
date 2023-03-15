import requests

# Token de acesso gerado para o aplicativo
ACCESS_TOKEN = 'EAAM4YOc2JFgBANg7oYNu2anyr6XZBOcdZBU7eII0CHKqN31LJIKQmZCsrZB314nKv9AkvQeHFPBdZASSvFVZA5DElqZBv1NnuKevrPfnoicHdO0ZBgTJpkWSF2ZAU468l8MSziGs1G0oGX6yjZB8sAUMCeCWwbv4TBXVWQPplf43O9D4VHqYQB9Mp3JsYIroCAaxZC8AJOBwcMxb5m7gvKnRsdtwqMIZCgR9THh7DgRlx7NbYkWuB1VLdJhD'

# URL da API do Messenger do Facebook
FB_API_URL = 'https://graph.facebook.com/v13.0/me/messages'

def enviar_resposta(mensagem, id_usuario):
    # Montar a mensagem de resposta
    mensagem_resposta = {
        'recipient': {'id': id_usuario},
        'message': {'text': 'Olá, obrigado por entrar em contato!'}
    }

    # Enviar a mensagem de resposta usando a API do Messenger do Facebook
    response = requests.post(
        FB_API_URL,
        params={'access_token': ACCESS_TOKEN},
        json=mensagem_resposta
    )

    if response.status_code != 200:
        print('Erro ao enviar mensagem de resposta!')
        return False

    return True