from fastapi import HTTPException
from psycopg2 import paramstyle
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.auth.auth_routes import get_password_hash
from src.database import models
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import models, schemas
from src.database.models import PostType, TariffType, OrderType
from collections import defaultdict
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import models, schemas
import os


async def get_portfolio_posts(db: AsyncSession):
    result = db.execute(select(models.Work))
    all_works = result.scalars().all()

    portfolio_posts = []

    for work in all_works:
        articles = [
            schemas.ArticleSchema(title=art.split(": ")[0], body=art.split(": ")[1]) if isinstance(art, str) else art
            for art in work.description]
        portfolio_posts.append({
            "id": work.id,
            "title": work.title,
            "deadline": work.deadline,
            "cost": work.cost,
            "square": work.square,
            "task": work.task,
            "description": work.description,
            "project_type": work.project_type,
            "preview_image": work.preview_image,
            "main_image": work.main_image,
            "result_image": work.result_image,
            "articles": articles,
            "result_video": work.result_video,
            "client_video": work.client_video
        })

    return portfolio_posts


def get_portfolio_post(id, db):
    result = db.execute(select(models.Work).where(models.Work.id == id))
    work = result.scalars().first()

    if work is None:
        raise HTTPException(status_code=404, detail="Work not found")
    articles = [
        schemas.ArticleSchema(title=art.split(": ")[0], body=art.split(": ")[1]) if isinstance(art, str) else art
        for art in work.description]
    work_response = {
        "id": work.id,
        "title": work.title,
        "deadline": work.deadline,
        "cost": work.cost,
        "square": work.square,
        "task": work.task,
        "description": work.description,
        "project_type": work.project_type,
        "preview_image": work.preview_image,
        "main_image": work.main_image,
        "result_image": work.result_image,
        "articles": articles,
        "result_video": work.result_video,
        "client_video": work.client_video
    }

    return work_response


async def create_portfolio_post(portfolio_post: schemas.PortfolioPostSchema, db: AsyncSession):
    result = db.execute(select(models.ProjectType).filter_by(name=portfolio_post.project_type.name))
    project_type_instance = result.scalars().first()
    articles = [f"{article.title}: {article.body}" for article in
                portfolio_post.description] if portfolio_post.description else []

    new_portfolio_post = models.Work(
        title=portfolio_post.title,
        deadline=portfolio_post.deadline,
        cost=portfolio_post.cost,
        square=portfolio_post.square,
        task=portfolio_post.task,
        preview_image=portfolio_post.preview_image,
        main_image=portfolio_post.main_image,
        result_image=portfolio_post.result_image,
        project_type_id=project_type_instance.id,
        description=articles,
        result_video=portfolio_post.result_video,
        client_video=portfolio_post.client_video
    )
    db.add(new_portfolio_post)
    db.commit()
    db.refresh(new_portfolio_post)

    return schemas.PortfolioPostSchema.from_orm(new_portfolio_post)


async def create_project_type(project_type: schemas.ProjectTypeSchema, db: AsyncSession):
    new_project_type = models.ProjectType(name=project_type.name)
    db.add(new_project_type)
    db.commit()
    db.refresh(new_project_type)
    return schemas.ProjectTypeSchema.from_orm(new_project_type)


async def get_posts(db: AsyncSession):
    result = db.execute(select(models.Post))
    all_posts = result.scalars().all()

    posts = []

    for post in all_posts:
        articles = [
            schemas.ArticleSchema(title=art.split(": ")[0], body=art.split(": ")[1]) if isinstance(art, str) else art
            for art in post.paragraphs]
        posts.append({
            "id": post.id,
            "title": post.title,
            "post_type": post.post_type,
            "images": post.images,
            "articles": articles
        })

    return posts


