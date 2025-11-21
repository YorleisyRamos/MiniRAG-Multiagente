from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def buscar_similitud(vectores, consulta_vector):
    similitudes = cosine_similarity([consulta_vector], vectores)
    indice = np.argmax(similitudes)
    score = similitudes[0][indice]
    return indice, score

def buscar_topk_similitudes(vectores, consulta_vector, top_k=3):
    similitudes = cosine_similarity([consulta_vector], vectores)
    indices = np.argsort(similitudes[0])[::-1][:top_k]  # top k índices más similares
    scores = similitudes[0][indices]
    return indices, scores



