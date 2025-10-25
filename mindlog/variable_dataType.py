print("----------Productivity Tracker----------")

study_hours = int(input("Enter how many hours do you study today? "))
english_practice = int(input("How long do you spend with english today?"))
coding_practice = int(input("How long do you Practice python? "))
tuition_done = int(input("How many tuition you have today? "))
varsity_day = int(input("How much hours you spend on varsity today?"))
wake_up_time = str(input("When you waking up today?"))
mood = int(input("Score your mood (1-100)"))
sleep = int(input("How many hours you sleep today?"))

gym_done = str(input("Do you complete your today gym session (yes/no)? "))


productive_hours = study_hours + (english_practice ) + (coding_practice ) + varsity_day + (tuition_done * 1.5)

gym_status = gym_done.lower() == "yes"

if productive_hours > 10:
  print("Greate job: You are doing very well")
elif productive_hours >= 6:
  print("Keep up the good work: You are doing well")
elif productive_hours < 6:
  print("Don't lose your focus, stay focus.")

print("\n ==== Today Summary ====")
print(f"Productive Hours: ", {productive_hours})
print(f"Mood Score: ", {mood})
print(f"Sleep Hours: ", {sleep})
print(f"Wake up time: ", {wake_up_time})
print(f"Gym Status: ", {gym_status})

