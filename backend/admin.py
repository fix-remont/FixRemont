# from asyncio import Future
# from sqladmin.fields import FileField
# from src.database.crud import create_post, create_work, create_notification
# import base64
# from markupsafe import Markup
# from src.database import schemas
# from src.database.db import get_db
# from src.database.models import User
# from src.auth.auth_routes import get_password_hash
# from wtforms import SelectField
# from sqladmin import ModelView
# from src.database.models import Flat
# from src.database.models import Style
# from src.database.models import AdditionalOption
# from src.database.models import Tariff
# from asyncio import Future
# from sqladmin.fields import FileField
# from src.database.crud import create_post, create_work, create_notification
# import base64
# from markupsafe import Markup
# from src.database import schemas
# from src.database.models import Contract, Post, Work, Notification, ProjectType, PostType, UserType, \
#     NotificationType
# from src.database.db import get_db
# from src.database.models import User
# from src.auth.auth_routes import get_password_hash
# from wtforms import SelectField
# from sqladmin import ModelView
# from src.database.models import Flat
# from src.database.models import Style
# from src.database.models import AdditionalOption
# from src.database.models import Tariff
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select
#
# db = get_db()
#
#
# async def get_all_model_values(db: AsyncSession, model):
#     result = await db.execute(select(model.name))
#     return [x[0] for x in result.scalars().all()]
#
#
# class UserAdmin(ModelView, model=User):
#     name = "Пользователь"
#     name_plural = "! Пользователи"
#     icon = "fa-solid fa-user-tie"
#     column_list = [User.email, User.name, User.surname, User.phone, User.user_type, User.notification_status,
#                    User.notifications]
#     column_searchable_list = [User.email, User.name, User.surname, User.user_type]
#     column_filters = [User.user_type]
#     column_sortable_list = [User.email, User.name, User.surname, User.user_type]
#     column_details_exclude_list = [User.hashed_password, User.id]
#     column_labels = dict(name="Имя", email="Email", surname="Фамилия", phone="Номер телефона", user_type="Роль",
#                          notification_status="Статус уведомлений", user_referral_code="Реферальный код пользователя",
#                          others_referral_code="Сторонний реферальный код", is_active="Активен",
#                          is_superuser="Является админом", clients="Клиенты", contracts="Контракты",
#                          hashed_password="Пароль", notifications="Уведомления")
#     form_edit_rules = ['name', 'surname', 'phone', 'user_type', 'notification_status', 'user_referral_code',
#                        'others_referral_code', 'is_superuser', 'clients', 'contracts', 'notifications']
#     form_create_rules = ['email', 'name', 'surname', 'phone', 'user_type', 'notification_status', 'user_referral_code',
#                          'others_referral_code', 'is_superuser', 'clients', 'contracts', 'hashed_password']
#     can_create = True
#     can_edit = True
#     can_delete = True
#
#     form_widget_args = {
#         "name": {
#             'placeholder="Пользователь пока не ввел имя"': True,
#         },
#         "surname": {
#             'placeholder="Пользователь пока не ввел фамилию"': True,
#         },
#         "phone": {
#             'pattern': "[0-9]",  # TODO: add pattern for phone number
#             'placeholder="Пользователь пока не ввел номер телефона"': True,
#         },
#         "others_referral_code": {
#             'placeholder="Пользователь пока не ввел сторонний реферальный код"': True,
#         },
#         "email": {
#             'placeholder="Введите email пользователя"': True,
#         },
#         "hashed_password": {
#             'placeholder="Введите пароль пользователя"': True,
#         },
#     }
#
#     async def on_model_change(self, data, model, is_created, request):
#         if is_created:
#             if not data.get('hashed_password'):
#                 raise ValueВложение отсутствует("Password cannot be None")
#             model.hashed_password = get_password_hash(data['hashed_password'])
#             model.user_type = db.query(UserType).filter_by(name=data['user_type']).first()
#         return Future().set_result(None)
#
#
#
# class ContractAdmin(ModelView, model=Contract):
#     name = "Контракт"
#     name_plural = "! Контракты"
#     icon = "fa-solid fa-file-signature"
#     column_list = [Contract.id, Contract.object, Contract.tariff, Contract.location, Contract.total_cost,
#                    Contract.current_stage, Contract.user_id]
#     column_searchable_list = [Contract.object]
#     can_create = True
#     can_edit = True
#     can_delete = True
#     column_labels = dict(object="Объект", tariff="Тариф", location="Местоположение", total_cost="Общая стоимость",
#                          current_stage="Текущий этап", user_id="ID пользователя")
#
#
# class PostAdmin(ModelView, model=Post):
#     name = "Пост"
#     name_plural = "! Посты"
#     icon = "fa-solid fa-newspaper"
#     column_list = [Post.title, Post.post_type, Post.content, Post.images]
#     column_searchable_list = [Post.title]
#     column_filters = [Post.post_type]
#     column_sortable_list = [Post.id, Post.title]
#     can_create = True
#     can_edit = True
#     can_delete = True
#     column_labels = dict(title="Заголовок", post_type="Тип поста", content="Содержание", images="Изображения")
#
#     form_overrides = {
#         'images': FileField,
#     }
#
#     column_formatters_detail = {
#         'images': lambda m, p: Markup(
#             ''.join(
#                 f'<img src="data:image/png;base64,{image}" width="100" />'
#                 for image in m.images
#             )
#         ) if m.images else 'Вложение отсутствует'
#     }
#
#     column_formatters = {
#         'images': lambda m, p: Markup(
#             ''.join(
#                 f'<img src="data:image/png;base64,{image}" width="100" />'
#                 for image in m.images
#             )
#         ) if m.images else 'Вложение отсутствует'
#     }
#
#     async def on_model_change(self, data, model, is_created, request):
#         if 'images' in data:
#             images = []
#             file = data['images']
#             content = await file.read()
#             images.append(base64.b64encode(content).decode('utf-8') if content else None)
#
#             post_data = schemas.PostCreate(
#                 title=data['title'],
#                 post_type=data['post_type'],
#                 content=data['content'],
#                 images=images
#             )
#
#             for db_session in get_db():
#                 await create_post(post_data, db_session)
#
#
# class WorkAdmin(ModelView, model=Work):
#     name = "Портфолио"
#     name_plural = "! Портфолио"
#     icon = "fa-solid fa-building-circle-check"
#
#     column_list = [Work.title, Work.project_type, Work.deadline, Work.cost, Work.square, Work.task,
#                    Work.description, Work.images]
#     column_searchable_list = [Work.title]
#     column_filters = [Work.project_type]
#     column_sortable_list = [Work.id, Work.title, Work.cost, Work.square, Work.deadline]
#     can_create = True
#     can_edit = True
#     can_delete = True
#     column_labels = dict(title="Заголовок", project_type="Тип проекта", deadline="Дедлайн", cost="Стоимость",
#                          square="Площадь", task="Задача", description="Описание", images="Изображения")
#
#     form_overrides = {
#         'images': FileField
#     }
#
#     column_formatters = {
#         'images': lambda m, p: Markup(
#             ''.join(
#                 f'<img src="data:image/png;base64,{image}" width="100" />'
#                 for image in m.images
#             )
#         ) if m.images else 'Вложение отсутствует'
#     }
#
#     column_formatters_detail = {
#         'images': lambda m, p: Markup(
#             ''.join(
#                 f'<img src="data:image/png;base64,{image}" width="100" />'
#                 for image in m.images
#             )
#         ) if m.images else 'Вложение отсутствует'
#     }
#
#     async def on_model_change(self, data, model, is_created, request):
#         if 'images' in data:
#             images = []
#             file = data['images']
#             content = await file.read()
#             images.append(base64.b64encode(content).decode('utf-8') if content else None)
#             data['images'] = images
#             work_data = schemas.WorkCreate(
#                 title=data['title'],
#                 project_type=data['project_type'],
#                 deadline=data['deadline'],
#                 cost=data['cost'],
#                 square=data['square'],
#                 task=data['task'],
#                 description=data['description'],
#                 images=images
#             )
#
#             for db_session in get_db():
#                 await create_work(work_data, db_session)
#
#
# class NotificationAdmin(ModelView, model=Notification):
#     name = "Уведомление"
#     name_plural = "! Уведомления"
#     icon = "fa-solid fa-bell"
#
#     column_list = [Notification.message_type, Notification.content, Notification.user_id,
#                    Notification.attachment]
#     column_searchable_list = [Notification.content]
#     can_create = True
#     can_edit = True
#     can_delete = True
#     column_labels = dict(message_type="Тип сообщения", content="Содержание", user_id="ID пользователя",
#                          attachment="Вложение", user="Пользователь")
#
#     column_details_exclude_list = [Notification.id]
#
#     form_overrides = {
#         'attachment': FileField
#     }
#
#     column_formatters_detail = {
#         'attachment': lambda m, p: Markup(
#             f'<a href="data:application/pdf;base64,{base64.b64encode(m.attachment).decode("utf-8")}" download="attachment.pdf">Скачать PDF</a>'
#         ) if m.attachment else 'Вложение отсутствует'
#     }
#
#     column_formatters = {
#         'attachment': lambda m, p: Markup(
#             f'<a href="data:application/pdf;base64,{base64.b64encode(m.attachment).decode("utf-8")}" download="attachment.pdf">Скачать PDF</a>'
#         ) if m.attachment else 'Вложение отсутствует'
#     }
#
#     async def on_model_change(self, data, model, is_created, request):
#         if 'attachment' in data:
#             file_data = await data['attachment'].read()
#             user_id = data['user']
#             notification_data = schemas.NotificationCreate(
#                 user_id=user_id,
#                 message_type=data['message_type'],
#                 content=data['content'],
#                 attachment=file_data,
#             )
#
#             for db_session in get_db():
#                 await create_notification(notification_data, db_session)
#
#
# class FlatAdmin(ModelView, model=Flat):
#     name = "Квартира"
#     name_plural = "! Квартиры"
#     icon = "fa-solid fa-building"
#     column_list = [Flat.square, Flat.address, Flat.number_of_rooms, Flat.number_of_doors, Flat.number_of_wc,
#                    Flat.demolition, Flat.wall_build, Flat.liquid_floor, Flat.ceiling_stretching, Flat.tariff_id,
#                    Flat.style_id]
#     column_searchable_list = [Flat.address]
#     can_create = True
#     can_edit = True
#     can_delete = True
#     column_labels = dict(square="Площадь", address="Адрес", number_of_rooms="Количество комнат",
#                          number_of_doors="Количество дверей", number_of_wc="Количество санузлов", demolition="Снос",
#                          wall_build="Постройка стен", liquid_floor="Жидкий пол", ceiling_stretching="Натяжной потолок",
#                          tariff_id="Тариф", style_id="Стиль")
#
#
# class TariffAdmin(ModelView, model=Tariff):
#     name = "Тариф"
#     name_plural = "! Тарифы"
#     icon = "fa-solid fa-money-bill"
#     category = "Ремонт квартир"
#     column_list = [Tariff.name, Tariff.description]
#     column_searchable_list = [Tariff.name]
#     can_create = True
#     can_edit = True
#     can_delete = True
#     column_labels = dict(name="Название", description="Описание")
#
#
# class StyleAdmin(ModelView, model=Style):
#     name = "Стиль"
#     name_plural = "! Стили"
#     icon = "fa-solid fa-paint-brush"
#     category = "Ремонт квартир"
#     column_list = [Style.name, Style.description]
#     column_searchable_list = [Style.name]
#     can_create = True
#     can_edit = True
#     can_delete = True
#     column_labels = dict(name="Название", description="Описание")
#
#
# class AdditionalOptionAdmin(ModelView, model=AdditionalOption):
#     name = "Дополнительная опция"
#     name_plural = "! Дополнительные опции"
#     category = "Ремонт квартир"
#     icon = "fa-solid fa-plus"
#     column_list = [AdditionalOption.name, AdditionalOption.description]
#     column_searchable_list = [AdditionalOption.name]
#     can_create = True
#     can_edit = True
#     can_delete = True
#     column_labels = dict(name="Название", description="Описание")
#
#
# class ProjectTypeAdmin(ModelView, model=ProjectType):
#     name = "Тип проекта"
#     name_plural = "! Типы проектов"
#     icon = "fa-solid fa-building"
#     column_list = [ProjectType.name]
#     column_searchable_list = [ProjectType.name]
#     can_create = True
#     can_edit = True
#     can_delete = True
#     column_labels = dict(name="Название")
#
#
# class PostTypeAdmin(ModelView, model=PostType):
#     name = "Тип поста"
#     name_plural = "! Типы постов"
#     icon = "fa-solid fa-newspaper"
#     column_list = [PostType.name]
#     column_searchable_list = [PostType.name]
#     can_create = True
#     can_edit = True
#     can_delete = True
#     column_labels = dict(name="Название")
#
#
# class UserTypeAdmin(ModelView, model=UserType):
#     name = "Тип пользователя"
#     name_plural = "! Типы пользователей"
#     icon = "fa-solid fa-user"
#     column_list = [UserType.name]
#     column_searchable_list = [UserType.name]
#     can_create = True
#     can_edit = True
#     can_delete = True
#     column_labels = dict(name="Название")
#
#
# class NotificationTypeAdmin(ModelView, model=NotificationType):
#     name = "Тип уведомления"
#     name_plural = "! Типы уведомлений"
#     icon = "fa-solid fa-bell"
#     column_list = [NotificationType.name]
#     column_searchable_list = [NotificationType.name]
#     can_create = True
#     can_edit = True
#     can_delete = True
#     column_labels = dict(name="Название")
#


