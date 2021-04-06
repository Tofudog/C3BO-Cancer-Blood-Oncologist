# C3BO-Cancer-Blood-Oncologist
Inspired by the artificially learned robot C-3PO from Star Wars, C-3BO intends to help out patients by diagnosing them with Blood Cancer before a tumor metastasizes.


# Components of C-3BO
Coded in tkinter, a C-3PO with a red arm appears and asks for the user to input a file. The file must contain at least two images.
Additionally, there are two buttons: one for the use to input the images of their blood cells and the other to predict the patient's blood cancer (if they have blood cancer).
C-3BO will be made with the following ML/DL algorithms:

1. CNN
2. Logistic Regression
3. SVM
4. KMeans Clustring

Accuracy of each of these models will be graphed and saved multiple times on Matplotlib. While none of these algorithms are perfect, figuring out which of these is ideal for certain functions is important.

File-handling will be done with both libraries: os and glob.
Using Tensorflow.keras.preprocessing.image will allow me to import ImageDataGenerator, a class that allows me to prepare training/testing images for my CNN.

Initially, the loss function to be used is binary crossentropy to predict two possible outputs: "has blood cancer" or "does not have blood cancer".
As mentioned in this webpage https://towardsdatascience.com/progress-bars-for-python-with-tqdm-4dba0d4cb4c, Doug Steen explains the usefulness of the tqdm module for visual progress checking, which may be useful for me.

The CNN architecture of C-3BO consists of several layers as follows:
Input >>> Conv2D >>> MaxPool >>> Conv2D >>> MaxPool >>> Conv2D >>> MaxPool >>> Flatten >>> Dense > activation="relu" >>> Dense > activation="sigmoid"

Using the GUI, the patient inputs a file containing images of their cells.
Then, each pixel (of the sample file) of each image is processed then shrinked to maintain only the important features.
I connected the layers with the flatten layer, converting the data to a 1D array.
Likewsie, I provided two dense layers to provide a certain of outputs (eventually one) with each neuron.
The second sense layer uses a sigmoid function to compute the probability of an image being classified as a certain category.

# Fine-tuning
C-3BO will be fine-tuned with the best possible combination of hyperparameters in a grid search.
The param_grid = {"epochs": [50 , 75], "batch_size": [5, 10], "learning rate": [0.01, 0.1, 1, 10], "optimizers": ("RMS Prop", "Adam")}.

A confusion matrix will be plotted to accentuate false negatives (FN) and true negatives (TN). Concerning this, even validation accuracy will be an insufficient statistic; therefore, precision and recall will hopefully help me gain insights on the validity of the model.

# Leukemia diagnostics
Leukemia can be diagnosed in various ways though a patient is most likely to develop leukemia if the number of white blood cells is too high. Unfortunately, current public datsets only have cell images of multiple-myeloma. Once I get a sufficient amount of multiple-myeloma and healthy cells, I can train C-3BO to diagnose patients with this approach.

Another way to predict leukemia is by examining proliferated cells. As many would presume, the ideal shape a cell takes is round- having cells that are ragged, elongated, abnormally large, etc. shows proliferation.

The dataset retreived from Kaggle contains thousands of images of healthy and leukemia cells. C-3BO finds underlying patterns in the cells and can fairly accurately identify them. Note that C-3BO has not yet been trained to identify specific types of leukemia (e.g. non-hodkins, AML, CML, etc).

