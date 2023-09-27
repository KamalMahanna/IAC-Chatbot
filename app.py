import streamlit as st

import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
'''
<iframe
    allow="microphone;"
    width="350"
    height="430"
    src="https://console.dialogflow.com/api-client/demo/embedded/11f19702-2d03-4372-9bce-01de319f02e7">
</iframe>
''',
height=800,
width=600
)