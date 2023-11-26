# pylint: skip-file

from fastapi import FastAPI, Request, WebSocket
from qa_flow import create_flow
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()
app.mount("/static", StaticFiles(directory="."), name="static")


@app.get("/")
async def read_index(request: Request):
    with open("index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)


@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"answer": "hi", "eli5_answer": "haha", "sources": None})
    while True:
        data = await websocket.receive_text()
        question = data
        result = await answer_question(question)
        await websocket.send_json(result)


@app.get("/qa/")
async def answer_question(question: str):
    """
    Endpoint to receive a question and return an answer.
    The answer is generated by a predefined flow and includes both a direct answer
    and an 'ELI5' explanation.

    Args:
        question: The question to be answered.

    Returns:
        A dictionary with three keys: 'answer' and 'eli5_answer', containing the
        respective answers, and 'sources' containing titles and links to Wikipedia
        articles.
    """
    rag_flow = create_flow()
    result = rag_flow.start(
        conversation_history="", question=question, verbose=True
    )

    answer = result["Answer Flowstep"]["generated"]
    eli5_answer = result["ELI5 Flowstep"]["generated"]
    vector_store_results = result["Vectorstore Flowstep"]["call_data"]["raw_outputs"]
    sources = [match["metadata"] for match in vector_store_results["matches"]]

    return {"answer": answer, "eli5_answer": eli5_answer, "sources": sources}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
