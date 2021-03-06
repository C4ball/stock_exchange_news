CREATE TABLE dadosb3 (
        TIPREG varchar(300),
        DATAPREG varchar(300),
        CODNEG varchar(300),
        NOMRES varchar(300),
        MODREF varchar(300),
        PREABE varchar(300),
        PREMAX varchar(300),
        PREMIN varchar(300),
        PREMD varchar(300),
        PREULT varchar(300),
        PREOFC varchar(300),
        PREOFV varchar(300),
        CODISI varchar(300),
        QUATOT varchar(300)
);

CREATE TABLE dadosb3_datas (
        TIPREG varchar(300), 
        DATAPREG varchar(300), 
        CODNEG varchar(300), 
        NOMRES varchar(300), 
        MODREF varchar(300), 
        PREABE varchar(300), 
        PREMAX varchar(300),
        PREMIN varchar(300), 
        PREMD  varchar(300), 
        PREULT varchar(300), 
        PREOFC varchar(300), 
        PREOFV varchar(300), 
        CODISI varchar(300), 
        QUATOT varchar(300),
        weekday varchar(300),
        week varchar(300), 
        month varchar(300), 
        year varchar(300), 
        day_1 varchar(300), 
        day_2 varchar(300), 
        day_3 varchar(300), 
        day_4 varchar(300),
        day_5 varchar(300), 
        week_2_w varchar(300), 
        week_2_y varchar(300), 
        week_3_w varchar(300), 
        week_3_y varchar(300), 
        week_4_w varchar(300),
        week_4_y varchar(300), 
        month_2_w varchar(300), 
        month_2_y varchar(300), 
        month_3_w varchar(300), 
        month_3_y varchar(300),
        month_4_w varchar(300), 
        month_4_y varchar(300)
);


CREATE TABLE historicob3_datas
AS
SELECT
	CAST(TIPREG AS int) as TIPREG,
        to_date(DATAPREG, 'YYYY-MM-DD') as DATAPREG,
        trim( BOTH FROM CODNEG) as CODNEG,
        trim( BOTH FROM NOMRES) as NOMRES,
        trim( BOTH FROM MODREF) as MODREF,
        CAST(PREABE AS float) as PREABE,
        CAST(PREMAX AS float) as PREMAX,
        CAST(PREMIN AS float) as PREMIN,
        CAST(PREMD AS float) as PREMD,
        CAST(PREULT AS float) as PREULT,
        CAST(PREOFC AS float) as PREOFC,
        CAST(PREOFV AS float) as PREOFV,
        trim( BOTH FROM CODISI) as CODISI,
        CAST(QUATOT AS float) as QUATOT,
        CAST(weekday AS float) as weekday,
        CAST(week AS float) as  week,
        CAST(month AS float) as  month,
        CAST(year AS float) as  year,
        day_1::date as  day_1,
        day_2::date as  day_2,
        day_3::date as  day_3,
        day_4::date as  day_4,
        day_5::date as  day_5, 
        CAST(week_2_w AS float) as week_2_w, 
        CAST(week_2_y AS float) as  week_2_y,
        CAST(week_3_w AS float) as  week_3_w,
        CAST(week_3_y AS float) as  week_3_y,
        CAST(week_4_w AS float) as  week_4_w,
        CAST(week_4_y AS float) as  week_4_y,
        CAST(month_2_w AS float) as  month_2_w,
        CAST(month_2_y AS float) as  month_2_y,
        CAST(month_3_w AS float) as  month_3_w,
        CAST(month_3_y AS float) as  month_3_y,
        CAST(month_4_w AS float) as  month_4_w,
        CAST(month_4_y AS float) as  month_4_y
FROM dadosb3_datas
;



