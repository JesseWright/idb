--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: _artists_eras_relationship; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE _artists_eras_relationship (
    artist_id integer NOT NULL,
    era_id integer NOT NULL
);


ALTER TABLE _artists_eras_relationship OWNER TO postgres;

--
-- Name: _artists_media_relationship; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE _artists_media_relationship (
    artist_id integer NOT NULL,
    medium_id integer NOT NULL
);


ALTER TABLE _artists_media_relationship OWNER TO postgres;

--
-- Name: _media_eras_relationship; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE _media_eras_relationship (
    medium_id integer NOT NULL,
    era_id integer NOT NULL
);


ALTER TABLE _media_eras_relationship OWNER TO postgres;

--
-- Name: _media_works_relationship; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE _media_works_relationship (
    medium_id integer NOT NULL,
    work_id integer NOT NULL
);


ALTER TABLE _media_works_relationship OWNER TO postgres;

--
-- Name: _works_eras_relationship; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE _works_eras_relationship (
    work_id integer NOT NULL,
    era_id integer NOT NULL
);


ALTER TABLE _works_eras_relationship OWNER TO postgres;

--
-- Name: artist; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE artist (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    dob date,
    dod date,
    nationality character varying(255),
    country character varying(255),
    image character varying(255),
    bio character varying(255)
);


ALTER TABLE artist OWNER TO postgres;

--
-- Name: artist_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE artist_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE artist_id_seq OWNER TO postgres;

--
-- Name: artist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE artist_id_seq OWNED BY artist.id;


--
-- Name: artists_works_relationship; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE artists_works_relationship (
    artist_id integer NOT NULL,
    work_id integer NOT NULL
);


ALTER TABLE artists_works_relationship OWNER TO postgres;

--
-- Name: era; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE era (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    type character varying(255) NOT NULL,
    countries character varying(255)
);


ALTER TABLE era OWNER TO postgres;

--
-- Name: era_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE era_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE era_id_seq OWNER TO postgres;

--
-- Name: era_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE era_id_seq OWNED BY era.id;


--
-- Name: medium; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE medium (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    colors character varying(255),
    average_age numeric,
    avg_height numeric,
    avg_width numeric,
    avg_depth numeric,
    images character varying(255),
    countries character varying(255)
);


ALTER TABLE medium OWNER TO postgres;

--
-- Name: medium_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE medium_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE medium_id_seq OWNER TO postgres;

--
-- Name: medium_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE medium_id_seq OWNED BY medium.id;


--
-- Name: work; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE work (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    date date,
    height numeric,
    width numeric,
    depth numeric,
    colors character varying(255),
    image character varying(255),
    motifs character varying(255)
);


ALTER TABLE work OWNER TO postgres;

--
-- Name: work_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE work_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE work_id_seq OWNER TO postgres;

