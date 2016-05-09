import csv
import json

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

training_data_csv = open('data/factual_vtax_training_data.csv', 'r', encoding='utf-8', errors='ignore')
factual_tax_json = open('data/factual_taxonomy.json', 'r')
outfile = open('data/mapped_name_factual_categories.csv', 'w')

# Training data
fieldnames = ("vtax","factual_id","ag_account","website", "company_name", "factual_category_ids")
training_data_reader = csv.DictReader(training_data_csv, fieldnames)

factual_tax = json.load(factual_tax_json)

names = []
fids = []
unique_names = set()

out = []

# Read training data Feature (vtax) Target (factual_category_ids) Test (unique_vtaxes)
for row in training_data_reader:
    # If the Factual Category is missing skip the row
    if row['factual_category_ids']:
        name = row['company_name']
        fid = row['factual_category_ids']

        names.append(name)
        fids.append(fid)
        unique_names.add(name)

X_train = np.array(names)
y_train = fids
X_test = sorted(unique_names)


# Pipeline to vectorize text data and set classifier
classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('clf', OneVsRestClassifier(LinearSVC()))])

# classify
classifier.fit(X_train, y_train)

# 'predict' matching Factual category for vtax
predicted = classifier.predict(X_test)


print(predicted)
print(X_test)

for item, labels in zip(X_test, predicted):
    tmp_fid = factual_tax[str(labels)]["labels"]["en"]
    out.append([item, labels, tmp_fid])
    print('%s => %s - %s' % (item, labels, tmp_fid))

writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
writer.writerows(out)

# Persist training
from sklearn.externals import joblib
joblib.dump(classifier, 'data/pickles/factualNameCategory.pkl', 6)