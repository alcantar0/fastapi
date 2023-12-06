'''
1 = positivo
0 =  negativo
2 = neutro
'''


from sklearn.feature_extraction.text import CountVectorizer
import joblib

def modelo(sentenca):
    loaded_model = joblib.load('modelo_svm.joblib')
    loaded_vect = joblib.load('vect.joblib')

    # Use o modelo carregado para fazer previsões
    
    new_sentences_vect = loaded_vect.transform(sentenca)
    
    predictions = loaded_model.predict(new_sentences_vect)
    return predictions