Python 3.5.1

Libraries:
* factual-api 1.7.0
* numpy 1.11.0
* scikit-learn 0.17.1 (sklearn 0.0??)

Source files:

**Addresses**
* [address_classifier/train_address.py](address_classifier/train_address.py)
  * Trains using addresses that are tokenized and each token is assigned a type

**Categories**
* [category_mapping/category_mapping.py](category_mapping/category_mapping.py)
  * Takes `factual_vtax_training_data.csv` and predicts mapping from vtax to Factual categories creating
    *  `mapped_factual_categories.csv`
    *  `pickles/factualCategory.pkl`
* [category_mapping/name_category_mapping.py](category_mapping/name_category_mapping.py)
  * Same as above, but maps using business names as well as vtax creating
    *  `mapped_factual_categories.csv`
    *  `mapped_name_factual_categories.csv`
    *  `pickles/factualCategory.pkl`
    *  `pickles/factualNameCategory.pkl`
* [category_mapping/generate_training_data/create_learning_data.py](category_mapping/generate_training_data/create_learning_data.py)
  * Takes CSV output from `extract_factual.sql` (removing header row and all instances of "FACTUAL:") creating
    *  A file thats can be used in place of or appended to `factual_vtax_training_data.csv`
* [category_mapping/sample_category_mapping_from_pickle.py](category_mapping/sample_category_mapping_from_pickle.py)
  * Uses `pickles/factualCategory.pkl` to predict Factual Category using vTaxes
* [category_mapping/generate_training_data/sample_factkey.py](category_mapping/generate_training_data/sample_factkey.py) (needs values to be set)
  * Copy this file to `factkey.py` and set OAuth key and secret (found here after creating free account https://factual.com/keys)

Data Files:
* [category_mapping/data/factual_vtax_training_data.csv](category_mapping/data/factual_vtax_training_data.csv)
  * Training input column 1 is the single feature used, and column 6 is the target
* [category_mapping/data/mapped_factual_categories.csv](category_mapping/data/mapped_factual_categories.csv)
  * Output, predicted, column 1 is the vtax (feature) and column 2 is the predicted factual category ID, column 3 is Factual's English label for that ID
* [category_mapping/data/mapped_name_factual_categories.csv](category_mapping/data/mapped_name_factual_categories.csv)
  * Output, predicted, column 1 is the name (feature) and column 2 is the predicted factual category ID, column 3 is Factual's English label for that ID
* [category_mapping/data/business_names.csv](category_mapping/data/business_names.csv)
  * Business names not used for training
* [category_mapping/data/factual_taxonomy.json](category_mapping/data/data/factual_taxonomy.json)
  * Mapping of Factual's category ID's to their labels
* [category_mapping/data/pickles/factualCategory.pkl](category_mapping/data/data/pickles/factualCategory.pkl)
  * Model (training) of vTax to Factual category persisted for future use without running training again
* [category_mapping/data/pickles/factualNameCategory.pkl](category_mapping/data/data/pickles/factualNameCategory.pkl)
  * Model (training) of business name to Factual category persisted for future use without running training again
* [category_mapping/data/extract_factual.sql](category_mapping/data/data/extract_factual.sql)
  * BigQuery SQL to fetch agid.vtax and lis.eid along with some other columns for sanity checking to be used for input for `create_learning_data.py`
