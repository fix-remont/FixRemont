from fastapi import APIRouter
from typing import List
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import cruds, schemas
from src.database.db import get_db
from src.database.schemas import *

router = APIRouter()


@router.get("/portfolio_posts", response_model=List[PortfolioPostSchema], tags=["GET"])
async def get_portfolio_posts(db: AsyncSession = Depends(get_db)):
    return await cruds.get_portfolio_posts(db)


@router.post("/portfolio_posts", response_model=PortfolioPostSchema, tags=["fixed"])
async def create_portfolio_post(portfolio_post: PortfolioPostSchema, db: AsyncSession = Depends(get_db)):
    return await cruds.create_portfolio_post(portfolio_post, db)


@router.post("/project_types", response_model=ProjectTypeSchema, tags=["fixed"])
async def create_project_type(project_type: ProjectTypeSchema, db: AsyncSession = Depends(get_db)):
    return await cruds.create_project_type(project_type, db)


@router.get("/posts", response_model=List[PostSchema], tags=["GET"])
async def get_posts(db: AsyncSession = Depends(get_db)):
    return await cruds.get_posts(db)


@router.post("/posts", response_model=PostSchema, tags=["fixed"])
async def create_post(post: PostSchema, db: AsyncSession = Depends(get_db)):
    return await cruds.create_post(post, db)


@router.get("/blog_bullets", response_model=List[BlogBulletSchema])
async def get_blog_bullets():
    return []


@router.get("/my_contracts", response_model=List[MyContractsSchema], tags=["GET"])
async def get_my_contracts(db: AsyncSession = Depends(get_db)):
    return await cruds.get_my_contracts(db)


@router.post("/my_contracts", response_model=MyContractsSchema, tags=["fixed"])
async def create_my_contract(my_contract: MyContractsSchema, db: AsyncSession = Depends(get_db)):
    return await cruds.create_my_contract(my_contract, db)


@router.get("/order_infos", response_model=List[OrderInfoSchema], tags=["GET"])
async def get_order_infos(db: AsyncSession = Depends(get_db)):
    return await cruds.get_order_infos(db)


@router.post("/order_infos", response_model=OrderInfoSchema, tags=["fixed"])
async def create_order_info(order_info: OrderInfoSchema, db: AsyncSession = Depends(get_db)):
    return await cruds.create_order_info(order_info, db)


@router.get("/work_states", response_model=List[WorkStateSchema], tags=["GET"])
async def get_work_states(db: AsyncSession = Depends(get_db)):
    return await cruds.get_work_states(db)


@router.post("/work_states", response_model=WorkStateSchema, tags=["fixed"])
async def create_work_state(work_state: WorkStateSchema, db: AsyncSession = Depends(get_db)):
    return await cruds.create_work_state(work_state, db)


@router.get("/work_statuses", response_model=List[WorkStatusSchema], tags=["GET"])
async def get_work_statuses(db: AsyncSession = Depends(get_db)):
    return await cruds.get_work_statuses(db)


@router.get("/estimates", response_model=List[EstimateSchema], tags=["GET"])
async def get_estimates(db: AsyncSession = Depends(get_db)):
    return await cruds.get_estimates(db)


@router.get("/profile_infos", response_model=List[ProfileInfoSchema], tags=["GET"])
async def get_profile_infos(db: AsyncSession = Depends(get_db)):
    return await cruds.get_profile_infos(db)


@router.get("/order_client_infos", response_model=List[OrderClientInfoSchema], tags=["GET"])
async def get_order_client_infos(db: AsyncSession = Depends(get_db)):
    return await cruds.get_order_client_infos(db)


@router.get("/order_notifications", response_model=List[OrderNotificationSchema], tags=["deprecated"])
async def get_order_notifications():
    return []


@router.get("/order_documents", response_model=List[OrderDocumentsSchema], tags=["GET"])
async def get_order_documents(db: AsyncSession = Depends(get_db)):
    return await cruds.get_order_documents(db)


@router.get("/contracts", response_model=List[ContractsSchema], tags=["GET"])
async def get_contracts(db: AsyncSession = Depends(get_db)):
    return await cruds.get_contracts(db)


@router.get("/invited_partners", response_model=List[InvitedPartnersSchema], tags=["GET"])
async def get_invited_partners(db: AsyncSession = Depends(get_db)):
    return await cruds.get_invited_partners(db)


@router.get("/profile_notifications", response_model=List[ProfileNotificationSchema], tags=["GET"])
async def get_profile_notifications(db: AsyncSession = Depends(get_db)):
    return await cruds.get_profile_notifications(db)


@router.post("/profile_notifications", response_model=ProfileNotificationSchema, tags=["fixed"])
async def create_profile_notification(profile_notification: ProfileNotificationSchema,
                                      db: AsyncSession = Depends(get_db)):
    return await cruds.create_profile_notification(profile_notification, db)


@router.get("/support_categories", response_model=List[SupportCategorySchema], tags=["GET"])
async def get_support_categories(db: AsyncSession = Depends(get_db)):
    return await cruds.get_support_categories(db)