from asyncio import Future
from sqladmin.fields import FileField

from src.database.cruds import *
import base64
from markupsafe import Markup
from src.database import schemas, models
from src.database.db import get_db
from src.database.models import *
from src.auth.auth_routes import get_password_hash
from wtforms import SelectField, RadioField, BooleanField, MultipleFileField
from sqladmin import ModelView
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database.schemas import PostTypeEnum, PortfolioPostSchema, ProjectTypeSchema, ArticleSchema, \
    ContractNotificationStatusEnum

db = get_db()


async def get_all_model_values(db: AsyncSession, model):
    result = await db.execute(select(model.name))
    return [x[0] for x in result.scalars().all()]


# async def get_project_type_by_id(db_session: AsyncSession, id: int):
#     result = await db_session.execute(select(ProjectType).filter_by(id=id))
#     return result.scalar_one()


class UserAdmin(ModelView, model=User):
    name = "Пользователь"
    name_plural = "Пользователи [BUG]"
    icon = "fa-solid fa-user-tie"
    column_list = [User.email, User.name, User.surname, User.patronymic, User.phone, User.user_type,
                   User.notification_status,
                   User.notifications]
    column_searchable_list = [User.email, User.name, User.surname, User.user_type]
    column_filters = [User.user_type]
    column_sortable_list = [User.email, User.name, User.surname, User.user_type]
    column_details_exclude_list = [User.hashed_password, User.id]
    column_labels = dict(name="Имя", email="Email", surname="Фамилия", phone="Номер телефона", user_type="Роль",
                         notification_status="Статус уведомлений", user_referral_code="Реферальный код пользователя",
                         others_referral_code="Сторонний реферальный код", is_active="Активен",
                         is_superuser="Является админом", contracts="Контракты", hashed_password="Пароль",
                         notifications="Уведомления", patronymic="Отчество")
    form_edit_rules = ['name', 'surname', 'patronymic', 'phone', 'user_type', 'notification_status',
                       'user_referral_code',
                       'others_referral_code', 'is_superuser', 'contracts', 'notifications']
    form_create_rules = ['email', 'name', 'surname', 'patronymic', 'phone', 'user_type', 'notification_status',
                         'user_referral_code',
                         'others_referral_code', 'is_superuser', 'contracts', 'hashed_password']
    can_create = True
    can_edit = True
    can_delete = True

    form_widget_args = {
        "name": {'placeholder': "Пользователь пока не ввел имя"},
        "surname": {'placeholder': "Пользователь пока не ввел фамилию"},
        "phone": {'pattern': "[0-9]", 'placeholder': "Пользователь пока не ввел номер телефона"},
        "others_referral_code": {'placeholder': "Пользователь пока не ввел сторонний реферальный код"},
        "email": {'placeholder': "Введите email пользователя"},
        "hashed_password": {'placeholder': "Введите пароль пользователя"},
    }

    # TODO: не сохраняется захешированный пароль
    async def on_model_change(self, data, model, is_created, request):
        create_user_data = schemas.UserSchema(
            email=data['email'] if 'email' in data else model.email,
            name=data['name'],
            surname=data['surname'],
            patronymic=data['patronymic'],
            hashed_password=data['hashed_password'] if 'hashed_password' in data else model.hashed_password,
            phone=data['phone'],
            user_type=data['user_type'],
            notification_status=data['notification_status'],
            user_referral_code=data['user_referral_code'],
            others_referral_code=data['others_referral_code'],
            is_superuser=data['is_superuser'],

        )
        for db_session in db:
            print("Creating user")
            await create_user(db_session, create_user_data)


