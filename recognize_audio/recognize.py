""" python recognize.py --audio speech.pcm
"""

from argparse import ArgumentParser
from speechkit import model_repository, configure_credentials, creds
from speechkit.stt import AudioProcessingType

# Аутентификация через API-ключ.
configure_credentials(
    yandex_credentials=creds.YandexCredentials(
        api_key='<API-ключ>'
    )
)

def recognize():
    model = model_repository.recognition_model()

    # Задайте настройки распознавания.
    model.model = 'general'
    model.language = 'ru-RU'
    model.audio_processing_type = AudioProcessingType.Full
    audio_path = "audio.m4a"
    output_path = "output.txt"

    # Распознавание речи в указанном аудиофайле и вывод результатов в консоль.
    result = model.transcribe_file(audio_path)
    with open(output_path, "a") as stream:

        for c, res in enumerate(result):
            print('=' * 80)
            print(f'channel: {c}\n\nraw_text:\n{res.raw_text}\n\nnorm_text:\n{res.normalized_text}\n')
            if res.has_utterances():
                print('utterances:')
                for utterance in res.utterances:
                    print(utterance)
            stream.write(res.normalized_text)

if __name__ == '__main__':

    recognize()