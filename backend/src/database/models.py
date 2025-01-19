from sqlalchemy import create_engine, Column, Integer, String, Enum, ARRAY, ForeignKey, Boolean, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
from typing import Any, List
import random
import string
import enum
from dotenv import load_dotenv
import os
from sqlalchemy import JSON

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt", "argon2", "pbkdf2_sha256"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


class ProjectType(Base):
    __tablename__ = 'project_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    portfolio_posts = relationship("PortfolioPost", back_populates="project_type")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class UserType(Base):
    __tablename__ = 'user_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship("User", back_populates="user_type")

    def __str__(self):
        return self.name


class NotificationType(Base):
    __tablename__ = 'notification_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship("User", back_populates="notification_status")

    def __str__(self):
        return self.name


class PageType(Base):
    __tablename__ = 'page_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    faqs = relationship("FAQ", back_populates="page_tag")
    seo_texts = relationship("SEOText", back_populates="page_tag")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Work(Base):
    __tablename__ = 'works'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    # project_type_id = Column(Integer, ForeignKey('project_type.id'))
    # project_type = relationship("ProjectType", back_populates="works")
    deadline = Column(String)
    cost = Column(Integer)
    square = Column(Integer)
    task = Column(String)
    description = Column(ARRAY(String))
    preview_image = Column(String)
    main_image = Column(String)
    result_image = Column(String)
    result_video = Column(String)
    client_video = Column(String)

    def __str__(self):
        return self.title


# класс Параграф DONE
# title = str
# body = str
class Paragraph(Base):
    __tablename__ = 'paragraphs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship("Post", back_populates="paragraphs")

    def __str__(self):
        return self.title


class PostType(enum.Enum):
    news = "Новость"
    blog = "Блог"

    def __str__(self):
        return self.value


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    post_type = Column(Enum(PostType))
    paragraphs = relationship("Paragraph", back_populates="post")
    images = Column(ARRAY(String))

    def __str__(self):
        return self.title


class FAQ(Base):
    __tablename__ = 'faqs'
    id = Column(Integer, primary_key=True, index=True)
    heading = Column(String, index=True)
    label = Column(String)
    date = Column(String, nullable=True)
    key_word = Column(String)
    page_tag_id = Column(Integer, ForeignKey('page_type.id'))
    page_tag = relationship("PageType", back_populates="faqs")

    def __str__(self):
        return self.heading


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String)
    surname = Column(String)
    # patronymic = str DONE
    patronymic = Column(String)
    phone = Column(String)
    user_type_id = Column(Integer, ForeignKey('user_type.id'))
    user_type = relationship("UserType", back_populates="users")
    user_referral_code = Column(String, unique=True, default=lambda: ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=16)))
    others_referral_code = Column(String)
    notification_status_id = Column(Integer, ForeignKey('notification_type.id'))
    notification_status = relationship("NotificationType", back_populates="users")
    is_verified = Column(Boolean, default=False)  # rename to is_verified (по пасспорту) DONE
    is_superuser = Column(Boolean, default=False)
    contracts = relationship("Contract", back_populates="client")
    notifications = relationship("Notification", back_populates="user")
    avatar = Column(String)

    # avatar = bytea (image) DONE

    def __str__(self):
        return self.email


class TariffType(enum.Enum):
    base = 'Базовый'
    standard = 'Стандартный'
    comfort = 'Комфорт'
    business = 'Бизнес'

    def __str__(self):
        return self.value


class OrderType(enum.Enum):
    renovation = 'Ремонт'
    building = 'Строительство'

    def __str__(self):
        return self.value


# class WorkStatus:
# id = int
# title = str
# document = ??? (документ)
# status = bool
class WorkStatus(Base):
    __tablename__ = 'work_status'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    document = Column(LargeBinary)
    status = Column(Boolean, default=False)
    contract_id = Column(Integer, ForeignKey('contracts.id'))
    contract = relationship("Contract", back_populates="work_statuses")

    def __str__(self):
        return self.title


class ContractNotificationStatus(enum.Enum):
    sign_act = 'Подписать акт'
    message = 'Сообщение'

    def __str__(self):
        return self.name


class Contract(Base):
    __tablename__ = "contracts"
    id = Column(Integer, primary_key=True, index=True)
    object = Column(String)
    order_type = Column(Enum(OrderType))
    tariff_type = Column(Enum(TariffType))
    square = Column(Integer)
    location = Column(String)
    current_stage = Column(String)
    total_cost = Column(Integer)
    materials_cost = Column(Integer)
    work_cost = Column(Integer)
    revenue = Column(Integer)
    client_id = Column(Integer, ForeignKey("users.id"))
    client = relationship("User", back_populates="contracts")
    work_statuses = relationship("WorkStatus", back_populates="contract")
    date = Column(String)
    notifications = relationship("Notification", back_populates="contract")
    document = Column(LargeBinary)

    def __str__(self):
        return self.object


class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    notification_status = Column(Enum(ContractNotificationStatus), default=ContractNotificationStatus.message)
    title = Column(String)
    date = Column(String)
    label = Column(String)
    attachment = Column(LargeBinary)
    contract_id = Column(Integer, ForeignKey("contracts.id"))
    contract = relationship("Contract", back_populates="notifications")
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="notifications")

    def __str__(self):
        return f'{self.title}'


