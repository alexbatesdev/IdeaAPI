# Initialization
import datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


# Models


class Idea(BaseModel):
    id: int = None
    title: str
    desc: str
    date_created: datetime.date = Field(default_factory=datetime.date.today)
    updated: datetime.datetime = Field(default_factory=datetime.datetime.now)


class IdeaIn(BaseModel):
    title: str
    desc: str


class IdeaList(BaseModel):
    ideas: dict[int, Idea]


# Data

ideas = {
    # 1: Idea(
    #     id=1, title="Jello Shower", desc="A shower that sprays jello instead of water"
    # ),
    # 2: Idea(id=2, title="Taco Pizza", desc="A pizza that is also a taco"),
}


# Methods


@app.post("/ideas", response_model=IdeaList)
async def add_idea(idea: IdeaIn):
    if len(ideas) == 0:
        ideas[1] = Idea(id=1, title=idea.title, desc=idea.desc)
    elif ideas.get(len(ideas) + 1) is None:
        ideas[len(ideas) + 1] = Idea(
            id=len(ideas) + 1, title=idea.title, desc=idea.desc
        )
    else:
        newNum = ideas[len(ideas) + 1].id + 1
        ideas[newNum] = Idea(id=newNum, title=idea.title, desc=idea.desc)

    return IdeaList(ideas=ideas)


@app.get("/ideas", response_model=IdeaList)
async def get_ideas():
    for idea in ideas.values():
        print(idea)
    return IdeaList(ideas=ideas)


@app.get("/ideas/{idea_id}", response_model=Idea)
async def get_idea(idea_id):
    idea_id = int(idea_id)
    if ideas.get(idea_id) is None:
        for idea in ideas.values():
            if idea.id == int(idea_id):
                return idea
        raise HTTPException(status_code=404, detail="Idea not found")
    elif ideas.get(idea_id).id == idea_id:
        return ideas.get(idea_id)
    else:
        for idea in ideas.values():
            if idea.id == int(idea_id):
                return idea
        raise HTTPException(status_code=404, detail="Idea not found, oops")


@app.patch("/ideas/{idea_id}", response_model=Idea)
async def overwrite_idea(idea_id, idea_in: IdeaIn):
    idea_id = int(idea_id)
    if ideas.get(idea_id) is None:
        for idea in ideas.values():
            if idea.id == int(idea_id):
                return idea
        raise HTTPException(status_code=404, detail="Idea not found")
    else:
        if idea_in.title == "":
            newTitle = ideas.get(idea_id).title
        else:
            newTitle = idea_in.title
        if idea_in.desc == "":
            newDesc = ideas.get(idea_id).desc
        else:
            newDesc = idea_in.desc
        newIdea = Idea(id=idea_id, title=newTitle, desc=newDesc)
        newIdea.date_created = ideas.get(idea_id).date_created
        newIdea.updated = datetime.datetime.now()
        ideas[idea_id] = newIdea
        return newIdea


@app.put("/ideas/{idea_id}", response_model=Idea)
async def update_idea(idea_id, idea_in: IdeaIn):
    idea_id = int(idea_id)
    if ideas.get(idea_id) is None:
        for idea in ideas.values():
            if idea.id == int(idea_id):
                return idea
        raise HTTPException(status_code=404, detail="Idea not found")
    else:
        newIdea = Idea(id=idea_id, title=idea_in.title, desc=idea_in.desc)
        newIdea.date_created = ideas.get(idea_id).date_created
        newIdea.updated = datetime.datetime.now()
        ideas[idea_id] = newIdea
        return newIdea


@app.delete("/ideas/{idea_id}", response_model=IdeaList)
async def delete_idea(idea_id):
    ideas.pop(int(idea_id))
    return IdeaList(ideas=ideas)


def DPrint(prompt, delineator="-------------------"):
    print(delineator)
    print(prompt)
    print(delineator)


# Debug
# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, port=8000, reload=True)
