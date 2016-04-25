from default import open_and_returns_bs4_object


urls = [
    'http://www.honda.com.br/motos/Paginas/pop110i.aspx',
    'http://www.honda.com.br/motos/Paginas/nova-lead-110.aspx',
    'http://www.honda.com.br/motos/Paginas/Biz-125.aspx'
]

for url in urls:
    obj = open_and_returns_bs4_object(url)
    motorcycle = obj.find('div', {'class': 'NomeVeiculo'}).get_text().strip()

    print(motorcycle)
