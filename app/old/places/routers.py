from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.infrastructure.database import get_session
from app.places.schemas import (
    OrganizationCreate, Organization,
    PlaceCreate, Place,
    GoogleReviewsCreate, GoogleReviews,
    YandexReviewsCreate, YandexReviews,
    CategoryCreate, Category,
    LabelCreate, Label,
    ImageCreate, Image,
    VideoCreate, Video,
    ServiceCreate, Service,
    MenuItemCreate, MenuItem,
    MenuCategoryCreate, MenuCategory,
    PlaceHoursCreate, PlaceHours
)
from app.places.crud import (
    create_organization, get_organization, get_organizations,
    update_organization, delete_organization,
    create_place, get_place, get_places,
    update_place, delete_place,
    create_google_review, get_google_review, get_google_reviews,
    update_google_review, delete_google_review,
    create_yandex_review, get_yandex_review, get_yandex_reviews,
    update_yandex_review, delete_yandex_review,
    create_category, get_category, get_categories,
    update_category, delete_category,
    create_label, get_label, get_labels,
    update_label, delete_label,
    create_image, get_image, get_images,
    update_image, delete_image,
    create_video, get_video, get_videos,
    update_video, delete_video,
    create_service, get_service, get_services,
    update_service, delete_service,
    create_menu_item, get_menu_item, get_menu_items,
    update_menu_item, delete_menu_item,
    create_menu_category, get_menu_category, get_menu_categories,
    update_menu_category, delete_menu_category,
    create_place_hours, get_place_hours, get_place_hours_list,
    update_place_hours, delete_place_hours
)

router = APIRouter()


# Маршруты для Label
@router.post("/labels/", response_model=Label)
async def create_label_endpoint(
    label: LabelCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_label(db, label)

@router.get("/labels/{label_id}", response_model=Label)
async def read_label(
    label_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_label = await get_label(db, label_id)
    if db_label is None:
        raise HTTPException(status_code=404, detail="Label not found")
    return db_label

@router.get("/labels/", response_model=List[Label])
async def read_labels(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_labels(db, skip, limit)

@router.put("/labels/{label_id}", response_model=Label)
async def update_label_endpoint(
    label_id: int, label: LabelCreate,
    db: AsyncSession = Depends(get_session)
):
    db_label = await update_label(db, label_id, label)
    if db_label is None:
        raise HTTPException(status_code=404, detail="Label not found")
    return db_label

@router.delete("/labels/{label_id}", response_model=Label)
async def delete_label_endpoint(
    label_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_label = await delete_label(db, label_id)
    if db_label is None:
        raise HTTPException(status_code=404, detail="Label not found")
    return db_label



# Маршруты для Image
@router.post("/images/", response_model=Image)
async def create_image_endpoint(
    image: ImageCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_image(db, image)

@router.get("/images/{image_id}", response_model=Image)
async def read_image(
    image_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_image = await get_image(db, image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

@router.get("/images/", response_model=List[Image])
async def read_images(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_images(db, skip, limit)

@router.put("/images/{image_id}", response_model=Image)
async def update_image_endpoint(
    image_id: int, image: ImageCreate,
    db: AsyncSession = Depends(get_session)
):
    db_image = await update_image(db, image_id, image)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

@router.delete("/images/{image_id}", response_model=Image)
async def delete_image_endpoint(
    image_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_image = await delete_image(db, image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

# Маршруты для Video
@router.post("/videos/", response_model=Video)
async def create_video_endpoint(
    video: VideoCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_video(db, video)

@router.get("/videos/{video_id}", response_model=Video)
async def read_video(
    video_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_video = await get_video(db, video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

@router.get("/videos/", response_model=List[Video])
async def read_videos(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_videos(db, skip, limit)

@router.put("/videos/{video_id}", response_model=Video)
async def update_video_endpoint(
    video_id: int, video: VideoCreate,
    db: AsyncSession = Depends(get_session)
):
    db_video = await update_video(db, video_id, video)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

@router.delete("/videos/{video_id}", response_model=Video)
async def delete_video_endpoint(
    video_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_video = await delete_video(db, video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video



# Маршруты для Service
@router.post("/services/", response_model=Service)
async def create_service_endpoint(
    service: ServiceCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_service(db, service)

@router.get("/services/{service_id}", response_model=Service)
async def read_service(
    service_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_service = await get_service(db, service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service

@router.get("/services/", response_model=List[Service])
async def read_services(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_services(db, skip, limit)

@router.put("/services/{service_id}", response_model=Service)
async def update_service_endpoint(
    service_id: int, service: ServiceCreate,
    db: AsyncSession = Depends(get_session)
):
    db_service = await update_service(db, service_id, service)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service

@router.delete("/services/{service_id}", response_model=Service)
async def delete_service_endpoint(
    service_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_service = await delete_service(db, service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service






# Маршруты для PlaceHours
@router.post("/place_hours/", response_model=PlaceHours)
async def create_place_hours_endpoint(
    place_hours: PlaceHoursCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_place_hours(db, place_hours)

@router.get("/place_hours/{place_hours_id}", response_model=PlaceHours)
async def read_place_hours(
    place_hours_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_place_hours = await get_place_hours(db, place_hours_id)
    if db_place_hours is None:
        raise HTTPException(status_code=404, detail="PlaceHours not found")
    return db_place_hours

@router.get("/place_hours/", response_model=List[PlaceHours])
async def read_place_hours_list(
    business_id: int,
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_place_hours_list(db, business_id, skip, limit)

@router.put("/place_hours/{place_hours_id}", response_model=PlaceHours)
async def update_place_hours_endpoint(
    place_hours_id: int, place_hours: PlaceHoursCreate,
    db: AsyncSession = Depends(get_session)
):
    db_place_hours = await update_place_hours(db, place_hours_id, place_hours)
    if db_place_hours is None:
        raise HTTPException(status_code=404, detail="PlaceHours not found")
    return db_place_hours

@router.delete("/place_hours/{place_hours_id}", response_model=PlaceHours)
async def delete_place_hours_endpoint(
    place_hours_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_place_hours = await delete_place_hours(db, place_hours_id)
    if db_place_hours is None:
        raise HTTPException(status_code=404, detail="PlaceHours not found")
    return db_place_hours