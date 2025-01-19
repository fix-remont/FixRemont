--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: contractnotificationstatus; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.contractnotificationstatus AS ENUM (
    'sign_act',
    'message'
);


ALTER TYPE public.contractnotificationstatus OWNER TO postgres;

--
-- Name: ordertype; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.ordertype AS ENUM (
    'renovation',
    'building'
);


ALTER TYPE public.ordertype OWNER TO postgres;

--
-- Name: posttype; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.posttype AS ENUM (
    'news',
    'blog'
);


ALTER TYPE public.posttype OWNER TO postgres;

--
-- Name: tarifftype; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.tarifftype AS ENUM (
    'base',
    'standard',
    'comfort',
    'business'
);


ALTER TYPE public.tarifftype OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: additional_options; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.additional_options (
    id integer NOT NULL,
    name character varying,
    description character varying
);


ALTER TABLE public.additional_options OWNER TO postgres;

--
-- Name: additional_options_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.additional_options_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.additional_options_id_seq OWNER TO postgres;

--
-- Name: additional_options_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.additional_options_id_seq OWNED BY public.additional_options.id;


--
-- Name: blog_blocks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.blog_blocks (
    id integer NOT NULL,
    images character varying[],
    blog_id integer
);


ALTER TABLE public.blog_blocks OWNER TO postgres;

--
-- Name: blog_blocks_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.blog_blocks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.blog_blocks_id_seq OWNER TO postgres;

--
-- Name: blog_blocks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.blog_blocks_id_seq OWNED BY public.blog_blocks.id;


--
-- Name: blog_paragraphs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.blog_paragraphs (
    id integer NOT NULL,
    title character varying,
    items character varying[],
    blog_block_id integer
);


ALTER TABLE public.blog_paragraphs OWNER TO postgres;

--
-- Name: blog_paragraphs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.blog_paragraphs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.blog_paragraphs_id_seq OWNER TO postgres;

--
-- Name: blog_paragraphs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.blog_paragraphs_id_seq OWNED BY public.blog_paragraphs.id;


--
-- Name: blog_videos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.blog_videos (
    id integer NOT NULL,
    video_link character varying,
    video_duration character varying,
    author character varying,
    object character varying
);


ALTER TABLE public.blog_videos OWNER TO postgres;

--
-- Name: blog_videos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.blog_videos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.blog_videos_id_seq OWNER TO postgres;

--
-- Name: blog_videos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.blog_videos_id_seq OWNED BY public.blog_videos.id;


--
-- Name: blogs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.blogs (
    id integer NOT NULL,
    title character varying,
    img_main character varying,
    text_main character varying
);


ALTER TABLE public.blogs OWNER TO postgres;

--
-- Name: blogs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.blogs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.blogs_id_seq OWNER TO postgres;

--
-- Name: blogs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.blogs_id_seq OWNED BY public.blogs.id;


--
-- Name: communication_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.communication_type (
    id integer NOT NULL,
    title character varying
);


ALTER TABLE public.communication_type OWNER TO postgres;

--
-- Name: communication_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.communication_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.communication_type_id_seq OWNER TO postgres;

--
-- Name: communication_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.communication_type_id_seq OWNED BY public.communication_type.id;


--
-- Name: consultation_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.consultation_list (
    id integer NOT NULL,
    phone character varying,
    answered boolean,
    communication_type_id integer
);


ALTER TABLE public.consultation_list OWNER TO postgres;

--
-- Name: consultation_list_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.consultation_list_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.consultation_list_id_seq OWNER TO postgres;

--
-- Name: consultation_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.consultation_list_id_seq OWNED BY public.consultation_list.id;


--
-- Name: contracts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contracts (
    id integer NOT NULL,
    object character varying,
    order_type public.ordertype,
    tariff_type public.tarifftype,
    square integer,
    location character varying,
    current_stage character varying,
    total_cost integer,
    materials_cost integer,
    work_cost integer,
    revenue integer,
    client_id integer,
    date character varying,
    document bytea
);


ALTER TABLE public.contracts OWNER TO postgres;

--
-- Name: contracts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contracts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.contracts_id_seq OWNER TO postgres;

