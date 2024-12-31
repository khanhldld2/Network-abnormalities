import streamlit
import pandas
import streamlit.web.cli as stcli
import os, sys

def resolve_path(path):
    resolve_path = os.path.abspath(os.path.join(os.getcwd(),path))
    return resolve_path

if __name__== "__main__":
    sys.argv=[
        "streamlit",
        "run",
        resolve_path("demo_web.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())