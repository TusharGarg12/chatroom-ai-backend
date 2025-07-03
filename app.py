from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
import google.generativeai
print("🧪 Gemini SDK version:", google.generativeai.__version__)
load_dotenv()

print("🔑 GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY"))



app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro-002")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "")

        response = model.generate_content(message)

        if response.candidates and response.candidates[0].content.parts:
            reply = response.candidates[0].content.parts[0].text
        else:
            reply = "Sorry, no response was generated."

        return jsonify({"reply": reply})

    except Exception as e:
        print("🔥 Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