class ContractAdmin(ModelView, model=Contract):
    name = "Контракт"
    name_plural = "Контракты"
    icon = "fa-solid fa-file-signature"
    column_list = [Contract.id, Contract.object, Contract.tariff_type, Contract.location, Contract.total_cost,
                   Contract.current_stage, Contract.client_id, Contract.date]
    column_searchable_list = [Contract.object]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID", object="Объект", order_type="Тип заказа", tariff_type="Тариф", square="Площадь",
                         location="Местоположение", current_stage="Текущий этап", total_cost="Общая стоимость",
                         materials_cost="Стоимость материалов", work_cost="Стоимость работы", revenue="Доход",
                         client_id="ID клиента", date="Дата", notifications="Уведомления", document="Документ",
                         work_statuses="Статусы работ", client="Клиент")


class PostAdmin(ModelView, model=Post):
    name = "Пост"
    name_plural = "Посты"
    icon = "fa-solid fa-newspaper"
    column_list = [Post.title, Post.post_type, Post.paragraphs, Post.image1, Post.image2, Post.image3]
    column_searchable_list = [Post.title]
    column_filters = [Post.post_type]
    column_sortable_list = [Post.id, Post.title]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(title="Заголовок", post_type="Тип поста", paragraphs="Параграфы", image1="Изображение 1",
                         image2="Изображение 2", image3="Изображение 3", id="ID", post_type_id="Тип поста")

    form_overrides = {
        'image1': FileField,
        'image2': FileField,
        'image3': FileField,
    }

    column_formatters_detail = {
        'image1': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image1}" width="100" />') if m.image1 else 'Вложение отсутствует',
        'image2': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image2}" width="100" />') if m.image2 else 'Вложение отсутствует',
        'image3': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image3}" width="100" />') if m.image3 else 'Вложение отсутствует',
        'post_type': lambda m, p: m.post_type.value,

    }

    column_formatters = {
        'image1': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image1}" width="100" />') if m.image1 else 'Вложение отсутствует',
        'image2': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image2}" width="100" />') if m.image2 else 'Вложение отсутствует',
        'image3': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image3}" width="100" />') if m.image3 else 'Вложение отсутствует',
        'post_type': lambda m, p: m.post_type.value,
    }

    async def on_model_change(self, data, model, is_created, request):
        if 'image1' in data:
            file = data['image1']
            content = await file.read()
            data['image1'] = base64.b64encode(content).decode('utf-8') if content else None
        if 'image2' in data:
            file = data['image2']
            content = await file.read()
            data['image2'] = base64.b64encode(content).decode('utf-8') if content else None
        if 'image3' in data:
            file = data['image3']
            content = await file.read()
            data['image3'] = base64.b64encode(content).decode('utf-8') if content else None

        post_type_value = data.get('post_type')
        if post_type_value not in PostTypeEnum.__members__:
            raise ValueError(f"'{post_type_value}' is not a valid PostTypeEnum")

        post_data = schemas.PostSchema(
            id=0,
            title=data.get('title'),
            post_type=PostTypeEnum[post_type_value],
            paragraphs=data.get('paragraphs', []),
            pictures=[data.get('image1'), data.get('image2'), data.get('image3')]
        )
        for db_session in get_db():
            await create_post(post_data, db_session)


