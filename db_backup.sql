-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.38

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
-- Table structure for table `blog`
--

DROP TABLE IF EXISTS `blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog` (
  `blog_id` int NOT NULL AUTO_INCREMENT,
  `blog_fotoUrl` varchar(255) NOT NULL,
  `blog_content` text NOT NULL,
  `blog_readCount` int NOT NULL DEFAULT '0',
  `blog_title` varchar(255) NOT NULL,
  `user_id` int NOT NULL,
  `blog_date` datetime DEFAULT NULL,
  `blog_deleteTime` datetime DEFAULT NULL,
  `blog_updateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`blog_id`),
  UNIQUE KEY `blog_id` (`blog_id`),
  KEY `Blog_fk6` (`user_id`),
  CONSTRAINT `Blog_fk6` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (1,'https://i.cbc.ca/1.5848130.1674158749!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_780/milky-way-night-sky.jpg','testcontent1',0,'testtitle1',1,NULL,NULL,NULL),(2,'https://i.cbc.ca/1.5848130.1674158749!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_780/milky-way-night-sky.jpg','testcontent2',1,'contenttitle2',1,'2024-07-12 21:08:37',NULL,NULL),(3,'https://media.steelseriescdn.com/blog/posts/elden-ring-how-to-start-dlc/elden-ring-dlc-banner_714f7df9a2b5457fa92605bac5d5d837.jpg','When I gave Elden Ring a 10 two years ago, I did so not just because it’s an incredible game, but because it also raised the bar for open-world games as a whole. The way it encourages exploration, rewards curiosity, and challenges you to find your own individual solutions to difficult combat encounters by including tons of different viable weapons, spells, and other build options is absolutely exemplary. Now, FromSoftware is back to raise the bar on everyone yet again, this time when it comes to what you’d expect from a \"simple\" DLC. Shadow of the Erdtree may not do anything radically different from the base game, but this expansion somehow feels like a scaled-down version of that same experience that recaptures all of the magic of playing Elden Ring for the first time, with more content packed within than many fully priced games. Its unexpectedly large realm is filled with new secrets, new discoveries, a ton of new build options to experiment with, as well as some of the most challenging and unforgettable boss battles Souls fans will have ever seen.\r\n\r\nI strolled into Shadow of the Erdtree thinking I was some kind of Elden Lord badass, having defeated Malenia, Mohg, Placidusax, the Elden Beast, and every other big threat around. My level 150 character was armed with fully upgraded gear and the maximum number of flasks… but let me tell you, it did not take very long for the Realm of Shadow to humble me. Even though the only requirement to access the new areas is to beat Radahn and Mohg – which, granted, is no small feat – you’re going to want to over prepare before stepping foot into this new arena, because it is brutal. FromSoftware definitely skirts the line between fair and unfair with some of the later boss designs in particular, perhaps getting closer than ever. But crucially, it never actually crosses that threshold, and that masterful tightrope walk – along with some truly spectacular boss design – results in some of the most thrilling and satisfying bosses Elden Ring, and the entire Soulslike genre, has to offer.',3,'Elden Ring DLC Review',1,'2024-07-14 02:00:56',NULL,NULL),(4,'https://media.steelseriescdn.com/blog/posts/elden-ring-how-to-start-dlc/elden-ring-dlc-banner_714f7df9a2b5457fa92605bac5d5d837.jpg','When I gave Elden Ring a 10 two years ago, I did so not just because it’s an incredible game, but because it also raised the bar for open-world games as a whole. The way it encourages exploration, rewards curiosity, and challenges you to find your own individual solutions to difficult combat encounters by including tons of different viable weapons, spells, and other build options is absolutely exemplary. Now, FromSoftware is back to raise the bar on everyone yet again, this time when it comes to what you’d expect from a \"simple\" DLC. Shadow of the Erdtree may not do anything radically different from the base game, but this expansion somehow feels like a scaled-down version of that same experience that recaptures all of the magic of playing Elden Ring for the first time, with more content packed within than many fully priced games. Its unexpectedly large realm is filled with new secrets, new discoveries, a ton of new build options to experiment with, as well as some of the most challenging and unforgettable boss battles Souls fans will have ever seen.\r\n \r\n I strolled into Shadow of the Erdtree thinking I was some kind of Elden Lord badass, having defeated Malenia, Mohg, Placidusax, the Elden Beast, and every other big threat around. My level 150 character was armed with fully upgraded gear and the maximum number of flasks… but let me tell you, it did not take very long for the Realm of Shadow to humble me. Even though the only requirement to access the new areas is to beat Radahn and Mohg – which, granted, is no small feat – you’re going to want to over prepare before stepping foot into this new arena, because it is brutal. FromSoftware definitely skirts the line between fair and unfair with some of the later boss designs in particular, perhaps getting closer than ever. But crucially, it never actually crosses that threshold, and that masterful tightrope walk – along with some truly spectacular boss design – results in some of the most thrilling and satisfying bosses Elden Ring, and the entire Soulslike genre, has to offer.',101,'Elden Ring DLC Review2',1,'2024-07-14 02:02:39',NULL,NULL),(5,'https://media.steelseriescdn.com/blog/posts/elden-ring-how-to-start-dlc/elden-ring-dlc-banner_714f7df9a2b5457fa92605bac5d5d837.jpg','When I gave Elden Ring a 10 two years ago, I did so not just because it’s an incredible game, but because it also raised the bar for open-world games as a whole. The way it encourages exploration, rewards curiosity, and challenges you to find your own individual solutions to difficult combat encounters by including tons of different viable weapons, spells, and other build options is absolutely exemplary. Now, FromSoftware is back to raise the bar on everyone yet again, this time when it comes to what you’d expect from a \"simple\" DLC. Shadow of the Erdtree may not do anything radically different from the base game, but this expansion somehow feels like a scaled-down version of that same experience that recaptures all of the magic of playing Elden Ring for the first time, with more content packed within than many fully priced games. Its unexpectedly large realm is filled with new secrets, new discoveries, a ton of new build options to experiment with, as well as some of the most challenging and unforgettable boss battles Souls fans will have ever seen.\r\n \r\n I strolled into Shadow of the Erdtree thinking I was some kind of Elden Lord badass, having defeated Malenia, Mohg, Placidusax, the Elden Beast, and every other big threat around. My level 150 character was armed with fully upgraded gear and the maximum number of flasks… but let me tell you, it did not take very long for the Realm of Shadow to humble me. Even though the only requirement to access the new areas is to beat Radahn and Mohg – which, granted, is no small feat – you’re going to want to over prepare before stepping foot into this new arena, because it is brutal. FromSoftware definitely skirts the line between fair and unfair with some of the later boss designs in particular, perhaps getting closer than ever. But crucially, it never actually crosses that threshold, and that masterful tightrope walk – along with some truly spectacular boss design – results in some of the most thrilling and satisfying bosses Elden Ring, and the entire Soulslike genre, has to offer.',0,'Elden Ring DLC Review3 Updated1new',1,'2024-07-16 04:19:07','2024-07-17 03:49:07','2024-07-16 04:30:38'),(6,'https://media.steelseriescdn.com/blog/posts/elden-ring-how-to-start-dlc/elden-ring-dlc-banner_714f7df9a2b5457fa92605bac5d5d837.jpg','When I gave Elden Ring a 10 two years ago, I did so not just because it’s an incredible game, but because it also raised the bar for open-world games as a whole. The way it encourages exploration, rewards curiosity, and challenges you to find your own individual solutions to difficult combat encounters by including tons of different viable weapons, spells, and other build options is absolutely exemplary. Now, FromSoftware is back to raise the bar on everyone yet again, this time when it comes to what you’d expect from a \"simple\" DLC. Shadow of the Erdtree may not do anything radically different from the base game, but this expansion somehow feels like a scaled-down version of that same experience that recaptures all of the magic of playing Elden Ring for the first time, with more content packed within than many fully priced games. Its unexpectedly large realm is filled with new secrets, new discoveries, a ton of new build options to experiment with, as well as some of the most challenging and unforgettable boss battles Souls fans will have ever seen.\r\n \r\n I strolled into Shadow of the Erdtree thinking I was some kind of Elden Lord badass, having defeated Malenia, Mohg, Placidusax, the Elden Beast, and every other big threat around. My level 150 character was armed with fully upgraded gear and the maximum number of flasks… but let me tell you, it did not take very long for the Realm of Shadow to humble me. Even though the only requirement to access the new areas is to beat Radahn and Mohg – which, granted, is no small feat – you’re going to want to over prepare before stepping foot into this new arena, because it is brutal. FromSoftware definitely skirts the line between fair and unfair with some of the later boss designs in particular, perhaps getting closer than ever. But crucially, it never actually crosses that threshold, and that masterful tightrope walk – along with some truly spectacular boss design – results in some of the most thrilling and satisfying bosses Elden Ring, and the entire Soulslike genre, has to offer.',0,'Elden Ring DLC Review4',1,'2024-07-14 02:03:15','2024-07-16 03:59:16',NULL);
/*!40000 ALTER TABLE `blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_category`
--

DROP TABLE IF EXISTS `blog_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_category` (
  `blog_category_id` int NOT NULL AUTO_INCREMENT,
  `blog_category_name` varchar(50) NOT NULL,
  PRIMARY KEY (`blog_category_id`),
  UNIQUE KEY `blog_category_id` (`blog_category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_category`
--

LOCK TABLES `blog_category` WRITE;
/*!40000 ALTER TABLE `blog_category` DISABLE KEYS */;
INSERT INTO `blog_category` VALUES (1,'kategori1'),(2,'kategori2'),(3,'kategori3'),(4,'kategori4');
/*!40000 ALTER TABLE `blog_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_category_combiner`
--

DROP TABLE IF EXISTS `blog_category_combiner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_category_combiner` (
  `id` int NOT NULL AUTO_INCREMENT,
  `blog_id` int DEFAULT NULL,
  `blog_category_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_id` (`blog_id`),
  KEY `blog_category_id` (`blog_category_id`),
  CONSTRAINT `blog_category_combiner_ibfk_1` FOREIGN KEY (`blog_id`) REFERENCES `blog` (`blog_id`),
  CONSTRAINT `blog_category_combiner_ibfk_2` FOREIGN KEY (`blog_category_id`) REFERENCES `blog_category` (`blog_category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_category_combiner`
--

LOCK TABLES `blog_category_combiner` WRITE;
/*!40000 ALTER TABLE `blog_category_combiner` DISABLE KEYS */;
INSERT INTO `blog_category_combiner` VALUES (1,1,1),(2,1,2),(3,1,3),(4,2,1),(5,2,2),(6,2,3),(7,3,3),(8,4,2),(10,6,3),(15,5,1),(16,5,2),(17,5,3);
/*!40000 ALTER TABLE `blog_category_combiner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_comments`
--

DROP TABLE IF EXISTS `blog_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_comments` (
  `blogcom_id` int NOT NULL AUTO_INCREMENT,
  `blog_id` int NOT NULL,
  `blogcom_content` text NOT NULL,
  `blogcom_name` varchar(100) NOT NULL,
  `blogcom_email` varchar(100) NOT NULL,
  `blogcom_date` datetime DEFAULT NULL,
  `blogcom_deleteTime` datetime DEFAULT NULL,
  `blogcom_isDeleted` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`blogcom_id`),
  UNIQUE KEY `blogcom_id` (`blogcom_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_comments`
--

LOCK TABLES `blog_comments` WRITE;
/*!40000 ALTER TABLE `blog_comments` DISABLE KEYS */;
INSERT INTO `blog_comments` VALUES (1,1,'test yorum 12344321','toprak','topraktest@demo.com','2024-07-13 05:47:06',NULL,0),(2,4,'testyorum123','toprak','testdemo@test.com','2024-07-18 05:26:16','2024-07-22 14:09:47',1),(3,4,'test456','toprak1','toprak1@demo.com','2024-07-22 13:06:38','2024-07-22 14:03:12',1),(4,4,'dasdasdasd','toprak','toprak@demo123.com','2024-07-22 14:10:03',NULL,0),(5,4,'fasfasfasf','toprak2','toprak2@test.com','2024-07-22 14:10:12',NULL,0);
/*!40000 ALTER TABLE `blog_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(255) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Beverages'),(2,'Snacks'),(3,'Meat Products'),(4,'Bakery'),(5,'Electronics'),(6,'Fruits');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact` (
  `contact_id` int NOT NULL AUTO_INCREMENT,
  `contact_address` varchar(255) NOT NULL,
  `contact_phone` varchar(15) NOT NULL,
  `contact_supEmail` varchar(255) NOT NULL,
  `contact_isDeleted` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`contact_id`),
  UNIQUE KEY `contact_id` (`contact_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES `contact` WRITE;
/*!40000 ALTER TABLE `contact` DISABLE KEYS */;
INSERT INTO `contact` VALUES (1,'Coza Store Center 8th floor, 379 Hudson St, New York, NY 10018 US','+1 800 1236879','contact@example.com',0);
/*!40000 ALTER TABLE `contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_tickets`
--

DROP TABLE IF EXISTS `contact_tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact_tickets` (
  `ticket_id` int NOT NULL AUTO_INCREMENT,
  `ticket_email` varchar(255) NOT NULL,
  `ticket_deleteUid` int DEFAULT NULL,
  `ticket_deleteTime` date DEFAULT NULL,
  `ticket_isDeleted` tinyint(1) DEFAULT '0',
  `ticket_content` text NOT NULL,
  PRIMARY KEY (`ticket_id`),
  UNIQUE KEY `ticket_id` (`ticket_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_tickets`
--

LOCK TABLES `contact_tickets` WRITE;
/*!40000 ALTER TABLE `contact_tickets` DISABLE KEYS */;
INSERT INTO `contact_tickets` VALUES (1,'test@test.com',NULL,NULL,0,'DASDASDAS'),(2,'test1@test.com',NULL,NULL,0,'test123'),(3,'test123@demo.com',1,'2024-07-23',1,'5132513513513gfasgasgqweghgweqhhasgfgqwgwqgasgbewhwe4r12512gwegeq  312412 asgfasgasgas'),(5,'test123@demo.com',NULL,NULL,1,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris consequat consequat enim, non auctor massa ultrices non. Morbi sed odio massa. Quisque at vehicula tellus, sed tincidunt augue. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas varius egestas diam, eu sodales metus scelerisque congue. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas gravida justo eu arcu egestas convallis. Nullam eu erat bibendum, tempus ipsum eget, dictum enim. Donec non neque ut enim dapibus tincidunt vitae nec augue. Suspendisse potenti. Proin ut est diam. Donec condimentum euismod tortor, eget facilisis diam faucibus et. Morbi a tempor elit.\r\n\r\nDonec gravida lorem elit, quis condimentum ex semper sit amet. Fusce eget ligula magna. Aliquam aliquam imperdiet sodales. Ut fringilla turpis in vehicula vehicula. Pellentesque congue ac orci ut gravida. Aliquam erat volutpat. Donec iaculis lectus a arcu facilisis, eu sodales lectus sagittis. Etiam pellentesque, magna vel dictum rutrum, neque justo eleifend elit, vel tincidunt erat arcu ut sem. Sed rutrum, turpis ut commodo efficitur, quam velit convallis ipsum, et maximus enim ligula ac ligula.'),(6,'test123@demo.com',NULL,NULL,0,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris consequat consequat enim, non auctor massa ultrices non. Morbi sed odio massa. Quisque at vehicula tellus, sed tincidunt augue. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas varius egestas diam, eu sodales metus scelerisque congue. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas gravida justo eu arcu egestas convallis. Nullam eu erat bibendum, tempus ipsum eget, dictum enim. Donec non neque ut enim dapibus tincidunt vitae nec augue. Suspendisse potenti. Proin ut est diam. Donec condimentum euismod tortor, eget facilisis diam faucibus et. Morbi a tempor elit.\r\n \r\n Donec gravida lorem elit, quis condimentum ex semper sit amet. Fusce eget ligula magna. Aliquam aliquam imperdiet sodales. Ut fringilla turpis in vehicula vehicula. Pellentesque congue ac orci ut gravida. Aliquam erat volutpat. Donec iaculis lectus a arcu facilisis, eu sodales lectus sagittis. Etiam pellentesque, magna vel dictum rutrum, neque justo eleifend elit, vel tincidunt erat arcu ut sem. Sed rutrum, turpis ut commodo efficitur, quam velit convallis ipsum, et maximus enim ligula ac ligula.');
/*!40000 ALTER TABLE `contact_tickets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `category_id` int NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_price` int NOT NULL,
  `product_description` text NOT NULL,
  `product_coverPictureUrl` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  KEY `Product_fk1` (`category_id`),
  CONSTRAINT `Product_fk1` FOREIGN KEY (`category_id`) REFERENCES `category` (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,1,'Milk',25,'Cow milk',NULL),(2,2,'Ruffles',10,'Potato chips',NULL),(3,3,'Pork',100,'Pork meat',NULL),(5,4,'Bread',10,'Loaf of bread',NULL),(10,1,'Milk2',15,'Sütaş Süt',NULL),(13,2,'Nutella',70,'Jar of nutella','3'),(14,1,'Redbull',30,'Can of redbull',NULL),(15,5,'MSI CYBORG 15 A13VF-892XTR Intel Core i7 13620H 16GB 512GB SSD RTX4060 Freedos 15.6\" FHD 144Hz Taşınabilir Bilgisayar',35990,'İşlemci: Intel® Core™ i7-13620H (24M Cache, up to 4.90 GHz)\r\nİşletim Sistemi: FreeDOS\r\nEkran: 15.6\" FHD (1920*1080), 144Hz\r\nChipset: Integrated SoC\r\nEkran Kartı: RTX 4060, GDDR6 8GB\r\nEkran Kartı Watt Değeri: 35W+10W (Dynamic Boost ile)\r\nHafıza: DDR V 16GB (8GB*2, 5200MHz)\r\nHafıza yuvası: 2 Slot\r\nMaksimum Hafıza: Max 64GB\r\nDepolama Kapasitesi: 512GB NVMe SSD\r\nDepolama Seçenekleri: 1x M.2 SSD slot (NVMe PCIe Gen4)\r\nÖn Kamera: HD type (30fps@720p)\r\nKlavye: Blue Backlit Gaming Keyboard\r\nPil: 3-Cells, 53.5 Whr\r\nGüç Adaptörü: 120W\r\nBoyutlar: 359.36 x 250.34 x 21.95~22.9 mm\r\nAğırlık: 1.98 kg','2'),(16,5,'BenQ Zowie XL2566K 24.5\" 0,5ms 360Hz FHD 2xHDMI TN FreeSync Premium DyAc+ S-Switch Pivot',29919,'XL2566K, rekabetçi oyunculara optimize edilmiş akıcılık ve hızlı tepki vermenin yanı sıra amatörlerin ve profesyonellerin ellerinden gelenin en iyisini yapmalarına yardımcı olacak birçok özelleştirilebilir özelliği sunan amiral gemisi modelidir. Bir TN panelinde 360 Hz yenileme hızına ek olarak özel DyAc⁺™ teknolojisi ile XL2566K, kendi sınıfında pazarın tekliflerinden genel olarak daha net hareket netliği sağlar. XL2566K üzerindeki DyAc⁺™, püskürtme gibi güçlü oyun içi eylemleri XL2546K üzerindeki DyAc⁺™\'den daha net hale getirir. Netlik, oyuncuların hızlı hareketler veya hızlı hareket eden hedefler sırasında düşmanın konumunu daha kolay görmelerine ve mermi yörüngesini daha net fark etmelerine yardımcı olur, bu da geri tepme kontrolüne ve nişan almasına yardımcı olabilir.','1'),(17,6,'Green Apple (Kg)',50,'Green apple',NULL),(18,6,'Pineapple (1 Piece)',65,'1 piece of pineapple',NULL);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_picture`
--

DROP TABLE IF EXISTS `product_picture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_picture` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_picture_url` varchar(255) NOT NULL,
  `product_picture_url2` varchar(255) DEFAULT NULL,
  `product_picture_url3` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `product_id` (`product_id`),
  CONSTRAINT `Product_Picture_fk0` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_picture`
--

LOCK TABLES `product_picture` WRITE;
/*!40000 ALTER TABLE `product_picture` DISABLE KEYS */;
INSERT INTO `product_picture` VALUES (1,'https://images.migrosone.com/hemen/product/11010702/11010702-19e24b-1650x1650.png',NULL,NULL),(2,'https://biistek.com/Resim/Minik/1500x1500_thumb_st011631.jpg',NULL,NULL),(3,'https://gipsfarmfresh.in/wp-content/uploads/2023/08/Pork-Curry-Cut-Boneless.jpg',NULL,NULL),(5,'https://ankarahalkekmek.com.tr/wp-content/uploads/2020/11/nekmek.jpg',NULL,NULL),(10,'https://www.gurmar.com.tr/images/thumbs/0001230_sutas-yarim-yagli-uht-sut-1-lt_510.png',NULL,NULL),(13,'https://m.media-amazon.com/images/I/71wAkcBRaTL.jpg',NULL,NULL),(14,'https://images.migrosone.com/hemen/product/08110030/08110030-a4b666-1650x1650.png',NULL,NULL),(15,'https://productimages.hepsiburada.net/s/553/550/110000615410510.jpg','https://productimages.hepsiburada.net/s/553/550/110000615269515.jpg',NULL),(16,'https://productimages.hepsiburada.net/s/335/550/110000340361109.jpg','https://productimages.hepsiburada.net/s/335/550/110000340361110.jpg','https://productimages.hepsiburada.net/s/335/550/110000340361111.jpg'),(17,'https://yodeli.in/cdn/shop/products/green-apple-organic-fruit.png?v=1592523286',NULL,NULL),(18,'https://www.kroger.com/product/images/large/front/0000000004430',NULL,NULL);
/*!40000 ALTER TABLE `product_picture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_username` varchar(26) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `user_username` (`user_username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','$2b$12$/C/qoY7KarytEsLHjFiZLOysHnU82xMufJFcUUPsILQdIXO0meX4a'),(3,'testuser1','$2b$12$QcVYCRAFlmHcJ9Z.GpCYv.1b9TFYzPcpfn0ufrFnpeMfZWM1.9cha'),(4,'testuser','$2b$12$.eFWFXZU2LM/syP2.SXZru/DoV4DPrOP964V5HsKspKuQGO1q2PZm'),(5,'testuser2','$2b$12$5UHD6S8jDHqMfaWbWxtl9.g7dOnsGDLb8O42k/ABcqR3mTKDTFNz.'),(6,'blogger','$2b$12$Ip6i0SJrWvHRuuQ3/xKhIO/deuFYh.h85jYD4J6djxkItmRhsFot.');
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

-- Dump completed on 2024-07-24 10:35:12
