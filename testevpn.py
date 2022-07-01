import json
import logging
import requests
from webex_bot.models.command import Command


log = logging.getLogger(__name__)

#Adiciondo parametro encoding="utf-8" para formatar em pt-br e mostrar "acentuação"
with open("./vpn-card.json", "r", encoding="utf-8") as card:
    INPUT_CARD = json.load(card)

class RespostaVPN(Command):
    def __init__(self):
        super().__init__(
            command_keyword="vpn",
            help_message="Clique aqui e receba as instruções para acesso a VPN.",
            card=INPUT_CARD,
        )

    def execute(self, message, attachment_actions, activity):
        vpn = message['vpn']