# class PlatformNews (profile notifications):
# id = int
# title = str
# date = str
# label = str
class PlatformNews(Base):
    __tablename__ = 'platform_news'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    date = Column(String)
    label = Column(String)

    def __str__(self):
        return self.title


class Flat(Base):
    __tablename__ = 'flats'
    id = Column(Integer, primary_key=True, index=True)
    square = Column(Integer)
    address = Column(String)
    number_of_rooms = Column(Integer)
    number_of_doors = Column(Integer)
    number_of_wc = Column(Integer)
    demolition = Column(Boolean, default=False)
    wall_build = Column(Boolean, default=False)
    liquid_floor = Column(Boolean, default=False)
    ceiling_stretching = Column(Boolean, default=False)
    tariff_id = Column(Integer, ForeignKey('tariffs.id'))
    style_id = Column(Integer, ForeignKey('styles.id'))
    additional_options = relationship('AdditionalOption', secondary='flat_additional_options')


class Tariff(Base):
    __tablename__ = 'tariffs'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    cost = Column(String)
    image = Column(String)


class Style(Base):
    __tablename__ = 'styles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)


class AdditionalOption(Base):
    __tablename__ = 'additional_options'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)


class FlatAdditionalOption(Base):
    __tablename__ = 'flat_additional_options'
    flat_id = Column(Integer, ForeignKey('flats.id'), primary_key=True)
    additional_option_id = Column(Integer, ForeignKey('additional_options.id'), primary_key=True)


class UserComments(Base):
    __tablename__ = 'user_comments'
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)


class IntroVideos(Base):
    __tablename__ = 'intro_videos'
    id = Column(Integer, primary_key=True, index=True)
    video = Column(String)
    video_duration = Column(String)
    author = Column(String)
    object = Column(String)


class SocialMediaAccounts(Base):
    __tablename__ = 'social_media_accounts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    logo = Column(String)
    link = Column(String)
    subscribers = Column(Integer)


class BlogVideos(Base):
    __tablename__ = 'blog_videos'
    id = Column(Integer, primary_key=True, index=True)
    video_link = Column(String)
    video_duration = Column(String, nullable=True)
    author = Column(String, nullable=True)
    object = Column(String, nullable=True)


class SEOText(Base):
    __tablename__ = 'seo_texts'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    page_tag_id = Column(Integer, ForeignKey('page_type.id'))
    page_tag = relationship("PageType", back_populates="seo_texts")


class CommunicationType(Base):
    __tablename__ = 'communication_type'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    consultation_list = relationship("ConsultationList", back_populates="communication_type")

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class ConsultationList(Base):
    __tablename__ = 'consultation_list'
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String)
    answered = Column(Boolean, default=False)
    communication_type_id = Column(Integer, ForeignKey('communication_type.id'))
    communication_type = relationship("CommunicationType", back_populates="consultation_list")


class BlogParagraph(Base):
    __tablename__ = 'blog_paragraphs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    items = Column(ARRAY(String), nullable=True)
    blog_block_id = Column(Integer, ForeignKey('blog_blocks.id'), nullable=True)
    blog_block = relationship("BlogBlock", back_populates="paragraphs")

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class BlogBlock(Base):
    __tablename__ = 'blog_blocks'
    id = Column(Integer, primary_key=True, index=True)
    images = Column(ARRAY(String), nullable=True)
    blog_id = Column(Integer, ForeignKey('blogs.id'), nullable=True)
    blog = relationship("Blog", back_populates="blog_blocks")
    paragraphs = relationship("BlogParagraph", uselist=False, back_populates="blog_block")

    def __str__(self):
        return "Блок " + str(self.id)

    def __repr__(self):
        return "Блок " + str(self.id)


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    img_main = Column(String)
    text_main = Column(String)
    blog_blocks = relationship("BlogBlock", back_populates="blog")

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class PortfolioPostVideo(Base):
    __tablename__ = 'portfolio_post_videos'
    id = Column(Integer, primary_key=True, index=True)
    duration = Column(String)
    link = Column(String)
    portfolio_post_id = Column(Integer, ForeignKey('portfolio_posts.id'))
    portfolio_post = relationship("PortfolioPost", back_populates="overview", overlaps="others,portfolio_post_others")
    portfolio_post_others = relationship("PortfolioPost", back_populates="others", overlaps="overview,portfolio_post")

    def __str__(self):
        return "Видео " + str(self.id)

    def __repr__(self):
        return "Видео " + str(self.id)


class PortfolioPost(Base):
    __tablename__ = 'portfolio_posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    img_main = Column(String)
    img_result = Column(String)
    price_amount = Column(String)
    object_area = Column(String)
    work_completion_time = Column(String)
    project_type_id = Column(Integer, ForeignKey('project_type.id'))
    project_type = relationship("ProjectType", back_populates="portfolio_posts")
    task = Column(String, nullable=True)
    steps_of_work = Column(ARRAY(String), nullable=True)
    images = Column(ARRAY(String), nullable=True)
    overview = relationship("PortfolioPostVideo", back_populates="portfolio_post", uselist=False,
                            overlaps="others,portfolio_post_others")
    others = relationship("PortfolioPostVideo", back_populates="portfolio_post_others",
                          overlaps="overview,portfolio_post")

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