class WorkAdmin(ModelView, model=Work):
    name = "Портфолио"
    name_plural = "Портфолио"
    icon = "fa-solid fa-building-circle-check"
    column_list = [Work.title, Work.project_type, Work.deadline, Work.cost, Work.square, Work.task, Work.description,
                   Work.image1, Work.image2, Work.image3, Work.image4, Work.image5, Work.video_link,
                   Work.video_duration]
    column_searchable_list = [Work.title]
    column_filters = [Work.project_type]
    column_sortable_list = [Work.id, Work.title, Work.cost, Work.square, Work.deadline]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(title="Заголовок", project_type="Тип проекта", deadline="Дедлайн", cost="Стоимость",
                         square="Площадь", task="Задача", description="Описание", image1="Изображение 1",
                         image2="Изображение 2", image3="Изображение 3", image4="Изображение 4", image5="Изображение 5",
                         video_link="Ссылка на видео", video_duration="Длительность видео", id="ID",
                         project_type_id="Тип проекта")

    form_overrides = {
        'image1': FileField,
        'image2': FileField,
        'image3': FileField,
        'image4': FileField,
        'image5': FileField,
    }

    column_formatters = {
        'image1': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image1}" width="100" />') if m.image1 else 'Вложение отсутствует',
        'image2': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image2}" width="100" />') if m.image2 else 'Вложение отсутствует',
        'image3': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image3}" width="100" />') if m.image3 else 'Вложение отсутствует',
        'image4': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image4}" width="100" />') if m.image4 else 'Вложение отсутствует',
        'image5': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image5}" width="100" />') if m.image5 else 'Вложение отсутствует',
        'project_type_id': lambda m, p: m.project_type.name,
        'description': lambda m, p: Markup(
            ''.join(
                f"<b>{article.split(':')[0]}</b> <br> <p>{article.split(':')[1]}</p>"
                for article in m.description
            ) if m.description else 'Описание отсутствует'),
        'task': lambda m, p: Markup(
            f'<p>{m.task[:30]}...</p>' if len(m.task) > 30 else f'<p>{m.task}</p>'
        )
    }

    column_formatters_detail = {
        'image1': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image1}" width="100" />') if m.image1 else 'Вложение отсутствует',
        'image2': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image2}" width="100" />') if m.image2 else 'Вложение отсутствует',
        'image3': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image3}" width="100" />') if m.image3 else 'Вложение отсутствует',
        'image4': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image4}" width="100" />') if m.image4 else 'Вложение отсутствует',
        'image5': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image5}" width="100" />') if m.image5 else 'Вложение отсутствует',
        'project_type_id': lambda m, p: m.project_type.name,
        'description': lambda m, p: Markup(
            ''.join(
                f"<b>{article.split(':')[0]}</b> <br> <p>{article.split(':')[1]}</p>"
                for article in m.description
            ) if m.description else 'Описание отсутствует'),

        'task': lambda m, p: Markup(
            f'<p style="display: inline-block; max-width: 300px; word-wrap: break-word; overflow-wrap: break-word; hyphens: auto; margin: 0; padding: 0;" id="task-{m.id}">{m.task}</p>'
            f'<script>'
            f'  const taskElement = document.getElementById("task-{m.id}");'
            f'  let text = taskElement.innerText;'
            f'  let breakPoint = 70;'
            f'  while (breakPoint < text.length) {{'
            f'    const spaceIndex = text.lastIndexOf(" ", breakPoint);'
            f'    if (spaceIndex !== -1) {{'
            f'      text = text.slice(0, spaceIndex) + "<wbr>" + text.slice(spaceIndex + 1);'
            f'      breakPoint = spaceIndex + 71;'
            f'    }} else {{'
            f'      breakPoint += 70;'
            f'    }}'
            f'  }}'
            f'  taskElement.innerHTML = text;'
            f'</script>'
        )
    }

    async def on_model_change(self, data, model, is_created, request):
        for image_field in ['image1', 'image2', 'image3', 'image4', 'image5']:
            if image_field in data:
                file = data[image_field]
                content = await file.read()
                data[image_field] = base64.b64encode(content).decode('utf-8') if content else None
        description = data.get('description')
        articles = []
        for block in description:
            key, value = block.split(":")
            articles.append(ArticleSchema(title=key.strip(), body=value.strip()))
        work_data = PortfolioPostSchema(
            id=0,
            title=data.get('title'),
            project_type=get_project_type_by_id(db, data.get('project_type')),
            deadline=data.get('deadline'),
            cost=data.get('cost'),
            square=data.get('square'),
            video_link=data.get('video_link'),
            video_duration=data.get('video_duration'),
            pictures=[data.get('image1'), data.get('image2'), data.get('image3'), data.get('image4'),
                      data.get('image5')],
            articles=articles
        )
        print(work_data)
        for db_session in get_db():
            await create_portfolio_post(work_data, db_session)


