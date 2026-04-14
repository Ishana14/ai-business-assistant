# from predictor import predict_intent

# # Import modules
# from modules import email_generator
# from modules import invoice_generator
# from modules import scheduler
# from modules import summarizer
# from modules import task_manager


# def route_task(user_input):

#     # Step 1: Predict intent
#     intent = predict_intent(user_input)

#     print("Detected Intent:", intent)

#     # Step 2: Route to correct module

#     if intent == "meeting":
#         return scheduler.schedule_meeting(user_input)

#     elif intent == "invoice":
#         return invoice_generator.create_invoice(user_input)

#     elif intent == "email":
#         return email_generator.generate_reply(user_input)

#     elif intent == "summary":
#         return summarizer.summarize(user_input)

#     elif intent == "task":
#         return task_manager.create_task(user_input)

#     else:
#         return "Sorry, I couldn't understand your request."




from predictor import predict_intent

from backend.modules import email_generator
from backend.modules import invoice_generator
from backend.modules import scheduler
from backend.modules import summarizer
from backend.modules import task_manager


def route_task(user_input):

    intent = predict_intent(user_input)
    print("Detected Intent:", intent)

    if intent == "meeting":
        return scheduler.schedule_meeting(user_input)

    elif intent == "invoice":
        return invoice_generator.create_invoice(user_input)

    elif intent == "email":
        return email_generator.generate_reply(user_input)

    elif intent == "summary":
        return summarizer.summarize(user_input)

    elif intent == "task":
        return task_manager.create_task(user_input)

    else:
        return "Sorry, I couldn't understand your request."