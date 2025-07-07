from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open("data.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sor", methods=["POST"])
def sor():
    gelen_soru = request.form.get("soru").strip().lower()
    
    for soru, cevap in knowledge.items():
        if gelen_soru in soru:
            return jsonify({"cevap": cevap})

    return jsonify({"cevap": "Bu soruyu anlayamadım. Lütfen daha basit bir şekilde sorar mısın?"})

if __name__ == "__main__":
    print("Kod çalişiyor, sunucu başlatiliyor...")

    app.run(debug=True)
