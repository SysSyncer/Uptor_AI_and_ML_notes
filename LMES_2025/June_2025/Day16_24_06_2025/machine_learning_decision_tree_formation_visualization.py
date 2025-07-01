# # Visualizing Decision Trees
# """
# A decision tree is a tree-based model used for both classification and regression problems. One of the key strengths of decision trees is their interpretability, as the rules for making a prediction are encoded as a set of if-then statements that can be visualized as a tree structure. Visualizing decision trees can be a powerful tool for understanding the relationships between the features and the target variable, and for interpreting the model's predictions.
#
#
# ### Plotting a Decision Tree
# One way to visualize a decision tree is to plot it using a library such as graphviz or scikit-plot. In order to plot a decision tree, you will first need to train the model on your data. Here's an example of how to do this using scikit-learn:
# """
#
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# import scikitplot as skplt
# from sklearn.tree import plot_tree
#
# """pip install scikit-plot"""
#
# import matplotlib.pyplot as plt
#
# # Load the iris dataset
# iris = load_iris()
# X = iris.data
# y = iris.target
#
# # Split the data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#
# # Train the decision tree classifier
# clf = DecisionTreeClassifier()
# clf.fit(X_train, y_train)
#
# # Plot the decision tree
# skplt.estimators.plot_tree(clf, X_train, plot_io=False)
# plt.show()
#
#
# plt.figure(figsize=(30, 15))
# plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
# plt.show()
#
# """
# ```
# ![1](https://user-images.githubusercontent.com/63750425/218250896-6ebe7890-2c7f-456a-b596-ee0dbb21c384.png)
#
#
#
# In this example, the decision tree is plotted using the plot_tree function from the scikit-plot library. The tree is plotted using the X_train data, which is the training data used to fit the model. The plot_io argument is set to False in order to plot the tree without showing the input and output nodes.
#
# ### Interpreting the Plot
#
# Once you have plotted the decision tree, you can interpret the tree structure to understand how the model is making predictions. The root node at the top of the tree represents the entire dataset, and each subsequent level in the tree represents a split based on one of the features. The final leaves of the tree represent the predicted class or target value.
#
# Each node in the tree contains several pieces of information, including the feature used for the split, the split value, the impurity of the split, and the number of samples in each node. The impurity of the split is a measure of how well the feature separates the samples into the different classes or target values, and is typically calculated using metrics such as Gini impurity or information gain.
#
# In order to make a prediction for a new sample, you would follow the path down the tree based on the feature values for that sample, until you reach a leaf node. The predicted class or target value for the sample is then given by the value in the leaf node.
#
# By visualizing the decision tree, you can gain insights into which features are most important for making predictions, and how the model is using those features to make predictions. This can be useful for both understanding the model and for identifying any potential issues, such as overfitting or biased splits.
#
# """
#
# # load the iris dataset
# iris = load_iris()
# X = iris.data
# y = iris.target
#
# # split the data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#
# # fit a decision tree classifier to the training data
# clf = DecisionTreeClassifier(criterion='entropy', max_depth=3)
# clf.fit(X_train, y_train)
#
# # make predictions on the test set
# y_pred = clf.predict(X_test)
#
# # evaluate the performance of the model
# accuracy = clf.score(X_test, y_test)
# print('Accuracy: {:.2f}'.format(accuracy))
#
#
#
# Import required libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)

# Initialize and train the Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='entropy', max_depth=130, random_state=0)
clf.fit(X_train, y_train)

# Predict on the test data
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = clf.score(X_test, y_test)
print('Accuracy: {:.2f}'.format(accuracy))

# Display the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# Display the classification report
cr = classification_report(y_test, y_pred, target_names=iris.target_names)
print("\nClassification Report:")
print(cr)

# Plot and visualize the decision tree
plt.figure(figsize=(20, 10))
plot_tree(
    clf,
    filled=True,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    rounded=True,
    fontsize=12
)
plt.title("Decision Tree for Iris Dataset", fontsize=16)
plt.show()