@router.post("/support_categories", response_model=SupportCategorySchema, tags=["fixed"])
async def create_support_category(support_category: SupportCategorySchema, db: AsyncSession = Depends(get_db)):
    return await cruds.create_support_category(support_category, db)


@router.get("/portfolio_posts/{id}", response_model=PortfolioPostSchema, tags=["GET"])
async def get_portfolio_post(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_portfolio_post(id, db)


@router.get("/portfolio_posts/{project_type}", response_model=PortfolioPostSchema, tags=["GET"])
async def get_portfolio_post(project_type: str = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_portfolio_post_by_project_type(project_type, db)


@router.get("/posts/{id}", response_model=PostSchema, tags=["GET"])
async def get_post(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_post(id, db)


@router.get("/my_contracts/{id}", response_model=MyContractsSchema, tags=["GET"])
async def get_my_contract(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_my_contract(id, db)


@router.get("/order_infos/{id}", response_model=OrderInfoSchema, tags=["GET"])
async def get_order_info(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_order_info(id, db)


@router.get("/work_states/{id}", response_model=WorkStateSchema, tags=["GET"])
async def get_work_state(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_work_state(id, db)


@router.get("/work_statuses/{id}", response_model=WorkStatusSchema, tags=["GET"])
async def get_work_status(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_work_status(id, db)


@router.get("/estimates/{id}", response_model=EstimateSchema, tags=["GET"])
async def get_estimate(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_estimate(id, db)


@router.get("/profile_infos/{id}", response_model=ProfileInfoSchema, tags=["GET"])
async def get_profile_info(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_profile_info(id, db)


@router.get("/order_client_infos/{id}", response_model=OrderClientInfoSchema, tags=["GET"])
async def get_order_client_info(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_order_client_info(id, db)


@router.get("/order_documents/{id}", response_model=OrderDocumentsSchema, tags=["GET"])
async def get_order_document(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_order_document(id, db)


@router.get("/contracts/{id}", response_model=ContractsSchema, tags=["GET"])
async def get_contract(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return await cruds.get_contract(id, db)


@router.get("/invited_partners/{id}", response_model=InvitedPartnersSchema, tags=["GET"])
async def get_invited_partner(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_invited_partner(id, db)


@router.get("/profile_notifications/{id}", response_model=ProfileNotificationSchema, tags=["GET"])
async def get_profile_notification(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_profile_notification(id, db)


@router.get("/support_categories/{id}", response_model=SupportCategorySchema, tags=["GET"])
async def get_support_category(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_support_category(id, db)


@router.get("/faqs", response_model=List[FAQSchema], tags=["GET"])
async def get_faqs(db: AsyncSession = Depends(get_db)):
    return cruds.get_faqs(db)


@router.get("/faqs/{page_tag}", response_model=List[FAQSchema], tags=["GET"])
async def get_faqs(page_tag: str = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_faqs_by_page_tag(page_tag, db)


@router.get("/faqs/{key_word}", response_model=FAQSchema, tags=["!BUG"])
async def get_faq(key_word: str = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_faqs_by_keyword(key_word, db)


@router.get("/seo_texts", response_model=List[SEOTextSchema], tags=["GET"])
async def get_seo_texts(db: AsyncSession = Depends(get_db)):
    return cruds.get_seo_texts(db)


@router.get("/seo_texts/{page_tag}", response_model=SEOTextSchema, tags=["GET"])
async def get_seo_text(page_tag: str = Path(...), db: AsyncSession = Depends(get_db)):
    return cruds.get_seo_text_by_page_tag(page_tag, db)


@router.get("/project_types", response_model=List[ProjectTypeSchema], tags=["GET"])
async def get_project_types(db: AsyncSession = Depends(get_db)):
    return cruds.get_project_types(db)


@router.get("/tariffs", response_model=List[TariffSchema], tags=["GET"])
async def get_tariffs(db: AsyncSession = Depends(get_db)):
    return cruds.get_tariffs(db)


@router.get("/user_comments", response_model=List[UserCommentsSchema], tags=["GET"])
async def get_user_comments(db: AsyncSession = Depends(get_db)):
    return cruds.get_user_comments(db)


@router.get("/intro_videos", response_model=List[IntroVideosSchema], tags=["GET"])
async def get_intro_videos(db: AsyncSession = Depends(get_db)):
    return cruds.get_intro_videos(db)


@router.get("/social_networks", response_model=List[SocialMediaAccountsSchema], tags=["GET"])
async def get_social_networks(db: AsyncSession = Depends(get_db)):
    return cruds.get_social_media_accounts(db)


@router.get("/blog_videos", response_model=List[BlogVideosSchema], tags=["GET"])
async def get_blog_videos(db: AsyncSession = Depends(get_db)):
    return cruds.get_blog_videos(db)


@router.get("/communications_types", response_model=List[CommunicationTypeSchema], tags=["GET"])
async def get_communication_types(db: AsyncSession = Depends(get_db)):
    return cruds.get_communication_types(db)


@router.post("/consultations", response_model=ConsultationsListSchema, tags=["POST"])
async def create_consultation(consultation: ConsultationsListSchema, db: AsyncSession = Depends(get_db)):
    return cruds.create_consultation(consultation, db)