class NotificationAdmin(ModelView, model=Notification):
    name = "Уведомление"
    name_plural = "Уведомления"
    icon = "fa-solid fa-bell"
    column_list = [Notification.notification_status, Notification.title, Notification.label, Notification.date,
                   Notification.attachment, Notification.contract_id, Notification.user_id]
    column_searchable_list = [Notification.title, Notification.date]
    column_sortable_list = [Notification.notification_status, Notification.title, Notification.date]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(notification_status="Статус уведомления", title="Заголовок", date="Дата",
                         attachment="Вложение", contract_id="ID контракта", user_id="ID пользователя",
                         label="Содержание", id="ID", contract="Контракт", user="Пользователь")

    form_overrides = {
        'attachment': FileField
    }

    column_formatters_detail = {
        'attachment': lambda m, p: Markup(
            f'<a href="data:application/pdf;base64,{base64.b64encode(m.attachment).decode("utf-8")}" download="attachment.pdf">Скачать PDF</a>') if m.attachment else 'Вложение отсутствует',
        'notification_status': lambda m, p: m.notification_status.value
    }

    column_formatters = {
        'attachment': lambda m, p: Markup(
            f'<a href="data:application/pdf;base64,{base64.b64encode(m.attachment).decode("utf-8")}" download="attachment.pdf">Скачать PDF</a>') if m.attachment else 'Вложение отсутствует',
        'notification_status': lambda m, p: m.notification_status.value
    }

    async def on_model_change(self, data, model, is_created, request):
        if 'attachment' in data:
            file = data['attachment']
            file_data = await file.read()
            data['attachment'] = file_data

        if data['notification_status'] == 'message':
            notification_data = schemas.OrderNotificationSchema(
                id=0,
                type=ContractNotificationStatusEnum[data['notification_status']],
                title=data['title'],
                label=data['label']
            )
        elif data['notification_status'] == 'sign_act':
            notification_data = schemas.OrderDocumentsSchema(
                id=0,
                type=ContractNotificationStatusEnum[data['notification_status']],
                title=data['title'],
                label=data['label'],
                attachment=data['attachment']
            )

        for db_session in get_db():
            await create_notification(notification_data, db_session)


