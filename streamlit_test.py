import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components as stc
import hashlib
import time
import base64
from PIL import Image
import emoji
import os
from termcolor import colored



timestr = time.strftime("%Y%m%d-%H%M%S")
def welcome():
    return "WELCOME ALL"


class FileDownloader(object):

    def __init__(self, data, filename="Encrypted data",file_ext="txt"):
        super(FileDownloader, self).__init__()
        self.data = data
        self.filename = filename
        self.file_ext = file_ext
 
        
    def download(self):
        b64 = base64.b64encode(self.data.encode()).decode()
        new_filename= "{}_{}_{}".format(self.filename, timestr, self.file_ext)
        st.markdown("### Download File ###")
        href = f'<a href="data:file/{self.file_ext};base64, {b64}" download="{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)

def encode_mobile(inp):
        return hashlib.sha256(str(inp).encode()).hexdigest()


def main():

    image = Image.open("Tata-AIA-Logojpg.jpg")
    st.image(image, width=300)
    # st.title("TATA AIA LIFE INSURANCE")
    html_temp  = """
    <div style="background-color:coral;padding:10px">
    <h2 style= "color:black;text-align:center;">DATA ENCRYPTION &#128274</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.subheader("Dataset")
    data_file=  st.file_uploader("Upload Excel File", type=[".xlsx"])
    if data_file is not None:

        file_details = {"filename": data_file.name, "filetype":data_file.type, "filesize": data_file.size}
        st.write(file_details)
        # df = pd.read_csv(data_file)
        df = pd.read_excel(data_file, engine='openpyxl')
        df = df.astype(str)
        st.dataframe(df)
        df.shape
        enc_column = st.selectbox("What would you like to encrypt?", tuple(df.columns))
        st.write("You selected: ", enc_column)
        df['ENCRYPTED_{}'.format(enc_column)]=df[enc_column].apply(encode_mobile)
        st.dataframe(df)
        st.download_button(
            label = "Download File",
            data = df.to_csv(),
            file_name = "Encrypted_file_{}_.csv".format(timestr))
        # if st.button("Download File"):
            # FileDownloader(df.to_csv(), file_ext=".csv").download()

    #     ### saving uploaded file

    #     with open(os.path.join("Streamlit_Test", data_file.name),"wb") as f:
    #         f.write((data_file).getbuffer())

    #     st.success("File Saved")

    ### Download file

    # df['ENCRYPTED_MOBILENO']=df['ADMOBILENO'].apply(encode_mobile)

    # menu = ["Excel", "CSV", "Text"]

    # choice = st.sidebar.selectbox("Menu", menu)

    # if choice == "Text":
    #     st.subheader("Text")
    #     my_text = st.text_area("message")
    #     if st.button("Save"):
    #         st.write(my_text)
    #         download = FileDownloader(my_text).download()

    # elif choice == "CSV":
    #     download = FileDownloader(df.to_csv(), file_ext=".csv").download()

    # elif choice== "Excel":
    #     download = FileDownloader(df.to_excel(excel_writer="file"), file_ext=".xlsx").download()
    
    



if __name__=='__main__':
    main()