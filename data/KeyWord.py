# All Code together
import sys
import os
import docx

if not sys.argv:
    print("need to specify file path")
    sys.exit(1)

file_name = sys.argv[1]
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_PATH = "{}/{}".format(ROOT_DIR, file_name)

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def check_key_words():
    keywords_list = {'Software Developer': ['teamwork',
 'workflow',
 'microsoft',
 'ecommerce',
 'html5',
 'developer',
 'online',
 'tools',
 'corporate',
 'html']}
    keywords = keywords_list['Software Developer']
    resume = getText(FILE_PATH)
    corpus = resume.split()
    corpus = [x.lower() for x in corpus]
    corpus = [x.replace(',', '') for x in corpus]
    corpus = [x.replace('.', '') for x in corpus]
    key_words_new = [x.lower() for x in keywords]
    for word in key_words_new:
        if (word in corpus):
            print ("Your resume used the word {} which is a keyword for resumes of this type.".format(word))
        else:
            print("You did not use the word {} which is key for a software developer job.".format(word))

if __name__ == '__main__':
    check_key_words()