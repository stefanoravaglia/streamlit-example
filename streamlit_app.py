import os
import streamlit as st

def secrets_display():
    ''' app '''

    '''
    # Welcome to Streamlit!

    ## [Secrets management](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)

    > Edit `/streamlit_app.py` to customize this app \n
    > [documentation](https://docs.streamlit.io) \n
    > [community forums](https://discuss.streamlit.io) \n

    '''

    ''' 
    ---
    ##### .\\\\.streamlit\secrets.toml
    ##### remove from commits using .gitignore
    ---
    '''
    st.write(st.secrets)
    st.write(type(st.secrets))

    '''
    ---
    ##### secrets are accessible via the st.secrets dict:
    ##### by *key notation*: st.secrets["key"]
    ---
    '''
    st.write("username: ", st.secrets["st_username"])
    st.write("password: ", st.secrets["st_password"])
    st.write("section: ", st.secrets["st_section"]["st_list"])
    st.write(type(st.secrets["st_section"]["st_list"]))
    st.write(type(st.secrets["st_section"].st_list))
    '''
    ---
    ##### by *attribute notation*: st.secrets.key
    ---
    '''
    st.write("username: ", st.secrets.st_username)
    st.write("password: ", st.secrets.st_password)
    st.write("section: ", st.secrets.st_section["st_list"])
    st.write(type(st.secrets.st_section["st_list"]))
    st.write(type(st.secrets.st_section.st_list))

    '''
    ---
    ##### root-level secrets are accessible as environment variables, too:
    ---
    '''
    st.write(
        "Has environment variables been set:",
        os.environ["st_username"] == st.secrets["st_username"]
    )

    '''
    ---
    ##### TOML sections to compactly pass multiple secrets as a single attribute
    ---
    '''

    def f(*args, **kwargs):
        ''' accessing args and key-value args
        '''
        st.write(" - args [{}]".format(type(args))) # touple
        for i, arg in enumerate(args):
            st.write( '- {}. {}'.format(i, arg))

        st.write("- kwargs [{}]".format(type(kwargs))) # dict
        for key, value in kwargs.items():
            st.write( '- {} = {}'.format(key, value))

    st.write(st.secrets.st_arguments)
    st.write(type(st.secrets.st_arguments))

    f(*st.secrets.st_arguments, **st.secrets.st_arguments)

    '''
    ...a
    '''
    
def secrets_manage():
    ''' st.secrets dict managing
    '''
    pass

def secrets_check():
    ''' tests if st.secrets dict is ok
    '''
    return st.secrets.has_key("st_username")

def app():
    ''' the app
    '''
    secrets_display()

def main():
    ''' launches app if st.secrets dict is ok
    '''
    if (secrets_check()):
        app()
    else:
        secrets_manage()


# app entry point
if __name__ == "__main__":
    main()
