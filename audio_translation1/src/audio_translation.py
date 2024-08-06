import datetime
from transformers import MarianMTModel, MarianTokenizer
from data_preprocessing import audio_to_text

model_name = 'Helsinki-NLP/opus-mt-en-hi'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_text(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
    return translated_text

def translate_audio_after_6pm(audio_file):
    current_time = datetime.datetime.now().time()
    if current_time >= datetime.time(18, 0):
        text = audio_to_text(audio_file)
        if "Could not" not in text:
            return translate_text(text, model, tokenizer)
        else:
            return text
    else:
        return "Translation is only available after 6 PM IST."
