Python 3.5.1

Libraries:
* factual-api 1.7.0
* numpy 1.11.0
* scikit-learn 0.17.1 (sklearn 0.0??)

Source files:
* category_mapping.py
  * Takes factual_vtax_training_data.csv and predicts mapping from vtax to Factual categories creating
    *  mapped_factual_categories.csv
    *  pickles/factualCategory.pkl
* create_learning_data.py
  * Takes CSV output from extract_factual.sql (removing header row and all instances of "FACTUAL:") creating
    *  A file that can be used in place of or appended to factual_vtax_training_data.csv
* category_mapping_from_pickle.py
  * Uses pickles/factualCategory.pkl to predict Factual Category using vTaxes
* factkey.py (needs values to be set)
  * Update this file by setting OAuth key and secret (found here after creating free account https://factual.com/keys)

Data Files:
* factual_vtax_training_data.csv
  * Training input column 1 is the single feature used, and column 6 is the target
* mapped_factual_categories.csv
  * Output, predicted, column 1 is the feature and column 2 is the predicted factual category  
* factual_taxonomy.json
  * Mapping of Factual's category ID's to their labels
* pickles/factualCategory.pkl
  * Model (training) persisted for future use without running training again
* extract_factual.sql
  * BigQuery SQL to fetch agid.vtax and lis.eid along with some other columns for sanity checking to be used for input for create_learning_data.py
