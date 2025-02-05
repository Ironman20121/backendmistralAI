from mistralai import Mistral
from gen_resume import generate_resume
from time import sleep 
from sys import argv

class ResumeHelper :

    def __init__(self,JD):
        self.JD = JD
        self.keywords_list =[]
        self.keywords_list_str=""
        self.resume =""
        with open('/Users/saikundansuddapalli/Documents/Automation/JobApplicationHelper/resume.txt')as f:self.resume=f.read()    
        self.getKeywords()
        # print(self.keywords_list_str)
    
    @staticmethod
    def askai(sentence):
        try:
            sleep(1)
            api_key = "FR3AgcQjoJmjaQyJlDaMmMvWquOMZv96"
            model = "mistral-large-latest"
            client = Mistral(api_key=api_key)
            chat_response = client.chat.complete(model=model,messages=[ {"role":"user", "content":f"{sentence}"}  ])
            return chat_response.choices[0].message.content
        except Exception as e:
            print(e)

    def remove_chars(self,sentence):
        chars_to_remove = ['[', ']', '\n']
        for char in chars_to_remove:
            sentence = sentence.replace(char, '')  
        return sentence

    def getKeywords(self):
        sen= f"Please extract all important keywords from the job description below and format them as a comma-separated string. This string should be easily parsable into a Python list. Only provide the keywords, avoiding any additional information: {self.JD}"
        self.keywords_list_str =  ResumeHelper.askai(sen)
        self.keywords_list =self.keywords_list_str.split(",")
        # print(self.keywords_list_str)
        # print(self.keywords_list)
    
    def getSummery(self):
        sen = f"""I am looking to create a compelling summary for my resume. 
        Here are some keywords that represent my skills and experience: {self.keywords_list_str}.
        Additionally, here are key details from my resume: {self.resume}.
        Please help me craft a concise and impactful summary that highlights my strengths and aligns with these keywords. 
        The summary should be a single paragraph, no more than 6 lines, and should not mention my BA/BS in Computer Science, as I have a Master's in Computer Science."""
        return ResumeHelper.askai(sen)
    
    def getGradeExp(self):
        prompt =f"""
        Analyze the following exprience  Graduate Researchip experience and job description keywords to generate a Python list of  sentences describing relevant experience. 
        Each sentence should be concise and focus on connecting skills and experience from the resume to the job description keywords.  
        The output should be a valid Python list of string , with each sentence as a string element within the list.  
        If no relevant connections can be made, return an empty list: []. 
        avoid give me like this this'``````python\\n[\\n "sentence1\\n,sentence2````\\n]\\n
        just give me like this setence1,sentenc2.........sentence n  just make easy for me to parse later simple.split(',')
        exprience : 
         Contributed to the development of an advanced version of the CrystaLLM library for large language models, focusing on interpretability and explainability, to aid in the discovery of novel therapeutic compounds for Alzheimer’s disease. Led
research in training deep models (e.g., GPT-based architecture) to predict chemical properties, accelerating drug
discovery processes.
• Utilized LoRA to fine-tune existing open-source LLM models (e.g., LLaMA, GEEMA) for specific chemical tasks.
• Utilized high-performance computing resources (HPC) on Bridges to expedite training and inference.
• Developed and led tutorials on Quantum Computing using IBM Quantum Experience and Qiskit.
        Job Description Keywords: {self.keywords_list_str}
        make sure I want only 4 sentence not
        """
        sentences = ResumeHelper.askai(prompt).split(',')
        return sentences

    def getCppExp(self):
        sen =f"""
        Analyze the following exprience  in TCS as C++ and python developer  experience and job description keywords to generate a Python list of up to only 4 sentences describing relevant experience. 
        Each sentence should be concise and focus on connecting skills and experience from the resume to the job description keywords.  
        The output should be a valid Python list of string , with each sentence as a string element within the list.  
        If no relevant connections can be made, return an empty list: []. 
        avoid give me like this this'``````python\\n[\\n "sentence1\\n,sentence2````\\n]\\n
        just give me like this setence1,sentenc2.........sentence n  just make easy for me to parse later simple.split(',')
        exprience : 
        
        Job Description Keywords: {self.keywords_list_str}
        """
        sentence = ResumeHelper.askai(sen).split(',')
        return sentence
    
    def getFullStack(self):
        sen =f"""
        Analyze the following exprience  in TCS as C++ and python developer  experience and job description keywords to generate a Python list of up to only 4 sentences describing relevant experience. 
        Each sentence should be concise and focus on connecting skills and experience from the resume to the job description keywords.  
        The output should be a valid Python list of string , with each sentence as a string element within the list.  
        If no relevant connections can be made, return an empty list: []. 
        avoid give me like this this'``````python\\n[\\n "sentence1\\n,sentence2````\\n]\\n
        just give me like this setence1,sentenc2.........sentence n  just make easy for me to parse later simple.split(',')
        exprience : 
        Job Description Keywords: {self.keywords_list_str}
        """
        sentence = ResumeHelper.askai(sen).split(',')
        return sentence
    def getDrdo(self):
        sen =f"""
        Analyze the following exprience  in TCS as C++ and python developer  experience and job description keywords to generate a Python list of up to only 4 sentences describing relevant experience. 
        Each sentence should be concise and focus on connecting skills and experience from the resume to the job description keywords.  
        The output should be a valid Python list of string , with each sentence as a string element within the list.  
        If no relevant connections can be made, return an empty list: []. 
        avoid give me like this this'``````python\\n[\\n "sentence1\\n,sentence2````\\n]\\n
        just give me like this setence1,sentenc2.........sentence n  just make easy for me to parse later simple.split(',')
        exprience : 
        Job Description Keywords: {self.keywords_list_str}
        """
        sentence = ResumeHelper.askai(sen).split(',')
        return sentence
    def getUnisys(self):
        sen =f"""
        Analyze the following exprience  in TCS as C++ and python developer  experience and job description keywords to generate a Python list of up to only 4 sentences describing relevant experience. 
        Each sentence should be concise and focus on connecting skills and experience from the resume to the job description keywords.  
        The output should be a valid Python list of string , with each sentence as a string element within the list.  
        If no relevant connections can be made, return an empty list: []. 
        avoid give me like this this'``````python\\n[\\n "sentence1\\n,sentence2````\\n]\\n
        just give me like this setence1,sentenc2.........sentence n  just make easy for me to parse later simple.split(',')
        exprience : 
        Job Description Keywords: {self.keywords_list_str}
        """
        sentence = ResumeHelper.askai(sen).split(',')
        return sentence
    
    def getPro_one(self):
        sen =f"""
        Analyze the following base resume's project 1 Multi-threaded TA-Student Simulation  and job description keywords to generate a Python list of up to 10 sentences describing relevant experience. 
        Each sentence should be concise and focus on connecting skills and experience from the resume to the job description keywords.  
        The output should be a valid Python list enclosed in square brackets, with each sentence as a string element within the list.  
        If no relevant connections can be made, return an empty list: [].
        Base Resume: {self.resume}
        Job Description Keywords: {self.keywords_list_str}
        """
        sentence = ResumeHelper.askai(sen).split(',')
        return sentence
    
    def getPro_two(self):
        sen =f"""
        Analyze the following base resume  TCS C++ and python experience and job description keywords to generate a Python list of up to 10 sentences describing relevant experience. 
        Each sentence should be concise and focus on connecting skills and experience from the resume to the job description keywords.  
        The output should be a valid Python list enclosed in square brackets, with each sentence as a string element within the list.  
        If no relevant connections can be made, return an empty list: [].
        Base Resume: {self.resume}
        Job Description Keywords: {self.keywords_list_str}
        """
        sentence = ResumeHelper.askai(sen).split(',')
        return sentence





    # def getExpCount(self):
    #     sen = f"Please review the job description: {self.JD} and provide the ideal number of years of experience to mention in order to maximize the chances of being shortlisted. Note: Please respond with only the number, without any additional characters."
    #     try:
    #         self.exp = int(ResumeHelper.askai(sen))
    #         # print(self.exp,type(self.exp))
    #     except Exception as e:
    #         print(e)
    # def getProjectCount(self):
    #     sen = f"Please review the job description: {self.JD} and provide the ideal number of projects  to mention in order to maximize the chances of being shortlisted. Please respond with only the number, without any additional characters or text"
    #     try:
    #         self.pro_num = int(ResumeHelper.askai(sen))
    #     except Exception as e:
    #         print(e)


def main():
    JD =''
    with open('/Users/saikundansuddapalli/Documents/Automation/JobApplicationHelper/userinput.txt','r') as f:
        JD = f.read()
    rh = ResumeHelper(JD)
    s,g = rh.getSummery(),rh.getGradeExp()
    print(type(g),len(g),g,sep=",")

    # summery, grad_exp,cpp_exp,drdo,unisys,proj1,proj2= rh.getSummery(),



if __name__=="__main__" : main()