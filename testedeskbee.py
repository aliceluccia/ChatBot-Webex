import json
import logging
import requests
from webex_bot.models.command import Command
# -- coding: utf-8 --
import sys

log = logging.getLogger(__name__)

#Adiciondo parametro encoding="utf-8" para formatar em pt-br e mostrar "acentuação"
with open("./deskbee-card.json", "r", encoding="utf-8") as card:
    INPUT_CARD = json.load(card)

class RespostaDeskbee(Command):
    def __init__(self):
        super().__init__(
            command_keyword="deskbee",
            help_message="Clique aqui e receba as instruções para acesso ao Deskbee.",
            card=INPUT_CARD,
        )

    def execute(self, message, attachment_actions, activity):
        deskbee = message['deskbee']