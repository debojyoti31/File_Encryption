import streamlit as st
from cryptography.fernet import Fernet

# Set page configuration
st.set_page_config(page_title="Encryption", page_icon=":shushing_face:")

# Main title
st.title('Simple File Encryption WebApp')
st.write('---')

# Operation type selection
with st.container():
    option = st.radio('**Select Operation Type**', ('Encryption', 'Decryption', 'Generate New Key'))

    # Encryption section
    if option == 'Encryption':
        enc_file = None
        uploaded_file = st.file_uploader("Upload file Here")
        uploaded_key = st.file_uploader("Upload Key Here")

        if uploaded_key is not None and uploaded_file is not None:
            if st.button('Encrypt'):
                with st.spinner('Encrypting....'):
                    try:
                        cipher_suite = Fernet(uploaded_key.read())
                        file_content = uploaded_file.read()
                        enc_file = cipher_suite.encrypt(file_content)
                    except Exception as e:
                        st.write(f'Error: {e}')

        if enc_file is not None:
            st.download_button(
                label="Download Encrypted File",
                data=enc_file,
                file_name=uploaded_file.name
            )

    # Decryption section
    if option == 'Decryption':
        dec_file = None
        uploaded_file = st.file_uploader("Upload file Here")
        uploaded_key = st.file_uploader("Upload Key Here")

        if uploaded_key is not None and uploaded_file is not None:
            if st.button('Decrypt'):
                with st.spinner('Decrypting....'):
                    try:
                        cipher_suite = Fernet(uploaded_key.read())
                        file_content = uploaded_file.read()
                        dec_file = cipher_suite.decrypt(file_content)
                    except Exception as e:
                        st.write(f'Error: {e}')

        if dec_file is not None:
            st.download_button(
                label="Download Decrypted File",
                data=dec_file,
                file_name=uploaded_file.name
            )

    # Generate New Key section
    if option == 'Generate New Key':
        key_name = st.text_input("Enter Key Name (without extension):", "secret")
        key = None
        with st.spinner('Generating new key....'):
            try:
                key = Fernet.generate_key()
            except Exception as e:
                st.write(f'Error: {e}')

        if key is not None:
            key_filename = f"{key_name}.key"
            st.download_button(
                label=f"Download New Key ({key_filename})",
                data=key,
                file_name=key_filename
            )
