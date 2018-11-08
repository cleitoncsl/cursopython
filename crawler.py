# -*- coding: utf-8 -*-
import lxml
import requests
from lxml import html

url = str(input('url: '))
r = requests.get('{}'.format(url))
status = r.status_code
if status == 200:
    print("conexão realizada com sucesso")
else:
    print("erro na conexão")
tree = html.fromstring(r.content)
cargo = (tree.xpath('//*[@id="article"]/div/div[2]/div/h1/span/text()'))[0].strip()
salario = (tree.xpath('//*[@id="article"]/div/div[2]/div/p[5]/text()'))[0].strip()
email = (tree.xpath('//*[@id="article"]/div/div[2]/div/p/a[2]/text()'))[0].strip()

print('Cargo: {}'.format(cargo))
print('Salário: {}'.format(salario))
print('E-mail: {}'.format(email))