class FlatAdmin(ModelView, model=Flat):
    name = "Квартира"
    name_plural = "! Квартиры"
    icon = "fa-solid fa-building"
    column_list = [Flat.square, Flat.address, Flat.number_of_rooms, Flat.number_of_doors, Flat.number_of_wc,
                   Flat.demolition, Flat.wall_build, Flat.liquid_floor, Flat.ceiling_stretching, Flat.tariff_id,
                   Flat.style_id]
    column_searchable_list = [Flat.address]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(square="Площадь", address="Адрес", number_of_rooms="Количество комнат",
                         number_of_doors="Количество дверей", number_of_wc="Количество санузлов", demolition="Снос",
                         wall_build="Постройка стен", liquid_floor="Жидкий пол", ceiling_stretching="Натяжной потолок",
                         tariff_id="Тариф", style_id="Стиль")


class PlatformNewsAdmin(ModelView, model=PlatformNews):
    name = "Новости платформы"
    name_plural = "Новости платформы"
    icon = "fa-solid fa-newspaper"
    column_list = [PlatformNews.id, PlatformNews.title, PlatformNews.date, PlatformNews.label]
    column_searchable_list = [PlatformNews.title]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID", title="Заголовок", date="Дата", label="Содержание")


class WorkStatusAdmin(ModelView, model=WorkStatus):
    name = "Статус работы"
    name_plural = "Статусы работы"
    icon = "fa-solid fa-tasks"
    column_list = [WorkStatus.title, WorkStatus.document, WorkStatus.status, WorkStatus.contract]
    column_searchable_list = [WorkStatus.title]
    column_sortable_list = [WorkStatus.id, WorkStatus.title, WorkStatus.status]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID", title="Название", document="Документ", status="Статус", contract_id="ID контракта",
                         contract="Контракт")

    form_overrides = {
        'document': FileField
    }

    column_formatters_detail = {
        'document': lambda m, p: Markup(
            f'<a href="data:application/pdf;base64,{base64.b64encode(m.document).decode("utf-8")}" download="attachment.pdf">Скачать PDF</a>') if m.document else 'Вложение отсутствует'
    }

    column_formatters = {
        'document': lambda m, p: Markup(
            f'<a href="data:application/pdf;base64,{base64.b64encode(m.document).decode("utf-8")}" download="attachment.pdf">Скачать PDF</a>') if m.document else 'Вложение отсутствует'
    }

    async def on_model_change(self, data, model, is_created, request):
        if 'document' in data:
            file = data['document']
            file_data = await file.read()
            data['document'] = file_data

        work_status_data = schemas.WorkStateSchema(
            id=0,
            title=data['title'],
            document=data['document'],
            status=data['status']
        )

        for db_session in get_db():
            await create_work_status(work_status_data, db_session)