--
-- Name: contracts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contracts_id_seq OWNED BY public.contracts.id;


--
-- Name: faqs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faqs (
    id integer NOT NULL,
    heading character varying,
    label character varying,
    date character varying,
    key_word character varying,
    page_tag_id integer
);


ALTER TABLE public.faqs OWNER TO postgres;

--
-- Name: faqs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.faqs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.faqs_id_seq OWNER TO postgres;

--
-- Name: faqs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.faqs_id_seq OWNED BY public.faqs.id;


--
-- Name: flat_additional_options; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.flat_additional_options (
    flat_id integer NOT NULL,
    additional_option_id integer NOT NULL
);


ALTER TABLE public.flat_additional_options OWNER TO postgres;

--
-- Name: flats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.flats (
    id integer NOT NULL,
    square integer,
    address character varying,
    number_of_rooms integer,
    number_of_doors integer,
    number_of_wc integer,
    demolition boolean,
    wall_build boolean,
    liquid_floor boolean,
    ceiling_stretching boolean,
    tariff_id integer,
    style_id integer
);


ALTER TABLE public.flats OWNER TO postgres;

--
-- Name: flats_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.flats_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.flats_id_seq OWNER TO postgres;

--
-- Name: flats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.flats_id_seq OWNED BY public.flats.id;


--
-- Name: intro_videos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.intro_videos (
    id integer NOT NULL,
    video character varying,
    video_duration character varying,
    author character varying,
    object character varying
);


ALTER TABLE public.intro_videos OWNER TO postgres;

--
-- Name: intro_videos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.intro_videos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.intro_videos_id_seq OWNER TO postgres;

--
-- Name: intro_videos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.intro_videos_id_seq OWNED BY public.intro_videos.id;


--
-- Name: notification_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notification_type (
    id integer NOT NULL,
    name character varying
);


ALTER TABLE public.notification_type OWNER TO postgres;

--
-- Name: notification_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.notification_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.notification_type_id_seq OWNER TO postgres;

--
-- Name: notification_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.notification_type_id_seq OWNED BY public.notification_type.id;


--
-- Name: notifications; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notifications (
    id integer NOT NULL,
    notification_status public.contractnotificationstatus,
    title character varying,
    date character varying,
    label character varying,
    attachment bytea,
    contract_id integer,
    user_id integer
);


ALTER TABLE public.notifications OWNER TO postgres;

--
-- Name: notifications_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.notifications_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.notifications_id_seq OWNER TO postgres;

--
-- Name: notifications_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.notifications_id_seq OWNED BY public.notifications.id;


--
-- Name: page_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.page_type (
    id integer NOT NULL,
    name character varying
);


ALTER TABLE public.page_type OWNER TO postgres;

--
-- Name: page_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.page_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.page_type_id_seq OWNER TO postgres;

--
-- Name: page_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.page_type_id_seq OWNED BY public.page_type.id;


--
-- Name: paragraphs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.paragraphs (
    id integer NOT NULL,
    title character varying,
    body character varying,
    post_id integer
);


ALTER TABLE public.paragraphs OWNER TO postgres;

--
-- Name: paragraphs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.paragraphs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.paragraphs_id_seq OWNER TO postgres;

--
-- Name: paragraphs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.paragraphs_id_seq OWNED BY public.paragraphs.id;


--
-- Name: platform_news; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.platform_news (
    id integer NOT NULL,
    title character varying,
    date character varying,
    label character varying
);


ALTER TABLE public.platform_news OWNER TO postgres;

--
-- Name: platform_news_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.platform_news_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.platform_news_id_seq OWNER TO postgres;

--
-- Name: platform_news_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.platform_news_id_seq OWNED BY public.platform_news.id;


--
-- Name: portfolio_post_videos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.portfolio_post_videos (
    id integer NOT NULL,
    duration character varying,
    link character varying,
    portfolio_post_id integer
);


ALTER TABLE public.portfolio_post_videos OWNER TO postgres;

--
-- Name: portfolio_post_videos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.portfolio_post_videos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.portfolio_post_videos_id_seq OWNER TO postgres;

