from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.metrics import precision_recall_curve, auc, classification_report
import matplotlib.pyplot as plt
import seaborn as sns


def metrics(y_true, y_pred):
    print(classification_report(y_true, y_pred))
    print('---------------------------------------------------')
    print(f'Precision score for this model is: {precision_score(y_true, y_pred, average= "micro")}')
    print(f'Recall score for this model is: {recall_score(y_true, y_pred, average= "micro")}')
    print(f'Accuracy score for this model is: {accuracy_score(y_true, y_pred, average = "micro")}')
    print(f'F1 score for this model is: {f1_score(y_true, y_pred, average= "micro")}')
    # print('---------------------------------------------------')
    # precision, recall, thresholds = precision_recall_curve(y_true, y_pred)
    # auc_pr = auc(recall, precision)
    # print(f'AUC for the precision-recall curve is: {auc_pr}')
    
    
    # Confusion matrix
def plot_matrix(y_true, y_pred, model):
    cf = confusion_matrix(y_true, y_pred)
    labels = model.classes_
    plt.figure(figsize=(8,6))
    sns.heatmap(cf, annot=True, 
                fmt='d', 
                cmap='Blues', 
                cbar=False, 
                xticklabels=labels, 
                yticklabels=labels)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.show();