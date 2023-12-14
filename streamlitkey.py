import streamlit as st
from cryptography.fernet import Fernet

# Set page configuration
st.set_page_config(page_title="Encryption", page_icon=":shushing_face:")

# Main title
st.title('Simple File/Text Encryption WebApp')

# How to Use section
how_to_use_expander = st.expander("README", expanded=False)
with how_to_use_expander:
    st.write("This simple File Encryption WebApp uses the [Fernet symmetric encryption algorithm](https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py),")
    st.write("to perform three operations:")
    st.write("1. **Encryption**: Upload a file or write text, and a key. Click 'Encrypt' to generate an encrypted file or text.")
    st.write("2. **Decryption**: Upload an encrypted file or write text, and its corresponding key. Click 'Decrypt' to get the original file or text.")
    st.write("3. **Generate New Key**: Enter a key name and click 'Generate New Key' to create a new encryption key.")

    st.write("Make sure to follow these steps:")
    st.write("1. Upload the correct files for the chosen operation or write text.")
    st.write("2. For Encryption and Decryption, ensure that the key matches the operation.")
    st.write("3. Download the result after the operation is complete.")

st.write('---')

# Operation type selection
with st.container():
    option = st.radio(':red[**Select Operation Type**]', ('Encryption', 'Decryption', 'Generate New Key'))

    # Encryption section
    if option == 'Encryption':
        enc_file = None

        uploaded_key = st.file_uploader("Upload Key Here")
        
        upload_option = st.radio("Select input type:", ('Upload File', 'Write Text'))

        if upload_option == 'Upload File':
            uploaded_file = st.file_uploader("Upload file Here")
            file_content = uploaded_file.read() if uploaded_file is not None else None

        elif upload_option == 'Write Text':
            file_content = st.text_area("Enter Text Here").encode()        

        if uploaded_key is not None and file_content is not None:
            if st.button('Encrypt'):
                with st.spinner('Encrypting....'):
                    try:
                        cipher_suite = Fernet(uploaded_key.read())
                        enc_file = cipher_suite.encrypt(file_content)
                    except Exception as e:
                        st.write(f'Error: {e}')

        if enc_file is not None:
            if upload_option == 'Upload File':
                st.download_button(
                    label="Download Encrypted File",
                    data=enc_file,
                    file_name=uploaded_file.name
                )
            elif upload_option == 'Write Text':
                st.write("Encrypted Text:")
                st.code(enc_file.decode(), language=None)

    # Decryption section
    if option == 'Decryption':
        dec_file = None

        uploaded_key = st.file_uploader("Upload Key Here")
        
        upload_option = st.radio("Select input type:", ('Upload File', 'Write Text'))

        if upload_option == 'Upload File':
            uploaded_file = st.file_uploader("Upload file Here")
            file_content = uploaded_file.read() if uploaded_file is not None else None

        elif upload_option == 'Write Text':
            file_content = st.text_area("Enter Text Here").encode()

        if uploaded_key is not None and file_content is not None:
            if st.button('Decrypt'):
                with st.spinner('Decrypting....'):
                    try:
                        cipher_suite = Fernet(uploaded_key.read())
                        dec_file = cipher_suite.decrypt(file_content)
                    except Exception as e:
                        st.write(f'Error: {e}')

        if dec_file is not None:
            if upload_option == 'Upload File':
                st.download_button(
                    label="Download Decrypted File",
                    data=dec_file,
                    file_name=uploaded_file.name
                )
            elif upload_option == 'Write Text':
                st.write("Decrypted Text:")
                st.code(dec_file.decode(), language=None)

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

st.write('---')
