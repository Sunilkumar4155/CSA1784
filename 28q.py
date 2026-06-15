rules = {
    "flu": ["fever", "cough", "fatigue"],
    "cold": ["cough", "runny_nose", "sneezing"],
    "allergy": ["runny_nose", "sneezing", "itchy_eyes"]
}

def diagnose(patient_symptoms):
    diagnoses = []
    for disease, disease_symptoms in rules.items():
        if all(symptom in patient_symptoms for symptom in disease_symptoms):
            diagnoses.append(disease)
    return diagnoses if diagnoses else ["Unknown condition"]

symptoms = ["cough", "runny_nose", "sneezing"]
print("Diagnosis:", diagnose(symptoms))
