class StringTools:

    def reverse(self, text):
        return text[::-1]

    def uppercase(self, text):
        return text.upper()

    def lowercase(self, text):
        return text.lower()

    def count_words(self, text):
        return len(text.split())