def generate_reply(text):
    return f"📧 Email Draft Generated:\n\nDear User,\n\nRegarding: {text}\n\nBest Regards."



from modules.email_sender import send_email

def generate_reply(text):
    reply = f"""
Dear Client,

Thank you for your message:
{text}

We will get back to you soon.

Best Regards,
AI Assistant
"""

    # Example email (you can make dynamic later)
    send_email(
        to="example@gmail.com",
        subject="Response from AI Assistant",
        message_text=reply
    )

    return "📧 Email generated and sent!"