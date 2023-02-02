import json
from fastapi import FastAPI
import openai
import pandas as pd
app1 = FastAPI()

openai.api_key = "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"

# this endpoint is for only selected paragraph in CSV
@app1.get("/mcq")
def index():
    data = pd.read_csv("data.csv")
    paragraph = data["paragraph"][9]
    gpt_prompt = "Can You cerate multiple choice question for this paragraph :"+paragraph + "\n\n Also format a the MCQ with this format: \n\
        question:question\n\
        option A:\n\
        option B:\n\
        option C:\n\
        option D:\n\
        answer:option\n\
        reason:\n\
        option A reason:\n\
        option B reason:\n\
        option C reason:\n\
        option D reason: \n"
    print(gpt_prompt)

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.99,
        max_tokens=600,
        top_p=1.0,
        frequency_penalty=0.3,
        presence_penalty=0.9
    )
    print("----------------MCQ----------------------")
    result = response['choices'][0]['text']
    print(result)
    with open("mcq.log", "a") as log_file:
        log_file.write(
            paragraph+"\n\n" + result + "\n------------------------------------------------------------------------------\n")
    return result

# this endpoint is for all the paragraphs of CSV and output save in log file 
@app1.get("/data")
def index():
    data = pd.read_csv("data.csv")
    print(data)
    #
    for i in range(len(data["paragraph"])):
        # print(data["paragraph"][i])
        # for j in range(2):
        paragraph = data["paragraph"][i]

        # gpt_prompt = '''Can you make a multiple choice question based on the following paragraph, including the correct answer and describe for each of the four options explaining why it is right or wrong?\
        #     \nparagraph:'''+paragraph
        #  Can you create a 5 different multiple choice question for below paragraph?
        gpt_prompt = "Can You cerate multiple choice question for this paragraph :"+paragraph + "\n\n Also format a the MCQ with this format: \n\
        question:question\n\
        option A:\n\
        option B:\n\
        option C:\n\
        option D:\n\
        answer:option\n\
        reason:\n\
        option A reason:\n\
        option B reason:\n\
        option C reason:\n\
        option D reason: \n"
        # gpt_prompt = "I have one paragraph, paragraph contain much of sentence so i have to create an one question with 4 multiple option using paragraph and also describe all the option, which is right and why, and which is wrong and why it's wrong with proper reason \
        #     \n\nParagraph:"\
        #     + paragraph
        print(gpt_prompt)

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=gpt_prompt,
            temperature=0.99,
            max_tokens=600,
            top_p=1.0,
            frequency_penalty=0.3,
            presence_penalty=0.9
        )
        print("----------------MCQ----------------------")
        result = response['choices'][0]['text']
        print(result)
        with open("demo.log", "a") as log_file:
            log_file.write(
                "\n\n" + result + "\n------------------------------------------------------------------------------\n")
    return result
