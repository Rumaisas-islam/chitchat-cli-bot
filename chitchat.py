import random
class ChitChat:
  def __init__(self):
    pass
  def choose_question(self):
    print("Lets select the number which question you want to ask?\n")
    print("1.Tell me todays motivaional quotes?\n")
    print("2.Tell me one islamic quotes?\n")
    print("3.Tell me the story?\n")
    print("4.Tell me any cake recipe?\n")
    print("5.Tell me the meaning of emphasize,susbstantial,immodest?\n")
    print("6:Tell me 5 new vocablary words?\n")
    print("7.Tell me the recent best skills?\n")
    print("8.Suggest me some youtube channel to improve my coding?\n")
    print("9:Tell me the some beauty secrets?\n")
    print("10:Tell me best cartoon movies?\n")
    ask=input("Enter what you want to ask(1/2/3/4/5/6/7/8/9/10): ")
    if ask == "1":
      Quotes=[
      "Believe in yourself and all that you are.",
      "Your only limit is your mind.",
      "Success doesnt come to you, you go to it.",
      "Push yourself, because no one else is going to do it for you.",
      "The harder you work for something, the greater you'll feel when you achieve it.",
      "Dont watch the clock; do what it does. Keep going."]
      print(random.choice(Quotes))
    elif ask == "2":
      IslamicQuote=[
      "And whoever puts their trust in Allah, then He alone is sufficient for them. — Quran 65:3",
      "Verily, in the remembrance of Allah do hearts find rest. — Quran 13:28",
      "Allah does not burden a soul beyond that it can bear. — Quran 2:286",
      "So remember Me; I will remember you. — Quran 2:152",
      "Indeed, with hardship comes ease. — Quran 94:6",
      "Do good deeds properly, sincerely and moderately… — Prophet Muhammad ﷺ"]
      print(random.choice(IslamicQuote)) 
    elif ask == "3":
      Story=[
      "Once upon a time, a lion got caught in a hunter's net. A small mouse whom the lion had once spared, came and nibbled the net and set the lion free. Moral: Kindness is never wasted.",
      "There was once a poor woodcutter who dropped his axe in the river. An angel gave him a golden axe, but he refused it saying it wasnt his. The angel rewarded him with all three axes for his honesty.",
      "A turtle and rabbit had a race. The rabbit was fast but lazy. The turtle kept going slowly and won the race. Moral: Slow and steady wins the race.",
      "There was a thirsty crow. It found a pot with little water. He dropped pebbles until the water rose and drank. Moral: Use your brain in difficult times.",
      "Once a boy cried Wolf! when there was none. People stopped trusting him, and when a wolf really came, no one helped. Moral: Never lie."]
      print(random.choice(Story))
    elif ask == "4":
      CakeRecipe=[
      "🧁 Vanilla Cake:\n- 1 cup sugar\n- 1/2 cup butter\n- 2 eggs\n- 1.5 cup flour\n- 1 tsp baking powder\n- 1/2 cup milk\nMix all & bake at 180°C for 30 minutes.",
      "🎂 Chocolate Mug Cake:\n- 4 tbsp flour\n- 4 tbsp sugar\n- 2 tbsp cocoa\n- 3 tbsp milk\n- 2 tbsp oil\nMicrowave for 2 mins.",
      "🍫 Fudgy Brownie:\n- 1/2 cup butter\n- 1 cup sugar\n- 2 eggs\n- 1/3 cup cocoa\n- 1/2 cup flour\nBake at 175°C for 25 mins.",
      "🍰 Yogurt Cake:\n- 1 cup yogurt\n- 1 cup sugar\n- 2 eggs\n- 2 cups flour\n- 1/2 cup oil\nMix & bake at 180°C for 35 mins.",
      "🍓 Strawberry Cake:\n- 1 box cake mix\n- Add 1/2 cup strawberry puree\n- Follow cake mix instructions & bake."]
      print(random.choice(CakeRecipe))
    elif ask == "5":
      Meaning={
      "emphasize": "To give special importance or attention to something.",
      "substantial": "Large in amount or importance; significant.",
      "immodest": "Not showing humility; too proud or showy; sometimes means not dressing modestly."}
      print(random.choice(Meaning))
    elif ask == "6":
      VocabularyWords=[
      {"word": "Serene", "meaning": "Calm and peaceful"},
      {"word": "Candid", "meaning": "Honest and straightforward"},
      {"word": "Resilient", "meaning": "Able to recover quickly from problems"},
      {"word": "Diligent", "meaning": "Hardworking and careful"},
      {"word": "Innovative", "meaning": "Creative and new in ideas or methods"}]
      print(random.choice(VocabularyWords))
    elif ask == "7":
      Skills=[
      "AI & Machine Learning",
      "Web Development (HTML, CSS, JavaScript, React)",
      "Graphic Designing (Illustrator, Photoshop)",
      "Digital Marketing & SEO",
      "UI/UX Designing",
      "Data Analysis (Excel, Python, Power BI)"]
      print(random.choice(Skills))
    elif ask == "8":
      YouTubechannels=[
      "CodeWithHarry (Hindi/Urdu)",
      "FreeCodeCamp",
      "Traversy Media",
      "Apna College (for students)",
      "The Net Ninja",
      "Programming with Mosh"]
      print(random.choice(YouTubechannels))
    elif ask == "9":
      Beautysecrets=[
      "Always remove makeup before sleeping.",
      "Drink 8–10 glasses of water daily for glowing skin.",
      "Apply aloe vera gel at night for smooth skin.",
      "Use sunscreen daily even indoors.",
      "Eat fruits like oranges, pomegranates, and avocados for skin health.",
      "Exfoliate your skin once or twice a week."]
      print(random.choice(Beautysecrets))
    elif ask == "10":
      Cartoonmovies=[
      "Frozen (1 & 2)",
      "Moana",
      "Kung Fu Panda (1–3)",
      "Inside Out",
      "Zootopia",
      "Toy Story (all parts)"]
      print(random.choice(Cartoonmovies))
obj=ChitChat()
print("============Welcome to the chit chat============")
while True:
  print("1.Start chitchat")
  print("2.Exit")
  menu=input("What you want to do(1/2): ")
  if menu == "1":
    obj.choose_question()
  elif menu == "2":
    print("Goodbye!Thanks for using chichat.")
    break