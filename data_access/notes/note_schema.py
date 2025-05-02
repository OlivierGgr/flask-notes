from pydantic import BaseModel, ConfigDict

class NoteUpdate(BaseModel):
    model_config = ConfigDict(extra='forbid') 

    content: str | None = None
    is_done: bool | None = None