INSERT INTO historicob3_datas
SELECT
	CAST(TIPREG AS int) as TIPREG,
        to_date(DATAPREG, 'YYYY-MM-DD') as DATAPREG,
        trim( BOTH FROM CODNEG) as CODNEG,
        trim( BOTH FROM NOMRES) as NOMRES,
        trim( BOTH FROM MODREF) as MODREF,
        CAST(PREABE AS float) as PREABE,
        CAST(PREMAX AS float) as PREMAX,
        CAST(PREMIN AS float) as PREMIN,
        CAST(PREMD AS float) as PREMD,
        CAST(PREULT AS float) as PREULT,
        CAST(PREOFC AS float) as PREOFC,
        CAST(PREOFV AS float) as PREOFV,
        trim( BOTH FROM CODISI) as CODISI,
        CAST(QUATOT AS float) as QUATOT,
        CAST(weekday AS float) as weekday,
        CAST(week AS float) as  week,
        CAST(month AS float) as  month,
        CAST(year AS float) as  year,
        CAST(day_1 AS float) as  day_1,
        CAST(day_2 AS float) as  day_2,
        CAST(day_3 AS float) as  day_3,
        CAST(day_4 AS float) as  day_4,
        CAST(day_5 AS float) as  day_5, 
        CAST(week_2_w AS float) as week_2_w, 
        CAST(week_2_y AS float) as  week_2_y,
        CAST(week_3_w AS float) as  week_3_w,
        CAST(week_3_y AS float) as  week_3_y,
        CAST(week_4_w AS float) as  week_4_w,
        CAST(week_4_y AS float) as  week_4_y,
        CAST(month_2_w AS float) as  month_2_w,
        CAST(month_2_y AS float) as  month_2_y,
        CAST(month_3_w AS float) as  month_3_w,
        CAST(month_3_y AS float) as  month_3_y,
        CAST(month_4_w AS float) as  month_4_w,
        CAST(month_4_y AS float) as  month_4_y
FROM dadosb3_datas
WHERE
    NOT EXISTS (
        SELECT DATAPREG, CODNEG FROM historicob3_datas 
		WHERE historicob3_datas.CODNEG = trim( BOTH FROM dadosb3_datas.CODNEG)
		AND historicob3_datas.DATAPREG = to_date(dadosb3_datas.DATAPREG, 'YYYYMMDD')
    );









CREATE TABLE historicob3
AS
SELECT
	CAST(TIPREG AS int) as TIPREG,
        to_date(DATAPREG, 'YYYYMMDD') as DATAPREG,
        trim( BOTH FROM CODNEG) as CODNEG,
        trim( BOTH FROM NOMRES) as NOMRES,
        trim( BOTH FROM MODREF) as MODREF,
        CAST(PREABE AS float) as PREABE,
        CAST(PREMAX AS float) as PREMAX,
        CAST(PREMIN AS float) as PREMIN,
        CAST(PREMD AS float) as PREMD,
        CAST(PREULT AS float) as PREULT,
        CAST(PREOFC AS float) as PREOFC,
        CAST(PREOFV AS float) as PREOFV,
        trim( BOTH FROM CODISI) as CODISI,
        CAST(QUATOT AS float) as QUATOT
FROM dadosb3
;



INSERT INTO dados_b3.historicob3
SELECT
	CAST(TIPREG AS int),
        to_date(DATAPREG, 'YYYYMMDD'),
        trim( BOTH FROM CODNEG),
        trim( BOTH FROM NOMRES),
        trim( BOTH FROM MODREF),
        CAST(PREABE AS float),
        CAST(PREMAX AS float),
        CAST(PREMIN AS float),
        CAST(PREMD AS float),
        CAST(PREULT AS float),
        CAST(PREOFC AS float),
        CAST(PREOFV AS float),
        trim( BOTH FROM CODISI),
        CAST(QUATOT AS float)
FROM dadosb3
WHERE
    NOT EXISTS (
        SELECT DATAPREG, CODNEG FROM historicob3 
		WHERE historicob3.CODNEG = trim( BOTH FROM dadosb3.CODNEG)
		AND historicob3.DATAPREG = to_date(dadosb3.DATAPREG, 'YYYYMMDD')
    );


