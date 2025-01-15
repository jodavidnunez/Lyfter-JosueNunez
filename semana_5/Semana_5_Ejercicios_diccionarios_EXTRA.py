"""Dada una lista de ventas con la siguiente información:
    date
    customer_email
    items
Y cada item teniendo la siguiente información:
    name
    upc
    unit_price
Cree un diccionario que guarde el total de ventas de cada UPC.

result = {
	'ITEM-453': 131.52,
	'ITEM-324': 32.45,
	'ITEM-432': 30.08,
	'ITEM-23': 8.84,
}
"""

sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

def get_upcs (sales):
    all_upcs = []
    for key_dict in sales:
        for item in key_dict["items"]:
            all_upcs.append(item["upc"])
    sorted_upcs = sorted(set(all_upcs))
    return sorted_upcs

list_upcs = get_upcs(sales)
result = {}
for target_upc in list_upcs: 
    total_sales = 0
    for key_dict in sales:
        for item in key_dict["items"]:
            if (item["upc"] == target_upc):
                total_sales += item["unit_price"]
                break
    result[target_upc] = total_sales

import pprint
pprint.pprint(result)