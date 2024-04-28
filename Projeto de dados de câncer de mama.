from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_diabetes
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pylab as plt

from ucimlrepo import fetch_ucirepo

training_accuracy = []
test_accuracy = []

kernels = ['linear', 'rbf', 'sigmoid']
for kernel in kernels:
    svm_
    model = svm.SVC(kernel=kernel)

    svm_model.fit(X_train_can, y_train_can)
    training_accuracy.append(svm_model.score(X_train_can, y_train_can))
    test_accuracy.append(svm_model.score(X_test_can, y_test_can))

plt.plot(kernels, training_accuracy, label='Acuracia no conj. treino')
plt.plot(kernels, test_accuracy, label='Acuracia no conj. teste')
plt.ylabel('Accuracy')
plt.xlabel('Kernels')
plt.legend()

training_accuracy = []
test_accuracy = []

prof_max = range(1,10)

for md in prof_max:
  tree = DecisionTreeClassifier(max_depth=md,random_state=0)
  tree.fit(X_train_can,y_train_can)
  training_accuracy.append(tree.score(X_train_can, y_train_can))
  test_accuracy.append(tree.score(X_test_can, y_test_can))

plt.plot(prof_max,training_accuracy, label='Acuracia no conj. treino')
plt.plot(prof_max,test_accuracy, label='Acuracia no conj. teste')
plt.ylabel('Acuracia')
plt.xlabel('Profundidade Maxima')
plt.legend()


training_accuracy = []
test_accuracy = []

for interception in [True, False]:
  regr = LinearRegression(fit_intercept=interception)
  regr.fit(X_train_dia, y_train_dia)
  training_accuracy.append(regr.score(X_train_dia, y_train_dia))
  test_accuracy.append(regr.score(X_test_dia, y_test_dia))

plt.plot(["Interc", "No Interc"],training_accuracy, label='Acuracia no conj. treino')
plt.plot(["Interc", "No Interc"],test_accuracy, label='Acuracia no conj. teste')
plt.ylabel('Acuracia')
plt.xlabel('Fit Intercept')
plt.legend()

Este código é uma demonstração de como usar diferentes algoritmos de aprendizado de máquina para resolver problemas de classificação e regressão. Vou explicar o que cada parte faz:

1. **Importação de bibliotecas e conjuntos de dados:**
   - As bibliotecas necessárias são importadas, incluindo `sklearn` para algoritmos de aprendizado de máquina, `matplotlib` para visualização e `fetch_ucirepo` para carregar conjuntos de dados de um repositório UCI.
   - Dois conjuntos de dados são carregados: "breast cancer" e "diabetes".

2. **Inicialização de listas para armazenar métricas de desempenho:**
   - Duas listas vazias, `training_accuracy` e `test_accuracy`, são inicializadas para armazenar a acurácia dos modelos em conjuntos de treinamento e teste, respectivamente.

3. **Suporte de Vetores de Máquinas (SVM) com diferentes kernels:**
   - Um loop `for` itera sobre diferentes kernels (`linear`, `rbf`, `sigmoid`).
   - Para cada kernel, um modelo SVM é inicializado e ajustado aos dados de treinamento.
   - A acurácia do modelo é calculada nos conjuntos de treinamento e teste e adicionada às listas correspondentes.
   - Um gráfico é gerado para mostrar a acurácia dos modelos SVM com diferentes kernels.

4. **Árvore de Decisão com diferentes profundidades máximas:**
   - Outro loop `for` itera sobre diferentes profundidades máximas (`prof_max`).
   - Para cada profundidade máxima, uma árvore de decisão é inicializada e ajustada aos dados de treinamento.
   - A acurácia do modelo é calculada nos conjuntos de treinamento e teste e adicionada às listas correspondentes.
   - Um segundo gráfico é gerado para mostrar a acurácia das árvores de decisão com diferentes profundidades máximas.

5. **Regressão Linear com e sem interceptação:**
   - Um último loop `for` itera sobre duas opções de interceptação (`True` e `False`).
   - Para cada opção de interceptação, um modelo de regressão linear é inicializado e ajustado aos dados de treinamento.
   - A acurácia do modelo é calculada nos conjuntos de treinamento e teste e adicionada às listas correspondentes.
   - Um terceiro gráfico é gerado para mostrar a acurácia dos modelos de regressão linear com e sem interceptação.

Este script demonstra a aplicação de diferentes algoritmos de aprendizado de máquina em diferentes conjuntos de dados e como ajustar seus parâmetros para otimizar o desempenho do modelo. A visualização dos resultados ajuda na comparação e seleção do melhor modelo para um determinado problema de machine learning.
