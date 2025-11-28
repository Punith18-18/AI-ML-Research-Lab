from fastapi import APIRouter
from pydantic import BaseModel
from .logic import deterministic_completion

router = APIRouter()

class CompletionRequest(BaseModel):
    prompt: str
    max_tokens: int = 32
    persona: str = "ghost"

class CompletionResponse(BaseModel):
    prompt: str
    completion: str

@router.post("/complete", response_model=CompletionResponse)
async def complete(req: CompletionRequest):
    """Return a deterministic completion for the given prompt.

    This is a placeholder for the real AI component. It demonstrates
    how a real model would be wrapped and tested.
    """
    completion = deterministic_completion(req.prompt, req.max_tokens)
    # apply persona transformation (ghost storyteller by default)
    try:
        from .logic import apply_persona
    except Exception:
        apply_persona = lambda c, p: c

    transformed = apply_persona(completion, req.persona)
    return CompletionResponse(prompt=req.prompt, completion=transformed)
