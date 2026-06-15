diets = {
    "diabetes": "Low sugar, high fiber",
    "hypertension": "Low sodium, low fat",
    "obesity": "Low calorie, high protein"
}

def suggest_diet(disease):
    return diets.get(disease.lower(), "Consult a doctor for a custom plan")

print(suggest_diet("diabetes"))
