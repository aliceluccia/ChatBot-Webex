import json
import logging
import requests
from webex_bot.models.command import Command
# -- coding: utf-8 --
import sys
#Para import do quote_info
from webex_bot.formatting import quote_info

log = logging.getLogger(__name__)

class TesteEmail(Command):
    def __init__(self):
        super().__init__(
            command_keyword="email",
            help_message="Envie seu chamado para a T.I!",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        log.info(
            f"activity={activity} ")
        email ='tecnologia@cesconbarrieu.com.br'
        return quote_info(f"Clique e seja direcionado para envio da sua solicitação: '{email}'")