class AdditionalOptionAdmin(ModelView, model=AdditionalOption):
    name = "Дополнительная опция"
    name_plural = "! Дополнительные опции"
    category = "Ремонт квартир"
    icon = "fa-solid fa-plus"
    column_list = [AdditionalOption.name, AdditionalOption.description]
    column_searchable_list = [AdditionalOption.name]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(name="Название", description="Описание")


class StyleAdmin(ModelView, model=Style):
    name = "Стиль"
    name_plural = "! Стили"
    icon = "fa-solid fa-paint-brush"
    category = "Ремонт квартир"
    column_list = [Style.name, Style.description]
    column_searchable_list = [Style.name]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(name="Название", description="Описание")


class TariffAdmin(ModelView, model=Tariff):
    name = "Тариф"
    name_plural = "Тарифы"
    icon = "fa-solid fa-money-bill"
    column_list = [Tariff.name, Tariff.description, Tariff.cost, Tariff.image]
    column_searchable_list = [Tariff.name]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(name="Название", description="Описание", cost="Стоимость", image="Изображение")

    form_overrides = {
        'image': FileField
    }

    column_formatters_detail = {
        'image': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image}" width="100" />') if m.image else 'Вложение отсутствует',

    }

    column_formatters = {
        'image': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image}" width="100" />') if m.image else 'Вложение отсутствует',
    }

    async def on_model_change(self, data, model, is_created, request):
        if 'image' in data:
            file = data['image']
            content = await file.read()
            data['image'] = base64.b64encode(content).decode('utf-8') if content else None

        tariff_data = schemas.TariffSchema(
            image=data.get('image'),
            name=data.get('name'),
            description=data.get('description'),
            cost=data.get('cost')
        )
        for db_session in get_db():
            await create_tariff(tariff_data, db_session)


class ParagraphAdmin(ModelView, model=Paragraph):
    name = "Параграф"
    name_plural = "Параграфы"
    icon = "fa-solid fa-paragraph"
    column_list = [Paragraph.title, Paragraph.post, Paragraph.body]
    column_searchable_list = [Paragraph.title, Paragraph.post]
    column_sortable_list = [Paragraph.title]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID", title="Заголовок", body="Содержание", post_id="ID поста", post="Пост")


class FAQAdmin(ModelView, model=FAQ):
    name = "Часто задаваемый вопрос"
    name_plural = "Часто задаваемые вопросы"
    icon = "fa-solid fa-question"
    column_list = [FAQ.heading, FAQ.label, FAQ.date, FAQ.key_word, FAQ.page_tag]
    column_searchable_list = [FAQ.heading]
    column_sortable_list = [FAQ.heading, FAQ.label, FAQ.date, FAQ.key_word, FAQ.page_tag]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID", title="Вопрос", label="Ответ", heading="Заголовок", date="Дата",
                         key_word="Ключевое слово (тег)", page_tag="Тег страницы")


class ProjectTypeAdmin(ModelView, model=ProjectType):
    name = "Тип проекта"
    name_plural = "Типы проектов"
    icon = "fa-solid fa-building"
    column_list = [ProjectType.name]
    column_searchable_list = [ProjectType.name]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(name="Название", works="Работы", works_id="ID работы", id="ID")


class UserCommentsAdmin(ModelView, model=UserComments):
    name = "Комментарии пользователей"
    name_plural = "Комментарии пользователей"
    icon = "fa-solid fa-comments"
    column_list = [UserComments.id, UserComments.image]
    column_sortable_list = [UserComments.id]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID фото", image="Фото")

    form_overrides = {
        'image': FileField
    }

    column_formatters_detail = {
        'image': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image}" width="100" />') if m.image else 'Вложение отсутствует',
    }

    column_formatters = {
        'image': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.image}" width="100" />') if m.image else 'Вложение отсутствует',
    }

    async def on_model_change(self, data, model, is_created, request):
        if 'image' in data:
            file = data['image']
            content = await file.read()
            image = base64.b64encode(content).decode('utf-8') if content else None
            data['image'] = image

        user_comment_data = schemas.UserCommentsSchema(
            image=data.get('image')
        )
        for db_session in get_db():
            await create_user_comment(db_session, user_comment_data)


class IntroVideoAdmin(ModelView, model=IntroVideos):
    name = "Видео приветствия"
    name_plural = "Видео приветствия"
    icon = "fa-solid fa-video"
    column_list = [IntroVideos.id, IntroVideos.video_link, IntroVideos.video_duration, IntroVideos.author,
                   IntroVideos.object]
    column_searchable_list = [IntroVideos.video_link, IntroVideos.author, IntroVideos.object]
    column_sortable_list = [IntroVideos.id, IntroVideos.video_link, IntroVideos.author, IntroVideos.object]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID", video_link="Ссылка на видео", video_duration="Длительность видео", author="Автор",
                         object="Объект")

    async def on_model_change(self, data, model, is_created, request):
        intro_video_data = schemas.IntroVideosSchema(
            video_link=data.get('video_link'),
            video_duration=data.get('video_duration'),
            author=data.get('author'),
            object=data.get('object')
        )
        for db_session in get_db():
            await create_intro_video(intro_video_data, db_session)


