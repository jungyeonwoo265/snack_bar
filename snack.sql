-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: snack
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bom`
--

DROP TABLE IF EXISTS `bom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bom` (
  `상품명` text,
  `재료` text,
  `수량` text,
  `단위` text,
  `단가` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bom`
--

LOCK TABLES `bom` WRITE;
/*!40000 ALTER TABLE `bom` DISABLE KEYS */;
INSERT INTO `bom` VALUES ('김밥','우엉','30','g','254'),('김밥','오이','50','g','463'),('김밥','계란','1','개','226'),('김밥','햄','30','g','171'),('김밥','당근','40','g','239'),('김밥','어묵','1','장','557'),('김밥','맛살','50','g','448'),('김밥','단무지','30','g','131'),('참치김밥','우엉','30','g','254'),('참치김밥','오이','50','g','463'),('참치김밥','계란','1','개','226'),('참치김밥','햄','30','g','171'),('참치김밥','당근','40','g','239'),('참치김밥','어묵','1','장','557'),('참치김밥','맛살','50','g','448'),('참치김밥','단무지','30','g','131'),('참치김밥','참치','50','g','845'),('치즈김밥','우엉','30','g','254'),('치즈김밥','오이','50','g','463'),('치즈김밥','계란','1','개','226'),('치즈김밥','햄','30','g','171'),('치즈김밥','당근','40','g','239'),('치즈김밥','어묵','1','장','557'),('치즈김밥','맛살','50','g','448'),('치즈김밥','단무지','30','g','131'),('치즈김밥','치즈','1','장','217'),('떡볶이','떡','400','g','720'),('떡볶이','물','500','ml','200'),('떡볶이','대파','50','g','160'),('떡볶이','설탕','20','g','26'),('떡볶이','간장','8','g','11'),('떡볶이','고추장','40','g','588'),('떡볶이','고추가루','40','g','440'),('라볶이','떡','400','g','720'),('라볶이','물','500','ml','200'),('라볶이','대파','50','g','160'),('라볶이','설탕','20','g','26'),('라볶이','간장','8','g','11'),('라볶이','고추장','40','g','588'),('라볶이','고추가루','40','g','440'),('라볶이','라면사리','1','개','258'),('치즈떡볶이','떡','400','g','720'),('치즈떡볶이','물','500','ml','200'),('치즈떡볶이','대파','50','g','160'),('치즈떡볶이','설탕','20','g','26'),('치즈떡볶이','간장','8','g','11'),('치즈떡볶이','고추장','40','g','588'),('치즈떡볶이','고추가루','40','g','440'),('치즈떡볶이','치즈','1','개','217'),('돼지김치찌개','돼지고기','300','g','2514'),('돼지김치찌개','설탕','10','g','14'),('돼지김치찌개','간장','12','g','17'),('돼지김치찌개','대파','50','g','160'),('돼지김치찌개','청양고추','15','g','104'),('돼지김치찌개','물','2000','ml','800'),('돼지김치찌개','새우젓','10','g','105'),('돼지김치찌개','김치','800','g','984'),('돼지김치찌개','고추가루','30','g','330'),('돼지김치찌개','양파','150','g','357'),('돼지김치찌개','다진마늘','4','g','10'),('돼지김치찌개','들기름','8','g','98'),('돼지김치찌개','된장','20','g','38'),('참치김치찌개','설탕','10','g','14'),('참치김치찌개','간장','12','g','17'),('참치김치찌개','대파','50','g','160'),('참치김치찌개','청양고추','15','g','104'),('참치김치찌개','물','2000','ml','800'),('참치김치찌개','새우젓','10','g','105'),('참치김치찌개','김치','800','g','984'),('참치김치찌개','고추가루','30','g','330'),('참치김치찌개','양파','150','g','357'),('참치김치찌개','다진마늘','4','g','10'),('참치김치찌개','들기름','8','g','98'),('참치김치찌개','된장','20','g','38'),('참치김치찌개','참치','50','g','845');
/*!40000 ALTER TABLE `bom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `buisness`
--

DROP TABLE IF EXISTS `buisness`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buisness` (
  `아이디` text,
  `비밀번호` text,
  `이름` text,
  `주소` text,
  `전화번호` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buisness`
--

LOCK TABLES `buisness` WRITE;
/*!40000 ALTER TABLE `buisness` DISABLE KEYS */;
/*!40000 ALTER TABLE `buisness` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `재료` text,
  `수량` text,
  `단위` text,
  `단가` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('간장','0','g','1.38'),('계란','0','개','226'),('고추가루','0','g','11'),('고추장','0','g','14.7'),('김치','0','g','1.23'),('다진마늘','0','g','2.3'),('단무지','0','g','4.34'),('당근','0','g','5.97'),('대파','0','g','3.2'),('돼지고기','0','g','8.38'),('된장','0','g','1.89'),('들기름','0','g','12.22'),('떡','0','g','1.8'),('라면사리','0','개','258'),('맛살','0','g','8.9'),('물','0','ml','0.4'),('새우젓','0','ml','10.45'),('설탕','0','g','1.31'),('양파','0','g','2.38'),('어묵','0','장','1114'),('오이','0','g','9.25'),('우엉','0','g','8.44'),('참치','0','g','16.9'),('청양고추','0','개','6.9'),('치즈','0','장','216.9'),('햄','0','g','5.7'),('김밥','0','개','7500'),('참치김밥','0','개','8200'),('치즈김밥','0','개','9900'),('떡복이','0','개','6500'),('라볶이','0','개','7300'),('치즈떡복이','0','개','7100'),('돼지김치찌개','0','개','16600'),('참치김치찌개','0','개','11600');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `주문번호` text,
  `아이디` text,
  `상품명` text,
  `수량` text,
  `주문시간` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `주문번호` text,
  `아이디` text,
  `문의내용` text,
  `문의시간` text,
  `답변` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `아이디` text,
  `비밀번호` text,
  `이름` text,
  `주소` text,
  `전화번호` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-16 17:28:55
