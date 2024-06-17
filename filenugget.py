import os
import dotenv
import requests
import telebot
import base64

dotenv.load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CONVERT_API_SECRET = os.getenv('CONVERT_API_SECRET')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    first_name = message.from_user.first_name
    user_id = str(message.from_user.id)

    bot.reply_to(message, f"Welcome to the FileNuggets bot, {first_name}! Please start by uploading your DOC file, and we'll convert it to a PDF for you.")

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    try:
        bot.reply_to(message, "File received! We’re processing your document, please wait...")

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        if not os.path.exists('documents'):
            os.makedirs('documents')
        
        src = os.path.join('documents', message.document.file_name)
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Read file content and encode it to Base64
        with open(src, 'rb') as doc_file:
            encoded_file = base64.b64encode(doc_file.read()).decode('utf-8')
        
        # Prepare the payload for ConvertAPI
        payload = {
            "Parameters": [
                {
                    "Name": "File",
                    "FileValue": {
                        "Name": message.document.file_name,
                        "Data": encoded_file
                    }
                },
                {
                    "Name": "StoreFile",
                    "Value": True
                }
            ]
        }

        # Send POST request to ConvertAPI
        response = requests.post(
            f'https://v2.convertapi.com/convert/doc/to/pdf?Secret={CONVERT_API_SECRET}',
            json=payload
        )

        if response.status_code == 200:
            response_data = response.json()
            file_url = response_data['Files'][0]['Url']

            # Download the converted PDF file
            pdf_response = requests.get(file_url)
            pdf_output = os.path.join('documents', message.document.file_name.replace('.docx', '.pdf'))

            with open(pdf_output, 'wb') as pdf_file:
                pdf_file.write(pdf_response.content)
            
            # Send back the PDF file to the user
            with open(pdf_output, 'rb') as pdf_file:
                bot.send_document(message.chat.id, pdf_file)

            bot.send_message(message.chat.id, "Thank you for using our service!😊 This bot was created by Basith. 📜")
            
            # Clean up files
            os.remove(src)
            os.remove(pdf_output)
        else:
            bot.reply_to(message, "An error occurred during the conversion process.")
    
    except Exception as e:
        bot.reply_to(message, "An error occurred: " + str(e))

bot.infinity_polling()
