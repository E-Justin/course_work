--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: portfolios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.portfolios (
    id integer NOT NULL,
    profit_amount money,
    net_worth money NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.portfolios OWNER TO postgres;

--
-- Name: portfolio_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.portfolio_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.portfolio_id_seq OWNER TO postgres;

--
-- Name: portfolio_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.portfolio_id_seq OWNED BY public.portfolios.id;


--
-- Name: portfolio_stocks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.portfolio_stocks (
    portfolio_id integer NOT NULL,
    stock_id integer NOT NULL
);


ALTER TABLE public.portfolio_stocks OWNER TO postgres;

--
-- Name: stocks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stocks (
    id integer NOT NULL,
    symbol text NOT NULL,
    profit_amount money,
    percent_change numeric NOT NULL,
    price_change numeric NOT NULL,
    current_price numeric NOT NULL,
    name text NOT NULL,
    quantity integer,
    purchase_price numeric
);


ALTER TABLE public.stocks OWNER TO postgres;

--
-- Name: stocks_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.stocks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stocks_id_seq OWNER TO postgres;

--
-- Name: stocks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.stocks_id_seq OWNED BY public.stocks.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name text NOT NULL,
    password text NOT NULL,
    email text NOT NULL
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


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: watch_list_stocks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.watch_list_stocks (
    watch_list_id integer NOT NULL,
    stock_id integer NOT NULL
);


ALTER TABLE public.watch_list_stocks OWNER TO postgres;

--
-- Name: watch_lists; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.watch_lists (
    id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.watch_lists OWNER TO postgres;

--
-- Name: watch_lists_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.watch_lists_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.watch_lists_id_seq OWNER TO postgres;

--
-- Name: watch_lists_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.watch_lists_id_seq OWNED BY public.watch_lists.id;


--
-- Name: portfolios id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.portfolios ALTER COLUMN id SET DEFAULT nextval('public.portfolio_id_seq'::regclass);


--
-- Name: stocks id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stocks ALTER COLUMN id SET DEFAULT nextval('public.stocks_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: watch_lists id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.watch_lists ALTER COLUMN id SET DEFAULT nextval('public.watch_lists_id_seq'::regclass);


--
-- Data for Name: portfolio_stocks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.portfolio_stocks (portfolio_id, stock_id) FROM stdin;
2	2
2	3
3	1
\.


--
-- Data for Name: portfolios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.portfolios (id, profit_amount, net_worth, user_id) FROM stdin;
2	\N	$0.00	4
3	\N	$0.00	5
4	\N	$0.00	6
\.


--
-- Data for Name: stocks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.stocks (id, symbol, profit_amount, percent_change, price_change, current_price, name, quantity, purchase_price) FROM stdin;
1	AAPL	\N	-1.51	-2.63	171.52	Apple Inc.	\N	\N
2	DIS	\N	-2.06	-2.53	120.14	The Walt Disney Company	\N	\N
3	F	\N	-1.67	-0.27	15.88	Ford Motor Company	\N	\N
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name, password, email) FROM stdin;
4	Bob	123	bob123@gmail.com
5	Jane	123	jane123@aol.com
6	John	123	john123@yahoo.com
\.


--
-- Data for Name: watch_list_stocks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.watch_list_stocks (watch_list_id, stock_id) FROM stdin;
1	3
1	2
2	2
3	2
\.


--
-- Data for Name: watch_lists; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.watch_lists (id, user_id) FROM stdin;
1	4
2	6
3	5
\.


--
-- Name: portfolio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.portfolio_id_seq', 4, true);


--
-- Name: stocks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.stocks_id_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 6, true);


--
-- Name: watch_lists_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.watch_lists_id_seq', 3, true);


--
-- Name: portfolios portfolio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.portfolios
    ADD CONSTRAINT portfolio_pkey PRIMARY KEY (id);


--
-- Name: portfolio_stocks portfolio_stocks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.portfolio_stocks
    ADD CONSTRAINT portfolio_stocks_pkey PRIMARY KEY (portfolio_id, stock_id);


--
-- Name: stocks stocks_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stocks
    ADD CONSTRAINT stocks_name_key UNIQUE (name);


--
-- Name: stocks stocks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stocks
    ADD CONSTRAINT stocks_pkey PRIMARY KEY (id);


--
-- Name: stocks stocks_symbol_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stocks
    ADD CONSTRAINT stocks_symbol_key UNIQUE (symbol);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: watch_lists watch_lists_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.watch_lists
    ADD CONSTRAINT watch_lists_pkey PRIMARY KEY (id);


--
-- Name: watch_list_stocks watchlist_stocks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.watch_list_stocks
    ADD CONSTRAINT watchlist_stocks_pkey PRIMARY KEY (watch_list_id, stock_id);


--
-- Name: portfolio_stocks fk_portfolio_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.portfolio_stocks
    ADD CONSTRAINT fk_portfolio_id FOREIGN KEY (portfolio_id) REFERENCES public.portfolios(id);


--
-- Name: portfolios fk_portfolios_users; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.portfolios
    ADD CONSTRAINT fk_portfolios_users FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: watch_list_stocks fk_stock_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.watch_list_stocks
    ADD CONSTRAINT fk_stock_id FOREIGN KEY (stock_id) REFERENCES public.stocks(id);


--
-- Name: portfolio_stocks fk_stock_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.portfolio_stocks
    ADD CONSTRAINT fk_stock_id FOREIGN KEY (stock_id) REFERENCES public.stocks(id);


--
-- Name: watch_list_stocks fk_watch_list_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.watch_list_stocks
    ADD CONSTRAINT fk_watch_list_id FOREIGN KEY (watch_list_id) REFERENCES public.watch_lists(id);


--
-- Name: watch_lists fk_watch_lists_users; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.watch_lists
    ADD CONSTRAINT fk_watch_lists_users FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

