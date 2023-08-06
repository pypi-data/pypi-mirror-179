# About
#### NeuroEvo is a platform for automated design and training of neural networks using evolutionary and particle swarm algorithms. The neuroevo Python package implements the algorithms used in the web application ([neuroevo.io](https://neuroevo.io)).
#### Developed by Philip Schroeder (pschroe9@jhu.edu, pschroed@broadinstitute.org)

# Example
```
from neuroevo import models
import uci_dataset as dataset

# Load example dataset
df=dataset.load_cardiotocography()

# Define dataset parameters
first_feature_column_number, last_feature_column_number, class_col_number, has_header = 1, 22, 23, False

# Define training method
train_method='PSO'

# Execute training
data=df.values.tolist()
res=models.train(data, first_feature_column_number, last_feature_column_number, class_col_number, has_header, train_method, n_hidden_nodes=[3,3], n_iterations=10, NP=10)

# View fitted weights of best candidate
nn1=res['best_candidate']
print(nn1.nn_weights)

# View previous class labels (based on given dataset) and new class labels (the labels used by the classifier)
print(res['old_class_labels'])
print(res['new_class_labels'])

# Example of using returned classifier to make a prediction 
example_input=[125.0, 0.004838709677419355, 0.0, 0.0016129032258064516, 0.0032258064516129032, 0.0, 0.0, 25.0, 1.7, 6.0, 11.6, 93.0, 72.0, 165.0, 3.0, 0.0, 133.0, 128.0, 132.0, 10.0, 0.0, 6.0]
print("Predicted class: " + str(nn1.predict_class(example_input)))
print("Activation function output for each class: " + str(nn1.get_last_class_act_funct_output()))
print("Input: " + str(nn1.get_last_input()))
```
