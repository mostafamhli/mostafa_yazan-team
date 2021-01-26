import random
def play():
    tries = 3;
    guessed = [];
    ans = []
    i=0
    d={"guitar":"a fretted musical instrument that typically played with both hands",
       "ronaldo":"Brazilion retired profissional footballer who played as a stricker",
       "canada":"North American country ,in the South to Arctic circle in the north",
       "python":"Python is a high-level, interpreted and general-purpose dynamic programming language",
       "culture":"the arts and other manifestations of human intellectual achievement regarded collectively.",
       "engineering":"the branch of science and technology concerned with the design, building, and use of engines, machines, and structures",
        "topology":": is the pattern used to connect the computers together. ",
        "medium":"The technology that connects the computers together, no matter what form it takes",
       "server":"is simply a computer (or more precisely, an application running on a computer) that provides a service to other computers. ",
       "client":"is a computer that avails itself of the services provided by server"}

    print("Welcome..!");
    word,description=random.choice(list(d.items()));
    print("Word description : \n", description);
    print("You have ",tries, " attempts")
    while i < len(word):
        ans.append('_ ');
        i=i+1;
    blank=len(word)
    while tries != 0:
        ltr = input();
        print("guess letter :"+ltr)
        if ltr in guessed:
            print("This letter already taken")
            continue
        guessed.append(ltr)
        if ltr in word:
            i=0;
            while i < len(word):
                if ltr == word[i]:
                    ans[i]=ltr
                    blank-=1
                i=i+1
            print("Correct letter")
        else:
            tries=tries-1
            print("Incorrect letter ! ")
        if blank == 0:
            print("..... YOU WIN .....")
            print("The word :", ''.join(ans))
            break;
        print("The word :", ''.join(ans))
        print("Guessed yet ",guessed )
        print("you have :",tries," attempts")

