EXPANDER_MARKDOWN = """
                <style>
                .streamlit-expanderHeader {
                    font-size: medium;
                    font-weight: bold
                }
                </style>
                """

SIDEBAR_MARKDOWN = f"""
                    <style>
                    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {{
                        width: 280px;
                        padding-top: 0px;
                        padding-bottom: 0px;
                        padding-right: 0px;
                        padding-left: 0px;
                       
                    }}
                    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {{
                        width: 0px;
                    }}
                    </style>
                    """

HORIZONTAL_LINE_MARDOWN = """<hr>"""


PAGE_MARKDOWN = """<style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>"""


BUTTON_MARKDOWN = """<style>
                        div.stButton > button:first-child {
                            background-color: #e01616;
                            color:#FFFFFF;
                        }div.stButton > button:hover {
                            background-color: #ffffff;
                            color:#000000;
                        }</style>"""

FONT_FAMILY = 'Verdana'