async def create_post(post: schemas.PostSchema, db: AsyncSession):
    # Convert the post_type string to a PostType enum instance
    post_type_enum = PostType(post.post_type)

    # Create Article instances from the articles list
    articles_instances = [models.Paragraph(title=article.title, body=article.body) for article in post.articles if
                          article is not None] if post.articles else []

    new_post = models.Post(
        title=post.title,
        post_type=post_type_enum,  # Use the PostType enum instance here
        images=post.images,
        paragraphs=articles_instances  # Assign the list of Article instances to paragraphs
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return schemas.PostSchema.from_orm(new_post)


# async def get_blog_bullets(db: AsyncSession):
#     result = db.execute(select(models.Post))
#     all_posts = result.scalars().all()
#
#     posts = []
#
#     for post in all_posts:
#         articles = [
#             schemas.ArticleSchema(title=art.split(": ")[0], body=art.split(": ")[1]) if isinstance(art, str) else art
#             for art in post.paragraphs]
#         posts.append({
#             "id": post.id,
#             "title": post.title,
#             "post_type": post.post_type,
#             "images": [post.image1, post.image2, post.image3],
#             "articles": articles
#         })
#
#     return posts


async def get_my_contracts(db: AsyncSession):
    result = db.execute(select(models.Contract))
    all_contracts = result.scalars().all()

    my_contracts = []

    for contract in all_contracts:
        my_contracts.append({
            "id": contract.id,
            "object": contract.object,
            "tariff": contract.tariff_type,
            "location": contract.location,
            "reward": contract.revenue,
            "status": contract.current_stage
        })

    return my_contracts


async def create_my_contract(my_contract: schemas.MyContractsSchema, db: AsyncSession):
    contract_type_enum = TariffType(my_contract.tariff)
    new_my_contract = models.Contract(
        object=my_contract.object,
        tariff_type=contract_type_enum,
        location=my_contract.location,
        revenue=my_contract.reward,
        current_stage=my_contract.status
    )

    db.add(new_my_contract)
    db.commit()
    db.refresh(new_my_contract)

    return schemas.MyContractsSchema.from_orm(new_my_contract)


async def get_order_infos(db: AsyncSession):
    result = db.execute(select(models.Contract))
    all_order_infos = result.scalars().all()

    order_infos = []

    for order_info in all_order_infos:
        order_infos.append({
            "id": order_info.id,
            "type": order_info.order_type,
            "tarrif": order_info.tariff_type,
            "area": order_info.square,
            "location": order_info.location
        })

    return order_infos


async def create_order_info(order_info: schemas.OrderInfoSchema, db: AsyncSession):
    order_type_enum = OrderType(order_info.type)
    tariff_type_enum = TariffType(order_info.tariff)
    new_order_info = models.Contract(
        object=order_info.object,
        order_type=order_type_enum,
        tariff_type=tariff_type_enum,
        square=order_info.area,
        location=order_info.location
    )

    db.add(new_order_info)
    db.commit()
    db.refresh(new_order_info)

    return schemas.OrderInfoSchema.from_orm(new_order_info)


async def get_work_states(db: AsyncSession):
    result = db.execute(select(models.WorkStatus))
    all_work_states = result.scalars().all()

    work_states = []

    for work_state in all_work_states:
        work_states.append({
            "id": work_state.id,
            "title": work_state.title,
            "status": work_state.status,
            "document": work_state.document
        })

    return work_states


async def create_work_state(work_state: schemas.WorkStateSchema, db: AsyncSession):
    new_work_state = models.WorkStatus(
        title=work_state.title,
        status=work_state.status,
        document=work_state.document
    )

    db.add(new_work_state)
    db.commit()
    db.refresh(new_work_state)

    return schemas.WorkStateSchema.from_orm(new_work_state)


async def get_work_statuses(db: AsyncSession):
    result = db.execute(select(models.WorkStatus))
    all_work_statuses = result.scalars().all()

    work_statuses = []

    for work_status in all_work_statuses:
        work_statuses.append({
            "id": work_status.id,
            "title": work_status.title,
            "status": work_status.status,
            "document": work_status.document,
            "contract_id": work_status.contract_id
        })

    return work_statuses


async def get_estimates(db: AsyncSession):
    result = db.execute(select(models.Contract))
    all_contracts = result.scalars().all()

    estimates = []

    for contract in all_contracts:
        estimates.append({
            "id": contract.id,
            "total": contract.total_cost if contract.total_cost else 0,
            "materials": contract.materials_cost if contract.materials_cost else 0,
            "job": contract.work_cost if contract.work_cost else 0,
            "reward": contract.revenue if contract.revenue else 0,
            "document": contract.document
        })

    return estimates


async def get_profile_infos(db: AsyncSession):
    result = db.execute(select(models.User))
    all_users = result.scalars().all()

    profile_infos = []

    for user in all_users:
        profile_infos.append({
            "id": user.id,
            "name": user.name,
            "surname": user.surname,
            "patronymic": user.patronymic,
            "phone": user.phone,
            "email": user.email,
            "role": user.user_type,
            "avatar": user.avatar,
            "passport_status": user.is_verified
        })

    return profile_infos


async def get_order_client_infos(db: AsyncSession):
    result = db.execute(select(models.User))
    all_users = result.scalars().all()

    clients_by_user_id = defaultdict(list)

    for user in all_users:
        clients_by_user_id[user.id].append({
            "id": user.id,
            "name": user.name,
            "surname": user.surname,
            "patronymic": user.patronymic,
            "phone": user.phone,
            "email": user.email,
            "role": user.user_type,
            "avatar": user.avatar,
            "passport_status": user.is_verified
        })

    # Convert defaultdict to a list of dictionaries
    clients_by_user_id_list = [{"id": i, "user_id": user_id, "client": clients[0], "date": "TEST DATE"}
                               for i, (user_id, clients) in enumerate(clients_by_user_id.items())]

    return clients_by_user_id_list


async def get_order_documents(db: AsyncSession):
    result = db.execute(select(models.Contract))
    all_contracts = result.scalars().all()

    order_documents = []

    for contract in all_contracts:
        order_documents.append({
            "id": contract.id,
            "title": contract.object,
            "label": contract.current_stage,
            "type": {"name": contract.order_type if contract.order_type else "No type"},  # handle None case
            "attachment": contract.document if contract.document else "No attachment",
            # replace with actual logic to get attachment
            "document": contract.document
        })

    return order_documents


async def get_contracts(db: AsyncSession):
    result = db.execute(select(models.Contract))
    all_contracts = result.scalars().all()

    work_statuses = await get_work_statuses(db)

    contracts = []

    for contract in all_contracts:
        contract_statuses = [
            {
                "id": state["id"],
                "title": state["title"],
                "status": state["status"],
                "document": state["document"],
                "current": state["current"] if "current" in state else False  # Add current field
            }
            for state in work_statuses if state["contract_id"] == contract.id
        ]

        contracts.append({
            "order": {
                "id": contract.id,
                "object": contract.object,
                "type": contract.order_type,
                "tariff": contract.tariff_type,
                "area": contract.square,
                "location": contract.location
            },
            "status": {
                "id": contract.id,
                "states": contract_statuses
            },
            "stage": contract.work_statuses[0].title if contract.work_statuses else "No stage",
            "reward": contract.revenue,
            "user_id": contract.client_id
        })

    return contracts


async def get_invited_partners(db: AsyncSession):
    result = db.execute(select(models.User))
    all_users = result.scalars().all()

    invited_partners = []

    for user in all_users:
        invited_partners.append({
            "id": user.id,
            "data": {
                "id": user.id,
                "name": user.name,
                "surname": user.surname,
                "patronymic": user.patronymic,
                "phone": user.phone,
                "email": user.email,
                "role": user.user_type,
                "avatar": user.avatar,
                "passport_status": user.is_verified
            },
            "reward": -10000
        })

    return invited_partners


async def get_profile_notifications(db: AsyncSession):
    result = db.execute(select(models.Notification))
    all_notifications = result.scalars().all()

    profile_notifications = []

    for notification in all_notifications:
        profile_notifications.append({
            "id": notification.id,
            "title": notification.title,
            "date": notification.date,
            "label": notification.label
        })

    return profile_notifications


async def create_profile_notification(profile_notification: schemas.ProfileNotificationSchema, db: AsyncSession):
    new_profile_notification = models.Notification(
        title=profile_notification.title,
        date=profile_notification.date,
        label=profile_notification.label,
    )

    db.add(new_profile_notification)
    db.commit()
    db.refresh(new_profile_notification)

    return schemas.ProfileNotificationSchema.from_orm(new_profile_notification)


async def get_support_categories(db: AsyncSession):
    result = db.execute(select(models.FAQ))
    all_faqs = result.scalars().all()

    support_categories = []

    for faq in all_faqs:
        support_categories.append({
            "heading": faq.heading,
            "date": faq.date,
            "key_word": faq.key_word,
        })

    return support_categories


async def create_support_category(support_category: schemas.SupportCategorySchema, db: AsyncSession):
    new_support_category = models.FAQ(
        heading=support_category.heading,
        date=support_category.date,
        key_word=support_category.key_word
    )

    db.add(new_support_category)
    db.commit()
    db.refresh(new_support_category)

    return schemas.SupportCategorySchema.from_orm(new_support_category)


def get_post(id, db):
    result = db.execute(select(models.Post).where(models.Post.id == id))
    post = result.scalars().first()

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    post_response = {
        "id": post.id,
        "title": post.title,
        "post_type": post.post_type,
        "images": [post.image1, post.image2, post.image3],
        "articles": [
            schemas.ArticleSchema(title=art.title, body=art.body)
            for art in post.paragraphs]
    }

    return post_response


def get_my_contract(id, db):
    result = db.execute(select(models.Contract).where(models.Contract.id == id))
    contract = result.scalars().first()

    if contract is None:
        raise HTTPException(status_code=404, detail="Contract not found")

    contract_response = {
        "id": contract.id,
        "object": contract.object,
        "tariff": contract.tariff_type,
        "location": contract.location,
        "reward": contract.revenue,
        "status": contract.current_stage
    }

    return contract_response


def get_order_info(id, db):
    result = db.execute(select(models.Contract).where(models.Contract.id == id))
    order_info = result.scalars().first()

    if order_info is None:
        raise HTTPException(status_code=404, detail="Order info not found")

    order_info_response = {
        "id": order_info.id,
        "type": order_info.order_type,
        "tarrif": order_info.tariff_type,
        "area": order_info.square,
        "location": order_info.location
    }

    return order_info_response


def get_work_state(id, db):
    result = db.execute(select(models.WorkStatus).where(models.WorkStatus.id == id))
    work_state = result.scalars().first()

    if work_state is None:
        raise HTTPException(status_code=404, detail="Work state not found")

    work_state_response = {
        "id": work_state.id,
        "title": work_state.title,
        "status": work_state.status,
        "document": work_state.document
    }

    return work_state_response


def get_work_status(id, db):
    result = db.execute(select(models.Contract).where(models.Contract.id == id))
    work_status = result.scalars().first()

    if work_status is None:
        raise HTTPException(status_code=404, detail="Work status not found")

    work_status_response = {
        "id": work_status.id,
        "title": work_status.current_stage,
        "document": work_status.document,
        "name": work_status.current_stage
    }

    return work_status_response


def create_work_status(work_status, db):
    new_work_status = models.WorkStatus(
        title=work_status.title,
        status=work_status.status,
        document=work_status.document
    )

    db.add(new_work_status)
    db.commit()
    db.refresh(new_work_status)

    return new_work_status


def get_estimate(id, db):
    result = db.execute(select(models.Contract).where(models.Contract.id == id))
    estimate = result.scalars().first()

    if estimate is None:
        raise HTTPException(status_code=404, detail="Estimate not found")

    estimate_response = {
        "id": estimate.id,
        "total": estimate.total_cost if estimate.total_cost else 0,
        "materials": estimate.materials_cost if estimate.materials_cost else 0,
        "job": estimate.work_cost if estimate.work_cost else 0,
        "reward": estimate.revenue if estimate.revenue else 0,
        "document": estimate.document
    }

    return estimate_response


def get_profile_info(id, db):
    result = db.execute(select(models.User).where(models.User.id == id))
    user = result.scalars().first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    profile_info_response = {
        "id": user.id,
        "name": user.name,
        "surname": user.surname,
        "patronymic": user.patronymic,
        "phone": user.phone,
        "email": user.email,
        "role": user.user_type,
        "avatar": user.avatar,
        "passport_status": user.is_verified
    }

    return profile_info_response


def get_order_client_info(id, db):
    result = db.execute(select(models.User).where(models.User.id == id))
    user = result.scalars().first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    order_client_info_response = {
        "id": user.id,
        "client": {
            "id": user.id,
            "name": user.name,
            "surname": user.surname,
            "patronymic": user.patronymic,
            "phone": user.phone,
            "email": user.email,
            "role": user.user_type,
            "avatar": user.avatar,
            "passport_status": user.is_verified
        },
        "date": "TEST DATE"
    }

    return order_client_info_response


def get_order_document(id, db):
    result = db.execute(select(models.Contract).where(models.Contract.id == id))
    contract = result.scalars().first()

    if contract is None:
        raise HTTPException(status_code=404, detail="Contract not found")

    order_document_response = {
        "id": contract.id,
        "title": contract.object,
        "label": contract.current_stage,
        "type": {"name": contract.order_type if contract.order_type else "No type"},  # handle None case
        "attachment": contract.document if contract.document else "No attachment",
        "document": contract.document
    }

    return order_document_response


def create_notification(notification, db):
    new_notification = models.Notification(
        notification_status=notification.notification_status,
        title=notification.title,
        date=notification.date,
        label=notification.label,
        attachment=notification.attachment if notification.attachment else "",
    )

    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)

    return new_notification


