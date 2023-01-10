# Initialization
import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Models


class Idea(BaseModel):
    id: int = None
    title: str
    desc: str
    date_created: datetime.date = datetime.date.today()
    updated: datetime.datetime = datetime.datetime.now()
    __fields_set__ = {"id", "title", "desc", "date_created", "updated"}

    def __init__(self, id, title, desc):
        self.id = id
        self.title = title
        self.desc = desc
        self.date_created = datetime.date.today()
        self.updated = datetime.datetime.now()


class IdeaIn(BaseModel):
    title: str
    desc: str


# Data

ideas = {
    # 1: Idea(1, "Jello Shower", "A shower that sprays jello instead of water"),
    # 2: Idea(2, "Taco Pizza", "A pizza that is also a taco"),
}


# Methods


@app.post("/ideas")
async def add_idea(idea: IdeaIn):
    ideas[len(ideas) + 1] = Idea(len(ideas) + 1, idea.title, idea.desc)
    return ideas


@app.get("/ideas")
async def get_ideas():
    for idea in ideas.values():
        print(idea)
    return ideas


@app.get("/ideas/{idea_id}")
async def get_idea(idea_id):
    idea_id = int(idea_id)
    if ideas.get(idea_id) is None:
        for idea in ideas.values():
            if idea.id == int(idea_id):
                return idea
        return "Idea not found"
    elif ideas.get(idea_id).id == idea_id:
        return ideas.get(idea_id)
    else:
        for idea in ideas.values():
            if idea.id == int(idea_id):
                return idea
        return "Idea not found, but in a weird way."


@app.patch("/ideas/{idea_id}")
async def overwrite_idea(idea_id, idea_in: IdeaIn):
    idea_id = int(idea_id)
    if ideas.get(idea_id) is None:
        for idea in ideas.values():
            if idea.id == int(idea_id):
                return idea
        return "Idea not found"
    else:
        if idea_in.title == "":
            newTitle = ideas.get(idea_id).title
        else:
            newTitle = idea_in.title
        if idea_in.desc == "":
            newDesc = ideas.get(idea_id).desc
        else:
            newDesc = idea_in.desc
        newIdea = Idea(idea_id, newTitle, newDesc)
        newIdea.date_created = ideas.get(idea_id).date_created
        newIdea.updated = datetime.datetime.now()
        ideas[idea_id] = newIdea
        return newIdea


@app.put("/ideas/{idea_id}")
async def update_idea(idea_id, idea_in: IdeaIn):
    idea_id = int(idea_id)
    if ideas.get(idea_id) is None:
        for idea in ideas.values():
            if idea.id == int(idea_id):
                return idea
        return "Idea not found"
    else:
        newIdea = Idea(idea_id, idea_in.title, idea_in.desc)
        newIdea.date_created = ideas.get(idea_id).date_created
        newIdea.updated = datetime.datetime.now()
        ideas[idea_id] = newIdea
        return newIdea


# REWORK THIS AND ALL FOLLOWING METHODS TO WORK WITH PYDANTIC OBJECTS
@app.delete("/ideas/{idea_id}")
async def delete_idea(idea_id):
    ideas.pop(int(idea_id))
    return ideas


def DPrint(prompt, delineator="-------------------"):
    print(delineator)
    print(prompt)
    print(delineator)
