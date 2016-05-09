import csv
import json

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

training_data_csv = open('data/factual_vtax_training_data.csv', 'r', encoding='utf-8', errors='ignore')
business_names_csv = open('data/business_names.csv', 'r', encoding='utf-8', errors='ignore')
factual_tax_json = open('data/factual_taxonomy.json', 'r')
name_outfile = open('data/mapped_name_factual_categories.csv', 'w')
vtax_outfile = open('data/mapped_factual_categories.csv', 'w')

# Training data
fieldnames = ("vtax","factual_id","ag_account","website", "company_name", "factual_category_ids")
training_data_reader = csv.DictReader(training_data_csv, fieldnames)

# Business names data
name_fieldnames = ("company_name", "factual_id")
business_name_reader = csv.DictReader(business_names_csv, name_fieldnames)


# Factual category ID's and labels
factual_tax = json.load(factual_tax_json)

def train(X_train, y_train):
    if len(X_train) != len(y_train):
        raise Exception('Training data and target data are of different lengths')
    # Pipeline to vectorize text data and set classifier
    classifier = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('clf', OneVsRestClassifier(LinearSVC()))])
    # Fit to data
    classifier.fit(X_train, y_train)

    return classifier


def format_write(X_test, predicted, outfile):
    out = []
    for item, labels in zip(X_test, predicted):
        tmp_fid = factual_tax[str(labels)]["labels"]["en"]
        out.append([item, labels, tmp_fid])
        #print('%s => %s - %s' % (item, labels, tmp_fid))

    writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
    writer.writerows(out)


vtaxes = []
names = []
fids = []
test_names = set()
unique_vtaxes = set()

#names_out = []

# Read training data Feature (vtax) Target (factual_category_ids) Test (unique_vtaxes)
print("Formatting Data")
for row in training_data_reader:
    # If the Factual Category is missing skip the row
    if row['factual_category_ids']:
        vtax = row['vtax']
        name = row['company_name']
        fid = row['factual_category_ids']

        vtaxes.append(vtax)
        fids.append(fid)
        names.append(name)
        unique_vtaxes.add(vtax)

for name_row in business_name_reader:
    name = name_row['company_name']
    test_names.add(name)

X_train_names = np.array(names)
X_train_vtaxes = np.array(vtaxes)
y_train = fids

X_test_names = sorted(test_names)
X_test_vtaxes = sorted(unique_vtaxes)


# Predict and write names
print("Learning names")
name_classifier = train(X_train_names, y_train)
# 'predict' matching Factual category for name
name_predicted = name_classifier.predict(test_names)
format_write(X_test_names, name_predicted, name_outfile)


# Predict and write vtaxes
print("Learning vtax")
vtax_classifier = train(X_train_vtaxes, y_train)
# 'predict' matching Factual category for vtax
vtax_predicted = vtax_classifier.predict(X_test_vtaxes)
format_write(X_test_vtaxes, vtax_predicted, vtax_outfile)


# Persist training
from sklearn.externals import joblib
joblib.dump(name_classifier, 'data/pickles/factualNameCategory.pkl', 6)
joblib.dump(vtax_classifier, 'data/pickles/factualCategory.pkl', 6)