--
-- Name: portfolio_post_videos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.portfolio_post_videos_id_seq OWNED BY public.portfolio_post_videos.id;


--
-- Name: portfolio_posts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.portfolio_posts (
    id integer NOT NULL,
    title character varying,
    img_main character varying,
    img_result character varying,
    price_amount character varying,
    object_area character varying,
    work_completion_time character varying,
    project_type_id integer,
    task character varying,
    steps_of_work character varying[],
    images character varying[]
);


ALTER TABLE public.portfolio_posts OWNER TO postgres;

--
-- Name: portfolio_posts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.portfolio_posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.portfolio_posts_id_seq OWNER TO postgres;

--
-- Name: portfolio_posts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.portfolio_posts_id_seq OWNED BY public.portfolio_posts.id;


--
-- Name: posts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    title character varying,
    post_type public.posttype,
    images character varying[]
);


ALTER TABLE public.posts OWNER TO postgres;

--
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.posts_id_seq OWNER TO postgres;

--
-- Name: posts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.posts_id_seq OWNED BY public.posts.id;


--
-- Name: project_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.project_type (
    id integer NOT NULL,
    name character varying
);


ALTER TABLE public.project_type OWNER TO postgres;

--
-- Name: project_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.project_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.project_type_id_seq OWNER TO postgres;

--
-- Name: project_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.project_type_id_seq OWNED BY public.project_type.id;


--
-- Name: seo_texts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.seo_texts (
    id integer NOT NULL,
    text character varying,
    page_tag_id integer
);


ALTER TABLE public.seo_texts OWNER TO postgres;

--
-- Name: seo_texts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.seo_texts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.seo_texts_id_seq OWNER TO postgres;

--
-- Name: seo_texts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.seo_texts_id_seq OWNED BY public.seo_texts.id;


--
-- Name: social_media_accounts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.social_media_accounts (
    id integer NOT NULL,
    name character varying,
    logo character varying,
    link character varying,
    subscribers integer
);


ALTER TABLE public.social_media_accounts OWNER TO postgres;

--
-- Name: social_media_accounts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.social_media_accounts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.social_media_accounts_id_seq OWNER TO postgres;

--
-- Name: social_media_accounts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.social_media_accounts_id_seq OWNED BY public.social_media_accounts.id;


--
-- Name: styles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.styles (
    id integer NOT NULL,
    name character varying,
    description character varying
);


ALTER TABLE public.styles OWNER TO postgres;

--
-- Name: styles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.styles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.styles_id_seq OWNER TO postgres;

--
-- Name: styles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.styles_id_seq OWNED BY public.styles.id;


--
-- Name: tariffs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tariffs (
    id integer NOT NULL,
    name character varying,
    description character varying,
    cost character varying,
    image character varying
);


ALTER TABLE public.tariffs OWNER TO postgres;

--
-- Name: tariffs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tariffs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tariffs_id_seq OWNER TO postgres;

--
-- Name: tariffs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tariffs_id_seq OWNED BY public.tariffs.id;


--
-- Name: user_comments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_comments (
    id integer NOT NULL,
    image character varying
);


ALTER TABLE public.user_comments OWNER TO postgres;

--
-- Name: user_comments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_comments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_comments_id_seq OWNER TO postgres;

--
-- Name: user_comments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_comments_id_seq OWNED BY public.user_comments.id;


--
-- Name: user_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_type (
    id integer NOT NULL,
    name character varying
);


ALTER TABLE public.user_type OWNER TO postgres;

--
-- Name: user_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_type_id_seq OWNER TO postgres;

--
-- Name: user_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_type_id_seq OWNED BY public.user_type.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying,
    hashed_password character varying,
    name character varying,
    surname character varying,
    patronymic character varying,
    phone character varying,
    user_type_id integer,
    user_referral_code character varying,
    others_referral_code character varying,
    notification_status_id integer,
    is_verified boolean,
    is_superuser boolean,
    avatar character varying
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: work_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.work_status (
    id integer NOT NULL,
    title character varying,
    document bytea,
    status boolean,
    contract_id integer
);


ALTER TABLE public.work_status OWNER TO postgres;

--
-- Name: work_status_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.work_status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.work_status_id_seq OWNER TO postgres;

