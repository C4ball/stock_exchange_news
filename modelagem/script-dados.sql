CREATE TABLE `dados`.`cotacaob3` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `TIPREG` VARCHAR(300) NULL,
  `DATAPREG` VARCHAR(300) NOT NULL,
  `NOMERES` VARCHAR(300) NOT NULL,
  `MODREF` VARCHAR(300) NULL,
  `PREABE` VARCHAR(300) NULL,
  `PREMAX` VARCHAR(300) NULL,
  `PREMIN` VARCHAR(300) NULL,
  `PREMD` VARCHAR(300) NULL,
  `PREULT` VARCHAR(300) NULL,
  `PREOFC` VARCHAR(300) NULL,
  `PREOFV` VARCHAR(300) NULL,
  `CODISI` VARCHAR(300) NULL,
  PRIMARY KEY (`ID`, `DATAPREG`, `NOMERES`),
  INDEX `ID` (`ID` ASC))
  