async def get_contract(id: int, db: AsyncSession):
    result = db.execute(select(models.Contract).where(models.Contract.id == id))
    contract = result.scalars().first()

    if contract is None:
        raise HTTPException(status_code=404, detail="Contract not found")

    work_statuses = await get_work_statuses(db)

    contract_statuses = [
        {
            "id": state["id"],
            "title": state["title"],
            "status": state["status"],
            "document": state["document"],
            "current": state["current"] if "current" in state else False
        }
        for state in work_statuses if state["contract_id"] == contract.id
    ]

    contract_response = {
        "order": {
            "id": contract.id,
            "object": contract.object,
            "type": contract.order_type,
            "tariff": contract.tariff_type,
            "area": contract.square,
            "location": contract.location
        },
        "status": {
            "id": contract.id,
            "states": contract_statuses
        },
        "stage": contract.work_statuses[0].title if contract.work_statuses else "No stage",
        "reward": contract.revenue,
        "user_id": contract.client_id
    }

    return contract_response


def get_invited_partner(id, db):
    result = db.execute(select(models.User).where(models.User.id == id))
    user = result.scalars().first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    invited_partner_response = {
        "id": user.id,
        "data": {
            "id": user.id,
            "name": user.name,
            "surname": user.surname,
            "patronymic": user.patronymic,
            "phone": user.phone,
            "email": user.email,
            "role": user.user_type,
            "avatar": user.avatar,
            "passport_status": user.is_verified
        },
        "reward": -10000
    }

    return invited_partner_response


