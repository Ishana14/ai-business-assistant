# import pickle

# model = pickle.load(open("../models/model.pkl", "rb"))
# vectorizer = pickle.load(open("../models/vectorizer.pkl", "rb"))

# def predict(text):
#     text_vec = vectorizer.transform([text])
#     return model.predict(text_vec)[0]

# print(predict("Schedule meeting tomorrow"))


import pickle

# Load trained model
model = pickle.load(open("../models/model.pkl", "rb"))
vectorizer = pickle.load(open("../models/vectorizer.pkl", "rb"))

def predict_intent(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)
    return prediction[0]