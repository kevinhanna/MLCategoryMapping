from simple_classifier import SimplePredictor
import simple_classifier_sample_data as scs
import numpy as np

simpleClassifier = None
simpleClassifier2 = None


def test1():
    # Test 1
    print("Running test 1")
    sample = [[2,1], [2,2], [1,1], [1,2]]
    classifications = [1, 1, 0, 0]
    test1 = [[2, 1], [1, 1]]
    test1_1 = [[1, 1], [2, 1]]
    simpleClassifier = SimplePredictor(sample_data=sample, target_classifications=classifications)

    print("Test 1.1: %s" % simpleClassifier.predict(test1))
    print("Test 1.2: %s" % simpleClassifier.predict(test1_1))

    # sc_pickle = simpleClassifier.pickle()
    # simpleClassifier_foo = SimplePredictor(pickle=sc_pickle)
    #
    # print("Test 1.3: %s" % simpleClassifier_foo.predict(test1_1))

    return simpleClassifier

def test2():
    # Test 2
    print("Running test 2")
    sample2 = ['foo bar', 'foo', 'dave', 'john']
    classifications2 = [1, 1, 0, 0]
    test2 = ['foo', 'bob']
    test2_1 = ['bob', 'foo']
    simpleClassifier2 = SimplePredictor(sample_data=sample2, target_classifications=classifications2)
    print()

    print("Test 2.1: %s" % simpleClassifier2.predict(test2))
    print("Test 2.2: %s" % simpleClassifier2.predict(test2_1))

    return simpleClassifier2

def test3():
    # Test 3
    # See 'simple_classifier_sample_data' to view data
    print("Running test 3")
    a = np.array(scs.car_eval_data)
    sample3 = a[:, 0:6]
    classifications3 = a[:, 6]

    test3 = a[200:400, 0:6]
    actuals = a[200:400, 6:7]

    simpleClassifier3 = SimplePredictor(sample_data=sample3, target_classifications=classifications3)

    results = simpleClassifier3.predict(test3)

    for result, actual in zip(results, actuals):
        print("%s == %s is %s" % (result, actual[0], (result == actual)))

    return simpleClassifier3

def test4(simpleClassifier):
    print("Running test 4")

    test4 = [[2, 1], [1, 1]]

    sc_pickle = simpleClassifier.pickle()
    simpleClassifier4 = SimplePredictor(pickle=sc_pickle)

    print("Pickle: %s" % sc_pickle)

    print("Test 4.1: %s" % simpleClassifier4.predict(test4))
    print("Test 4.2: %s" % simpleClassifier4.predict([[0,1]]))

    return simpleClassifier4


#simpleClassifier1 = test1()
#simpleClassifier2 = test2()
simpleClassifier3 = test3()

#simpleClassifier4 = test4(simpleClassifier1)
