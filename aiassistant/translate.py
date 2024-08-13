from googletrans import Translator

def translate(phrase, target_language):
    """
    Translates a given phrase to the specified target language using Google Translate.

    Args:
        phrase (str): The text to translate.
        target_language (str): The language code of the target language (e.g., 'es' for Spanish).

    Returns:
        str: The translated text.
    """
    translator = Translator()
    try:
        translation = translator.translate(phrase, dest=target_language)
        return translation.text
    except Exception as e:
        return f"Error: {str(e)}"


