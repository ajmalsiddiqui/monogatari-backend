# The implementation of TextRank from the gensim library
# from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

def extract_keywords(text):
  '''
  Returns the keywords from a given body of text. Requires more than one sentence as input.

  Parameters
  text: A body of text with multiple sentences
  '''

  return keywords(text)