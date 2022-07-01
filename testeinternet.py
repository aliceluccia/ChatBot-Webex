import json
import logging
import requests
from webex_bot.models.command import Command
# -- coding: utf-8 --
import sys

log = logging.getLogger(__name__)

#Adiciondo parametro encoding="utf-8" para formatar em pt-br e mostrar "acentuação"
with open("./internet-card.json", "r", encoding="utf-8") as card:
    INPUT_CARD = json.load(card)

class RespostaInternet(Command):
    def __init__(self):
        super().__init__(
            command_keyword="wifi",
            help_message="Clique aqui e receba as instruções para acesso ao Wi-Fi.",
            card=INPUT_CARD,
        )

    def execute(self, message, attachment_actions, activity):
        internet = message['internet']


