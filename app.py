from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here or use environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")  # Or replace with your key directly

@app.route('/resume-builder', methods=['POST'])
def resume_builder():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # Prompt for resume building
    prompt = f"""
    You are a resume builder chatbot. Help the user build a resume based on their input.
    User says: "{user_input}"
    Generate a professional response or ask for more details.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)