CREATE TABLE dados_b3.historico_b3_N2 as (
SELECT 
d0.D0_DATAPREG,
D0.CODNEG,
D0.NOMRES,
D0.EMPRESA,
D0.week,
D0.MONTH,
D0.YEAR,
D0.day_1,	
D0.day_2,	
D0.day_3,	
D0.day_4,	
D0.day_5,	
D0.week_2_w,
D0.week_2_y,
D0.week_3_w,
D0.week_3_y,
D0.week_4_w,
D0.week_4_y,
D0.month_2_w,
D0.month_2_y,
D0.month_3_w,
D0.month_3_y,
D0.month_4_w,
D0.month_4_y,
D0.PREABE_D0,
D0.PREULT_D0,
D0.QUATOT_D0,
D0.VARI_D0,

D0.PREABE_D1,
D0.PREMAX_D1,
D0.PREMIN_D1, 
D0.PREMD__D1,
D0.PREULT_D1,
D0.PREOFC_D1,
D0.PREOFV_D1,
D0.QUATOT_D1,
D0.VARI_D1,

D0.PREABE_D2,
D0.PREMAX_D2,
D0.PREMIN_D2, 
D0.PREMD__D2,
D0.PREULT_D2,
D0.PREOFC_D2,
D0.PREOFV_D2,
D0.QUATOT_D2,
D0.VARI_D2,

D0.PREABE_D3,
D0.PREMAX_D3,
D0.PREMIN_D3, 
D0.PREMD__D3,
D0.PREULT_D3,
D0.PREOFC_D3,
D0.PREOFV_D3,
D0.QUATOT_D3,
D0.VARI_D3,

D0.PREABE_D4,
D0.PREMAX_D4,
D0.PREMIN_D4, 
D0.PREMD__D4,
D0.PREULT_D4,
D0.PREOFC_D4,
D0.PREOFV_D4,
D0.QUATOT_D4,
D0.VARI_D4,

D0.PREABE_D5,
D0.PREMAX_D5,
D0.PREMIN_D5, 
D0.PREMD__D5,
D0.PREULT_D5,
D0.PREOFC_D5,
D0.PREOFV_D5,
D0.QUATOT_D5,
D0.VARI_D5,

D0.PREABE_W2,
D0.PREMAX_W2,
D0.PREMIN_W2, 
D0.PREMD__W2,
D0.PREULT_W2,
D0.PREOFC_W2,
D0.PREOFV_W2,
D0.QUATOT_W2,
D0.VARI_W2,

D0.PREABE_W3,
D0.PREMAX_W3,
D0.PREMIN_W3, 
D0.PREMD__W3,
D0.PREULT_W3,
D0.PREOFC_W3,
D0.PREOFV_W3,
D0.QUATOT_W3,
D0.VARI_W3,

D0.PREABE_W4,
D0.PREMAX_W4,
D0.PREMIN_W4, 
D0.PREMD__W4,
D0.PREULT_W4,
D0.PREOFC_W4,
D0.PREOFV_W4,
D0.QUATOT_W4,
D0.VARI_W4,

D0.PREABE_M2,
D0.PREMAX_M2,
D0.PREMIN_M2, 
D0.PREMD__M2,
D0.PREULT_M2,
D0.PREOFC_M2,
D0.PREOFV_M2,
D0.QUATOT_M2,
D0.VARI_M2,

D0.PREABE_M3,
D0.PREMAX_M3,
D0.PREMIN_M3, 
D0.PREMD__M3,
D0.PREULT_M3,
D0.PREOFC_M3,
D0.PREOFV_M3,
D0.QUATOT_M3,
D0.VARI_M3,

D1.TITLE_SENTIMENT_AVG AS TITLE_SENTIMENT_AVG_D1,
D1.TEXT_SENTIMENT_AVG AS TEXT_SENTIMENT_AVG_D1,
D1.QTD_NOTICIA AS QTD_NOTICIA_D1,
D1.QTD_NOTICIA_POS AS QTD_NOTICIA_POS_D1,
D1.QTD_NOTICIA_NEG AS QTD_NOTICIA_NEG_D1,
D1.QTD_TITLE_POS AS QTD_TITLE_POS_D1,
D1.QTD_TITLE_NEG AS QTD_TITLE_NEG_D1,

D2.TITLE_SENTIMENT_AVG AS TITLE_SENTIMENT_AVG_D2,
D2.TEXT_SENTIMENT_AVG AS TEXT_SENTIMENT_AVG_D2,
D2.QTD_NOTICIA AS QTD_NOTICIA_D2,
D2.QTD_NOTICIA_POS AS QTD_NOTICIA_POS_D2,
D2.QTD_NOTICIA_NEG AS QTD_NOTICIA_NEG_D2,
D2.QTD_TITLE_POS AS QTD_TITLE_POS_D2,
D2.QTD_TITLE_NEG AS QTD_TITLE_NEG_D2,

D3.TITLE_SENTIMENT_AVG AS TITLE_SENTIMENT_AVG_D3,
D3.TEXT_SENTIMENT_AVG AS TEXT_SENTIMENT_AVG_D3,
D3.QTD_NOTICIA AS QTD_NOTICIA_D3,
D3.QTD_NOTICIA_POS AS QTD_NOTICIA_POS_D3,
D3.QTD_NOTICIA_NEG AS QTD_NOTICIA_NEG_D3,
D3.QTD_TITLE_POS AS QTD_TITLE_POS_D3,
D3.QTD_TITLE_NEG AS QTD_TITLE_NEG_D3,

D4.TITLE_SENTIMENT_AVG AS TITLE_SENTIMENT_AVG_D4,
D4.TEXT_SENTIMENT_AVG AS TEXT_SENTIMENT_AVG_D4,
D4.QTD_NOTICIA AS QTD_NOTICIA_D4,
D4.QTD_NOTICIA_POS AS QTD_NOTICIA_POS_D4,
D4.QTD_NOTICIA_NEG AS QTD_NOTICIA_NEG_D4,
D4.QTD_TITLE_POS AS QTD_TITLE_POS_D4,
D4.QTD_TITLE_NEG AS QTD_TITLE_NEG_D4,

D5.TITLE_SENTIMENT_AVG AS TITLE_SENTIMENT_AVG_D5,
D5.TEXT_SENTIMENT_AVG AS TEXT_SENTIMENT_AVG_D5,
D5.QTD_NOTICIA AS QTD_NOTICIA_D5,
D5.QTD_NOTICIA_POS AS QTD_NOTICIA_POS_D5,
D5.QTD_NOTICIA_NEG AS QTD_NOTICIA_NEG_D5,
D5.QTD_TITLE_POS AS QTD_TITLE_POS_D5,
D5.QTD_TITLE_NEG AS QTD_TITLE_NEG_D5,

AVG(W2.TITLE_SENTIMENT_AVG) AS TITLE_SENTIMENT_AVG_W2,
AVG(W2.TEXT_SENTIMENT_AVG) AS TEXT_SENTIMENT_AVG_W2,
SUM(W2.QTD_NOTICIA) AS QTD_NOTICIA_W2,
SUM(W2.QTD_NOTICIA_POS) AS QTD_NOTICIA_POS_W2,
SUM(W2.QTD_NOTICIA_NEG) AS QTD_NOTICIA_NEG_W2,
SUM(W2.QTD_TITLE_POS) AS QTD_TITLE_POS_W2,
SUM(W2.QTD_TITLE_NEG) AS QTD_TITLE_NEG_W2,


AVG(W3.TITLE_SENTIMENT_AVG) AS TITLE_SENTIMENT_AVG_W3,
AVG(W3.TEXT_SENTIMENT_AVG) AS TEXT_SENTIMENT_AVG_W3,
SUM(W3.QTD_NOTICIA) AS QTD_NOTICIA_W3,
SUM(W3.QTD_NOTICIA_POS) AS QTD_NOTICIA_POS_W3,
SUM(W3.QTD_NOTICIA_NEG) AS QTD_NOTICIA_NEG_W3,
SUM(W3.QTD_TITLE_POS) AS QTD_TITLE_POS_W3,
SUM(W3.QTD_TITLE_NEG) AS QTD_TITLE_NEG_W3,


AVG(W4.TITLE_SENTIMENT_AVG) AS TITLE_SENTIMENT_AVG_W4,
AVG(W4.TEXT_SENTIMENT_AVG) AS TEXT_SENTIMENT_AVG_W4,
SUM(W4.QTD_NOTICIA) AS QTD_NOTICIA_W4,
SUM(W4.QTD_NOTICIA_POS) AS QTD_NOTICIA_POS_W4,
SUM(W4.QTD_NOTICIA_NEG) AS QTD_NOTICIA_NEG_W4,
SUM(W4.QTD_TITLE_POS) AS QTD_TITLE_POS_W4,
SUM(W4.QTD_TITLE_NEG) AS QTD_TITLE_NEG_W4,


AVG(M2.TITLE_SENTIMENT_AVG) AS TITLE_SENTIMENT_AVG_M2,
AVG(M2.TEXT_SENTIMENT_AVG) AS TEXT_SENTIMENT_AVG_M2,
SUM(M2.QTD_NOTICIA) AS QTD_NOTICIA_M2,
SUM(M2.QTD_NOTICIA_POS) AS QTD_NOTICIA_POS_M2,
SUM(M2.QTD_NOTICIA_NEG) AS QTD_NOTICIA_NEG_M2,
SUM(M2.QTD_TITLE_POS) AS QTD_TITLE_POS_M2,
SUM(M2.QTD_TITLE_NEG) AS QTD_TITLE_NEG_M2,


AVG(M3.TITLE_SENTIMENT_AVG) AS TITLE_SENTIMENT_AVG_M3,
AVG(M3.TEXT_SENTIMENT_AVG) AS TEXT_SENTIMENT_AVG_M3,
SUM(M3.QTD_NOTICIA) AS QTD_NOTICIA_M3,
SUM(M3.QTD_NOTICIA_POS) AS QTD_NOTICIA_POS_M3,
SUM(M3.QTD_NOTICIA_NEG) AS QTD_NOTICIA_NEG_M3,
SUM(M3.QTD_TITLE_POS) AS QTD_TITLE_POS_M3,
SUM(M3.QTD_TITLE_NEG) AS QTD_TITLE_NEG_M3

FROM dados_b3.historico_b3_N D0

LEFT JOIN dados_b3.SENTIMENTOS_EMPRESAS D1
	on d1.DATA = D0.DAY_1
	AND D1.EMPRESA = D0.EMPRESA

LEFT JOIN dados_b3.SENTIMENTOS_EMPRESAS D2
	on D2.DATA = D0.DAY_2
	AND D2.EMPRESA = D0.EMPRESA

LEFT JOIN dados_b3.SENTIMENTOS_EMPRESAS D3
	on D3.DATA = D0.DAY_3
	AND D3.EMPRESA = D0.EMPRESA

LEFT JOIN dados_b3.SENTIMENTOS_EMPRESAS D4
	on D4.DATA = D0.DAY_4
	AND D4.EMPRESA = D0.EMPRESA

LEFT JOIN dados_b3.SENTIMENTOS_EMPRESAS D5
	on D5.DATA = D0.DAY_5
	AND D5.EMPRESA = D0.EMPRESA

LEFT JOIN dados_b3.SENTIMENTOS_EMPRESAS W2
	on W2.WEEK = D0.week_2_w
	AND W2.YEAR = D0.week_2_y
	AND W2.EMPRESA = D0.EMPRESA


LEFT JOIN dados_b3.SENTIMENTOS_EMPRESAS W3
	on W3.WEEK = D0.week_3_w
	AND W3.YEAR = D0.week_3_y
	AND W3.EMPRESA = D0.EMPRESA


LEFT JOIN dados_b3.SENTIMENTOS_EMPRESAS W4
	on W4.WEEK = D0.week_4_w
	AND W4.YEAR = D0.week_4_y
	AND W4.EMPRESA = D0.EMPRESA


LEFT JOIN dados_b3.SENTIMENTOS_EMPRESAS M2
	on M2.MONTH = D0.month_2_w
	AND M2.YEAR = D0.month_2_Y
	AND M2.EMPRESA = D0.EMPRESA


LEFT JOIN dados_b3.SENTIMENTOS_EMPRESAS M3
	on M3.MONTH = D0.month_3_w
	AND M3.YEAR = D0.month_3_Y
	AND M3.EMPRESA = D0.EMPRESA


GROUP BY 	
			01,02,03,04,05,06,07,08,09,10,
			11,12,13,14,15,16,17,18,19,20,
			21,22,23,24,25,26,27,28,29,30,
			31,32,33,34,35,36,37,38,39,40,
			41,42,43,44,45,46,47,48,49,50,
			51,52,53,54,55,56,57,58,59,60,
			61,62,63,64,65,66,67,68,69,70,
			71,72,73,74,75,76,77,78,79,80,
			81,82,83,84,85,86,87,88,89,90,
			91,92,93,94,95,96,97,98,99,100,
			101,102,103,104,105,106,107,108,109,110,
			111,112,113,114,115,116,117,118,119,120,
			121,122,123,124,125,126,127,128,129,130,
			131,132,133,134,135,136,137,138,139,140,
			141,142,143,144,145,146,147,148,149,150,
			151,152,153
);


