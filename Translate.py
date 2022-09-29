import translators as ts


def translate(text, lang):
    trans = ts.google(text, to_language=lang)
    return trans
