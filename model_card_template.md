# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details


The model utilizes the Random Forest Classifier from scikit-learn, with its random state fixed at 42 to ensure reproducible outcomes.

## Intended Use

The purpose of the model is to estimate an individual's salary based on various attributes.

## Training Data

The dataset is sourced from the UC Irvine Machine Learning Repository and comprises the 1994 census data. It contains 48,842 entries and 14 attributes. For training, 80% of the dataset is utilized.

## Evaluation Data


The evaluation set comprises 20% of the data, ensuring consistency in data splitting across different runs by setting the random state to 42.

## Metrics

The precision achieved was 0.7419, recall stood at 0.638, and the F1 score was 0.6863.

## Ethical Considerations


Resulting predictions coould stem fro mther manner in which the data is partitioned anmd the volume of data.

## Caveats and Recommendations

sinse data is derived from the 1994 census, it would be wise to only make predictions off that year for accuracy.


