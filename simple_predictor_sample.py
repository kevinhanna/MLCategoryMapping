from simple_predictor import SimplePredictor

print("Running test 1")
sample = [[2,1], [2,2], [1,1], [1,2]]
classifications = [1, 1, 0, 0]
test1 = [[2, 1], [1, 1]]
test1_1 = [[1, 1], [2, 1]]
simplePredictor = SimplePredictor(sample, classifications)

print("Tes1 1.1: %s" % simplePredictor.train(test1))
print("Test 1.2: %s" % simplePredictor.train(test1_1))

print("Running test 2")
sample2 = ['foo bar', 'foo', 'dave', 'john']
classifications2 = [1, 1, 0, 0]
test2 = ['foo', 'bob']
test2_1 = ['bob', 'foo']
simplePredictor2 = SimplePredictor(sample2, classifications2)

print("Tes1 2.1: %s" % simplePredictor2.train(test2))
print("Test 2.2: %s" % simplePredictor2.train(test2_1))


