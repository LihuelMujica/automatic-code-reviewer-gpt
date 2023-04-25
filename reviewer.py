import openai
from dotenv import load_dotenv
import os
import argparse

PROMPT_ENG = """"
You will recieve a file's contents as text.
Generate a code review for the file. Indicate what changes shoul be made to improve its style, performance, readability, and maintainability. If there are any reputable libraries that could be introduced to improve the code, suggest them. Be kind and constructive. For each suggested change, include line numbers to wich you are referring
"""

PROMPT_ESP = """"
Recibirás el contenido de un archivo como texto.
Genera una review de código para el archivo. Indica qué cambios se deben hacer para mejorar su estilo, rendimiento, legibilidad y mantenibilidad. Si hay alguna biblioteca de renombre que se pueda introducir para mejorar el código, sugiérala. Sé amable y constructivo. Para cada cambio sugerido, incluye los números de línea a los que te refieres. Al final muestra el código refactorizado
"""

def codeReview(filePath, model):
    with open(filePath) as file:
        filecontent = file.read()
    review = codeReviewRequest(filecontent, model)
    print(review)

def codeReviewRequest(filecontent, model):
    messages = [
        {"role": "system", "content": PROMPT_ESP},
        {"role": "user", "content": f"Haz una code review del siguiente archivo: {filecontent}"},
    ]

    res = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    return res["choices"][0]["message"]["content"]



def main():
    parse = argparse.ArgumentParser(description='Code Reviewer')
    parse.add_argument("file")
    parse.add_argument("--model", default="gpt-3.5-turbo")
    args = parse.parse_args()
    codeReview(args.file, args.model)

if __name__ == "__main__":


    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main()