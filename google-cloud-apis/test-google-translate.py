# pip install google-cloud-translate
# export GOOGLE_APPLICATION_CREDENTIALS

from google.cloud import translate
client = translate.TranslationServiceClient()

print("Please enter text to be translated in English:")
text_source = input()
text = client.translate_text(contents=[text_source], 
    target_language_code='en', 
    parent='projects/platinum-device-722')
print(text)