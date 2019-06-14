#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""      
    Documento de integração Python E-Notas API
    
    Criar um cliente criar uma venda e emitir uma nota fiscal

    #cadastrar_cliente
    
    Realiza o cadastro de um cliente

    #emitir_nota_cliente

    emite uma nota fiscal para o cliente cadastrado
     
    #use sem moderação!
"""
 
__author__ = "Ricardo Sousa"
__copyright__ = "Free"
__credits__ = "Ricardo De Maria Sousa"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ricardo Sousa"
__email__ = "ricardo.dmsousa@gmail.com"
__status__ = "Production"


import json
import urllib.parse
import urllib.request
import requests
from datetime import datetime
import sys

class EmitirNfe:

    """Construtor que seta as urls e o secret key """

    def __init__(self):
        now = datetime.now()
        self.data_pagamento = str(now.day) + '/' + str(now.month) + '/' + str(now.year)
        secret = 'SECRET KEY'
        self.header = header = {'Authorization':'Basic %s' % secret}
        self.url_cliente = 'https://app.enotas.com.br/api/clientes'
        self.url_venda = 'https://app.enotas.com.br/api/vendas'

    """ cadastra um cliente """
    
    def cadastrar_cliente(self, email, telefone, nome, doc, cep, cidade, logadouro, numero, complemento, bairro):
        dados_cliente = {"email":email,"telefone":telefone,"nome":nome,"cpfCnpj":doc,
                        'endereco':{'cep':cep, 'cidade':cidade, 'logadouro':logadouro, 'numero':numero,
                        'complemento':complemento, 'bairro':bairro}}    
        envia_cliente =  requests.post(self.url_cliente, headers=self.header, json=dados_cliente)
        retorno_cliente_json = envia_cliente.json()
        id_do_cliente = retorno_cliente_json['clienteId']
        self.return_status = envia_cliente.status_code
        return id_do_cliente

    """emite uma nosta fiscal se o cliente foi cadastradao"""

    def emitir_nota_cliente(self, id, valor):
        if self.return_status == 200:
            emitir_nota = {"cliente":{"id":id}, "data": self.data_pagamento,"produto": {"nome": "Nome Produto","idExterno": "1231","valorTotal": ID,"diasGarantia": 30,"tags": "Tag_Descri"},"valorTotal":valor,"quandoEmitirNFe": 1,"enviarNFeCliente": "true","meioPagamento": 2,"tags": "Tag_descricao",
            "municipioPrestacao": {"nome": "Cidade","codigoIbge": 215651},"discriminacao": "Infos","valorTotalNFe":valor}
            resposta_emitir_nota = requests.post(self.url_cliente, headers=self.header, json=emitir_nota)
        return resposta_emitir_nota.status_code