def get_profile_notification(id, db):
    result = db.execute(select(models.Notification).where(models.Notification.id == id))
    notification = result.scalars().first()

    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")

    profile_notification_response = {
        "id": notification.id,
        "title": notification.title,
        "date": notification.date,
        "label": notification.label
    }

    return profile_notification_response


def get_support_category(id, db):
    result = db.execute(select(models.FAQ).where(models.FAQ.id == id))
    faq = result.scalars().first()

    if faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")

    support_category_response = {
        "heading": faq.heading,
        "date": faq.date,
        "key_word": faq.key_word
    }

    return support_category_response


def get_user_by_email(db, email):
    result = db.execute(select(models.User).where(models.User.email == email))
    user = result.scalars().first()
    return user


def get_project_type_by_id(db, id):
    result = db.execute(select(models.ProjectType).where(models.ProjectType.id == id))
    project_type = result.scalars().first()
    return project_type


def create_user(db, user):
    print("Entering create_user function")
    db_user = models.User(
        email=user.email,
        hashed_password=get_password_hash(user.hashed_password),
    )
    print("User object created")
    print(db_user.hashed_password, "<----")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print("User added to the database and committed")
    return db_user


def get_faqs(db):
    result = db.execute(select(models.FAQ))
    all_faqs = result.scalars().all()

    faqs = []

    for faq in all_faqs:
        faqs.append({
            "title": faq.heading,
            "label": faq.label,
            "date": faq.date,
            "key_word": faq.key_word,
            "page_tag": faq.page_tag
        })

    return faqs


