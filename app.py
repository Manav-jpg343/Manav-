from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from data import lessons, summaries, quizzes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# In-memory quiz session tracking
user_quiz_progress = {}

@app.route("/bot", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').strip().lower()
    user_id = request.values.get('From', 'anonymous')  # WhatsApp number as session ID
    resp = MessagingResponse()
    msg = resp.message()

    # Quiz response handling
    if user_id in user_quiz_progress:
        quiz_data = user_quiz_progress[user_id]
        answer = incoming_msg.strip().lower()

        current_q = quiz_data['questions'][quiz_data['current']]
        correct = current_q['answer'].lower()

        if answer == correct.lower() or answer in correct.lower():
            quiz_data['score'] += 1
            msg.body("✅ Correct!")
        else:
            msg.body(f"❌ Incorrect. Correct answer: {correct}")

        quiz_data['current'] += 1

        if quiz_data['current'] < len(quiz_data['questions']):
            next_q = quiz_data['questions'][quiz_data['current']]
            options_text = "\n".join([f"{chr(65+i)}. {opt}" for i, opt in enumerate(next_q['options'])])
            msg.body(f"\nQ{quiz_data['current']+1}: {next_q['question']}\n{options_text}")
        else:
            total = len(quiz_data['questions'])
            score = quiz_data['score']
            msg.body(f"\n🎉 Quiz Completed!\nYour Score: {score}/{total}")
            del user_quiz_progress[user_id]
        return str(resp)

    # Lessons
    if "lesson" in incoming_msg:
        subject = ""
        unit = ""
        for s in lessons:
            if s in incoming_msg:
                subject = s
                break
        if "unit 1" in incoming_msg:
            unit = "unit 1"

        if subject and unit in lessons.get(subject, {}):
            msg.body(lessons[subject][unit])
        else:
            msg.body("❗ Try: lesson OS unit 1, lesson CN unit 1, or lesson DBMS unit 1")

    # Summaries
    elif "summary" in incoming_msg:
        for s in summaries:
            if s in incoming_msg:
                msg.body(f"📘 Summary of {s.upper()}:\n{summaries[s]}")
                break
        else:
            msg.body("❗ Try: summary OS, summary CN, or summary DBMS")

    # Quizzes
    elif "quiz" in incoming_msg:
        for s in quizzes:
            if s in incoming_msg:
                questions = quizzes[s]
                user_quiz_progress[user_id] = {
                    "subject": s,
                    "questions": questions,
                    "current": 0,
                    "score": 0
                }
                q1 = questions[0]
                options_text = "\n".join([f"{chr(65+i)}. {opt}" for i, opt in enumerate(q1['options'])])
                msg.body(f"🧠 Starting {s.upper()} Quiz!\nQ1: {q1['question']}\n{options_text}")
                break
        else:
            msg.body("❗ Try: quiz OS, quiz CN, or quiz DBMS")

    else:
        msg.body("👋 Welcome to StudyBot!\nYou can ask:\n• lesson OS unit 1\n• summary CN\n• quiz DBMS")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