--
-- Name: work_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.work_status_id_seq OWNED BY public.work_status.id;


--
-- Name: works; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.works (
    id integer NOT NULL,
    title character varying,
    deadline character varying,
    cost integer,
    square integer,
    task character varying,
    description character varying[],
    preview_image character varying,
    main_image character varying,
    result_image character varying,
    result_video character varying,
    client_video character varying
);


ALTER TABLE public.works OWNER TO postgres;

--
-- Name: works_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.works_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.works_id_seq OWNER TO postgres;

--
-- Name: works_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.works_id_seq OWNED BY public.works.id;


--
-- Name: additional_options id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.additional_options ALTER COLUMN id SET DEFAULT nextval('public.additional_options_id_seq'::regclass);


--
-- Name: blog_blocks id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_blocks ALTER COLUMN id SET DEFAULT nextval('public.blog_blocks_id_seq'::regclass);


--
-- Name: blog_paragraphs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_paragraphs ALTER COLUMN id SET DEFAULT nextval('public.blog_paragraphs_id_seq'::regclass);


--
-- Name: blog_videos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_videos ALTER COLUMN id SET DEFAULT nextval('public.blog_videos_id_seq'::regclass);


--
-- Name: blogs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blogs ALTER COLUMN id SET DEFAULT nextval('public.blogs_id_seq'::regclass);


--
-- Name: communication_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.communication_type ALTER COLUMN id SET DEFAULT nextval('public.communication_type_id_seq'::regclass);


--
-- Name: consultation_list id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.consultation_list ALTER COLUMN id SET DEFAULT nextval('public.consultation_list_id_seq'::regclass);


--
-- Name: contracts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contracts ALTER COLUMN id SET DEFAULT nextval('public.contracts_id_seq'::regclass);


--
-- Name: faqs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faqs ALTER COLUMN id SET DEFAULT nextval('public.faqs_id_seq'::regclass);


--
-- Name: flats id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flats ALTER COLUMN id SET DEFAULT nextval('public.flats_id_seq'::regclass);


--
-- Name: intro_videos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.intro_videos ALTER COLUMN id SET DEFAULT nextval('public.intro_videos_id_seq'::regclass);


--
-- Name: notification_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notification_type ALTER COLUMN id SET DEFAULT nextval('public.notification_type_id_seq'::regclass);


--
-- Name: notifications id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications ALTER COLUMN id SET DEFAULT nextval('public.notifications_id_seq'::regclass);


--
-- Name: page_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.page_type ALTER COLUMN id SET DEFAULT nextval('public.page_type_id_seq'::regclass);


--
-- Name: paragraphs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paragraphs ALTER COLUMN id SET DEFAULT nextval('public.paragraphs_id_seq'::regclass);


--
-- Name: platform_news id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platform_news ALTER COLUMN id SET DEFAULT nextval('public.platform_news_id_seq'::regclass);


--
-- Name: portfolio_post_videos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.portfolio_post_videos ALTER COLUMN id SET DEFAULT nextval('public.portfolio_post_videos_id_seq'::regclass);


--
-- Name: portfolio_posts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.portfolio_posts ALTER COLUMN id SET DEFAULT nextval('public.portfolio_posts_id_seq'::regclass);


--
-- Name: posts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts ALTER COLUMN id SET DEFAULT nextval('public.posts_id_seq'::regclass);


--
-- Name: project_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_type ALTER COLUMN id SET DEFAULT nextval('public.project_type_id_seq'::regclass);


--
-- Name: seo_texts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.seo_texts ALTER COLUMN id SET DEFAULT nextval('public.seo_texts_id_seq'::regclass);


--
-- Name: social_media_accounts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.social_media_accounts ALTER COLUMN id SET DEFAULT nextval('public.social_media_accounts_id_seq'::regclass);


--
-- Name: styles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.styles ALTER COLUMN id SET DEFAULT nextval('public.styles_id_seq'::regclass);


--
-- Name: tariffs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tariffs ALTER COLUMN id SET DEFAULT nextval('public.tariffs_id_seq'::regclass);