def get_faqs_by_keyword(db: AsyncSession, keyword: str):
    result = db.execute(select(models.FAQ).where(models.FAQ.key_word == keyword))
    faqs = result.scalars().all()

    faqs_response = []

    for faq in faqs:
        faqs_response.append({
            "title": faq.heading,
            "label": faq.label,
            "date": faq.date,
            "key_word": faq.key_word,
            "page_tag": faq.page_tag
        })

    return faqs_response


def get_project_types(db):
    result = db.execute(select(models.ProjectType))
    all_project_types = result.scalars().all()

    project_types = []

    for project_type in all_project_types:
        project_types.append({
            "id": project_type.id,
            "name": project_type.name
        })

    return project_types


def get_tariffs(db):
    result = db.execute(select(models.Tariff))
    all_tariffs = result.scalars().all()

    tariffs = []

    for tariff in all_tariffs:
        tariffs.append({
            "id": tariff.id,
            "name": tariff.name,
            "description": tariff.description,
            "cost": tariff.cost,
            "image": tariff.image,
        })

    return tariffs


def create_tariff(db, tariff):
    new_tariff = models.Tariff(
        name=tariff.name,
        description=tariff.description,
        cost=tariff.cost,
        image=tariff.image
    )

    db.add(new_tariff)
    db.commit()
    db.refresh(new_tariff)

    return new_tariff


def create_user_comment(db, user_comment):
    new_user_comment = models.UserComments(
        image=user_comment.image,
    )

    db.add(new_user_comment)
    db.commit()
    db.refresh(new_user_comment)

    return new_user_comment


def get_user_comments(db):
    result = db.execute(select(models.UserComments))
    all_user_comments = result.scalars().all()

    user_comments = []

    for user_comment in all_user_comments:
        user_comments.append({
            "id": user_comment.id,
            "image": user_comment.image,
        })

    return user_comments


def get_intro_videos(db):
    result = db.execute(select(models.IntroVideos))
    all_intro_videos = result.scalars().all()

    intro_videos = []

    for intro_video in all_intro_videos:
        intro_videos.append({
            "id": intro_video.id,
            "video": intro_video.video,
            "video_duration": intro_video.video_duration,
            "author": intro_video.author,
            "object": intro_video.object,
        })

    return intro_videos


def create_intro_video(db, intro_video):
    new_intro_video = models.IntroVideos(
        video=intro_video.video,
        video_duration=intro_video.video_duration,
        author=intro_video.author,
        object=intro_video.object
    )

    db.add(new_intro_video)
    db.commit()
    db.refresh(new_intro_video)

    return new_intro_video


def create_social_media_account(db, social_media_account):
    new_social_media_account = models.SocialMediaAccounts(
        name=social_media_account.name,
        logo=social_media_account.logo,
        link=social_media_account.link,
        subscribers=social_media_account.subscribers
    )

    db.add(new_social_media_account)
    db.commit()
    db.refresh(new_social_media_account)

    return new_social_media_account


def get_social_media_accounts(db):
    result = db.execute(select(models.SocialMediaAccounts))
    all_social_media_accounts = result.scalars().all()

    social_media_accounts = []

    for social_media_account in all_social_media_accounts:
        social_media_accounts.append({
            "id": social_media_account.id,
            "name": social_media_account.name,
            "logo": social_media_account.logo,
            "link": social_media_account.link,
            "subscribers": social_media_account.subscribers
        })

    return social_media_accounts


def create_blog_video(db, blog_video):
    new_blog_video = models.BlogVideos(
        video_link=blog_video.video_link,
        video_duration=blog_video.video_duration,
        author=blog_video.author,
        object=blog_video.object
    )

    db.add(new_blog_video)
    db.commit()
    db.refresh(new_blog_video)

    return new_blog_video


def get_blog_videos(db):
    result = db.execute(select(models.BlogVideos))
    all_blog_videos = result.scalars().all()

    blog_videos = []

    for blog_video in all_blog_videos:
        blog_videos.append({
            "id": blog_video.id,
            "video_link": blog_video.video_link,
            "video_duration": blog_video.video_duration,
            "author": blog_video.author,
            "object": blog_video.object
        })

    return blog_videos


def create_page_type(db, page_type):
    new_page_type = models.PageType(
        name=page_type.name
    )

    db.add(new_page_type)
    db.commit()
    db.refresh(new_page_type)

    return new_page_type


def get_page_types(db):
    result = db.execute(select(models.PageType))
    all_page_types = result.scalars().all()

    page_types = []

    for page_type in all_page_types:
        page_types.append({
            "id": page_type.id,
            "name": page_type.name
        })

    return page_types


