import json



with open('/home/arjuna/python_dev/ test_tasks/wildberries_pars_app/result.json', "r") as file:
    content = json.loads(file.read())
    print(content)

    products_lst = content['data']['products'][:10]
    print(products_lst)

    for product in products_lst:
        print(product["name"])
        
        print('____________________')
