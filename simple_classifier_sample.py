from simple_classifier import SimplePredictor
import simple_classifier_sample_data as scs
import numpy as np

def test1():
    # Test 1
    print("Running test 1")
    sample = [[2,1], [2,2], [1,1], [1,2]]
    classifications = [1, 1, 0, 0]
    test1 = [[2, 1], [1, 1]]
    test1_1 = [[1, 1], [2, 1]]
    simplePredictor = SimplePredictor(sample, classifications)

    print("Test 1.1: %s" % simplePredictor.train(test1))
    print("Test 1.2: %s" % simplePredictor.train(test1_1))

def test2():
    # Test 2
    print("Running test 2")
    sample2 = ['foo bar', 'foo', 'dave', 'john']
    classifications2 = [1, 1, 0, 0]
    test2 = ['foo', 'bob']
    test2_1 = ['bob', 'foo']
    simplePredictor2 = SimplePredictor(sample2, classifications2)

    print("Test 2.1: %s" % simplePredictor2.train(test2))
    print("Test 2.2: %s" % simplePredictor2.train(test2_1))

def test3():
    # Test 3
    # See 'simple_classifier_sample_data' to view data
    print("Running test 3")
    a = np.array(scs.car_eval_data)
    sample3 = a[:, 0:6]
    classifications3 = a[:, 6]
    test3 = a[1000:, 6]
    simplePredictor3 = SimplePredictor(sample3, classifications3)

    print("Test 3: %s" % simplePredictor3.train(test3))

test1()
test2()
# not yet implemented test3()