--
-- Name: user_comments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_comments ALTER COLUMN id SET DEFAULT nextval('public.user_comments_id_seq'::regclass);


--
-- Name: user_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_type ALTER COLUMN id SET DEFAULT nextval('public.user_type_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: work_status id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.work_status ALTER COLUMN id SET DEFAULT nextval('public.work_status_id_seq'::regclass);


--
-- Name: works id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.works ALTER COLUMN id SET DEFAULT nextval('public.works_id_seq'::regclass);


--
-- Data for Name: additional_options; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.additional_options (id, name, description) FROM stdin;
\.


--
-- Data for Name: blog_blocks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.blog_blocks (id, images, blog_id) FROM stdin;
\.


--
-- Data for Name: blog_paragraphs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.blog_paragraphs (id, title, items, blog_block_id) FROM stdin;
\.


--
-- Data for Name: blog_videos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.blog_videos (id, video_link, video_duration, author, object) FROM stdin;
\.


--
-- Data for Name: blogs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.blogs (id, title, img_main, text_main) FROM stdin;
\.


--
-- Data for Name: communication_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.communication_type (id, title) FROM stdin;
\.


--
-- Data for Name: consultation_list; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.consultation_list (id, phone, answered, communication_type_id) FROM stdin;
\.


--
-- Data for Name: contracts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contracts (id, object, order_type, tariff_type, square, location, current_stage, total_cost, materials_cost, work_cost, revenue, client_id, date, document) FROM stdin;
\.


--
-- Data for Name: faqs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.faqs (id, heading, label, date, key_word, page_tag_id) FROM stdin;
\.


--
-- Data for Name: flat_additional_options; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.flat_additional_options (flat_id, additional_option_id) FROM stdin;
\.


--
-- Data for Name: flats; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.flats (id, square, address, number_of_rooms, number_of_doors, number_of_wc, demolition, wall_build, liquid_floor, ceiling_stretching, tariff_id, style_id) FROM stdin;
\.


--
-- Data for Name: intro_videos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.intro_videos (id, video, video_duration, author, object) FROM stdin;
\.


--
-- Data for Name: notification_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notification_type (id, name) FROM stdin;
\.


--
-- Data for Name: notifications; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notifications (id, notification_status, title, date, label, attachment, contract_id, user_id) FROM stdin;
\.


--
-- Data for Name: page_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.page_type (id, name) FROM stdin;
\.


--
-- Data for Name: paragraphs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.paragraphs (id, title, body, post_id) FROM stdin;
\.


--
-- Data for Name: platform_news; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.platform_news (id, title, date, label) FROM stdin;
\.


--
-- Data for Name: portfolio_post_videos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.portfolio_post_videos (id, duration, link, portfolio_post_id) FROM stdin;
\.


--
-- Data for Name: portfolio_posts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.portfolio_posts (id, title, img_main, img_result, price_amount, object_area, work_completion_time, project_type_id, task, steps_of_work, images) FROM stdin;
\.


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.posts (id, title, post_type, images) FROM stdin;
\.


--
-- Data for Name: project_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.project_type (id, name) FROM stdin;
\.


--
-- Data for Name: seo_texts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.seo_texts (id, text, page_tag_id) FROM stdin;
\.


--
-- Data for Name: social_media_accounts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.social_media_accounts (id, name, logo, link, subscribers) FROM stdin;
\.


--
-- Data for Name: styles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.styles (id, name, description) FROM stdin;
\.


--
-- Data for Name: tariffs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tariffs (id, name, description, cost, image) FROM stdin;
\.


--
-- Data for Name: user_comments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_comments (id, image) FROM stdin;
\.


--
-- Data for Name: user_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_type (id, name) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, email, hashed_password, name, surname, patronymic, phone, user_type_id, user_referral_code, others_referral_code, notification_status_id, is_verified, is_superuser, avatar) FROM stdin;
\.


--
-- Data for Name: work_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.work_status (id, title, document, status, contract_id) FROM stdin;
\.


--
-- Data for Name: works; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.works (id, title, deadline, cost, square, task, description, preview_image, main_image, result_image, result_video, client_video) FROM stdin;
\.


