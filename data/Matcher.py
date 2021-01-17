# Import the library
# pip install docx2txt
import pandas as pd
import docx2txt
import sys
import os
import docx

if not sys.argv:
    print("need to specify file path")
    sys.exit(1)

file_name = sys.argv[1]
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_PATH = "{}/{}".format(ROOT_DIR, file_name)

def which_data(name):
    if name == 'Developer':
        return "{}/{}".format(ROOT_DIR, 'dev.csv')
    
def Get_Corpus(Data):
    dataframe = pd.read_csv(Data, encoding='cp1252')
    dataframe.columns = [list(range(len(dataframe.columns)))]
    return list(dataframe[(2,)])

# Store the resume in a variable
def MATCHER(name):
    resume_doc = docx2txt.process(FILE_PATH)
    Job_Description_Data = which_data(name)
    Percentages = []
    DataFrame = pd.read_csv(Job_Description_Data, encoding='cp1252')
    DataFrame.columns = ['Index', 'Job Name', 'Job Description', 'Link to Job']
    for i in range(len(DataFrame)):
        job_description = Get_Corpus(Job_Description_Data)[i] 

        text = [resume_doc, job_description]

        from sklearn.feature_extraction.text import CountVectorizer
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(text)

        from sklearn.metrics.pairwise import cosine_similarity

    #Print the similarity scores
    #print("\nSimilarity Scores:")
    #print(cosine_similarity(count_matrix))

        #get the match percentage
        matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
        matchPercentage = round(matchPercentage, 2) # round to two decimal
        Percentages.append(matchPercentage)
    Per_data = pd.DataFrame(Percentages)
    Per_data.columns = ['Percentage Match']
    output = pd.concat([DataFrame, Per_data], axis=1)
    output.drop(columns=['Index'], inplace = True)
    output.drop(columns=['Job Description'], inplace = True)
    output = output.sort_values(by=['Percentage Match'], ascending = False)
    output.to_csv("data/Output.csv")

    
if __name__ == '__main__':
    MATCHER('Developer')

  
