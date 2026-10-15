from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.models import Idea, IdeaRequest
from app.store import IdeaStore

def create_app() -> FastAPI:
    app = FastAPI(title="Campus Idea Board")
    store = IdeaStore()

    @app.exception_handler(RequestValidationError)
    async def invalid_request(request: Request, error: RequestValidationError):
        return JSONResponse(status_code=400, content={"message": "Invalid request"})

    @app.get("/api/hello")
    def hello():
        return {"message": "Hello from the Campus Idea Board! - Joseph"}

    @app.get("/api/ideas")
    def get_ideas() -> list[Idea]:
        return store.find_all()

    @app.post("/api/ideas", status_code=201)
    def create_idea(request: IdeaRequest) -> Idea:
        return store.add(request)

    return app

app = create_app()
