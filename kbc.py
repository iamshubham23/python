questions=[
    ["which language was used to create fb?","python","french","javascript","php","none",4],    
    ["which language was used to create fb?","python","french","javascript","php","none",4],
    ["which language was used to create fb?","python","french","javascript","php","none",4],
    ["which language was used to create fb?","python","french","javascript","php","none",4],
    ["which language was used to create fb?","python","french","javascript","php","none",4],
    ["which language was used to create fb?","python","french","javascript","php","none",4],
    ["which language was used to create fb?","python","french","javascript","php","none",4],
    ["which language was used to create fb?","python","french","javascript","php","none",4],
    ["which language was used to create fb?","python","french","javascript","php","none",4],
    ["which language was used to create fb?","python","french","javascript","php","none",4],
    ["which language was used to create fb?","python","french","javascript","php","none",4],
    ["which language was used to create fb?","python","french","javascript","php","none",4],
    ["which language was used to create fb?","python","french","javascript","php","none",4]
 
]  
levels=[1000,2000,3000,4000,5000,60000,7000,8000,10000,50000,80000,1000000]
money=0
for i in range (0,len(questions)):
    question=questions[i]
    print(f"question for RS {levels[i]}")
    print(f"a.{question[1]}          b.{question[2]}")
    print(f"c.{question[3]}           d.{question[4]} ")
    reply=int(input("enter your answer(1-4)"))
    if(reply == question[-1]):
        print(f"correct answer,you have won rs. {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=50000
        
    else:
        print("wrong answer!") 
        break   
print(f"your take home money is {money}")    