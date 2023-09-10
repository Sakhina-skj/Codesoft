 #Quiz Game
question={
     1:{"ques":" Who developed Python Programming Language?",
        "Option": ["Wick van Rossum" ,"Rasmus Lerdorf" ,"Guido van Rossum" ,"Niene Stom"] ,
        "answer": 3
     },
     2: {"ques": "Which type of Programming does Python support?",
         "Option": ["object-oriented programming", " structured programming", "functional programming", "all of the mentioned"],
         "answer": 4
         },
     3:{"ques":" Which of the following is the correct extension of the Python file?",
        "Option": [".python" ,".pl" ,".py" ,".p"] ,
        "answer": 3
     },
     4:{"ques":"Which keyword is used for function in Python language?",
        "Option": ["Function" ,"def" ,"fun" ,"Define"] ,
        "answer": 2
     },
     5:{"ques":" Which of the following character is used to give single-line comments in Python?",
        "Option": ["//" ,"#" ,"/*" ,"!"] ,
        "answer": 2
     },
     6:{"ques":"What arithmetic operators cannot be used with strings in Python?",
        "Option": ["+" ,"-" ,"*" ,"all the mentioned"] ,
        "answer": 2
     },
     7:{"ques":"What is the maximum length of a Python identifier?",
        "Option": ["32" ,"16" ,"128" ,"No fixed length is specified "] ,
        "answer": 4
     },
     8:{"ques":"Which of the following types of loops are not supported in Python?",
        "Option": ["while" ,"do-while" ,"for" ,"None of the above"] ,
        "answer": 2
     },
     9:{"ques":"Which of the following are valid escape sequences in Python?",
        "Option": ["\n" ,"\t" ,"\\" ,"All of the above"] ,
        "answer": 4
     },
     10:{"ques":"Which of the following are valid string manipulation functions in Python?",
        "Option": ["count()" ,"upper()" ,"strip()" ,"all of the mentioned"] ,
        "answer": 4
     },
 }

import random
que_list=[1,2,3,4,5,6,7,8,9,10]
que_asked=0
score=0
while que_asked<10:
    que_num=random.choice(que_list)
    print(question[que_num]["question"])
    num=1
    for Option in question[que_num]["Option"]:
        print[str(num)+" ."+Option]
        num +=1
    print("please choose correct option--")
    try:
        user_choice=int(input())
    except:
        print("please choose valid option")
        print("-"*30)
        continue
     if user_choice==question[que_num]["answer"]:
        print("Answer is right.")
        score+=1
     else:
        print("Answer is wrong")
        que_asked+=1
        que_list.remove(que_num)
        print("-"*30)
    print("Your score is:",score,"/10")


