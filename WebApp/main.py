import streamlit as st
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

st.title("Classifier Comparison")

st.write("""
## Exhaustive comparison of different classifiers across renowned datasets.
Find the best one, can you!
""")

dataset_name = st.sidebar.selectbox("Select a Dataset", ("Iris", "Breast Cancer", "Wines"))
classifier_name = st.sidebar.selectbox("Select a Classifier", ("KNN", "SVM", "Random Forest"))


def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == 'Breast Cancer':
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()
    x = data.data
    y = data.target
    return x, y


X, y = get_dataset(dataset_name)
# check the dataset once
st.write("Shape of Dataset  ", X.shape)
st.write("Number of Classes ", len(np.unique(y)))


def add_param_ui(clf_name):
    params = dict()
    if clf_name == "KNN":
        k = st.sidebar.slider("K", 1, 15)
        # adding slider for choosing k value
        params["K"] = k

    elif clf_name == "SVM":
        c = st.sidebar.slider("C", 0.01, 10.0)
        params["C"] = c

    else:
        n_estimators = st.sidebar.slider("n_estimators", 10, 100)
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        params["max_depth"] = max_depth
        params["n_estimators"] = n_estimators
    return params


params = add_param_ui(classifier_name)


def get_classifier(clf_name, params):

    if clf_name == "KNN":
        clf = KNeighborsClassifier(n_neighbors=params["K"])

    elif clf_name == "SVM":
        clf = SVC(C=params["C"])

    else:
        clf = RandomForestClassifier(n_estimators=params["n_estimators"],
                                     max_depth=params["max_depth"],
                                     random_state=1234)
    return clf


clf = get_classifier(classifier_name, params)

# Classification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

acc = accuracy_score((y_test), (y_pred))
st.write(f"classifier = {classifier_name}")
st.write(f"accuracy = {acc}")

# Plot these datasets
# all dimensions can't be plotted so we plot the 2 most principal
# unsupervised so dont need to pass 'y' to PCA
pca = PCA(2)
X_projected = pca.fit_transform(X)
x1 = X_projected[:, 0]
x2 = X_projected[:, 1]


fig = plt.figure()
plt.scatter(x1, x2, c=y, alpha=0.8, cmap="rainbow")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()

st.pyplot(fig)
# instead of plt.show() that we do normally

#play around with more parameters, classifiers and feature_Scaling as well as more datasets

# if __name__ == '__main__':
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
