# Explainable Machine Learning for Gallstone Disease

Project for DAT305 at the University of Stavanger.

We train three tree-based classifiers (Decision Tree, Random Forest, Gradient Boosting) on a public dataset of 319 patients with bioimpedance and laboratory data to detect gallstone disease. Because tree-based models provide built-in feature importance, we can ask which markers the models rank highest and whether these match real medical evidence.

**Key finding:** all three models rank C-reactive protein, vitamin D and aspartate aminotransferase (AST) highest. C-reactive protein and AST are supported by medical research, the evidence for vitamin D is mixed. A model ranking a feature highly does not mean it is a medical cause.

## Dataset

The dataset comes from Esen et al. (2024), *Early prediction of gallstone disease with a machine learning-based method from bioimpedance and laboratory data*, Medicine, and is available at the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/1150/gallstone-1). It contains 319 patients with 38 features and the gallstone status.

The notebook expects the file `dataset-uci.xlsx` in the same folder. If it is not included in this repository, download the dataset from the link above and save it under that name.

## What the notebook does

`main.ipynb` runs through these steps:

1. Load and inspect the dataset
2. Remove three rows with extreme values (outliers)
3. Drop columns that are mathematically related to others (e.g. height and weight, as BMI covers them)
4. Split into 70% training and 30% test data (stratified, `random_state = 7`)
5. Train a Decision Tree, a Random Forest and a Gradient Boosting classifier
6. Evaluate with accuracy and precision, plus recall, F1 and confusion matrices
7. Plot the top features of each model
8. Additional checks: 5-fold cross-validation and permutation importance

## Models and results

| Model             | Max. depth | Other settings                          | Accuracy | Precision |
|-------------------|-----------:|-----------------------------------------|---------:|----------:|
| Decision Tree     | 3          | min. 5 samples per leaf                 | 0.7053   | 0.7317    |
| Random Forest     | 6          | 200 trees, min. 3 samples per leaf      | 0.7474   | 0.7556    |
| Gradient Boosting | 3          | 100 trees, learning rate 0.05           | 0.7368   | 0.7750    |

Scores are on the test set of 95 patients. With a test set this small, one patient is about one percentage point of accuracy, so the models should be seen as comparable.

## How to run

You need Python 3 and Jupyter (or VS Code with the Jupyter extension).

```bash
pip install pandas numpy matplotlib seaborn python-calamine scikit-learn jupyter
jupyter notebook main.ipynb
```

Then run all cells from top to bottom. The first cell also installs the dependencies.

## Authors

- Joe Finn Meyer-Koester
- Alexander Björn Rebello

Both authors worked on all parts of the project together. Joe put slightly more work into the data part, Alexander into the models part.