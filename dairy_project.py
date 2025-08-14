from datetime import datetime

now = datetime.now().strftime("%d %B %Y | %I:%M %p")
print("📅", now)

entry = input("💬 How was your day? ")

print("\n✅ Saved! 🌟 All the best for the next day! 🌟😊🌸💖✨💪")
print("\n📖 Your Diary Entry:")
print(f"📅 {now}\n{entry}\n😊🌸💖✨💪")