def get_faqs_by_page_tag(page_tag: str, db: AsyncSession):
    result = db.execute(select(models.FAQ).where(models.FAQ.page_tag.has(name=page_tag)))
    faqs = result.scalars().all()

    faqs_response = []

    for faq in faqs:
        faqs_response.append({
            "title": faq.heading,
            "label": faq.label,
            "date": faq.date,
            "key_word": faq.key_word,
            "page_tag": faq.page_tag
        })

    return faqs_response


def get_seo_texts(db):
    result = db.execute(select(models.SEOText))
    all_seo_texts = result.scalars().all()

    seo_texts = []

    for seo_text in all_seo_texts:
        seo_texts.append({
            "text": seo_text.text,
            "page_tag": seo_text.page_tag
        })

    return seo_texts


def get_seo_text_by_page_tag(page_tag: str, db: AsyncSession):
    result = db.execute(select(models.SEOText).where(models.SEOText.page_tag.has(name=page_tag)))
    seo_text = result.scalars().first()

    if seo_text is None:
        raise HTTPException(status_code=404, detail="SEO text not found")

    seo_text_response = {
        "text": seo_text.text,
        "page_tag": seo_text.page_tag
    }

    return seo_text_response


def get_communication_types(db):
    result = db.execute(select(models.CommunicationType))
    all_communication_types = result.scalars().all()

    communication_types = []

    for communication_type in all_communication_types:
        communication_types.append({
            "title": communication_type.title
        })

    return communication_types


def create_consultation(consultation, db):
    type_of_communication = db.execute(select(models.CommunicationType).where(
        models.CommunicationType.title == consultation.communication_type.title)).scalars().first()
    if type_of_communication is None:
        raise HTTPException(status_code=404, detail="Communication type is incorrect")
    new_consultation = models.ConsultationList(
        phone=consultation.phone,
        answered=consultation.answered,
        communication_type=type_of_communication
    )

    db.add(new_consultation)
    db.commit()
    db.refresh(new_consultation)

    return new_consultation


def get_last_work_id(db):
    result = db.execute(select(models.Work.id).order_by(models.Work.id.desc()).limit(1))
    try:
        last_id = result.scalar_one()
    except:
        last_id = 0
    return last_id


def create_directory_for_last_work_id(db, base_path):
    last_id = get_last_work_id(db)
    directory_path = os.path.join(base_path, str(last_id + 1))
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_last_post_id(db):
    result = db.execute(select(models.Post.id).order_by(models.Post.id.desc()).limit(1))
    try:
        last_id = result.scalar_one()
    except:
        last_id = 0
    return last_id


def create_directory_for_last_post_id(db, base_path):
    last_id = get_last_post_id(db)
    directory_path = os.path.join(base_path, str(last_id + 1))
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_last_tariff_id(db):
    result = db.execute(select(models.Tariff.id).order_by(models.Tariff.id.desc()).limit(1))
    try:
        last_id = result.scalar_one()
    except:
        last_id = 0
    return last_id


def create_directory_for_last_tariff_id(db, base_path):
    last_id = get_last_tariff_id(db)
    directory_path = os.path.join(base_path, str(last_id + 1))
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_last_intro_video_id(db):
    result = db.execute(select(models.IntroVideos.id).order_by(models.IntroVideos.id.desc()).limit(1))
    try:
        last_id = result.scalar_one()
    except:
        last_id = 0
    return last_id


def create_directory_for_last_intro_video_id(db, base_path):
    last_id = get_last_intro_video_id(db)
    directory_path = os.path.join(base_path, str(last_id + 1))
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_last_user_comment_id(db):
    result = db.execute(select(models.UserComments.id).order_by(models.UserComments.id.desc()).limit(1))
    try:
        last_id = result.scalar_one()
    except:
        last_id = 0
    return last_id


def create_directory_for_last_user_comment_id(db, base_path):
    last_id = get_last_user_comment_id(db)
    directory_path = os.path.join(base_path, str(last_id + 1))
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def create_directory_for_last_social_networks_id(db, base_path):
    last_id = get_last_social_networks_id(db)
    directory_path = os.path.join(base_path, str(last_id + 1))
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_last_social_networks_id(db):
    result = db.execute(select(models.SocialMediaAccounts.id).order_by(models.SocialMediaAccounts.id.desc()).limit(1))
    try:
        last_id = result.scalar_one()
    except:
        last_id = 0
    return last_id


# Get all blogs
def get_blogs(db: AsyncSession):
    result = db.execute(select(models.Blog))
    blogs = result.scalars().all()

    blog_list = []
    for blog in blogs:
        blocks = []
        for block in blog.blog_blocks:
            texts = []
            if block.paragraphs:
                texts.append({
                    "title": block.paragraphs.title,
                    "items": block.paragraphs.items
                })
            blocks.append({
                "images": block.images,
                "texts": texts,
                "paragraphs": block.paragraphs if block.paragraphs else []
            })
        blog_list.append({
            "id": blog.id,
            "title": blog.title,
            "img_main": blog.img_main,
            "text_main": blog.text_main,
            "blocks": blocks
        })

    return blog_list


