from flask import Flask
from flask import render_template
from flask import request
import torch
import torchvision.models as models

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        bmi = request.form["bmi"]

        try:
            if request.form["smoking"] == "on":
                smoking = 1
        except:
                smoking = 0

        try:
            if request.form["alcoholDrinking"] == "on":
                alcoholDrinking = 1
        except:
                alcoholDrinking = 0

        try:
            if request.form["stroke"] == "on":
                stroke = 1
        except:
                stroke = 0

        physicalHealth = request.form["physicalHealth"]
        mentalHealth = request.form["mentalHealth"]

        try:
            if request.form["difficultyWalking"] == "on":
                difficultyWalking = 1
        except:
                difficultyWalking = 0


        sex = request.form["sex"]
        ageCategory = request.form["ageCategory"]
        race = request.form["race"]
        diabetic = request.form["diabetic"]

        try:
            if request.form["physicalActivity"] == "on":
                physicalActivity = 1
        except:
                physicalActivity = 0


        ageCategory = request.form["genHealth"]
        race = request.form["sleepTime"]

        try:
            if request.form["asthma"] == "on":
                asthma = 1
        except:
                asthma = 0

        try:
            if request.form["kidneyDisease"] == "on":
                kidneyDisease = 1
        except:
                kidneyDisease = 0

        try:
            if request.form["skinCancer"] == "on":
                skinCancer = 1
        except:
                skinCancer = 0


        input_data = [[int(bmi), int(smoking), int(alcoholDrinking), int(stroke), int(physicalHealth), int(mentalHealth), int(difficultyWalking), int(sex), int(ageCategory), int(race), int(diabetic), int(physicalActivity),int(ageCategory), int(race), int(asthma), int(kidneyDisease), int(skinCancer)]]

        print(input_data)

        tensor_data = torch.tensor(input_data, dtype=torch.float32)


        model = torch.jit.load('model_scripted.pt')
        model.eval()

        with torch.no_grad():
            output = model(tensor_data)

        return render_template("heart_disease.html", percentage = (output[0][1].item() * 100))

    return render_template("heart_disease.html")

if __name__ == "__main__":
    app.run()

