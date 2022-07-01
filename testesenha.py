import json
import logging
import requests
from webex_bot.models.command import Command
# -- coding: utf-8 --
import sys

log = logging.getLogger(__name__)


with open("./cardinicial-card.json", "r") as card:
    INPUT_CARD = json.load(card)

class RedefinirSenha(Command):
    def __init__(self):
        super().__init__(
            command_keyword="senha",
            help_message="Clique aqui e receba as instruções para redefinir a senha.",
            card=INPUT_CARD,
        )
    def execute(self, message, attachment_actions, activity):
        senha = attachment_actions.submit['senha']

        response = requests.get()
        senha = response.json()

        #return Resposta1  
        
#Adiciondo parametro encoding="utf-8" para formatar em pt-br e mostrar "acentuação"
with open("./senha-card.json", "r", encoding="utf-8") as card:
    INPUT_CARD = json.load(card)


class RespostaSenha(Command):
    def __init__(self):
        super().__init__(
            card=INPUT_CARD
        )
    
    def execute(self, message, attachment_actions, activity):
        senha = message['senha']
        