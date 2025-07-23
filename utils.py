def predict_salary(model, experience, education, location):
    data = [[experience, education, location]]
    prediction = model.predict(data)
    return prediction[0]
