import pickle
import numpy as np
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC


class SimplePredictor:


    def __init__(self, sample_data=None, target_classifications=None, pickle=None, file_dump_path=None):
        """
        
        :param sample_data: Iterable of sample features (samples)
        :param target_classifications: Iterable of target (expected classification from sample_data samples) classifications
        """
        if isinstance(sample_data, np.ndarray):
             print(len(sample_data))

        if (isinstance(sample_data, np.ndarray) or sample_data) and \
                (isinstance(target_classifications, np.ndarray) or target_classifications):
            self.__sample_data = sample_data
            self.__target_classifications = target_classifications
            self.__train()
        elif pickle:
            self.__unpickle(pickle)
        elif file_dump_path:
            self.__load(file_dump_path)
        else:
            raise Exception("WTF?")


    def __getClassifier(self):
        return self.__classifier

    def __setClassifier(self, classifier):
        self.__classifier = classifier

    def getPredictor(self):
        return self.__predictor

    def __setPredictor(self, predictor):
        self.__predictor = predictor


    def __train(self):
        """
        Creates mapping from sample_data (features) to target_classifications (classes) and then predicts target_classifications values for to_predict
        - sample_data and target_classifications need to be same length
        - to_predict should have similar data as sample_data

        :return: Iterable of predicted classifications for each to_predict
        """

        if len(self.__sample_data) != len(self.__target_classifications):
            #TODO There's probably a more appropriate Exception type
            raise Exception('Training data and target data are of different lengths')

        sample_data_np = self.__sample_data #np.array(self.__sample_data) TODO is np.array better?

        self.__setClassifier(self.__getPipeline(self.__sample_data))

        # Fit to data
        self.__getClassifier().fit(sample_data_np, self.__target_classifications)



    def predict(self, test_data):
        if not self.__classifier:
            #TODO There's probably a more appropriate Exception type
            raise Exception("Must run train before calling predict")

        self.__setPredictor(self.__getClassifier().predict(test_data))

        return self.getPredictor()


    def __getPipeline(self, sample_data):
        """

        :param sample_data:
        :return:
        """

        if isinstance(sample_data[0], str):
            # list of strings ['one', 'two', 'three']

            # Pipeline to vectorize text data and set classifier
            pipeline = Pipeline([
                ('vectorizer', CountVectorizer()),
                ('clf', OneVsRestClassifier(LinearSVC()))])
        elif hasattr(sample_data[0], '__iter__') and (isinstance(sample_data[0][0], int) or (isinstance(sample_data[0][0], np.int64))):
            # list of lists of ints [[1,2], [3,4]]

            # Pipeline to set classifier
            pipeline = Pipeline([
                ('clf', OneVsRestClassifier(LinearSVC()))])
        elif hasattr(sample_data[0], '__iter__') and isinstance(sample_data[0][0], str):
            # list of lists of ints [[1,2], [3,4]]

            #raise Exception("Not yet implemented")
            # Pipeline to set classifier
            pipeline = Pipeline([
                ('vectorizer', CountVectorizer()),
                ('clf', MultinomialNB())])
        else:
            raise Exception("Unable to use types stored in sample_data:" + type(sample_data))

        return pipeline

    def dump(self, target):
        joblib.dump(self.__getClassifier(), target, 6)

    def __load(self, path):
        self.__setClassifier(joblib.load('path'))

    def pickle(self):
        return pickle.dumps(self.__getClassifier())

    def __unpickle(self, foo_pickle):
        self.__setClassifier(pickle.loads(foo_pickle))
