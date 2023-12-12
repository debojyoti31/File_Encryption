import streamlit as st
from cryptography.fernet import Fernet

st.set_page_config(page_title="Encryption", page_icon=":shushing_face:")

st.title('Simple File Encryption WebApp')
st.write('---')

with st.container():
    option = st.radio('**Select Operation Type**', ('Generate New Key','Encode', 'Decode'))



    if option == 'Generate New Key':
        key = None
        with st.spinner('generating new key....'):
                    try:
                        key = Fernet.generate_key()
                    except Exception as e:
                        st.write(f'Error: {e}')
        
        if key is not None:
            st.download_button(
                    label="Download New key",
                    data=key,
                    file_name='secret.key'
                )


    if option == 'Encode':
        encFile = None
        uploaded_file = st.file_uploader("Upload file Here")
        uploaded_key = st.file_uploader("Upload Key Here")
        if uploaded_key is not None and uploaded_file is not None:
            if st.button('Encode'):
                with st.spinner('encoding....'):
                    try:
                        cipher_suite = Fernet(uploaded_key.read())
                        file_content = uploaded_file.read()
                        encFile = cipher_suite.encrypt(file_content)

                    except Exception as e:
                        st.write(f'Error: {e}')

        if encFile is not None:
            st.download_button(
                label="Download encoded file",
                data=encFile,  # Download buffer
                file_name=uploaded_file.name
            )


    if option == 'Decode':
        decFile = None
        uploaded_file = st.file_uploader("Upload file Here")
        uploaded_key = st.file_uploader("Upload Key Here")
        if uploaded_key is not None and uploaded_file is not None:
            if st.button('Decode'):
                with st.spinner('decoding....'):
                    try:
                        cipher_suite = Fernet(uploaded_key.read())
                        file_content = uploaded_file.read()
                        decFile = cipher_suite.decrypt(file_content)

                    except Exception as e:
                        st.write(f'Error: {e}')

        if decFile is not None:
            st.download_button(
                label="Download decoded file",
                data=decFile,  # Download buffer
                file_name=uploaded_file.name
            )
