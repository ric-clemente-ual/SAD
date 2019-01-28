#Trabalho realizado por :

#Alícia Silva – 30001928 
#Maria dos Santos 20160732 
#Pedro Lourenço – 20160718 
#Ricardo Clemente-30000794



import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,roc_curve,auc,confusion_matrix
from sklearn.preprocessing import label_binarize
import pandas as pd





#Da uma label da Vista do carro
def assign_label(img,vista):
    return vista
    

def make_train_data(vista,DIR): 
    i=0
    
    for img in os.listdir(DIR):
        
        label=assign_label(img,vista)
        path = os.path.join(DIR,img)
        img = cv2.imread(path,cv2.IMREAD_COLOR)

        #Pre processamento das imagens
        res = cv2.resize(img,(64,64),interpolation = cv2.INTER_CUBIC)
        edges = cv2.Canny(res,100,100)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        res_2 = cv2.resize(gray, (200, 100))
        
        
        #Hog Settings

        winSize = (64,64)
        blockSize = (16,16)
        blockStride = (8,8)
        cellSize = (8,8)
        nbins = 9
        derivAperture = 1
        winSigma = 4.
        histogramNormType = 0
        L2HysThreshold = 2.0000000000000001e-01
        gammaCorrection = 0
        nlevels = 64
        hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,
                        histogramNormType,L2HysThreshold,gammaCorrection,nlevels)
        winStride = (8,8)
        padding = (8,8)
        locations = ((10,20),)
        hog_image = hog.compute(res_2,winStride,padding,locations)
     
        
        
        #id_imagem.append(i)
        H.append(np.array(hog_image)) #imagens com o Hog Descriptor
        O.append(np.array(res)) #imagem a cores 64x64       
        X.append(np.array(edges)) #imagem com o canny
        
        W.append(str(label)) #labels das vistas de cada imagem
        i=i+1
        
     

X=[]
H=[]
W=[]
O=[]
id_imagem=[]
label=[]


#directoria das imagens
CARRO_ATRAS_DIR='carro_atras'
CARRO_FRENTE_DIR='carro_frente'
CARRO_PRESPECTIVA_DIR='carro_prespectiva'





#Associa uma label a cada imagem       
make_train_data('ATRAS',CARRO_ATRAS_DIR)
print("numero de imagens",len(X))
make_train_data('FRENTE',CARRO_FRENTE_DIR)
print("numero de imagens",len(X))
make_train_data('PRESPECTIVA',CARRO_PRESPECTIVA_DIR)
print("numero de imagens",len(X))


# 20 random images do Dataset para teste
#for i in range(10):
#
#    l=rn.randint(0,len(W))
#    plt.subplot(121),plt.imshow(O[l],cmap = 'gray')
#    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#    plt.subplot(122),plt.imshow(X[l],cmap = 'gray')
#    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#    
#    
#    print('CARRO: '+W[l])
#    
#    plt.show()     

carro_imagens=[]

#redução de dimensionalidade da matriz que contem a informacao das imagens
for i in range (len(X)):
    #carro_imagens.append(np.asarray(O[i]).reshape(-1))
    #carro_imagens.append(np.asarray(X[i]).reshape(-1))
    carro_imagens.append(np.asarray(H[i]).reshape(-1))

#guarda as labels das vistas de cada imagem
labels = np.array(W)    



#labels_dict = {
        
#        'ATRAS':0,
#        'FRENTE':1,
#        'PRESPECTIVA':2
#        }


#label_ids = np.array([labels_dict[x] for x in labels])


#split
[carro_imagens_train, carro_imagens_test, labels_train, labels_test] = model_selection.train_test_split(carro_imagens, labels, test_size=0.30)

#menu
print("Modelo de classificação")
print("1-Random Forest")
print("2-Decision Tree")
print("3-LSVC")
x = input("OPCAO:")

if int(x)==1:
    print("RANDOM FOREST")
    model = RandomForestClassifier(n_estimators=100)
    
if int(x)==2:    
    print("DECISION TREE")
    model = DecisionTreeClassifier()

if int(x)==3:    
    print("LSVC")
    model = svm.LinearSVC()


#resultados
clf = model.fit(carro_imagens_train, labels_train)

#training accuracy
score_train = model.score(carro_imagens_train, labels_train)
#test accuracy
score_test = model.score(carro_imagens_test, labels_test)

print("score_train:", score_train)
print("score_test:", score_test)

   
result = model.predict(carro_imagens_test)

#precision e recall resultados
print(classification_report(labels_test, result))


#one hot encoding 
label_hot = np.array(label_binarize(labels_test, classes=["ATRAS","FRENTE","PRESPECTIVA"]))
result_hot = np.array(label_binarize(result, classes=["ATRAS","FRENTE","PRESPECTIVA"]))


fpr = dict()
tpr = dict()
roc_auc = dict()

#recolha dos dados para implementar a ROC CURVE
for i in range(3):
    
    fpr[i], tpr[i], _ = roc_curve(label_hot[:, i], result_hot[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])
fpr["micro"], tpr["micro"], _ = roc_curve(label_hot.ravel(), result_hot.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])


#Plot da ROC CURVE

plt.figure()
lw = 2
plt.plot(fpr[2], tpr[2], color='darkorange',lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[2])
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Falsos Positivos Rate')
plt.ylabel('True Positivos Rate')
plt.title('ROC CURVE')
plt.legend(loc="lower right")
plt.show()

#Tabela com a Matriz da confusao
print(pd.DataFrame(confusion_matrix(labels_test, result, labels=["ATRAS","FRENTE","PRESPECTIVA"]), index=['ACTUAL:ATRAS', 'ACTUAL:FRENTE','ACTUAL:PRESPECTIVA'], columns=['PREDICTED:ATRAS', 'PREDICTED:FRENTE','PREDICTED:PRESPECTIVA']))