--
-- Name: additional_options_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.additional_options_id_seq', 1, false);


--
-- Name: blog_blocks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_blocks_id_seq', 1, false);


--
-- Name: blog_paragraphs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_paragraphs_id_seq', 1, false);


--
-- Name: blog_videos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_videos_id_seq', 1, false);


--
-- Name: blogs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blogs_id_seq', 1, false);


--
-- Name: communication_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.communication_type_id_seq', 1, false);


--
-- Name: consultation_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.consultation_list_id_seq', 1, false);


--
-- Name: contracts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contracts_id_seq', 1, false);


--
-- Name: faqs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.faqs_id_seq', 1, false);


--
-- Name: flats_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.flats_id_seq', 1, false);


--
-- Name: intro_videos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.intro_videos_id_seq', 1, false);


--
-- Name: notification_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.notification_type_id_seq', 1, false);


--
-- Name: notifications_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.notifications_id_seq', 1, false);


--
-- Name: page_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.page_type_id_seq', 1, false);


--
-- Name: paragraphs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.paragraphs_id_seq', 1, false);


--
-- Name: platform_news_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.platform_news_id_seq', 1, false);


--
-- Name: portfolio_post_videos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.portfolio_post_videos_id_seq', 1, false);


--
-- Name: portfolio_posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.portfolio_posts_id_seq', 1, false);


--
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.posts_id_seq', 1, false);


--
-- Name: project_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.project_type_id_seq', 1, false);


--
-- Name: seo_texts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.seo_texts_id_seq', 1, false);


--
-- Name: social_media_accounts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.social_media_accounts_id_seq', 1, false);


--
-- Name: styles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.styles_id_seq', 1, false);


--
-- Name: tariffs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tariffs_id_seq', 1, false);


--
-- Name: user_comments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_comments_id_seq', 1, false);


--
-- Name: user_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_type_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: work_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.work_status_id_seq', 1, false);


--
-- Name: works_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.works_id_seq', 1, false);


--
-- Name: additional_options additional_options_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.additional_options
    ADD CONSTRAINT additional_options_pkey PRIMARY KEY (id);


--
-- Name: blog_blocks blog_blocks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_blocks
    ADD CONSTRAINT blog_blocks_pkey PRIMARY KEY (id);


--
-- Name: blog_paragraphs blog_paragraphs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_paragraphs
    ADD CONSTRAINT blog_paragraphs_pkey PRIMARY KEY (id);


--
-- Name: blog_videos blog_videos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_videos
    ADD CONSTRAINT blog_videos_pkey PRIMARY KEY (id);


--
-- Name: blogs blogs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blogs
    ADD CONSTRAINT blogs_pkey PRIMARY KEY (id);


--
-- Name: communication_type communication_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.communication_type
    ADD CONSTRAINT communication_type_pkey PRIMARY KEY (id);


--
-- Name: consultation_list consultation_list_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.consultation_list
    ADD CONSTRAINT consultation_list_pkey PRIMARY KEY (id);


--
-- Name: contracts contracts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contracts
    ADD CONSTRAINT contracts_pkey PRIMARY KEY (id);


--
-- Name: faqs faqs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faqs
    ADD CONSTRAINT faqs_pkey PRIMARY KEY (id);


--
-- Name: flat_additional_options flat_additional_options_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flat_additional_options
    ADD CONSTRAINT flat_additional_options_pkey PRIMARY KEY (flat_id, additional_option_id);


--
-- Name: flats flats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flats
    ADD CONSTRAINT flats_pkey PRIMARY KEY (id);


--
-- Name: intro_videos intro_videos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.intro_videos
    ADD CONSTRAINT intro_videos_pkey PRIMARY KEY (id);


--
-- Name: notification_type notification_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notification_type
    ADD CONSTRAINT notification_type_pkey PRIMARY KEY (id);


--
-- Name: notifications notifications_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_pkey PRIMARY KEY (id);


--
-- Name: page_type page_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.page_type
    ADD CONSTRAINT page_type_pkey PRIMARY KEY (id);


--
-- Name: paragraphs paragraphs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paragraphs
    ADD CONSTRAINT paragraphs_pkey PRIMARY KEY (id);


