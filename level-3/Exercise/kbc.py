

questions = ["Q1 Which Indian city is known as the Pink City?",
             "Q2 What is the name of the largest mangrove forest in the world?",
             "Q3 Which Indian state is the largest producer of tea?",
             "Q4 What is called the Forbidden City in China?",
             "Q5 In Indian mythology, who is the guardian of the southern gate of heaven?"]

answers = ("Sundarbans","Imperial Palace","Garuda","Jaipur","Assam")
n=0
amount = 0
def askquestion(n): #function for asking question
    print(questions[n])


print("--Welcome to Kon Bnega Karodpati--")
print()
name =input("Enter Your name\n --> ")
print("================================================")
print()
askquestion(0)
print()
print("a) Jaipur \nb) Mumbai \nc) Kolkata \nd) Delhi")
print()
new_ans = input("--> ")
print()
if new_ans in answers:
    amount +=1000
    print("Sahi jawaab 🥳🥳")
    print("\nAap ",amount,"Rs jeetgaye 💰")
    next = 0
else:
    print("Ye galat jawab hain,\n sahi jawab Jaipur tha")
    print("\nAfsos hain ki aaj aap iss khel se koi rashi nahi lekar japayenge ☠️")
    next = 1

# question 2
if next == 0:
    n+=1
    print("================================================")
    print()
    askquestion(n)
    print()
    print("a) Sundarbans \nb) Amazon rainforest \nc) Congo Basin \nd) Daintree rainforest")
    print()
    new_ans = input("--> ")
    if new_ans in answers:
        amount +=2000
        print("Sahi jawab 🏆")
        print("Aap ",amount,"Rs jeetgaye")
        print()
        next =0
    else:
        print("Ye galat jawab hain 🫥,\nsahi jawab Sundarbans tha")
        print("\nAfsos hain ki aaj aap iss khel se keval ",amount,"Rs rashi lekar ja paoge 😭")
        print("Aur ye gaye aapke ",amount,"Rs sidha aapke account main 😏✅")
        next = 1 

# Question 3:
if next == 0:
    n+=1
    print("================================================")
    print()
    askquestion(n)
    print()
    print("a) Assam \nb) Kerala \nc) West Bengal \nd) Tamil Nadu")
    print()
    new_ans = input("--> ")
    if new_ans in answers:
        amount +=5000
        print("Ye jawaab bilkul sahi hain 🥳🎉🎉")
        print("Aap ",amount,"Rs jeetgaye")
        print()
        next =0
    else:
        print("Ye galat jawab hain 🫥,\nsahi jawab Assam tha")
        print("\nAfsos hain ki aaj aap iss khel se keval ",amount,"Rs rashi lekar ja paoge 😭")
        print("Aur ye gaye aapke ",amount,"Rs sidha aapke account main 😏✅")
        next = 1 

# Question 4:
if next == 0:
    n+=1
    print("================================================")
    print()
    askquestion(n)
    print()
    print("a) Summer Palace \nb) Great Wall of China \nc) Temple of Heaven \nd) Imperial Palace")
    print()
    new_ans = input("--> ")
    if new_ans in answers:
        amount +=10000
        print("Ye jawaab bilkul sahi hain 🥳🎉🎉")
        print("Aap ",amount,"Rs jeetgaye")
        print()
        next =0
    else:
        print("Ye galat jawab hain 🫥,\nsahi jawab Imperial Palace tha")
        print("\nAfsos hain ki aaj aap iss khel se keval ",amount,"Rs rashi lekar ja paoge 😭")
        print("Aur ye gaye aapke ",amount,"Rs sidha aapke account main 😏✅")
        next = 1 

# Question 5:
if next == 0:
    n+=1
    print("================================================")
    print()
    askquestion(n)
    print()
    print("a) Hanuman \nb) Garuda \nc) Yama \nd) Indra")
    print()
    new_ans = input("--> ")
    if new_ans in answers:
        amount +=9982000
        print("Ye jawaab bilkul sahi hain 🥳🎉🎉")
        print("Aap ",amount,"Rs jeetgaye")
        print()
        print("Iss shandar aur jaandar khel keliye taliya honi chahiye 👏👏🎉")
        print("aaj ke vijeta",name,"🥳🥳🎉🎉👏")
        next =0
    else:
        print("Ye galat jawab hain 🫥,\nsahi jawab Garuda tha")
        print("\nAfsos hain ki aaj aap iss khel se keval ",amount,"Rs rashi lekar ja paoge 😭")
        print("Aur ye gaye aapke ",amount,"Rs sidha aapke account main 😏✅")
        next = 1 