# Get a single blog by ID
def get_blog(id: int, db: AsyncSession):
    result = db.execute(select(models.Blog).where(models.Blog.id == id))
    blog = result.scalars().first()
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    blocks = []
    for block in blog.blog_blocks:
        texts = []
        if block.paragraphs:
            texts.append({
                "title": block.paragraphs.title,
                "items": block.paragraphs.items
            })
        blocks.append({
            "images": block.images,
            "texts": texts,
            "paragraphs": block.paragraphs if block.paragraphs else []
        })
    result_blog = {
        "id": blog.id,
        "title": blog.title,
        "img_main": blog.img_main,
        "text_main": blog.text_main,
        "blocks": blocks
    }
    return result_blog


# Create a new blog
async def create_blog(blog: schemas.BlogSchema, db: AsyncSession):
    new_blog = models.Blog(
        title=blog.title,
        img_main=blog.img_main,
        text_main=blog.text_main
    )
    db.add(new_blog)
    await db.commit()
    await db.refresh(new_blog)
    return schemas.BlogSchema.from_orm(new_blog)


def get_last_blog_id(db: AsyncSession):
    result = db.execute(select(models.Blog.id).order_by(models.Blog.id.desc()).limit(1))
    try:
        last_id = result.scalar_one()
    except:
        last_id = 0
    return last_id


def create_directory_for_last_blog_id(db: AsyncSession, base_path):
    last_id = get_last_blog_id(db)
    directory_path = os.path.join(base_path, str(last_id + 1))
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def create_directory_for_last_blog_block_id(db: AsyncSession, base_path):
    last_id = get_last_blog_block_id(db)
    directory_path = os.path.join(base_path, str(last_id + 1))
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_last_blog_block_id(db: AsyncSession):
    result = db.execute(select(models.BlogBlock.id).order_by(models.BlogBlock.id.desc()).limit(1))
    try:
        last_id = result.scalar_one()
    except:
        last_id = 0
    return last_id


# Get all blog blocks
def get_blog_blocks(db: AsyncSession):
    result = db.execute(select(models.BlogBlock))
    blog_blocks = result.scalars().all()
    return [schemas.BlogBlockSchema.from_orm(blog_block) for blog_block in blog_blocks]


# Get a single blog block by ID
def get_blog_block(id: int, db: AsyncSession):
    result = db.execute(select(models.BlogBlock).where(models.BlogBlock.id == id))
    blog_block = result.scalars().first()
    if blog_block is None:
        raise HTTPException(status_code=404, detail="BlogBlock not found")
    return schemas.BlogBlockSchema.from_orm(blog_block)


# Create a new blog block
def create_blog_block(blog_block: schemas.BlogBlockSchema, db: AsyncSession):
    new_blog_block = models.BlogBlock(
        images=blog_block.images
    )
    db.add(new_blog_block)
    db.commit()
    db.refresh(new_blog_block)
    # block_paragraph = db.execute(select(models.BlogParagraph).where(models.BlogParagraph.id == blog_block.paragraphs))
    # block_paragraph.blog_block_id = new_blog_block.id
    # db.commit()
    # db.refresh(block_paragraph)
    return new_blog_block


# Get all blog paragraphs
def get_blog_paragraphs(db: AsyncSession):
    result = db.execute(select(models.BlogParagraph))
    blog_paragraphs = result.scalars().all()
    return [schemas.BlogParagraphSchema.from_orm(blog_paragraph) for blog_paragraph in blog_paragraphs]


# Get a single blog paragraph by ID
def get_blog_paragraph(id: int, db: AsyncSession):
    result = db.execute(select(models.BlogParagraph).where(models.BlogParagraph.id == id))
    blog_paragraph = result.scalars().first()
    if blog_paragraph is None:
        raise HTTPException(status_code=404, detail="BlogParagraph not found")
    return schemas.BlogParagraphSchema.from_orm(blog_paragraph)


# Create a new blog paragraph
def create_blog_paragraph(blog_paragraph: schemas.BlogParagraphSchema, db: AsyncSession):
    new_blog_paragraph = models.BlogParagraph(
        title=blog_paragraph.title,
        items=blog_paragraph.items,
        blog_block_id=blog_paragraph.blog_block_id
    )
    db.add(new_blog_paragraph)
    db.commit()
    db.refresh(new_blog_paragraph)
    return new_blog_paragraph


def get_portfolio_posts(db: AsyncSession):
    result = db.execute(select(models.PortfolioPost).options(
        selectinload(models.PortfolioPost.overview),
        selectinload(models.PortfolioPost.others)
    ))
    portfolio_posts = result.scalars().all()

    portfolio_posts_list = []
    for portfolio_post in portfolio_posts:
        portfolio_posts_list.append({
            "id": portfolio_post.id,
            "title": portfolio_post.title,
            "img_main": portfolio_post.img_main,
            "img_result": portfolio_post.img_result,
            "price_amount": portfolio_post.price_amount,
            "object_area": portfolio_post.object_area,
            "work_completion_time": portfolio_post.work_completion_time,
            "type_of_work": str(portfolio_post.project_type),
            "texts": [
                {
                    "task": portfolio_post_text.task,
                    "steps_of_work": portfolio_post_text.steps_of_work,
                } for portfolio_post_text in portfolio_post.texts if
                portfolio_post_text.task and portfolio_post_text.steps_of_work
            ],
            "images": portfolio_post.images,
            "overview": {
                "id": portfolio_post.overview.id,
                "duration": portfolio_post.overview.duration,
                "link": portfolio_post.overview.link,
                "portfolio_post_id": portfolio_post.overview.portfolio_post_id
            } if portfolio_post.overview else None,
            "others": [
                {
                    "id": other.id,
                    "duration": other.duration,
                    "link": other.link,
                    "portfolio_post_id": other.portfolio_post_id
                } for other in portfolio_post.others
            ] if portfolio_post.others else []
        })

    return portfolio_posts_list


