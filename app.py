# We iwll create all the application here.
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#FUNTION TO GET RESPONSE FROM THE LLAMA MODEL
def GetLLamaResponse(input_text,no_word,blog_style):
    '''Calling LLama2 model
    '''
    llm = CTransformers(model =r'C:\Users\hafsa\Desktop\Blog_generation\models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type= 'llama',
                         config = {'max_new_tokens':256,
                                   'temperature':0.01} )
    ##Prompt Tempelate
    template = """
     write a blog for {blog_style} job profile for a topic{input_text} for {no_word} number of words
    """
    prompt = PromptTemplate(input_variables = ['blog_style','input_text','no_word'],
                             template=template)
    ##Generate the response from LLama 2
    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_word=no_word))
    print("response", response)
    return response





#THIS IS A GUI SETUP USING STREAMLIT
st.set_page_config(page_title="Generate Blogs",
                   layout="centered",
                   initial_sidebar_state="collapsed"

)
st.header("GENERATE BLOGS")
input_text  = st.text_input('Enter Blog Topic:')

#creating 2 more coloumns
col1,col2 = st.columns([5,5])
with col1:
    no_word = st.text_input("No. of words")
with col2:
    blog_style = st.selectbox('Writing blog for',('Researchers','Data Scientist','Common People'),index=0)
submit = st.button("Generate")
if submit:
    st.write(GetLLamaResponse(input_text,no_word,blog_style))