import urllib.request
import re
import io
import random
import pytesseract
import requests
from PIL import Image

res = 'CON, PRN, AUX, NUL,COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8, COM9, LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, LPT9'
res = res.split(',')
for i in ['#', '<', '>', '$', '+', '%', '!', '`', '&', '*', "'", '|', '{', '}', '/', '\\', '?', ':', '"', '=', '@', '.', ',', '\n']:
    res.append(i)


def deEmojify(text):
    regrex_pattern = re.compile(pattern="["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "❗"
                                "�🥂"
                                "@""]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


def text_extractor(text):
    end = ''
    try:
        start, end = re.search("text that says", text).span()
        new_string = ''

        for i in range(end+1, len(text)):
            new_string += text[i]

        new_string = new_string.lower()

        words = ['300x', '6amsuc', 'Success  ', 'fuck failure', 'fuck failur', 'age_of_attitude', 'age_o', '300xsuccess', '3qoxsuccess',
                 'instagram', 'joel brown', 'word_of_wizard', '6amsuccess', 'millionaire dream', 'success slogans', 'xcom', 'houseofmat', '�', '日', 'ge_of_attitude',
                 'e_of_attitude', '10', '_attitude', 'f attitude', 'fuck eailure', 'fuck', 'ho fuck', 'luxquotes', '团', '一', '_of_',
                 '.jpg', '24hoursuccess', 'ハ4', '可福ご國и到', '可福ご國и', '可福ご國', '可福ご', '可福', '可', 'eeeeeece', 'ηy', 'η', 'కండి', 'కం', 'డి',
                 'follow cess', '星m', '🤙', '🤓', '🤷‍♂️', '🧞‍♂️', 'audrey hepburn', '제', 'f_attitud', 'uck', '3q0xsuccess', 'wordofwizard', 'word_of', 'f_ttitude', 'Xx', 'ufc', 'Ufc', '[', ']', 'THRIVIX', 'thrivix', 'Thrivix']

        extracted_text = new_string

        for i in words:
            extracted_text = extracted_text.replace(i, '')
    except:
        extracted_text = ''
    return extracted_text.strip().capitalize()
# file = open("Image Downloader/Download " +
#             str(dt.datetime.now().strftime("%Y-%m-%d"))+".txt", 'w')
# file.write("Downloads\n\n\n")


def download_image(url, loc, string):
    text = string
    for i in res:
        text = text.replace(i, '')
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content))
    # try:
    #     string = string[string.index('Im'):]
    # except:
    #     pass
    try:
        text = text.strip()
        text = deEmojify(text)
        text = text_extractor(text)
    except:
        pass
    fullname = loc + text + ".jpg"

    if text == '': 
        fullname = loc+'No Alt/' + str(random.randint(1, 10000)) + ".jpg"

    try:
        urllib.request.urlretrieve(url, fullname)
        print(fullname, "saved")
    except Exception as e:
        print(e)
        pass
