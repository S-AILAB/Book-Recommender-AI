from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


#agent1: Generate summary of a book
def generate_summary(book_title, author_name):
    prompt =  """Generate a short summary dricetly without any introductory line for the book titled: {{Title}} by {{Author}}.
        Rules to follow:
        1. Word limit 100 it should not be crossed.
        2. Tone should be soft and like a human.
        3. Keep it in simple english don't use tough vocabulary.
        4. Assume that it is to be read by class 10th student.
        5. Do not include any introduction or explanation — just give the summary directly. 
        """
    
    # Replace variables in prompt manually
    prompt = prompt.replace("{{Title}}", book_title).replace("{{Author}}", author_name)


    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content.strip()


# #agent 2: Buy_links of books.
# def generate_buy_links(book_title, author_name):
#     prompt= """You are a helpful assisstant that provide purchase links for books.

#             Respond only Amazon and flipkart links of the book titles: {{Title}} by {{Author}}. 
#             Make sure the links are valid,functional and point to the correct book page.
#             No extra commentary or explaination.
#             Strictly follow the format shown in example.

#             Format of your response like this:
#             Amazon: <amazone_link>
#             Flipkart: <flipkart_link>

#             Example:

#             Input:
#             Title: Ikigai
#             Author: Francesc García, Héctor,Miralles

#             Output:
#             😊 Here are your Amazon and Flipkart links are:
#             🛍️Amazon: https://www.amazon.in/Ikigai-H%C3%A9ctor-Garc%C3%ADa/dp/178633089X/ref=sr_1_4?crid=2JHYDJH3E3SP6&dib=eyJ2IjoiMSJ9.8gpfjPQstcSKc4a8occHF5iXg4oirrVijyfFqq4J--k2shoYveCya3Xw3NUvEA2Wq91b10Y96OFvPHnJHtzpclK4Wwo8rGObSJJW1JiUWqsXkOWsE0SYGVrAxOsCfnfkDTLyhQ5B7F3-3MnE4PaUrBjZ9rGDMqjivEe91KbE888XixLTD0EpLyOsraBLQYh-CZWQmNcAqcG8CojlViJt45xYOgCv-gRDXS-ZfaC5V_Y.L5nmS2TUTEkDcv7n_qyQfzNo9mjWa3i1Ja9XqBgAJbQ&dib_tag=se&keywords=books&qid=1749754983&s=books&sprefix=books%2Cstripbooks%2C192&sr=1-4
#             🛍️Flipkart:https://www.flipkart.com/ikigai-long-happy-life-3-disc/p/itmf6tphzunajmgh?pid=9781786330895&lid=LSTBOK9781786330895HQGF7J&marketplace=FLIPKART&q=Ikigai&store=bks&srno=s_1_3&otracker=search&otracker1=search&fm=organic&iid=2c092901-c8fc-4df4-ae4f-ed4a9524e6e5.9781786330895.SEARCH&ppt=hp&ppn=homepage&ssid=7u45ion1gg0000001749755109714&qH=1c34f8a8b5febdce

#             Incase, if you are unable to find the links don't share anything else just say "Sorry 😔 Unable to find the link."
#         """
#     # Replace variables in prompt manually
#     prompt = prompt.replace("{{Title}}", book_title).replace("{{Author}}", author_name)


#     response = client.chat.completions.create(
#         model="gemini-2.5-flash-preview-05-20",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user","content": prompt}
#         ]
#     )

#     return response.choices[0].message.content.strip()