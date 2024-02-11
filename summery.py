import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """India is a beautiful land with a variety of wildlife and rich cultural diversity. The Bengal Tiger is considered the national animal of India. India celebrates its Independence Day on 15th August every year. It is observed to commemorate the freedom of India from the British. The tri-coloured national flag is called Tiranga, designed with saffron, white and green with the Ashok Chakra in navy blue at the centre of the flag. ‘Lion Capital of Ashoka’ is the country’s national emblem. The national motto is ‘Satyameva Jayate,’ which means truth alone wins.

In order to run the country smoothly, and make it an independent country, there was a need for a constitution which came into force on 26th January 1950. We observe this day as Republic Day every year.

India is a land of many different languages and many different religions such as Buddhism, Jainism, Islam, Hinduism, etc. There are various food styles and dressing styles depending on the regions of the country, setting the perfect example of Unity in Diversity."""

def summarizer(rawdocs):

    stopwords = list(STOP_WORDS)
    # print(STOP_WORDS) 
    # - stop words are those by removing which the senstence has no meaning

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    # print(doc)
    #  - prints the entire paragraph

    tokens = [token.text for token in doc]
    # print(tokens) 
    # - tokenizes all the words including punctuations and commas


    #The following function will pick all the wordss from the document (23,24), and words will we converted in to text and then lowercase (25) , the we will check word should not be presesnt in stopwords and punctuations. if it is a punctutaion or stopword then we will eleminate else we will go in line 26,
    # 26 states that weather the word is in word freq table or not which is 
        # {
        #     a : 1,
        #     b : 1
        # }

    # if not present then put 1 and if already exist then add +1 (36,37)


    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

        # print(word_freq)

    #finding maximum frequency           
    max_freq = max(word_freq.values())

    # print(max_freq)


    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

    # print(word_freq)

    sent_tokens =  [sent for sent in doc.sents]
    # print(sent_tokens)

    sent_scores = {}
    for sent in sent_tokens :
        for word in sent :
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else :
                    sent_scores[sent] += word_freq[word.text]



    # print(sent_scores)
                    
    select_len = int(len(sent_tokens) * 0.3)
    # print(select_len)
    summary = nlargest(select_len, sent_scores, key=sent_scores.get)
    # print(summery)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    # print(text)
    # print(summary)

    # print("Length of original text", len(text.split(' ')))
    # print("Length of summary text", len(summary.split(' ')))

    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))






