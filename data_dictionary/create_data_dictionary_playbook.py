from data_dictionary import constants
from docx import Document


# PLAYBOOK_FILE = constants.PLAYBOOK_FOLDER / 'USAID NextGen SCCT Implementing Partner Onboarding Playbook v1.1.docx'
PLAYBOOK_FILE = constants.PLAYBOOK_FOLDER / 'small.docx'

def read_word_doc(filename):
    doc = Document(filename)
    full_text = []
    print(str(doc))
    for para in doc.paragraphs:
        full_text.append(para.text)
        #print(str(para.text))
    return '\n'.join(full_text)

if __name__ == "__main__":
    text = read_word_doc(PLAYBOOK_FILE)
    #print(text)