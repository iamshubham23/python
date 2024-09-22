import random
print("welcome to the higher lower game")
data=[
    {
        'name':'virat kholi',
        'followers':246,
        'description':'crickter',
        'country':'india'
    },
    {
        'name':'cristiano ronaldo',
        'followers':330,
        'description':'footboller',
        'country':'portugal'
    },
    {
        'name':'instagram',
        'followers':600,
        'description':'social media platform',
        'country':'America'
    },
    {
        'name':'shardha kappor',
        'followers':100,
        'description':'actress',
        'country':'india'
    },
    {
        'name':'Ariana Grande',
        'followers':113,
        'description':'musician and actress',
        'country':'united states'
    },
]
def format_data(account):
    """format the account data into printable format"""
    account_name=account["name"]
    account_description=account["description"]
    account_country=account["country"]
    return f"{account_name},a {account_description} ,from {account_country}"
def check_answer(guess,a_followers,b_followers):
    """use if statement to check if user is correct"""
    if a_followers >b_followers:
        return guess=="a"
    else:
        return guess=="b"
score=0
game_should_continue=True
while game_should_continue: 
    account_a=random.choice(data)
    account_b=random.choice(data)

    print(f"compare A:{format_data(account_a)}")
    print(f"compare B:{format_data(account_b)}")
    guess=input("which has more number of follower type A or B").lower()
    a_follower=account_a["followers"]
    b_follower=account_b["followers"]

    is_correct=check_answer(guess,a_follower,b_follower)
    if is_correct:
        score+=1
        print(f"you are right! and your current score is{score}")
    else:
        game_should_continue=False
        print("sorry thats wrong")    
       