def get_portfolio_post(id: int, db: AsyncSession):
    result = db.execute(select(models.PortfolioPost).where(models.PortfolioPost.id == id).options(
        selectinload(models.PortfolioPost.overview),
        selectinload(models.PortfolioPost.others)
    ))
    portfolio_post = result.scalars().first()
    if portfolio_post is None:
        raise HTTPException(status_code=404, detail="PortfolioPost not found")

    portfolio_post_response = {
        "id": portfolio_post.id,
        "title": portfolio_post.title,
        "img_main": portfolio_post.img_main,
        "img_result": portfolio_post.img_result,
        "price_amount": portfolio_post.price_amount,
        "object_area": portfolio_post.object_area,
        "work_completion_time": portfolio_post.work_completion_time,
        "type_of_work": str(portfolio_post.project_type),
        "texts": [
            {
                "task": portfolio_post_text.task,
                "steps_of_work": portfolio_post_text.steps_of_work,
            } for portfolio_post_text in portfolio_post.texts
        ],
        "images": portfolio_post.images,
        "overview": {
            "id": portfolio_post.overview.id,
            "duration": portfolio_post.overview.duration,
            "link": portfolio_post.overview.link,
            "portfolio_post_id": portfolio_post.overview.portfolio_post_id
        } if portfolio_post.overview else None,
        "others": [
            {
                "id": other.id,
                "duration": other.duration,
                "link": other.link,
                "portfolio_post_id": other.portfolio_post_id
            } for other in portfolio_post.others
        ] if portfolio_post.others else []
    }

    return portfolio_post_response


def create_portfolio_post(portfolio_post: schemas.PortfolioPostSchema, db: AsyncSession):
    new_portfolio_post = models.PortfolioPost(
        title=portfolio_post.title,
        img_main=portfolio_post.img_main,
        img_result=portfolio_post.img_result,
        price_amount=portfolio_post.price_amount,
        object_area=portfolio_post.object_area,
        work_completion_time=portfolio_post.work_completion_time,
        type_of_work=portfolio_post.type_of_work,
        texts=portfolio_post.texts,
        images=portfolio_post.images,
        project_type_id=portfolio_post.project_type_id,
        overview=portfolio_post.overview,
        videos=portfolio_post.videos

    )
    db.add(new_portfolio_post)
    db.commit()
    db.refresh(new_portfolio_post)
    return new_portfolio_post


def create_portfolio_post_video(portfolio_post_video: schemas.PortfolioPostVideoSchema, db: AsyncSession):
    new_portfolio_post_video = models.PortfolioPostVideo(
        duration=portfolio_post_video.duration,
        link=portfolio_post_video.link,
        portfolio_post_id=portfolio_post_video.portfolio_post_id
    )
    db.add(new_portfolio_post_video)
    db.commit()
    db.refresh(new_portfolio_post_video)
    return new_portfolio_post_video


def create_directory_for_last_portfolio_post_id(db: AsyncSession, base_path):
    last_id = get_last_portfolio_post_id(db)
    directory_path = os.path.join(base_path, str(last_id + 1))
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_last_portfolio_post_id(db: AsyncSession):
    result = db.execute(select(models.PortfolioPost.id).order_by(models.PortfolioPost.id.desc()).limit(1))
    try:
        last_id = result.scalar_one()
    except:
        last_id = 0
    return last_id


def get_user_stories(db: AsyncSession):
    result = db.execute(select(models.UserStory))
    user_stories = result.scalars().all()

    user_stories_list = []
    for user_story in user_stories:
        user_stories_list.append({
            "id": user_story.id,
            "image": user_story.image
        })

    return user_stories_list


def create_directory_for_last_user_story_id(db: AsyncSession, base_path):
    last_id = get_last_user_story_id(db)
    directory_path = os.path.join(base_path, str(last_id + 1))
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_last_user_story_id(db: AsyncSession):
    result = db.execute(select(models.UserStory.id).order_by(models.UserStory.id.desc()).limit(1))
    try:
        last_id = result.scalar_one()
    except:
        last_id = 0
    return last_id


def get_profiles_roles(db: AsyncSession):
    result = db.execute(select(models.UserType))
    profile_roles = result.scalars().all()

    profile_roles_list = []
    for profile_role in profile_roles:
        profile_roles_list.append({
            "id": profile_role.id,
            "name": profile_role.name,
            "description": profile_role.description
        })

    return profile_roles_list
