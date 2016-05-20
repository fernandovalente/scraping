from default import open_and_returns_bs4_object, create_json_file


urls = [
    'http://www.honda.com.br/motos/Paginas/pop110i.aspx',
    'http://www.honda.com.br/motos/Paginas/Biz110i.aspx',
    'http://www.honda.com.br/motos/Paginas/nova-lead-110.aspx',
    'http://www.honda.com.br/motos/Paginas/PCX.aspx',
    'http://www.honda.com.br/motos/Paginas/cg-125i-fan.aspx',
    'http://www.honda.com.br/motos/Paginas/cg-125-cargo.aspx',
    'http://www.honda.com.br/motos/Paginas/CRF150F.aspx',
    'http://www.honda.com.br/motos/Paginas/CG160Cargo.aspx',
    'http://www.honda.com.br/motos/Paginas/CG160Start.aspx',
    'http://www.honda.com.br/motos/Paginas/cg160fan.aspx',
    'http://www.honda.com.br/motos/Paginas/cg160titan.aspx',
    'http://www.honda.com.br/motos/Paginas/nxr160bros.aspx',
    'http://www.honda.com.br/motos/Paginas/XRE190.aspx',
    'http://www.honda.com.br/motos/Paginas/crf-230f.aspx',
    'http://www.honda.com.br/motos/Paginas/cbtwister.aspx',
    'http://www.honda.com.br/motos/Paginas/sh300i.aspx',
    'http://www.honda.com.br/motos/Paginas/NC750X.aspx',
    'http://www.honda.com.br/motos/Paginas/CB1000R.aspx',
    'http://www.honda.com.br/motos/Paginas/trx-420-fourtrax.aspx',
    'http://www.honda.com.br/motos/Paginas/cbr-600rr.aspx',
    'http://www.honda.com.br/motos/Paginas/cbr-1000rr-fireblade-2011.aspx',
    'http://www.honda.com.br/motos/Paginas/gl-1800-gold-wing.aspx',
]

motos = dict()

for url in urls:
    obj = open_and_returns_bs4_object(url)

    nome = obj.find('div', {'class': 'NomeVeiculo'}).get_text().strip()
    foto = obj.find('div', {'id': 'ctl00_PlaceHolderMain_PageImage__ControlWrapper_RichImageField'})

    data = dict(
        nome=nome,
        foto='{}{}'.format(
            'http://www.honda.com.br',
            foto.find('img').get('src')
        ),
        ficha_tecnica=[]
    )

    # Propriedades da moto
    table = obj.find('table', {'class', 'ms-rteTable-EspecificacoesTecnicas'})

    for tr in table.findAll({'tr'}):
        td = tr.findAll({'td'})

        data['ficha_tecnica'].append(
            [
                td[0].getText().strip().replace('\n', ''),
                td[1].getText().strip().replace('\n', '')
            ]
        )

        td3 = td[3].getText().strip().replace('\n', '')
        try:
            td4 = td[4].getText().strip().replace('\n', '')
        except:
            td4 = ''

        data['ficha_tecnica'].append([td3, td4])

    print(nome)
    motos[nome] = data

create_json_file(motos, 'honda')
