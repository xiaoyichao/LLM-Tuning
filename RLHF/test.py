import evaluate

print(1)
accuracy_metric = evaluate.load("evaluate/metrics/accuracy")
results = accuracy_metric.compute(references=[0, 1], predictions=[0, 1])
print(results)
