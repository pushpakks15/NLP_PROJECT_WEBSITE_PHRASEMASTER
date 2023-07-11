import paralleldots


class API:
    def __init__(self):
        paralleldots.set_api_key('lY5sxD5viMh6oOgJ5486gsGHhv5L7Nm8EWJ9nyJCBMI')

    def perform_sentiment(self,text):
        lang_code = "en"
        response=paralleldots.sentiment(text,lang_code)
        return response

    def perform_taxonomy(self,text):
        response = paralleldots.taxonomy(text)
        return response

    def perform_pe(self,text):
        response = paralleldots.phrase_extractor(text)
        return response

