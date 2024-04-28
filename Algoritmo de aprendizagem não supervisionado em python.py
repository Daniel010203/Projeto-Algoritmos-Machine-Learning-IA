# Exemplo simples de aprendizado não supervisionado usando o algoritmo K-Means. Neste exemplo, usaremos a biblioteca scikit-learne o conjunto de dados Iris:

# Importar bibliotecas
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Carregar conjunto de dados de exemplo (iris dataset)
iris = datasets.load_iris()
X = iris.data

# Criar o modelo K-Means com 3 clusters (porque sabemos que o conjunto de dados Iris tem 3 classes)
kmeans_model = KMeans(n_clusters=3, random_state=42)

# Treinar o modelo
kmeans_model.fit(X)

# Obter rótulos dos clusters e centróides
labels = kmeans_model.labels_
centroids = kmeans_model.cluster_centers_

# Visualizar os resultados
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolor='k')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, linewidths=3, color='r')
plt.title('Clusters identificados pelo K-Means')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()

Esse código é um exemplo simples de como usar o algoritmo de aprendizado não supervisionado K-Means para agrupar dados. Aqui está uma explicação passo a passo:

1. **Importação de bibliotecas**: As bibliotecas necessárias são importadas. Isso inclui `datasets` e `KMeans` do scikit-learn para carregar o conjunto de dados Iris e aplicar o algoritmo K-Means, respectivamente. Também é importado `matplotlib.pyplot` para visualização dos resultados.
2. **Carregamento do conjunto de dados**: O conjunto de dados Iris é carregado usando o método `load_iris()` da biblioteca `datasets` do scikit-learn. Os dados são armazenados na variável `X`.
3. **Criação do modelo K-Means**: Um objeto do modelo K-Means é criado com `n_clusters=3`, indicando que queremos agrupar os dados em 3 clusters. Isso é feito porque sabemos que o conjunto de dados Iris possui 3 classes distintas.
4. **Treinamento do modelo**: O modelo K-Means é treinado com os dados usando o método `fit()`.
5. **Obtenção dos rótulos dos clusters e centróides**: Após o treinamento, obtemos os rótulos dos clusters para cada amostra usando `kmeans_model.labels_`. Além disso, os centróides de cada cluster são obtidos com `kmeans_model.cluster_centers_`.
6. **Visualização dos resultados**: Os dados são visualizados no plano bidimensional. Cada ponto é colorido de acordo com o cluster ao qual foi atribuído. Os centróides de cada cluster são representados por um marcador "X" vermelho. O gráfico resultante mostra como os dados foram agrupados pelo algoritmo K-Means.
Essencialmente, o código demonstra como usar o K-Means para encontrar padrões nos dados, mesmo sem rótulos prévios, e visualizar esses padrões por meio da clusterização.
