import streamlit as st
from cryptography.fernet import Fernet

# Set page configuration
st.set_page_config(page_title="Encryption", page_icon=":shushing_face:")

# Main title
st.title('Simple File Encryption WebApp')
st.write('---')

# Operation type selection
with st.container():
    option = st.radio('**Select Operation Type**', ('Generate New Key', 'Encode', 'Decode'))

    # Generate New Key section
    if option == 'Generate New Key':
        key = None
        with st.spinner('Generating new key....'):
            try:
                key = Fernet.generate_key()
            except Exception as e:
                st.write(f'Error: {e}')

        if key is not None:
            st.download_button(
                label="Download New Key",
                data=key,
                file_name='secret.key'
            )

    # Encode section
    if option == 'Encode':
        enc_file = None
        uploaded_file = st.file_uploader("Upload file Here")
        uploaded_key = st.file_uploader("Upload Key Here")

        if uploaded_key is not None and uploaded_file is not None:
            if st.button('Encode'):
                with st.spinner('Encoding....'):
                    try:
                        cipher_suite = Fernet(uploaded_key.read())
                        file_content = uploaded_file.read()
                        enc_file = cipher_suite.encrypt(file_content)
                    except Exception as e:
                        st.write(f'Error: {e}')

        if enc_file is not None:
            st.download_button(
                label="Download Encoded File",
                data=enc_file,
                file_name=uploaded_file.name
            )

    # Decode section
    if option == 'Decode':
        dec_file = None
        uploaded_file = st.file_uploader("Upload file Here")
        uploaded_key = st.file_uploader("Upload Key Here")

        if uploaded_key is not None and uploaded_file is not None:
            if st.button('Decode'):
                with st.spinner('Decoding....'):
                    try:
                        cipher_suite = Fernet(uploaded_key.read())
                        file_content = uploaded_file.read()
                        dec_file = cipher_suite.decrypt(file_content)
                    except Exception as e:
                        st.write(f'Error: {e}')

        if dec_file is not None:
            st.download_button(
                label="Download Decoded File",
                data=dec_file,
                file_name=uploaded_file.name
            )
