import json
import requests

from dotenv import load_dotenv
import os

# load in packages
load_dotenv()

headers = {"Authorization": f"Bearer {os.getenv('HF_READ_API_TOKEN')}"}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

input_text = """\
Mary Elizabeth Truss[8] was born on 26 July 1975 in Oxford, England,\
to John Truss and Priscilla Truss (née Grasby).[9][10][11] She is a\
descendant of Charles Truss, after whom Truss's Island on the River\
Thames is named. From an early age, she has been known by her middle name.\
Her father is an emeritus professor of pure mathematics at the University of Leeds,\
while her mother was a nurse and teacher.[15][16] Truss has described her parents\ 
as being "to the left of Labour"; her mother was a member of the Campaign for\
Nuclear Disarmament.[16][17] Truss's parents divorced in 2003; at the 2004 Leeds City\
Council election, her mother unsuccessfully stood for election as a Liberal Democrat.\
"""

data = query(
    {
        "inputs": input_text,
        "parameters": {"do_sample": False},
    }
)


# Response
# self.assertEqual(
#     data,
#     [
#         {
#             "summary_text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world.",
#         },
#     ],
# )


