import streamlit as st
from cryptography.fernet import Fernet

# Set page configuration
st.set_page_config(page_title="Encryption", page_icon=":shushing_face:")

# Main title
st.title('Simple File Encryption WebApp')

# How to Use section
how_to_use_expander = st.expander("How to Use", expanded=False)
with how_to_use_expander:
    st.write("This simple File Encryption WebApp allows you to perform three operations:")
    st.write("1. **Encryption**: Upload a file and a key, and click 'Encrypt' to generate an encrypted file.")
    st.write("2. **Decryption**: Upload an encrypted file and its corresponding key, and click 'Decrypt' to get the original file.")
    st.write("3. **Generate New Key**: Enter a key name and click 'Generate New Key' to create a new encryption key.")

    st.write("Make sure to follow these steps:")
    st.write("1. Upload the correct files for the chosen operation.")
    st.write("2. For Encryption and Decryption, ensure that the key matches the operation.")
    st.write("3. Download the result after the operation is complete.")

st.write('---')

# Operation type selection
with st.container():
    option = st.radio('**Select Operation Type**', ('Encryption', 'Decryption', 'Generate New Key'))

    # Encryption section
    if option == 'Encryption':
        enc_file = None
        uploaded_file = st.file_uploader("Upload file Here")
        key_option = st.radio("Select Key Option", ('Upload Key', 'Type Key'))

        if key_option == 'Upload Key':
            uploaded_key = st.file_uploader("Upload Key Here", key="encryption_key")

            if uploaded_key is not None and uploaded_file is not None:
                if st.button('Encrypt'):
                    with st.spinner('Encrypting....'):
                        try:
                            cipher_suite = Fernet(uploaded_key.read())
                            file_content = uploaded_file.read()
                            enc_file = cipher_suite.encrypt(file_content)
                        except Exception as e:
                            st.write(f'Error: {e}')

        elif key_option == 'Type Key':
            entered_key = st.text_input("Enter Key:", type="password")

            if entered_key and uploaded_file is not None:
                if st.button('Encrypt'):
                    with st.spinner('Encrypting....'):
                        try:
                            cipher_suite = Fernet(entered_key.encode())
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
        key_option = st.radio("Select Key Option", ('Upload Key', 'Type Key'))

        if key_option == 'Upload Key':
            uploaded_key = st.file_uploader("Upload Key Here", key="decryption_key")

            if uploaded_key is not None and uploaded_file is not None:
                if st.button('Decrypt'):
                    with st.spinner('Decrypting....'):
                        try:
                            cipher_suite = Fernet(uploaded_key.read())
                            file_content = uploaded_file.read()
                            dec_file = cipher_suite.decrypt(file_content)
                        except Exception as e:
                            st.write(f'Error: {e}')

        elif key_option == 'Type Key':
            entered_key = st.text_input("Enter Key:", type="password")

            if entered_key and uploaded_file is not None:
                if st.button('Decrypt'):
                    with st.spinner('Decrypting....'):
                        try:
                            cipher_suite = Fernet(entered_key.encode())
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
            # Display the key in a text area for copying
            st.text_area("Copy this key:", value=key, height=100, key="copy_key_text_area", disabled=True)

st.write('---')
