from router import route_task

while True:
    user_input = input("\nEnter command: ")
    result = route_task(user_input)
    print("\nAI Response:", result)