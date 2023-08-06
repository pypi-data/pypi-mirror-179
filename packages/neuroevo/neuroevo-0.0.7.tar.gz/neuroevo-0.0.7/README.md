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


## Basic options


| Option | Argument | Type | Description|
|---|-------|------|----|
| `first_feature_column_number`, `last_feature_column_number`  | INT | Required | column number of first and last feature in training data |
| `class_col_number`  | INT | Required | column number of class label in training data |
| `has_header`  | BOOL | Required | indicates whether first row of training data includes column names/labels  |
| `train_method`  | STRING | Required | 'PSO' for particle swarm optimization; 'DE' for differential evolution; 'GA' for genetic algorithm  |
| `act_fun_type`  | STRING | Optional | activation function used in neural network: 'tanh' (default), 'logistic', or 'linear  |
| `n_hidden_nodes`  | LIST | Optional | list with number of nodes used in each hidden layer of neural network (default: n_hidden_nodes=[3,5,3]) |
| `NP`  | INT | Optional | training population size (default: NP=100 ) |
| `stopping_criteria`  | STRING | Optional | 'best_candidate_fitness_min' (default; most-fit candidate neural network must achieve minimum fitness threshold), 'avg_fitness_min' (average population fitness must achieve minimum fitness threshold), or 'worst_candidate_fitness_min' (least-fit candidate must achieve minimum fitness threshold) |
| `n_iterations`  | INT | Optional | maximum number of training iterations (default: n_iterations=100) |
| `min_fitness_best_candidate`, `min_fitness_avg_population`, `min_fitness_worst_candidate`  | FLOAT | Optional | fitness threshold that applies to the selected stopping_criteria (see above; default = 0.99) |
| `w_type`  | STRING | Optional | used for particle swarm optimization (train_method='PSO'); inertial weight type: 'nonlinear_decreasing' (default), 'linear_decreasing', or 'constant'; see https://arxiv.org/abs/2210.00286 for details |
| `w_0`  | FLOAT | Optional | used for particle swarm optimization (train_method='PSO'); starting and final inertial weight when w_type is 'nonlinear_decreasing' or 'linear_decreasing' (see above; default: w_0=0.9)|
| `w_Tmax`  | FLOAT | Optional | used for particle swarm optimization (train_method='PSO'); final inertial weight when w_type is 'nonlinear_decreasing' or 'linear_decreasing' (see above; default: w_Tmax=0.5)|
| `w_constant`  | FLOAT | Optional | used for particle swarm optimization (train_method='PSO'); inertial weight constant when w_type is 'constant' (see above; default: w_constant=0.73);
| `C_personal`, `C_global`  | FLOAT | Optional | used for particle swarm optimization (train_method='PSO'); the degree of influence from the personal best and global best position when updating the particle velocity (default: C_personal=0.5, C_global=0.5); see https://arxiv.org/abs/2210.00286 for details |
| `donor_vec_strategy`  | STRING | Optional | used for differential evolution (train_method='DE'); strategy used to generate donor vector: 'DE/rand/1' (default), 'DE/rand/2', 'DE/best/1', 'DE/best/2', and 'DE/current-to-best'; see https://arxiv.org/abs/2210.00286 for details |
| `CR`  | FLOAT | Optional | used for differential evolution (train_method='DE'); crossover rate (defualt: CR=0.5) |
| `F`  | FLOAT | Optional | used for differential evolution (train_method='DE'); scaling factor (defualt: F=1) |
| `selection_strategy`  | STRING | Optional | used for genetic algorithm (train_method='GA'); selection strategy: 'fitness_proportionate' (default) or 'tournament'; see https://arxiv.org/abs/2210.00286 for details |
| `crossover_strategy`  | STRING | Optional | used for genetic algorithm (train_method='GA'); crossover strategy: 'single_point' (default) or 'two_point' |
| `mutation_strategy`  | STRING | Optional | used for genetic algorithm (train_method='GA'); mutation stategy: 'random_substitution' (default) or 'random_interchange' |
| `p_c`  | FLOAT | Optional | used for genetic algorithm (train_method='GA'); crossover probability (default: p_c=0.8) |
| `p_m`  | FLOAT | Optional | used for genetic algorithm (train_method='GA'); mutation probability (default: p_m=0.5) |
| `imputation_method`  | STRING | Optional | 'mean' for mean imputation (default); 'remove' to have observations with missing values removed |
| `transformation_method`  | STRING | Optional | 'None' for no transformation (default); 'norm' for normalization using min and max; 'standardize' for standardization using mean and sd; 'log' for log transformation |


