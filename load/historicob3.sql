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