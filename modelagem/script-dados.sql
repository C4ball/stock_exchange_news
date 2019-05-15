CREATE TABLE `cotacaob3` (
  `TIPREG` varchar(300) NOT NULL,
  `DATAPREG` varchar(300) NOT NULL,
  `CODNEG` varchar(300) NOT NULL,
  `NOMERES` varchar(300) DEFAULT NULL,
  `MODREF` varchar(300) DEFAULT NULL,
  `PREABE` varchar(300) DEFAULT NULL,
  `PREMAX` varchar(300) DEFAULT NULL,
  `PREMIN` varchar(300) DEFAULT NULL,
  `PREMD` varchar(300) DEFAULT NULL,
  `PREULT` varchar(300) DEFAULT NULL,
  `PREOFC` varchar(300) DEFAULT NULL,
  `PREOFV` varchar(300) DEFAULT NULL,
  `CODISI` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`DATAPREG`,`CODNEG`,`TIPREG`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `noticias` (
  `URL` varchar(3000) DEFAULT NULL,
  `EMPRESA` varchar(300) DEFAULT NULL,
  `DATA` varchar(300) DEFAULT NULL,
  `TITULO` varchar(1000) DEFAULT NULL,
  `ARTIGO` varchar(10000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `twitter` (
  `ID` varchar(300) NOT NULL,
  `CRIADO` varchar(300) DEFAULT NULL,
  `USER` varchar(100) DEFAULT NULL,
  `EMPRESA` varchar(100) DEFAULT NULL,
  `TEXTO` varchar(4000) DEFAULT NULL,
  `LINGUA` varchar(45) DEFAULT NULL,
  `RETWEET` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

########### PostgreSQL

DROP TABLE "dadosb3" ;
DROP TABLE "dadosnoticias";
DROP TABLE "dadostwitter";

CREATE TABLE "dadosb3" (
  "TIPREG" varchar(300) NOT NULL,
  "DATAPREG" varchar(300) NOT NULL,
  "CODNEG" varchar(300) NOT NULL,
  "NOMERES" varchar(300) DEFAULT NULL,
  "MODREF" varchar(300) DEFAULT NULL,
  "PREABE" varchar(300) DEFAULT NULL,
  "PREMAX" varchar(300) DEFAULT NULL,
  "PREMIN" varchar(300) DEFAULT NULL,
  "PREMD" varchar(300) DEFAULT NULL,
  "PREULT" varchar(300) DEFAULT NULL,
  "PREOFC" varchar(300) DEFAULT NULL,
  "PREOFV" varchar(300) DEFAULT NULL,
  "CODISI" varchar(300) DEFAULT NULL
) tablespace "dadostwitter";



CREATE TABLE "dadosnoticias" (
  "URL" varchar(3000) DEFAULT NULL,
  "EMPRESA" varchar(300) DEFAULT NULL,
  "DATA" varchar(300) DEFAULT NULL,
  "TITULO" varchar(1000) DEFAULT NULL,
  "ARTIGO" varchar(10000) DEFAULT NULL,
	PRIMARY KEY ("URL")
) tablespace "dadostwitter";


CREATE TABLE "dadostwitter" (
  "ID" varchar(300) NOT NULL,
  "CRIADO" varchar(300) DEFAULT NULL,
  "USER" varchar(100) DEFAULT NULL,
  "EMPRESA" varchar(100) DEFAULT NULL,
  "TEXTO" varchar(4000) DEFAULT NULL,
  "LINGUA" varchar(45) DEFAULT NULL,
  "RETWEET" varchar(45) DEFAULT NULL,
  PRIMARY KEY ("ID")
) tablespace "dadostwitter";


