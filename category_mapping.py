import csv
import json

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

training_data_csv = open('data/factual_vtax_training_data.csv', 'r', encoding='utf-8', errors='ignore')
factual_tax_json = open('data/factual_taxonomy.json', 'r')
outfile = open('data/mapped_factual_categories.csv', 'w')


fieldnames = ("vtax","eid","ag_account","website", "company_name", "factual_category_ids")
training_data_reader = csv.DictReader(training_data_csv, fieldnames)

factual_tax = json.load(factual_tax_json)

vtaxes = []
fids = []
unique_vtaxes = set()

out = []

for row in training_data_reader:
    if row['factual_category_ids']:
        vtax = row['vtax']
        fid = row['factual_category_ids']

        vtaxes.append(vtax)
        fids.append(fid)
        unique_vtaxes.add(vtax)

X_train = np.array(vtaxes)
y_train = fids
X_test = unique_vtaxes


classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('clf', OneVsRestClassifier(LinearSVC()))])

classifier.fit(X_train, y_train)


predicted = classifier.predict(X_test)


print(predicted)
print(X_test)

for item, labels in zip(X_test, predicted):
    tmp_fid = factual_tax[str(labels)]["labels"]["en"]
    out.append([item, labels, tmp_fid])
    print('%s => %s - %s' % (item, labels, tmp_fid))

writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
writer.writerows(out)


from sklearn.externals import joblib
joblib.dump(classifier, 'data/pickles/factualCategory.pkl', 6)