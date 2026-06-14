from flask import Flask, render_template, request, jsonify
from model import (
    load_and_preprocess_pdf,
    create_or_load_vector_store,
    answer_question
)
import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db = None

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload_pdf", methods=["POST"])
def upload_pdf():

    global db

    try:
        pdf_file = request.files.get("pdf")

        if pdf_file is None:
            return jsonify({
                "error": "No PDF uploaded"
            }), 400

        # Save PDF
        pdf_path = os.path.join(
            UPLOAD_FOLDER,
            pdf_file.filename
        )

        pdf_file.save(pdf_path)

        print("Saved:", pdf_path)

        # Pass FILE PATH, not FileStorage object
        chunks = load_and_preprocess_pdf(pdf_path)

        db = create_or_load_vector_store(chunks)

        return jsonify({
            "response": f"{pdf_file.filename} uploaded successfully"
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

@app.route("/get_response", methods=["POST"])
def get_response():

    global db

    if db is None:
        return jsonify({
            "error": "Please upload a PDF first"
        }), 400

    data = request.get_json()

    user_message = data.get("message", "")

    answer = answer_question(db, user_message)

    return jsonify({
        "response": answer
    })


if __name__ == "__main__":
    app.run(debug=True)