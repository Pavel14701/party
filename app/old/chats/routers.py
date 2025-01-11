from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.infrastructure.database import get_session
from app.chats.schemas import (
    ChatCreate, ChatRead,
    GroupCreate, GroupRead,
    MessageCreate, MessageReadFull,
    HistoryCreate, HistoryReadFull,
    ImageCreate, ImageReadFull
)
from app.chats.crud import (
    create_chat, get_chat, get_chats, update_chat, delete_chat,
    create_group, get_group, get_groups, update_group, delete_group,
    create_message, get_message, get_messages, update_message, delete_message,
    create_history, get_history, get_histories, update_history, delete_history,
    create_image, get_image, get_images, update_image, delete_image
)

router = APIRouter()

# Маршруты для Chat
@router.post("/chats/", response_model=ChatRead)
async def create_chat_endpoint(
    chat: ChatCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_chat(db, chat)

@router.get("/chats/{chat_id}", response_model=ChatRead)
async def read_chat(
    chat_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_chat = await get_chat(db, chat_id)
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return db_chat

@router.get("/chats/", response_model=List[ChatRead])
async def read_chats(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_chats(db, skip, limit)

@router.put("/chats/{chat_id}", response_model=ChatRead)
async def update_chat_endpoint(
    chat_id: int, chat: ChatCreate,
    db: AsyncSession = Depends(get_session)
):
    db_chat = await update_chat(db, chat_id, chat)
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return db_chat

@router.delete("/chats/{chat_id}", response_model=ChatRead)
async def delete_chat_endpoint(
    chat_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_chat = await delete_chat(db, chat_id)
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return db_chat




# Маршруты для Group
@router.post("/groups/", response_model=GroupRead)
async def create_group_endpoint(
    group: GroupCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_group(db, group)

@router.get("/groups/{group_id}", response_model=GroupRead)
async def read_group(
    group_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_group = await get_group(db, group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

@router.get("/groups/", response_model=List[GroupRead])
async def read_groups(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_groups(db, skip, limit)

@router.put("/groups/{group_id}", response_model=GroupRead)
async def update_group_endpoint(
    group_id: int, group: GroupCreate,
    db: AsyncSession = Depends(get_session)
):
    db_group = await update_group(db, group_id, group)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

@router.delete("/groups/{group_id}", response_model=GroupRead)
async def delete_group_endpoint(
    group_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_group = await delete_group(db, group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group




# Маршруты для Message
@router.post("/messages/", response_model=MessageReadFull)
async def create_message_endpoint(
    message: MessageCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_message(db, message)

@router.get("/messages/{message_id}", response_model=MessageReadFull)
async def read_message(
    message_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_message = await get_message(db, message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message

@router.get("/messages/", response_model=List[MessageReadFull])
async def read_messages(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_messages(db, skip, limit)

@router.put("/messages/{message_id}", response_model=MessageReadFull)
async def update_message_endpoint(
    message_id: int, message: MessageCreate,
    db: AsyncSession = Depends(get_session)
):
    db_message = await update_message(db, message_id, message)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message

@router.delete("/messages/{message_id}", response_model=MessageReadFull)
async def delete_message_endpoint(
    message_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_message = await delete_message(db, message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message




# Маршруты для History
@router.post("/histories/", response_model=HistoryReadFull)
async def create_history_endpoint(
    history: HistoryCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_history(db, history)

@router.get("/histories/{history_id}", response_model=HistoryReadFull)
async def read_history(
    history_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_history = await get_history(db, history_id)
    if db_history is None:
        raise HTTPException(status_code=404, detail="History not found")
    return db_history

@router.get("/histories/", response_model=List[HistoryReadFull])
async def read_histories(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_histories(db, skip, limit)

@router.put("/histories/{history_id}", response_model=HistoryReadFull)
async def update_history_endpoint(
    history_id: int, history: HistoryCreate,
    db: AsyncSession = Depends(get_session)
):
    db_history = await update_history(db, history_id, history)
    if db_history is None:
        raise HTTPException(status_code=404, detail="History not found")
    return db_history

@router.delete("/histories/{history_id}", response_model=HistoryReadFull)
async def delete_history_endpoint(
    history_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_history = await delete_history(db, history_id)
    if db_history is None:
        raise HTTPException(status_code=404, detail="History not found")
    return db_history




# Маршруты для Image
@router.post("/images/", response_model=ImageReadFull)
async def create_image_endpoint(
    image: ImageCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_image(db, image)

@router.get("/images/{image_id}", response_model=ImageReadFull)
async def read_image(
    image_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_image = await get_image(db, image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

@router.get("/images/", response_model=List[ImageReadFull])
async def read_images(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_images(db, skip, limit)

@router.put("/images/{image_id}", response_model=ImageReadFull)
async def update_image_endpoint(
    image_id: int, image: ImageCreate,
    db: AsyncSession = Depends(get_session)
):
    db_image = await update_image(db, image_id, image)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

@router.delete("/images/{image_id}", response_model=ImageReadFull)
async def delete_image_endpoint(
    image_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_image = await delete_image(db, image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image
