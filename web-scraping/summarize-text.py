# pip install sumy
# python -c "import nltk; nltk.download('punkt')"

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"
SENTENCES_COUNT = 10

def summarize_from_parser(parser, language, sentences_count):
    stemmer = Stemmer(language)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)

    for sentence in summarizer(parser.document, sentences_count):
        print(sentence)

def summarize_from_url(url, language, sentences_count):
    parser = HtmlParser.from_url(url, Tokenizer(language))
    summarize_from_parser(parser,language, sentences_count)

def summarize_from_text_file(filename, language, sentences_count):
    parser = PlaintextParser.from_file(filename, Tokenizer(language))
    summarize_from_parser(parser, language, sentences_count)

# main program

summarize_from_url(
        #url="https://en.wikipedia.org/wiki/Automatic_summarization", 
        #url="https://en.wikipedia.org/wiki/Python_(programming_language)",
        url="https://time.com/5521860/2019-state-of-the-union-trump-transcript/",
        language=LANGUAGE, 
        sentences_count=SENTENCES_COUNT)

#summarize_from_text_file(
#        filename="thoreau-walden.txt", 
#        language=LANGUAGE, 
#        sentences_count=SENTENCES_COUNT)
