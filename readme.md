Python 3.5.1

Libraries
* factual-api 1.7.0
* numpy 1.11.0
* scikit-learn 0.17.1 (sklearn 0.0??)
 
Data:
* factual_vtax_training_data.csv
  * Training input column 1 is the single feature used, and column 6 is the target
* mapped_factual_categories.csv
  * Output, predicted, column 1 is the feature and column 2 is the predicted factual category  
* factual_taxonomy.json
  * Mapping of Factual's category ID's to their labels
* pickles/factualCategory.pkl
  * Model (training) persisted for future use without running training again
