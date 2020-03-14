from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('__main__', '.'))
template = env.get_template('zadanie0701_template.html')

items = [
    {'name': 'Karkówka bez kości', 'price': 8.99, 'unit': 'kg', 'on_sale': True},
    {'name': 'Twaróg sernikowy 1kg', 'price': 5.99, 'unit': 'op', 'on_sale': True},
    {'name': 'Mleko Świeże 2%', 'price': 1.99, 'unit': 'op', 'on_sale': True},
    {'name': 'Herbata torebki 200g', 'price': 9.99, 'unit': 'op', 'on_sale': False},
    {'name': 'Czekolada', 'price': 2.49, 'unit': 'op', 'on_sale': True},
    {'name': 'Gruszki', 'price': 2.99, 'unit': 'kg', 'on_sale': True},
    {'name': 'Cytryny', 'price': 4.99, 'unit': 'kg', 'on_sale': False},
    {'name': 'Mydło w płynie', 'price': 12.99, 'unit': 'l', 'on_sale': False},
]

rendered_html = template.render(items=items)

with open('zadanie0701.html', mode='w', encoding='utf-8') as f:
    f.write(rendered_html)
