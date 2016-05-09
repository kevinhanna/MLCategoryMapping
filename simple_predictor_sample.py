from simple_predictor import SimplePredictor

sample = [[2,1], [2,2], [1,1], [1,2]]
test = [[2,1], [1,1]]

sample2 = ['foo bar', 'foo', 'dave', 'john']
test2 = ['foo', 'bob']

classifications = [1, 1, 0, 0]

kev = SimplePredictor(sample, classifications)
kev2 = SimplePredictor(sample2, classifications)

result = kev.train(test)
result2 = kev2.train(test2)

print(result)
print(result2)