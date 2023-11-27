# 🤖 llmflows-ws-template

Live Demo: https://llmflows-ws-template-96085e33adde.herokuapp.com

## Introduction
This is a template repository for building RAG chat apps with llmflows.

The app is built with FastAPI and uses websockets to communicate with the frontend.
The frontend uses HTML, CSS and JavaScript and Bootstrap for styling.
The app uses the qa_flow.py file to create a flow that can be used to answer questions.
The flow is created in the answer_question function and the answer_question function
is used as an endpoint to receive questions and return answers.

## Prerequisites

The app requires a Pinecone index to be created and populated.
To create a Pinecone index, follow the instructions in LLMFlows official [user guide](https://llmflows.readthedocs.io/en/latest/user_guide/Vector%20Stores/)

## Running locally
To run the app locally make sure to create a virtual environment and install the 
requirements.txt file.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start the app by running the following command in the terminal:
```
uvicorn app:app --reload
```

## Deploying to Heroku
To deploy the app to Heroku, you will have to create a Heroku account, fork this
repository and connect it to your Heroku account. Make sure you include the following 
envuronment variables in your Heroku app:

```
PINECONE_API_KEY: <your pinecone api key>
OPENAI_API_KEY: <your openai api key>
```

## 📃 License
This repository is covered by the MIT license. For more information, check [`LICENCE`](https://github.com/stoyan-stoyanov/llmflows-ws-template/blob/main/LICENSE).