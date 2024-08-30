from flask import Flask, request, jsonify
from libretranslatepy import LibreTranslateAPI

app = Flask(__name__)

lt = LibreTranslateAPI("https://translate.terraprint.co/")

LANGUAGE_MAP = {
    "english": "en",
    "spanish": "es",
    "french": "fr",
    "german": "de",
    "chinese": "zh",
    "japanese": "ja",
    "russian": "ru",
    "italian": "it",
    "portuguese": "pt",
    "arabic": "ar",
    "korean": "ko",
    "hindi": "hi",
    "bengali": "bn",
    "urdu": "ur",
    "turkish": "tr",
    "albanian":"sq",
    "azerbaijani":"az",
    "bulgarian":"bg",
    "Catalan":"ca",
    "Chinese (traditional)":"zt",
    "Czech":"cs",
    "Danish":"da",
    "Dutch":"nl",
    "Esperanto":"eo",
    "Estonian":"et",
    "Finnish":"fi",
    "Greek":"el",
    "Hebrew":"he",
    "Hungarian":"hu",
    "Indonesian":"id",
    "Irish":"ga",
    "Latvian":"lv",
    "Lithuanian":"lt",
    "Malay":"ms",
    "Norwegian":"nb",
    "Persian":"fa",
    "Polish":"pl",
    "Romanian":"ro",
    "Serbian":"sr",
    "Slovak":"sk",
    "Slovenian":"sl",
    "Swedish":"sv",
    "Tagalog":"tl",
    "Thai":"th"
}

@app.route('/api/translate', methods=['POST'])
def translate():
    try:
        data = request.json
        text = data.get('text')
        source_lang_name = data.get('source_lang', 'auto')
        target_lang_name = data.get('target_lang')

        if not text or not target_lang_name:
            return jsonify({"error": "Please provide text and target_lang"}), 400

        source_lang = LANGUAGE_MAP.get(source_lang_name.lower(), 'auto')
        if source_lang_name != 'auto' and source_lang == 'auto':
            return jsonify({"error": "Unsupported source language"}), 400

        target_lang = LANGUAGE_MAP.get(target_lang_name.lower())
        if not target_lang:
            return jsonify({"error": "Unsupported target language"}), 400

        translation = lt.translate(text, source_lang, target_lang)
        response_data = {
            "text": text,
            "text_language": source_lang_name,
            "translated_text": translation,
            "translated_language": target_lang_name
        }
        return jsonify(response_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