class SocialMediaAccountsAdmin(ModelView, model=SocialMediaAccounts):
    name = "Аккаунты социальных сетей"
    name_plural = "Аккаунты социальных сетей"
    icon = "fa-solid fa-users"
    column_list = [SocialMediaAccounts.id, SocialMediaAccounts.name, SocialMediaAccounts.link, SocialMediaAccounts.logo,
                   SocialMediaAccounts.subscribers]
    column_searchable_list = [SocialMediaAccounts.name, SocialMediaAccounts.link]
    column_sortable_list = [SocialMediaAccounts.id, SocialMediaAccounts.name, SocialMediaAccounts.link]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID", name="Название", link="Ссылка")

    form_overrides = {
        'logo': FileField
    }

    column_formatters_detail = {
        'logo': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.logo}" width="100" />') if m.logo else 'Вложение отсутствует',
    }

    column_formatters = {
        'logo': lambda m, p: Markup(
            f'<img src="data:image/png;base64,{m.logo}" width="100" />') if m.logo else 'Вложение отсутствует',
    }

    async def on_model_change(self, data, model, is_created, request):
        if 'logo' in data:
            file = data['logo']
            content = await file.read()
            image = base64.b64encode(content).decode('utf-8') if content else None
            data['logo'] = image

        social_media_data = schemas.SocialMediaAccountsSchema(
            name=data.get('name'),
            link=data.get('link'),
            logo=data.get('logo'),
            subscribers=data.get('subscribers')
        )
        for db_session in get_db():
            await create_social_media_account(db_session, social_media_data)


class BlogVideosAdmin(ModelView, model=BlogVideos):
    name = "Видео блог"
    name_plural = "Видео блог"
    icon = "fa-solid fa-video"
    column_list = [BlogVideos.id, BlogVideos.video_link, BlogVideos.video_duration, BlogVideos.author,
                   BlogVideos.object]
    column_searchable_list = [BlogVideos.video_link, BlogVideos.author, BlogVideos.object]
    column_sortable_list = [BlogVideos.id, BlogVideos.video_link, BlogVideos.author, BlogVideos.object]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID", video_link="Ссылка на видео", video_duration="Длительность видео", author="Автор",
                         object="Объект")

    async def on_model_change(self, data, model, is_created, request):
        blog_video_data = schemas.BlogVideosSchema(
            video_link=data.get('video_link'),
            video_duration=data.get('video_duration'),
            author=data.get('author'),
            object=data.get('object')
        )
        for db_session in get_db():
            await create_blog_video(blog_video_data, db_session)


class PagesAdmin(ModelView, model=PageType):
    name = "Страницы"
    name_plural = "Страницы"
    icon = "fa-solid fa-file"
    column_list = [PageType.id, PageType.name]
    column_searchable_list = [PageType.name]
    column_sortable_list = [PageType.id, PageType.name]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID", name="Заголовок")

    async def on_model_change(self, data, model, is_created, request):
        page_data = schemas.PageTypeSchema(
            name=data.get('name')
        )
        for db_session in get_db():
            await create_page_type(db_session, page_data)


class SEOTextAdmin(ModelView, model=SEOText):
    name = "SEO текст"
    name_plural = "SEO текст"
    icon = "fa-solid fa-file"
    column_list = [SEOText.id, SEOText.text, SEOText.page_tag]
    column_searchable_list = [SEOText.text, SEOText.page_tag]
    column_sortable_list = [SEOText.id, SEOText.text, SEOText.page_tag]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID", text="Текст", page_tag="Тег страницы")


class CommunicationTypeAdmin(ModelView, model=CommunicationType):
    name = "Тип коммуникации"
    name_plural = "Типы коммуникации"
    icon = "fa-solid fa-phone"
    column_list = [CommunicationType.title]
    column_searchable_list = [CommunicationType.title]
    column_sortable_list = [CommunicationType.id, CommunicationType.title]
    can_create = True
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID", title="Название")


class ConsultationListAdmin(ModelView, model=ConsultationList):
    name = "Список консультаций"
    name_plural = "Список консультаций"
    icon = "fa-solid fa-list"
    column_list = [ConsultationList.id, ConsultationList.phone, ConsultationList.communication_type,
                   ConsultationList.answered]
    column_searchable_list = [ConsultationList.phone]
    column_sortable_list = [ConsultationList.id, ConsultationList.answered, ConsultationList.communication_type]
    can_create = False
    can_edit = True
    can_delete = True
    column_labels = dict(id="ID", communication_type="Тип коммуникации", phone="Телефон", answered="Отвечено")

    column_formatters = {
        'answered': lambda m, p: "Да" if m.answered else "Нет"
    }

    column_formatters_detail = {
        'answered': lambda m, p: "Да" if m.answered else "Нет"
    }