--
-- Name: platform_news platform_news_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platform_news
    ADD CONSTRAINT platform_news_pkey PRIMARY KEY (id);


--
-- Name: portfolio_post_videos portfolio_post_videos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.portfolio_post_videos
    ADD CONSTRAINT portfolio_post_videos_pkey PRIMARY KEY (id);


--
-- Name: portfolio_posts portfolio_posts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.portfolio_posts
    ADD CONSTRAINT portfolio_posts_pkey PRIMARY KEY (id);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);


--
-- Name: project_type project_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_type
    ADD CONSTRAINT project_type_pkey PRIMARY KEY (id);


--
-- Name: seo_texts seo_texts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.seo_texts
    ADD CONSTRAINT seo_texts_pkey PRIMARY KEY (id);


--
-- Name: social_media_accounts social_media_accounts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.social_media_accounts
    ADD CONSTRAINT social_media_accounts_pkey PRIMARY KEY (id);


--
-- Name: styles styles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.styles
    ADD CONSTRAINT styles_pkey PRIMARY KEY (id);


--
-- Name: tariffs tariffs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tariffs
    ADD CONSTRAINT tariffs_pkey PRIMARY KEY (id);


--
-- Name: user_comments user_comments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_comments
    ADD CONSTRAINT user_comments_pkey PRIMARY KEY (id);


--
-- Name: user_type user_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_type
    ADD CONSTRAINT user_type_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_user_referral_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_user_referral_code_key UNIQUE (user_referral_code);


--
-- Name: work_status work_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.work_status
    ADD CONSTRAINT work_status_pkey PRIMARY KEY (id);


--
-- Name: works works_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.works
    ADD CONSTRAINT works_pkey PRIMARY KEY (id);


--
-- Name: ix_additional_options_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_additional_options_id ON public.additional_options USING btree (id);


--
-- Name: ix_blog_blocks_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_blog_blocks_id ON public.blog_blocks USING btree (id);


--
-- Name: ix_blog_paragraphs_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_blog_paragraphs_id ON public.blog_paragraphs USING btree (id);


--
-- Name: ix_blog_videos_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_blog_videos_id ON public.blog_videos USING btree (id);


--
-- Name: ix_blogs_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_blogs_id ON public.blogs USING btree (id);


--
-- Name: ix_communication_type_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_communication_type_id ON public.communication_type USING btree (id);


--
-- Name: ix_consultation_list_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_consultation_list_id ON public.consultation_list USING btree (id);


--
-- Name: ix_contracts_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_contracts_id ON public.contracts USING btree (id);


--
-- Name: ix_faqs_heading; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_faqs_heading ON public.faqs USING btree (heading);


--
-- Name: ix_faqs_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_faqs_id ON public.faqs USING btree (id);


--
-- Name: ix_flats_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_flats_id ON public.flats USING btree (id);


--
-- Name: ix_intro_videos_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_intro_videos_id ON public.intro_videos USING btree (id);


--
-- Name: ix_notifications_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_notifications_id ON public.notifications USING btree (id);


--
-- Name: ix_paragraphs_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_paragraphs_id ON public.paragraphs USING btree (id);


--
-- Name: ix_paragraphs_title; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_paragraphs_title ON public.paragraphs USING btree (title);


--
-- Name: ix_platform_news_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_platform_news_id ON public.platform_news USING btree (id);


--
-- Name: ix_platform_news_title; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_platform_news_title ON public.platform_news USING btree (title);


--
-- Name: ix_portfolio_post_videos_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_portfolio_post_videos_id ON public.portfolio_post_videos USING btree (id);


--
-- Name: ix_portfolio_posts_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_portfolio_posts_id ON public.portfolio_posts USING btree (id);


--
-- Name: ix_posts_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_posts_id ON public.posts USING btree (id);


--
-- Name: ix_posts_title; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_posts_title ON public.posts USING btree (title);


--
-- Name: ix_seo_texts_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_seo_texts_id ON public.seo_texts USING btree (id);


--
-- Name: ix_social_media_accounts_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_social_media_accounts_id ON public.social_media_accounts USING btree (id);


