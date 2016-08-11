import csv

from factual import Factual

from category_mapping.generate_training_data import factkey

csvfile = open('data/2000FinalFactual.csv', 'r', encoding='utf-8', errors='ignore')
outfile = open('data/2000FinalFactualMapped.csv', 'w')


# Create factkey.py with factual_key and factual_secret set to values on https://factual.com/keys
factual = Factual(factkey.factual_key, factkey.factual_secret)

def get_factual_category( factual_id ):
    try:
        data = factual.get_row('places', factual_id)
        return data["category_ids"]
    except:
        print('excption: ' + factual_id)
        return []


fieldnames = ("vtax","factual_id","ag_account","website", "company_name", "factual_category_ids")
reader = csv.DictReader( csvfile, fieldnames)
out = []

for row in reader:
    vtax = eval(row['vtax'])[0]

    if not row['factual_category_ids']:
        tmp_factual_category_ids = get_factual_category( row['factual_id'] )
        if tmp_factual_category_ids:
            factual_category_ids = tmp_factual_category_ids[0]
        else:
            factual_category_ids = None

    else:
        factual_category_ids = eval(row['factual_category_ids'])[0]

    line = [vtax, row['factual_id'], row['ag_account'], row['website'], row['company_name'], factual_category_ids]
    print(line)
    out.append(line)


writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
writer.writerows(out)


