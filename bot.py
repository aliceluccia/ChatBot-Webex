from audioop import add
from dotenv import load_dotenv
from setuptools import Command
from webex_bot.webex_bot import WebexBot

#Importando as funções para adicionar o comando ao card do webex
from testesenha import RedefinirSenha
from testevpn import RespostaVPN
from testeinternet import RespostaInternet
from testedeskbee import RespostaDeskbee
from testeemail import TesteEmail


import json
import os
import codecs
#from webex_bot.commands.echo import EchoCommand

load_dotenv()

access_token = os.getenv('WEBEX_TEAMS_ACCESS_TOKEN')

bot = WebexBot(access_token , approved_domains=["cesconbarrieu.com.br"])


#bot.add_command(EchoCommand())

#Comando que serão adicionados nos cards do Webex
bot.add_command(RedefinirSenha())
bot.add_command(RespostaVPN())
bot.add_command(RespostaInternet())
bot.add_command(RespostaDeskbee())
bot.add_command(TesteEmail())

bot.run()