--
-- Name: work_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE work_id_seq OWNED BY work.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY artist ALTER COLUMN id SET DEFAULT nextval('artist_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY era ALTER COLUMN id SET DEFAULT nextval('era_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY medium ALTER COLUMN id SET DEFAULT nextval('medium_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY work ALTER COLUMN id SET DEFAULT nextval('work_id_seq'::regclass);


--
-- Data for Name: _artists_eras_relationship; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY _artists_eras_relationship (artist_id, era_id) FROM stdin;
\.


--
-- Data for Name: _artists_media_relationship; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY _artists_media_relationship (artist_id, medium_id) FROM stdin;
1	1
2	1
3	2
4	3
5	3
6	2
7	2
8	3
9	2
10	4
11	5
12	6
13	7
14	8
15	3
16	2
17	3
18	2
19	3
20	3
21	3
4	2
22	3
23	3
24	2
25	3
26	2
27	2
28	9
29	4
30	6
31	2
32	2
33	3
34	3
35	3
36	2
37	2
38	10
39	3
40	3
41	2
42	1
1	11
43	12
\.


--
-- Data for Name: _media_eras_relationship; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY _media_eras_relationship (medium_id, era_id) FROM stdin;
\.


--
-- Data for Name: _media_works_relationship; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY _media_works_relationship (medium_id, work_id) FROM stdin;
1	1
1	2
1	3
2	4
3	5
3	6
3	7
2	8
2	9
3	10
2	11
4	12
4	13
5	14
6	15
7	16
8	17
3	18
3	19
2	20
4	21
2	22
3	23
2	24
3	25
3	26
3	27
2	28
3	29
3	30
3	31
2	32
3	33
2	34
2	35
9	36
4	37
4	38
6	39
4	40
2	41
2	42
2	43
2	44
3	45
3	46
3	47
3	48
2	49
2	50
10	51
3	52
3	53
2	54
1	55
11	56
12	57
4	58
4	59
\.


--
-- Data for Name: _works_eras_relationship; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY _works_eras_relationship (work_id, era_id) FROM stdin;
\.


--
-- Data for Name: artist; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY artist (id, name, dob, dod, nationality, country, image, bio) FROM stdin;
1	anonymous	\N	\N	\N	\N	https://s-media-cache-ak0.pinimg.com/736x/3c/3a/e9/3c3ae9d65d325dbf6a6bab860f1c4172.jpg	\N
2	Abraham Roentgen	1711-01-30	1793-03-01	Duits	\N	https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Roentgenportrait.jpg/220px-Roentgenportrait.jpg	\N
3	Piero di Cosimo	1462-01-01	1522-04-12	\N	\N	https://upload.wikimedia.org/wikipedia/commons/6/6e/Piero_di_Cosimo_-_Portrait_de_jeune_homme.jpg	\N
4	Rembrandt Harmensz. van Rijn	1606-07-15	1669-10-08	Noord-Nederlands	\N	http://daystarvisions.com/Pix/Masters/Full/Rembrandt_Harmenszoon_van_Rijn-Self_Portrait-1660-222256-edited_DC_lvl11.jpg	\N
5	Jacob Isaacksz. van Ruisdael	\N	1682-03-14	Noord-Nederlands	\N	https://upload.wikimedia.org/wikipedia/commons/c/cf/Portrait_of_Jacob_van_Ruisdael_01.jpg	\N
6	Hendrick Avercamp	\N	\N	\N	\N	http://p9.storage.canalblog.com/99/93/119589/66367522.jpg	\N
7	Hans Bollongier	\N	\N	\N	\N	http://www.oceansbridge.com/paintings/artists/masters/small/b/bollongi/flower_p_painting.jpg	\N
8	Francisco de Goya	1746-03-30	1828-04-16	Spaans	\N	http://www.franciscodegoya.net/download-178557-self-portrait-i.download	\N
9	Lucas van Leyden	\N	\N	Noord-Nederlands	\N	https://upload.wikimedia.org/wikipedia/commons/d/d8/Lucas_van_Leyden_-_Self-portrait_-_WGA12920.jpg	\N
10	Renier van Thienen	\N	\N	Vlaams	\N	https://s-media-cache-ak0.pinimg.com/736x/8d/f3/c1/8df3c183616af7da93bb6f5d772f440d.jpg	\N
11	Adriaen van Wesel	\N	\N	Noord-Nederlands	\N	https://www.artsy.net/artwork/adriaen-van-wesel-virgin-and-child/download/adriaen-van-wesel-virgin-and-child-ca-1470-1480.jpg	\N
12	Artus Quellinus (I)	\N	1668-08-23	Zuid-Nederlands (vóór 1775)	\N	http://upload.wikimedia.org/wikipedia/commons/1/14/Richard_Collin_-_Portrait_of_Artus_Quellinus_the_Elder.jpg	\N
13	Rombout Verhulst	1624-01-15	1698-11-27	Noord-Nederlands	\N	https://upload.wikimedia.org/wikipedia/commons/d/d1/Rombout_Verhulst_-_Bust_of_Jacob_van_Reygersberg.jpg	\N
14	Meissener Porzellan Manufaktur	\N	\N	\N	\N	https://s-media-cache-ak0.pinimg.com/564x/55/d0/a3/55d0a3d893bb0edf32aeeadf88c9c395.jpg	\N
15	Johannes Cornelisz. Verspronck	\N	1662-06-30	Noord-Nederlands	\N	https://s-media-cache-ak0.pinimg.com/originals/66/02/0a/66020a3997b4b97cb7078dd64d49495b.jpg	\N
16	Jacob Cornelisz van Oostsanen	\N	\N	Noord-Nederlands	\N	https://upload.wikimedia.org/wikipedia/commons/d/da/Jacob_Cornelisz._van_Oostsanen_-_Portrait_of_a_Man_-_WGA05264.jpg	\N
17	Aelbert Cuyp	1620-10-20	1691-11-15	\N	\N	https://upload.wikimedia.org/wikipedia/commons/e/e4/10_Albert_Cuyp%2C_Schilder%2C_1620-1691.jpg	\N
18	Dirck Hals	1591-03-19	1656-05-17	\N	\N	http://www.fineart-china.com/upload1/file-admin/images/new24/Dirck%20Hals-755784.jpg	\N
19	Bartholomeus van der Helst	\N	1670-12-16	Noord-Nederlands	\N	https://upload.wikimedia.org/wikipedia/commons/5/59/Bartholomeus_van_der_Helst_-_Self-Portrait_-_Google_Art_Project.jpg	\N
20	Pieter de Hooch	1629-12-20	\N	\N	\N	https://uploads7.wikiart.org/images/pieter-de-hooch.jpg!Portrait.jpg	\N
21	Jan Willem Pieneman	1779-11-04	1853-04-08	\N	\N	https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Jan_Willem_Pieneman02.jpg/250px-Jan_Willem_Pieneman02.jpg	\N
22	George Hendrik Breitner	1857-09-12	1923-06-05	Nederlands	\N	http://cultured.com/images/image_files/2864/7921_o_george_hendrik_breitner___self_portrait.jpg	\N
23	Johannes Vermeer	1632-10-31	1675-12-15	Noord-Nederlands	\N	http://www.essentialvermeer.com/fakes_thefts_school_of_delft_lost_sp/delft_school_lost_self_portrait_mages/unknown_man.jpg	\N
24	Joachim Bueckelaer	\N	\N	\N	\N	https://upload.wikimedia.org/wikipedia/commons/6/69/Joachim_Beuckelaer_Portrait_of_a_Young_Woman.jpg	\N
25	Frans Hals	\N	1666-08-26	\N	\N	https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/After_Frans_Hals_-_Portrait_of_Frans_Hals_-_Indianapolis.jpg/220px-After_Frans_Hals_-_Portrait_of_Frans_Hals_-_Indianapolis.jpg	\N
26	Willem Claesz. Heda	\N	\N	\N	\N	http://p6.storage.canalblog.com/69/23/577050/62326292.jpg	\N
27	Master of Alkmaar	\N	\N	Noord-Nederlands	\N	https://upload.wikimedia.org/wikipedia/commons/5/55/Master_of_Alkmaar_portraits_Jan_III_of_Egmont_(1438-1516).jpg	\N
28	Vincent van Gogh	1853-03-30	1890-07-29	Nederlands	\N	https://upload.wikimedia.org/wikipedia/commons/b/b2/Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project.jpg	\N
29	Jan Borman (II)	\N	\N	Vlaams	\N	https://s-media-cache-ak0.pinimg.com/736x/2e/08/45/2e0845506e789f9baf37309116bf80f6.jpg	\N
30	Étienne-Maurice Falconet	1716-12-01	1791-01-24	Frans	\N	http://images.metmuseum.org/CRDImages/dp/original/DP826265.jpg	\N
31	Pieter Jansz. Saenredam	1597-06-09	\N	Noord-Nederlands	\N	http://c8.alamy.com/comp/G2JB8D/portrait-of-laurens-jansz-coster-pieter-jansz-saenredam-pieter-casteleyn-G2JB8D.jpg	\N
32	Jan van Scorel	1495-01-09	1562-12-06	Noord-Nederlands	\N	https://upload.wikimedia.org/wikipedia/commons/8/85/Jan_van_Scorel_-_Portrait_of_a_Man_of_Thirty-Two_Years_-_WGA21086.jpg	\N
33	Jan Havicksz. Steen	\N	\N	Noord-Nederlands	\N	https://upload.wikimedia.org/wikipedia/commons/d/d3/1670_Jan_Havicksz._Steen_-_zelfportret.jpg	\N
34	Gerard ter Borch (II)	\N	1681-12-08	Noord-Nederlands	\N	https://upload.wikimedia.org/wikipedia/commons/6/67/Zelfportret_by_Gerard_ter_Borch.jpg	\N
35	Jan Both	\N	1652-08-09	\N	\N	https://art.famsf.org/sites/default/files/artwork/waumans/3328201304880061.jpg	\N
36	Adriaen Pietersz. van de Venne	\N	1662-11-12	Noord-Nederlands	\N	https://s-media-cache-ak0.pinimg.com/564x/89/92/96/8992968e210e77c56b28082746cc5679.jpg	\N
37	Geertgen tot Sint Jans	\N	\N	\N	\N	http://www.artbible.info/portrait/50.jpg	\N
38	Adriaen Coorte	\N	\N	Nederlands	\N	http://www.thefashiongrid.com/storage/WearLACMAPortrait.jpg?__SQUARESPACE_CACHEVERSION=1349891453183	\N
39	Melchior d' Hondecoeter	\N	1695-04-03	\N	\N	https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Portrait_of_Melchior_d%27Hondecoeter_001.jpg/250px-Portrait_of_Melchior_d%27Hondecoeter_001.jpg	\N
40	Gabriël Metsu	\N	1667-10-24	\N	\N	https://upload.wikimedia.org/wikipedia/commons/7/79/Gabriel_Metsu_-_Portrait_of_a_Lady_-_Google_Art_Project.jpg	\N
41	Adriaen Thomasz. Key	\N	\N	\N	\N	http://www.sothebys.com/content/dam/stb/lots/N09/N09003/046N09003_6RWX6.jpg	\N
42	Herman Doomer	\N	\N	\N	\N	https://upload.wikimedia.org/wikipedia/commons/b/b9/Rembrandt_van_Rijn_Harmen_Doomer_circa_1640.jpg	\N
43	Wenzel Jamnitzer	\N	\N	Duits	\N	http://nrs.harvard.edu/urn-3:HUAM:DDC107808_dynmc?width=3000&height=3000	\N
\.


--
-- Name: artist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('artist_id_seq', 43, true);


--
-- Data for Name: artists_works_relationship; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY artists_works_relationship (artist_id, work_id) FROM stdin;
1	1
2	2
1	3
3	4
4	5
4	6
5	7
6	8
7	9
8	10
9	11
10	12
10	13
11	14
12	15
13	16
14	17
4	18
15	19
16	20
10	21
16	22
17	23
18	24
19	25
20	26
21	27
4	28
22	29
23	30
23	31
24	32
25	33
26	34
27	35
28	36
10	37
29	38
30	39
10	40
3	41
4	42
31	43
32	44
33	45
34	46
35	47
22	48
36	49
37	50
38	51
39	52
40	53
41	54
42	55
1	56
43	57
10	58
10	59
\.


--
-- Data for Name: era; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY era (id, name, type, countries) FROM stdin;
\.


--
-- Name: era_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('era_id_seq', 1, false);


--
-- Data for Name: medium; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY medium (id, name, colors, average_age, avg_height, avg_width, avg_depth, images, countries) FROM stdin;
1	wood (plant material)	\N	\N	\N	\N	\N	\N	\N
2	oil on panel	\N	\N	\N	\N	\N	\N	\N
3	oil on canvas	\N	\N	\N	\N	\N	\N	\N
4	brass copper alloy	\N	\N	\N	\N	\N	\N	\N
5	oak with traces of polychromy	\N	\N	\N	\N	\N	\N	\N
6	marble (rock)	\N	\N	\N	\N	\N	\N	\N
7	terracotta (clay material)	\N	\N	\N	\N	\N	\N	\N
8	porcelain (material)	\N	\N	\N	\N	\N	\N	\N
9	painting	\N	\N	\N	\N	\N	\N	\N
10	paper	\N	\N	\N	\N	\N	\N	\N
11	bronze	\N	\N	\N	\N	\N	\N	\N
12	silver (metal)	\N	\N	\N	\N	\N	\N	\N
\.


--
-- Name: medium_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('medium_id_seq', 12, true);


--
-- Data for Name: work; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY work (id, title, date, height, width, depth, colors, image, motifs) FROM stdin;
1	Cabinet of a militia company	1520-01-01	147.0	110.0	80.0	{#9D958D," #C7BDB4"," #796553"," #8B7E72"," #2B1D17"," #4C3B31"," #0D0503"}	http://lh6.ggpht.com/y9FmgZB4UrtrBz5hmXjWwIKSgXs_UcARxiYGtRJEeAfZ8kD1BQ_xORtEXcjXLjxwWYskHt7fBX7KHe7RX9ZB39IMpQ=s0	\N
2	Desk	1758-01-01	148.5	110.0	58.5	{#C6BBA6," #88745B"," #A79984"," #504033"," #21150E"," #835B2B"," #EBE4CD"}	http://lh4.ggpht.com/FeheHnW8-KOx-prHRCvly8ReF9WKysmPJDEd99EEVDViH1DvYytyDpkjnkeyqqj85WNbrkXFaoFe0jBKB9DdNJApLQ=s0	\N
3	Dolls’ house of Petronella Oortman	1686-01-01	255.0	190.0	28.0	{#D9D5C6," #5B422A"," #979081"," #9B6032"," #1A150D"," #B98E4A"," #DCBC6A"}	http://lh3.ggpht.com/OIaBDlLOhgpAQHGdfYfIh0ygXRqgBNR-tW7se4OTwOtD6dsr6xLAmp8u_pfsqJ-0EqB_wbCF_0mvCl979lWxfFIyFQQ=s0	\N
4	Portraits of Giuliano and Francesco Giamberti da Sangallo	1482-01-01	47.5	33.5	\N	{#345171," #5F7E9D"," #B0B5A7"," #100F0A"," #A28559"," #664730"}	http://lh4.ggpht.com/NwCWmjro4h__Ord5RqicIJsJbTY104UditPHR-swB9a7pQRt67KfneX_tBEazLnkNGsWqCvfsZam8Pxj1Ixiqbne7Q=s0	\N
5	Militia Company of District II under the Command of Captain Frans Banninck Cocq, Known as the ‘Night Watch’	1642-01-01	379.5	453.5	\N	{#261808," #5E3C14"," #9C8238"," #885617"," #AF9F6B"," #6C6238"," #D7CB9E"}	http://lh6.ggpht.com/ZYWwML8mVFonXzbmg2rQBulNuCSr3rAaf5ppNcUc2Id8qXqudDL1NSYxaqjEXyDLSbeNFzOHRu0H7rbIws0Js4d7s_M=s0	\N
6	Portrait of a Couple as Isaac and Rebecca, known as ‘The Jewish Bride’	1665-01-01	121.5	166.5	\N	{}	http://lh5.ggpht.com/H-KfOaNgW2an_g0kODWKua5BELckMTr7zauQZCbnOZ69fyNlr67uavKaDmvSawg8j6TB88abmtAjNbcMjbOdU94zuzM=s0	\N
7	The Windmill at Wijk bij Duurstede	1668-01-01	83.0	101.0	\N	{#65563B," #77705A"," #898D83"," #231E12"," #3C3828"," #A7A58F"," #988561"}	http://lh6.ggpht.com/1gH99j2GD85SW4r3CA18uwTDuRioMYTNZlH5N2xuZsbh_4QUnzxettm6WqCsLa_ciGCzhWwLzF35QtHEpz4M9LWv_yvl=s0	\N
8	Winter Landscape with Ice Skaters	1608-01-01	77.3	131.9	\N	{#B0AD92," #64614A"," #D7D3BA"," #76806F"," #373B30"," #1F1C15"," #9E824E"}	http://lh5.ggpht.com/fnW9Pyd4QvVnz1NmbiU2j1v5gRHgtmjEcmNGAhgqJ0nD9oQSmi8Iddje-Da6ozlYLI9QP32OASS7A3qT9izEYTmcDA=s0	\N
9	Floral Still Life	1639-01-01	66.0	52.3	\N	{#563629," #1F130B"," #7D6347"," #AA9B75"," #EAEBDA"," #CAC6B8"," #E8D98D"}	http://lh4.ggpht.com/y-B7FwRdKdFzKCrrAzgvnGOW1e1-z0w2sfJqjVWuqDt_Du6s8q5Y2_bAyjk_SVTPDWb9ZLqwMCq3FemdsGHJkf7tdC46=s0	\N
10	Portrait of Don Ramón Satué	1823-01-01	135.5	112.0	\N	{#322318," #0F0E09"," #573525"," #764736"," #796956"," #9F947C"," #BDB89D"}	http://lh4.ggpht.com/wyy5JOPbVx1wQ9ax57OmfOz4kooWGwaW7iX7OS5VkveFRTxLQ6J73t4bunTkrerA9nvlgUIyutax_0KzR9kbhKOesMY=s0	\N
11	Worship of the Golden Calf	1530-01-01	91.8	30.2	\N	{#FDFCFB," #E3DBB0"," #AAAA93"," #1C1610"," #593629"," #857A62"}	http://lh5.ggpht.com/s6sGZ2OFkUPvX83i1JwioP0RckwCQfI2xXIjgcI1V5WlEbTXfFQvcr97gFMVwFqJNofPycMeB1u5Wwo6CJ8y1pVenLGZ=s0	\N
12	Ten weepers from the tomb of Isabella of Bourbon	1475-01-01	54.5	24.5	14.0	{#DBD9D9," #8C8887"," #716D6B"," #4E4843"," #AEACAC"," #1F1D1B"}	http://lh5.ggpht.com/EHhJDrv4IB_89m9w9VlcYRYHYOuvU72iwD11oZ1HL3J5QcCMfmAD48CVxAtUwts9RT55W4lWSPI19wb1lSRZ9zecKMA=s0	\N
13	Ten weepers from the tomb of Isabella of Bourbon	1475-01-01	58.0	20.5	13.5	{#F1EBEA," #7A7673"," #9E9C9B"," #4F4A44"," #C5C4C4"," #1D1B19"}	http://lh3.ggpht.com/hWw39CO9_f8Layr6PT_REdtl_nJflH6L_o8jeF3XxmAquB2PKQhWK2kKRCd16TUvhdTl1UrfFC0-Wn1es9LxfdtcZQ=s0	\N
14	Virgin and Child	1470-01-01	55.0	18.0	14.0	{#BE9553," #CBB290"," #DECCAC"," #8D6941"," #653F19"," #2B130A"," #F1E8D9"}	http://lh6.ggpht.com/w51qt-qW6i-7WJL4SJzFLw1JQAa0lx0Kem6vI0TgQv9fFVDzLaq70UV3SmAQfdN4AhcnnspmU7eG1zaQxOu_z2z5caY=s0	\N
15	Portrait of Andries de Graeff	1661-01-01	76.0	22.4	22.4	{}	http://lh5.ggpht.com/Dm4qOkEfe0P9YqnN7s-KRxy6K_o4trePSnlVvGNg0TPGcKmiDS_sdmqqbSeSENg22FFjyIz0xI2CEJhkrk9IfmDYHwo=s0	\N
16	Portrait of Michiel de Ruyter	1677-01-01	35.0	32.0	30.0	{#101209," #4F4528"," #332C14"," #81764F"," #645A3B"," #9A8F63"," #B2AD89"}	http://lh3.ggpht.com/7eeRiDQLguCwPA7159-wn9Jd3AhGzmFzra0kda7SX5Vm1TqTW3sLf6UksceWq6MUJmrUSxVC5bCviXAMX1S0qd0lUi0=s0	\N
17	Blue Macaw	1731-01-01	69.5	22.5	28.0	{#3C3C45," #161511"," #DCCE87"," #757376"," #AFA481"," #E2E1D7"}	http://lh3.ggpht.com/5sc-SGzzgobkHnmnykUi4B1PqMtadoFqXOhYLQmsAI0Mcs_FeCoXT6loaiAUhr_zKvp2iyXntDxVhCzeVwjFulsjzRE=s0	\N
18	Self Portrait as the Apostle Paul	1661-01-01	91.0	77.0	\N	{#0B0906," #2A2111"," #4E3F23"," #725E3B"," #9A8356"," #B4A376"," #C6B88F"}	http://lh4.ggpht.com/HFwjp18jTNpNV0V2ZCvuBCNgEn4HUbF8FrcxTDpD7koJ7HuZrKIso_5-TukpFNP01riC2x0Oa32MI3vt3p7-tf4bqQ=s0	\N
19	Portrait of a Girl Dressed in Blue	1641-01-01	82.0	66.5	\N	{#181815," #C5C2B5"," #37362D"," #918470"," #504F42"," #6B6856"}	http://lh6.ggpht.com/gOTbLnfHUVFp3PgQQSNiEmQ0fjVAPCNJbO8ofTXlFJMpUWDye9ernn75qmkGj8KqAQTr60cyOHiXK3LnWwhwvc1mGQ=s0	\N
20	Portrait of Jacob Cornelisz van Oostsanen	1533-01-01	37.8	29.4	\N	{#0C0C0A," #372D1B"," #796841"," #9E8B6F"," #AFA68A"," #514333"}	http://lh6.ggpht.com/6TaPf10g0DwIK271jaX9tgrTqWb-h0kp8VbvLVNkSvFqxeyi289j827c9XSj_q2mk4K2HCyhPZ6frcwgh64XbNAk2Q=s0	\N
21	Ten weepers from the tomb of Isabella of Bourbon	1475-01-01	56.0	21.0	13.5	{#CDCCCC," #6C645D"," #443D37"," #221F1D"," #ABA8A7"," #928E8D"," #F7F1EF"}	http://lh3.ggpht.com/3bzg_jUPUnsPxCugY78L5mF-nOg9_l_7rMGkHVfTK0wUFU0J2kfZ_vMLT65F6nRDm5Ck7hy9iQoYCiWC2V1Becaj15E=s0	\N
22	Portrait of Jacob Cornelisz van Oostsanen	1533-01-01	37.8	29.4	\N	{#0C0C0A," #372D1B"," #796841"," #9E8B6F"," #AFA68A"," #514333"}	http://lh6.ggpht.com/6TaPf10g0DwIK271jaX9tgrTqWb-h0kp8VbvLVNkSvFqxeyi289j827c9XSj_q2mk4K2HCyhPZ6frcwgh64XbNAk2Q=s0	\N
23	River Landscape with Riders	1653-01-01	128.0	227.5	\N	{#C2BFA4," #8D8C7C"," #766A48"," #DEDDC6"," #2F2819"," #7C4B25"}	http://lh4.ggpht.com/1OOoY0qISJncBpdzHk1dKTkNcmXJndXA7kfUMrm9B_-g57lGyb-eEjl_BCQzdmsthkk7HS93eSpHx_l_P_sFXoEDKeo=s0	\N
24	The Fête champêtre	1627-01-01	77.6	135.7	\N	{#768388," #656D60"," #382C24"," #5F4B35"," #A59A80"," #91633D"}	http://lh4.ggpht.com/aSyhtY1rLfuYrMOVhEuvUua1WDwph30DIs4nJc6ACRpAM-avOaQHb9lmdqNsSWq1H-3rCEjBFlozD3f50b3Qf_XFLaaK=s0	\N
25	Banquet at the Crossbowmen’s Guild in Celebration of the Treaty of Münster	1648-01-01	232.0	547.0	\N	{#120F09," #4E402C"," #856E47"," #9F8E6A"," #ABA892"," #425763"," #C7C5B1"}	http://lh5.ggpht.com/dMaR9T0-0j9erOeI3dFRnTt4L7UeL1qtt-IA1_Kj-WDLwt5RHFc45I5n6aluaMFL1b8gZIYIIYsHavL-FWpl-gOQpw=s0	\N
26	A Mother Delousing her Child’s Hair, Known as ‘A Mother’s Duty’	1658-01-01	52.5	61.0	\N	{#5C391E," #2A2018"," #0E0F09"," #6A573A"," #8C7758"," #B29F81"," #CFC8B0"}	http://lh6.ggpht.com/5uBzvjv5x3kYBP5I4k193sxz9VaLNm4Ga6NpUlQY7FKUUCVGE2VLgaifqjbGC5s7OHNZZVpK9z62BnlLuJ5Jb54BlQ=s0	\N
27	The Battle of Waterloo	1824-01-01	567.0	40.0	\N	{#130C08," #D5B586"," #BF9762"," #F6E3AF"," #5A301B"," #865D3A"}	http://lh3.googleusercontent.com/MHkVLylkz-ITQAhXck5aQUTXxJX6xequIQbsppMh9eFx2fbg1Botuex8eQidQwyAgGttsISWm2FDipZ0SD5CWEIm_WA=s0	\N
28	Portrait of a Woman, Possibly Maria Trip	1639-01-01	107.0	82.0	\N	{#0B0906," #2F2718"," #A69272"," #CEC9B6"," #755F42"," #BBAC8E"," #4D4534"}	http://lh6.ggpht.com/EcRbIeCJDvhPrCvIapeonP-VAWdGUwJNBuIq5DqY9d9O-1DNtvrxOYQCFOlpLvuDcOqynNafPpcJXzI7KXDvV1Eqnw=s0	\N
29	Girl in a White Kimono	1894-01-01	59.0	57.0	11.0	{#1A140D," #7C6235"," #38302D"," #968661"," #B8A67B"," #9C3B29"," #B89B14"}	http://lh3.ggpht.com/NovVOG9SpVtD-MogOk4KHI-GFO0Z6KUIigSe7q55gr1X9QI7VGygF8WgIokWrm_E9ZTsW8Qomi8RDx0q5H38Dat6BXc=s0	\N
30	View of Houses in Delft, Known as The Little Street	1658-01-01	54.3	44.0	9.0	{#664B39," #BDB69F"," #988F7A"," #31291F"," #716957"," #DDD6BE"," #11100C"}	http://lh4.ggpht.com/u-sROQ5mLanzq7i06ja0yXBxZpBPazZN3z590K7F4ZNufmxuaA5BRHjJTiatQO_gXI-gDAWMFJeBXb55z-5NrCAl8g=s0	\N
31	Woman Reading a Letter	1663-01-01	61.5	53.0	6.5	{#565435," #D0D2C8"," #989E9B"," #747868"," #333F4F"," #0F1219"}	http://lh3.ggpht.com/_hNgP8xlzkSVD_XfBIy3j6BSWyGqdc0N921xFJbXG7jwFbQ7hi8IuTO6AIAsQf_RI3_dt4_EEncuuLY5pVO0vT50qpY=s0	\N
32	The Well-stocked Kitchen	1566-01-01	171.0	250.0	\N	{#1B1815," #503D2E"," #A19782"," #BBB5A0"," #776048"," #94805E"}	http://lh4.ggpht.com/geMErXtSoypSyBaGkBOYHG8XxO1sP2MoYtfbs70fRbPbpWjvP04jEvhlamJ0kmbuo6C2UZYCBZQumngASkyZjO4MRgI=s0	\N
33	Portrait of a Couple, Probably Isaac Abrahamsz Massa and Beatrix van der Laen	1622-01-01	140.0	166.5	\N	{#181812," #313024"," #5E5B47"," #A5A599"," #616D73"," #8A8269"," #889291"}	http://lh4.ggpht.com/5EAw9FBBwVmOwHhFvXCUupfoMZjd3-NHj8HdDvVecJEgFHfKeofAfpEEEvj4MTn3JBW-hhLABubkbchqMVYjdL0nxIo=s0	\N
34	Still Life with a Gilt Cup	1635-01-01	88.0	113.0	\N	{#433624," #A18D61"," #705838"," #8A7348"," #19170E"," #BAAB78"," #CBC5AF"}	http://lh6.ggpht.com/fyibXVnDQ5lG-8aKgiF7VXiv_6uFRFugZTAcdfKHO2-4TLpiUeDkXaxfak9H5epLghPseBrn5maSbfjn4UYDANpDmF4=s0	\N
35	The Seven Works of Mercy	1504-01-01	119.1	469.5	\N	{#D1B681," #A0A7AA"," #F3EBCD"," #916541"," #0D0F0C"," #37362A"}	http://lh5.ggpht.com/ZynTzaTG5YZ2CM7PstlgbDKzSBT6Rw4XlvkkhsTwiVzgNjP7x16DXMR1OqdqumSVE72nEWFyEIVwMsc6pH6hv_BgEEE=s0	\N
36	Self-portrait	1887-01-01	42.0	34.0	8.0	{#52686D," #50524C"," #9CA097"," #936D59"," #C2C1B8"," #6A84A2"," #2F3031"}	http://lh4.ggpht.com/RKAJ3z2mOcw83Ju0a7NIp71oUoJbVWJQzxwki5PSERissvWIrELCuxxGZ12U0PeAnf6WLkRCzpFdvjweUBjlcr2I4dl_=s0	\N
37	Ten weepers from the tomb of Isabella of Bourbon	1475-01-01	55.5	25.5	12.5	{#D8D7D8," #383431"," #595654"," #8A8786"," #181716"," #B9B8B8"}	http://lh6.ggpht.com/z37VVIUgOOW4cumA4FvSwyvuMWdk6rjD7CBu1aAL5OGz_-RRuuQ2Xq4jEuHWn7plIwhD4bT2Qp8pnGRqbWPiNPpM0gwE=s0	\N
38	Ten weepers from the tomb of Isabella of Bourbon	1475-01-01	58.0	20.5	12.5	{#DBD8D7," #827F7E"," #625D5B"," #454039"," #201E1D"," #AFAEAE"}	http://lh4.ggpht.com/-xIJabR1yHWNnbX277YqLXC0H4bcKRWEDvulNRXOi75nB-jHBsCwwraBSXOhQ7coAyltbAmPhfFvSb2NFlU5ibSbhA=s0	\N
39	Seated Cupid	1757-01-01	185.0	47.5	68.5	{#D6D1C5," #F5F4F3"," #A49982"," #6F6750"," #4B4531"," #201B10"}	http://lh3.googleusercontent.com/i8S7we9zDW-AqUbZvE91O4bqsgVI_MamJhChLz6lE55MIn_kAjrYNoudrM-YEKjZTLUPyXVBgi__m6n1MMWmcbsHMy8=s0	\N
40	Ten weepers from the tomb of Isabella of Bourbon	1475-01-01	55.0	22.5	12.5	{#B9B8B8," #E2DEDC"," #201D1B"," #4C453E"," #6A6561"," #9F9D9C"," #84807E"}	http://lh6.ggpht.com/zEY5JwpbGa7M7ueF5Nyqx3N0xeCXrQ_Ck83xIws2OxWScEOdOfxv-jZwRqSoxfz4Kqq4o96XKkIggCx3_JUjpYolsw=s0	\N
41	Portraits of Giuliano and Francesco Giamberti da Sangallo	1482-01-01	47.5	33.5	\N	{#464A49," #11100B"," #9F8458"," #547392"," #9EADB2"," #7E2C1A"," #D5CBA6"}	http://lh4.ggpht.com/TbI1qyk1HcFlADzNX57Qfz4loEzZDBpOYVzCcAffIjiwyC8KWDSewv9F1_FHlB7wTOA2qSjozwHKWV2u5WTaEQ80Zabm=s0	\N
42	Self-portrait	1628-01-01	33.2	29.3	5.9	{}	http://lh5.ggpht.com/nhR4HlWt_rsB6k9LafDI8Nhg7HEoN01xc2UQBvDnQngX6rC6NjK6Th7i7TT5yFvZiEDQmV-qntbNGe_1oKH6XhUXAIqP=s0	\N
43	Interior of the Sint-Odulphuskerk in Assendelft	1649-01-01	49.0	73.6	\N	{#312818," #947A4D"," #9A8F72"," #C7BFA9"," #6A5738"," #726D5F"}	http://lh6.ggpht.com/G73iScQScILCyv6kezv_vbvoPYAsCXnBWho8e0zRvc9jfEW-Rv5zoR6X0oUFrS9SSYsP6R7fxSI8GTm2__x3iuv8T-es=s0	\N
44	Mary Magdalene	1530-01-01	86.5	96.0	\N	{#1D150D," #4E3E25"," #B1B09F"," #959480"," #5F563E"," #CBCBB7"," #7A755C"}	http://lh4.ggpht.com/63ihNfp589xL3z8GTq4gGeY1dLk37LgcGAPyT1_meK5KT3QdKLI3jj4mvcAv7t9EUkbsOVDCnNyBt-5kLjDp8sPgrgg=s0	\N
45	The Merry Family	1668-01-01	110.5	141.0	\N	{#7A5532," #BBAD89"," #D0C9A9"," #2F281B"," #9A855C"," #EAE8CA"}	http://lh4.ggpht.com/Zc6xkBJ4-wOxPX-CAbyMbakk8xbv_jr-xFAaybFFMnnkKsEIKVeWDATJx2EMyiqOps9t0ejyTd3_AHyp4T9sNnJ8qRg=s0	\N
46	Gallant Conversation, Known as ‘The Paternal Admonition’	1654-01-01	85.0	87.0	\N	{#0F0E0A," #2D261D"," #ABAC97"," #7D7251"," #938F75"," #504235"}	http://lh4.ggpht.com/Y67gZImh7YyQCvJCwHeuncnqZBbV3hospIwAGRRfMNnK3jVhO9yWPKLvttE2zsCIVEB5-Fn-JAzB5uRZDCf4aYzMnic=s0	\N
47	Italian Landscape with a Draughtsman	1650-01-01	187.0	240.0	\N	{#2B2415," #C1B07E"," #54401F"," #73633B"," #A19164"," #827A5E"," #9EA190"}	http://lh3.ggpht.com/AeQ9jLC5bjDig69cVAKQGaR7FnQnxYNoI8sbzpZbV38PxeCx4cBPzdKfA5KtfQ4UxjEjPe4q45ssxue0HG09BegRQA=s0	\N
48	The Singel Bridge at the Paleisstraat in Amsterdam	1896-01-01	100.0	152.0	\N	{#523821," #17130D"," #66533A"," #85765F"," #9B8C72"," #B4A488"," #76674D"}	http://lh5.ggpht.com/0-ZgadVGiJ83JIG0DOQZ4-m6qifm1TwHZfWAIfFdJfysOm58_5e4rdmPdpzJe4TD4ch6HHyCKuVGenVsZvkIKJwoUwg=s0	\N
49	Fishing for Souls	1614-01-01	121.1	211.0	\N	{#585946," #2A2818"," #918B71"," #4B3C29"," #7A735B"," #BDBDA4"," #0F100B"}	http://lh6.ggpht.com/Xs-MA3fK89Sf0JGqb_Ql08EZ3FwcClZoGpur1F3rsQg1aozydwvn4265scRFvJtTSvZO4Q7fIKac4-Iv_XdSHzO9piE=s0	\N
50	The Holy Kinship	1495-01-01	137.2	105.8	\N	{#323224," #A39380"," #6E4C37"," #947958"," #BDB9AA"," #15140D"," #5C201E"}	http://lh6.ggpht.com/wgSBVm-XNw4Ms-0dWpzcW-5aRfykN1VwHzS3PTepKC3GsCII0ORnZqxHSp2OcMALzb-e--fqDlxISf-V4zQyamshPQ=s0	\N
51	Still Life with Asparagus	1697-01-01	25.0	20.5	\N	{#110E07," #3F3120"," #84755B"," #A49C7F"," #6A5638"," #BDB89E"," #D8D5BD"}	http://lh4.ggpht.com/VQhG6FdMTlcssFuJsuzBvaTifOxSkPdnZhAhV9YuvroAGslng1ylZF5mi7v_r-SREb0CaoK9FDvW-CnY5k1RORYio8yS=s0	\N
52	A Pelican and other Birds near a Pool, Known as ‘The Floating Feather’	1680-01-01	159.0	144.0	\N	{#14120B," #6E644F"," #918A75"," #553927"," #B3A88A"," #C8C6B7"}	http://lh5.ggpht.com/rlHrWWRyqM1sZLCZxcGNv0uiTTZwijqp8F61Jis0D31i3X7s2mYU8pVJq-Z_TDiqoH5fn1SE9uP5Hz4oG1CCSjbW4sg=s0	\N
53	The Sick Child	1664-01-01	50.5	56.0	\N	{#969280," #B5B29F"," #897752"," #682D1C"," #241E1D"," #49504D"}	http://lh4.ggpht.com/DGpigU6g4PNtqzS-NgfiVceLDmk_CJv9YqUO-1wes9Sr63L93ZZDW1_LAbTi85RQBL7gnpMlEit2FB7trCJ6ghbVUw=s0	\N
54	William I, Prince of Oranje	1579-01-01	68.0	55.0	5.5	{#1F1D15," #463623"," #A2906B"," #907954"," #6B4F31"," #7C6344"," #B6AE89"}	http://lh3.ggpht.com/-Z1rNSeJ02Z4AD9xP4W2Zyp-NzQBZbb56nB1-m5TQp03ph9DNOFmVDz0pU7VZYEXKd9UDli00VLzqM-rpr95ErdpPAI=s0	\N
55	Cupboard	1635-01-01	220.5	206.0	83.5	{}	http://lh3.googleusercontent.com/tGI4dOAfJLBbewwspzXpUnSZxEKFACv9Y3FHqAxQUtN2p4AXt2MS9oFv6eJyIBtr7gvzmv58vSitMFVeHY0TGsfOfDN2=s0	\N
56	Shiva Nataraja	1100-01-01	19.0	73.5	44.0	{#949489," #31322C"," #6E6E63"," #B4B4AF"," #53534A"," #0F100D"," #D6D7D3"}	http://lh5.ggpht.com/vV5DJTpPEL5dOCFmytemK61JuTSX_9SQKI11U7uAhm4WB48zX6oyv8rXbBwYrSb7tPXUhERrROL8k2P9C5Q0NiOpCbs=s0	\N
57	Table ornament	1549-01-01	99.8	\N	\N	{#EDEEEA," #CACBC9"," #A2A3A1"," #64635F"," #868581"," #3F3E38"," #191612"}	http://lh6.ggpht.com/9ulJVSDjPC6uiOPm-0Lj44cicGWRmukCmE98Ut3EAn6BhQeo76QZe_YIGiMTTX9rr4k3nqPymTmhrGjZDohEIR5ZrQ=s0	\N
58	Ten weepers from the tomb of Isabella of Bourbon	1475-01-01	55.0	22.5	12.5	{#B9B8B8," #E2DEDC"," #201D1B"," #4C453E"," #6A6561"," #9F9D9C"," #84807E"}	http://lh6.ggpht.com/zEY5JwpbGa7M7ueF5Nyqx3N0xeCXrQ_Ck83xIws2OxWScEOdOfxv-jZwRqSoxfz4Kqq4o96XKkIggCx3_JUjpYolsw=s0	\N
59	Ten weepers from the tomb of Isabella of Bourbon	1475-01-01	55.5	20.5	13.5	{#888583," #5D5852"," #CBCACA"," #A6A5A4"," #2F2B27"," #F3ECE9"}	http://lh5.ggpht.com/XfGMlfAXKb8qHOLKbcluQCUHbW24UxS5vhE6-pY77EMN0MDLgW3bCODlF1QpChtqzXW0DGI3za1WdVwE38QuIrg-CYi0=s0	\N
\.


--
-- Name: work_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('work_id_seq', 59, true);


--
-- Name: _artists_eras_relationship_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _artists_eras_relationship
    ADD CONSTRAINT _artists_eras_relationship_pkey PRIMARY KEY (artist_id, era_id);


--
-- Name: _artists_media_relationship_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _artists_media_relationship
    ADD CONSTRAINT _artists_media_relationship_pkey PRIMARY KEY (artist_id, medium_id);


--
-- Name: _media_eras_relationship_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _media_eras_relationship
    ADD CONSTRAINT _media_eras_relationship_pkey PRIMARY KEY (medium_id, era_id);


--
-- Name: _media_works_relationship_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _media_works_relationship
    ADD CONSTRAINT _media_works_relationship_pkey PRIMARY KEY (medium_id, work_id);


--
-- Name: _works_eras_relationship_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _works_eras_relationship
    ADD CONSTRAINT _works_eras_relationship_pkey PRIMARY KEY (work_id, era_id);


--
-- Name: artist_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY artist
    ADD CONSTRAINT artist_pkey PRIMARY KEY (id);


--
-- Name: artists_works_relationship_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY artists_works_relationship
    ADD CONSTRAINT artists_works_relationship_pkey PRIMARY KEY (artist_id, work_id);


--
-- Name: era_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY era
    ADD CONSTRAINT era_name_key UNIQUE (name);


--
-- Name: era_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY era
    ADD CONSTRAINT era_pkey PRIMARY KEY (id);


--
-- Name: medium_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY medium
    ADD CONSTRAINT medium_name_key UNIQUE (name);


--
-- Name: medium_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY medium
    ADD CONSTRAINT medium_pkey PRIMARY KEY (id);


--
-- Name: work_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY work
    ADD CONSTRAINT work_pkey PRIMARY KEY (id);


--
-- Name: _artists_eras_relationship_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _artists_eras_relationship
    ADD CONSTRAINT _artists_eras_relationship_artist_id_fkey FOREIGN KEY (artist_id) REFERENCES artist(id);


--
-- Name: _artists_eras_relationship_era_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _artists_eras_relationship
    ADD CONSTRAINT _artists_eras_relationship_era_id_fkey FOREIGN KEY (era_id) REFERENCES era(id);


--
-- Name: _artists_media_relationship_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _artists_media_relationship
    ADD CONSTRAINT _artists_media_relationship_artist_id_fkey FOREIGN KEY (artist_id) REFERENCES artist(id);


--
-- Name: _artists_media_relationship_medium_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _artists_media_relationship
    ADD CONSTRAINT _artists_media_relationship_medium_id_fkey FOREIGN KEY (medium_id) REFERENCES medium(id);


--
-- Name: _media_eras_relationship_era_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _media_eras_relationship
    ADD CONSTRAINT _media_eras_relationship_era_id_fkey FOREIGN KEY (era_id) REFERENCES era(id);


--
-- Name: _media_eras_relationship_medium_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _media_eras_relationship
    ADD CONSTRAINT _media_eras_relationship_medium_id_fkey FOREIGN KEY (medium_id) REFERENCES medium(id);


--
-- Name: _media_works_relationship_medium_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _media_works_relationship
    ADD CONSTRAINT _media_works_relationship_medium_id_fkey FOREIGN KEY (medium_id) REFERENCES medium(id);


--
-- Name: _media_works_relationship_work_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _media_works_relationship
    ADD CONSTRAINT _media_works_relationship_work_id_fkey FOREIGN KEY (work_id) REFERENCES work(id);


--
-- Name: _works_eras_relationship_era_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _works_eras_relationship
    ADD CONSTRAINT _works_eras_relationship_era_id_fkey FOREIGN KEY (era_id) REFERENCES era(id);


--
-- Name: _works_eras_relationship_work_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY _works_eras_relationship
    ADD CONSTRAINT _works_eras_relationship_work_id_fkey FOREIGN KEY (work_id) REFERENCES work(id);


--
-- Name: artists_works_relationship_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY artists_works_relationship
    ADD CONSTRAINT artists_works_relationship_artist_id_fkey FOREIGN KEY (artist_id) REFERENCES artist(id);


--
-- Name: artists_works_relationship_work_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY artists_works_relationship
    ADD CONSTRAINT artists_works_relationship_work_id_fkey FOREIGN KEY (work_id) REFERENCES work(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

