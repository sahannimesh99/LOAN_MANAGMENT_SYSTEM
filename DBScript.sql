-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema web
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema web
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `web` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `web` ;
-- -----------------------------------------------------
-- Table `web`.`AccountHolders`
-- -----------------------------------------------------
CREATE TABLE `web`.`accountHolders`  (
  `holderID` INT NOT NULL ,
  `holdernmae` VARCHAR(45) ,
  `ammount` INT,
  PRIMARY KEY (`holderID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `web`.`LoanDetails`
-- -----------------------------------------------------
CREATE TABLE `web`.`loanDetails` (
    `loanID` INT NOT NULL,
    `loanReciverName` VARCHAR(45),
    `loanApproverName` VARCHAR(45),
    `ammount` INT NOT NULL,
    `refundDetails` BOOLEAN,
    PRIMARY KEY (`loanID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
 