--
-- Name: ix_styles_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_styles_id ON public.styles USING btree (id);


--
-- Name: ix_tariffs_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tariffs_id ON public.tariffs USING btree (id);


--
-- Name: ix_user_comments_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_user_comments_id ON public.user_comments USING btree (id);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: ix_users_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_users_id ON public.users USING btree (id);


--
-- Name: ix_work_status_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_work_status_id ON public.work_status USING btree (id);


--
-- Name: ix_work_status_title; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_work_status_title ON public.work_status USING btree (title);


--
-- Name: ix_works_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_works_id ON public.works USING btree (id);


--
-- Name: ix_works_title; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_works_title ON public.works USING btree (title);


--
-- Name: blog_blocks blog_blocks_blog_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_blocks
    ADD CONSTRAINT blog_blocks_blog_id_fkey FOREIGN KEY (blog_id) REFERENCES public.blogs(id);


--
-- Name: blog_paragraphs blog_paragraphs_blog_block_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_paragraphs
    ADD CONSTRAINT blog_paragraphs_blog_block_id_fkey FOREIGN KEY (blog_block_id) REFERENCES public.blog_blocks(id);


--
-- Name: consultation_list consultation_list_communication_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.consultation_list
    ADD CONSTRAINT consultation_list_communication_type_id_fkey FOREIGN KEY (communication_type_id) REFERENCES public.communication_type(id);


--
-- Name: contracts contracts_client_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contracts
    ADD CONSTRAINT contracts_client_id_fkey FOREIGN KEY (client_id) REFERENCES public.users(id);


--
-- Name: faqs faqs_page_tag_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faqs
    ADD CONSTRAINT faqs_page_tag_id_fkey FOREIGN KEY (page_tag_id) REFERENCES public.page_type(id);


--
-- Name: flat_additional_options flat_additional_options_additional_option_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flat_additional_options
    ADD CONSTRAINT flat_additional_options_additional_option_id_fkey FOREIGN KEY (additional_option_id) REFERENCES public.additional_options(id);


--
-- Name: flat_additional_options flat_additional_options_flat_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flat_additional_options
    ADD CONSTRAINT flat_additional_options_flat_id_fkey FOREIGN KEY (flat_id) REFERENCES public.flats(id);


--
-- Name: flats flats_style_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flats
    ADD CONSTRAINT flats_style_id_fkey FOREIGN KEY (style_id) REFERENCES public.styles(id);


--
-- Name: flats flats_tariff_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flats
    ADD CONSTRAINT flats_tariff_id_fkey FOREIGN KEY (tariff_id) REFERENCES public.tariffs(id);


--
-- Name: notifications notifications_contract_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_contract_id_fkey FOREIGN KEY (contract_id) REFERENCES public.contracts(id);


--
-- Name: notifications notifications_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: paragraphs paragraphs_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paragraphs
    ADD CONSTRAINT paragraphs_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- Name: portfolio_post_videos portfolio_post_videos_portfolio_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.portfolio_post_videos
    ADD CONSTRAINT portfolio_post_videos_portfolio_post_id_fkey FOREIGN KEY (portfolio_post_id) REFERENCES public.portfolio_posts(id);


--
-- Name: portfolio_posts portfolio_posts_project_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.portfolio_posts
    ADD CONSTRAINT portfolio_posts_project_type_id_fkey FOREIGN KEY (project_type_id) REFERENCES public.project_type(id);


--
-- Name: seo_texts seo_texts_page_tag_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.seo_texts
    ADD CONSTRAINT seo_texts_page_tag_id_fkey FOREIGN KEY (page_tag_id) REFERENCES public.page_type(id);


--
-- Name: users users_notification_status_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_notification_status_id_fkey FOREIGN KEY (notification_status_id) REFERENCES public.notification_type(id);


--
-- Name: users users_user_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_user_type_id_fkey FOREIGN KEY (user_type_id) REFERENCES public.user_type(id);


--
-- Name: work_status work_status_contract_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.work_status
    ADD CONSTRAINT work_status_contract_id_fkey FOREIGN KEY (contract_id) REFERENCES public.contracts(id);


--
-- PostgreSQL database dump complete
--

