-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 09, 2022 at 06:01 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `palamtech`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `adminID` int(11) NOT NULL,
  `adminName` varchar(255) NOT NULL,
  `adminEmail` varchar(255) NOT NULL,
  `adminPass` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`adminID`, `adminName`, `adminEmail`, `adminPass`) VALUES
(1, 'Administrator', 'admin@gmail.com', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `casing`
--

CREATE TABLE `casing` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `casing`
--

INSERT INTO `casing` (`id`, `name`, `brand`, `price`) VALUES
(1, 'AIGO DLM 21 MESH BLACK MATX CASING w/ 4 ARGB FAN', 'AIGO', 229),
(2, 'AIGO DLM 21 MESH WHITE MATX CASING W/ 4 ARGB FAN', 'AIGO', 229),
(3, 'AIGO DLM 22 PINK MATX CASING W/ 3 RGB FAN', 'AIGO', 189),
(4, 'INVASION H-1 MATX CASING W/ 6 ARGB FAN', 'INVASION', 209),
(5, 'SEGOTEP PRIMEM MATX CASING W/ 3 RGB FAN', 'SEGOTEP', 159),
(9, 'NZXT H510 FLOW MATTE WHITE', 'NZXT', 399),
(10, 'TECWARE NEXUS M2 BLACK MATX CASING w/ 3 FAN', 'TECWARE', 129),
(11, 'TECWARE NEXUS AIR M WHITE MATX CASING w/ 4 ARGB FAN', 'TECWARE', 198),
(12, 'TECWARE FORGE S BLACK w/ 4 ARGB FAN', 'TECWARE', 248),
(13, 'MONTECH AIR 100 BLACK MATX w/ 4 ARGB FAN', 'MONTECH', 190),
(14, 'LIAN LI O11 DYNAMIC BLACK', 'LIAN LI', 700),
(15, 'LIAN LI O11 Dynamic Mini White', 'LIAN LI', 776),
(16, 'SEGOTEP LUX S WHITE', 'SEGOTEP', 201),
(17, 'COOLER MASTER NR200P White', 'COOLER MASTER', 330);

-- --------------------------------------------------------

--
-- Table structure for table `cpu`
--

CREATE TABLE `cpu` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cpu`
--

INSERT INTO `cpu` (`id`, `name`, `brand`, `price`) VALUES
(1, 'INTEL I3 10100 (4C/8T)', 'INTEL', 549),
(2, 'AMD RYZEN 5 3600 (6C/12T)', 'AMD', 859),
(3, 'AMD RYZEN 3 3100 (4C/8T)', 'AMD', 499),
(4, 'INTEL I5 10400 (6C/12T)', 'INTEL', 699),
(5, 'INTEL I7 10700F (8C/16T)', 'INTEL', 1299),
(6, 'AMD RYZEN 9 5900X (12/24T)', 'AMD', 1900),
(7, 'AMD RYZEN 7 5800X (8C/16T)', 'AMD', 1600),
(8, 'INTEL I5 11400 (6C/12T)', 'INTEL', 799),
(9, 'AMD RYZEN 3 3300X (4C/8T)', 'AMD', 599),
(10, 'INTEL I9 12900K (16C/24T)', 'INTEL', 2599),
(12, 'INTEL I7 12700KF', 'INTEL', 1649),
(13, 'INTEL I5 12400F (6C/12T)', 'INTEL', 779),
(14, 'AMD RYZEN 5 3600 (6C/12T)', 'AMD', 669),
(15, 'INTEL I3 10105F (4C/8T)', 'INTEL', 369);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `custEmail` varchar(255) NOT NULL,
  `custName` varchar(255) NOT NULL,
  `custPhoneNo` varchar(255) NOT NULL,
  `custAdd` varchar(255) NOT NULL,
  `custPass` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `custEmail`, `custName`, `custPhoneNo`, `custAdd`, `custPass`) VALUES
(4, 'arif@gmail.com', 'Arif azhar', '234234234234', 'ampang', '123');

-- --------------------------------------------------------

--
-- Table structure for table `feedbacks`
--

CREATE TABLE `feedbacks` (
  `fbID` int(11) NOT NULL,
  `custEmail` varchar(255) NOT NULL,
  `fbType` varchar(255) NOT NULL,
  `fbDate` date NOT NULL,
  `fbDesc` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `gpu`
--

CREATE TABLE `gpu` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gpu`
--

INSERT INTO `gpu` (`id`, `name`, `brand`, `price`) VALUES
(1, 'GALAX RTX 2060 (1-CLICK OC) 6GB DDR6', 'GALAX', 2550),
(2, 'COLORFUL GAME RTX 3070 ADVANCED OC 8GB DDR6', 'COLORFUL IGAME', 3599),
(3, 'SAPPHIRE NITRO+ RX 590 8GB DDR5', 'AMD', 850),
(4, 'GIGABYTE GTX 1650 SUPER WINDFORCE 4GB DDR6', 'GIGABYTE', 849),
(5, 'ZOTAC GTX 1650 AMP CORE 4GB DDR6', 'ZOTAC', 1199),
(6, 'COLORFUL GTX 1650 SUPER NB 4GB DDR6', 'COLORFUL IGAME', 1200),
(7, 'ASUS TUF GTX 1660 SUPER GAMING OC 6GB DDR6', 'ASUS', 1799),
(9, 'ZOTAC RTX 3060 TWIN EDGE OC 12GB DDR6', 'ZOTAC', 1949),
(10, 'COLORFUL IGAME RTX 3050 ULTRA WHITE DUO OC 8GB DDR6', 'COLORFUL', 2029),
(11, 'MSI GTX 1650 VENTUS XS OC 4GB DDR6', 'MSI', 1199),
(12, 'ZOTAC RTX 3060 TWIN EDGE OC 12GB DDR6', 'ZOTAC', 1949),
(13, 'COLORFUL GTX 1650 NB 4GB DDR6', 'COLORFUL', 999),
(14, 'COLORFUL RTX 3050 NB EX 8GB GDDR6', 'COLORFUL', 1699),
(15, 'COLORFUL RTX 3070 TI NB 8GB GDDR6', 'COLORFUL ', 3800),
(16, 'ZOTAC RTX 3050 TWIN EDGE OC 8GB GDDR6', 'ZOTAC', 1599),
(17, 'INNO3D RTX 3070 TI X3 OC 8GB DRR6', 'INNO3D', 3488),
(18, 'ZOTAC RTX 3070Ti TRINITY OC 8GB GDDR6', 'ZOTAC', 3298);

-- --------------------------------------------------------

--
-- Table structure for table `mb`
--

CREATE TABLE `mb` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mb`
--

INSERT INTO `mb` (`id`, `name`, `brand`, `price`) VALUES
(1, 'GIGABYTE B450M S2H', 'GIGABYTE', 349),
(2, 'MSI B450M MORTAR MAX', '469', 469),
(3, 'ASROCK B450M STEEL LEGEND', 'ASROCK', 389),
(4, 'GIGABYTE B550 AORUS ELITE', 'GIGABYTE', 750),
(5, 'GIGABYTE B550M AORUS ELITE', 'GIGABYTE', 549),
(6, 'MSI MAG B550 TOMAHAWK', 'MSI', 749),
(7, 'MSI MPG B550 GAMING PLUS', 'MSI', 749),
(8, 'GIGABYTE B450M DS3H', 'GIGABYTE', 359),
(13, 'GIGABYTE Z690 UD AX DDR4', 'GIGABYTE', 1099),
(14, 'GIGABYTE B660M DS3H AX', 'GIGABYTE', 645),
(15, 'GIGABYTE H410M S2H V3', 'GIGABYTE', 285),
(16, 'ASROCK B550 PG RIPTIDE', 'ASROCK', 659),
(17, 'MSI B560M-A PRO', 'MSI', 395),
(18, 'GIGABYTE B550M AORUS ELITE', 'GIGABYTE', 845),
(19, 'ASUS B560M-A PRIME', 'ASUS', 358),
(20, 'MSI B550M PRO-VDH', 'MSI', 399),
(21, 'GIGABYTE B550M DS3H', 'GIGABYTE', 395);

-- --------------------------------------------------------

--
-- Table structure for table `pcpackage`
--

CREATE TABLE `pcpackage` (
  `id` int(11) NOT NULL,
  `casing` int(11) NOT NULL,
  `mb` int(11) NOT NULL,
  `gpu` int(11) NOT NULL,
  `ram` int(11) NOT NULL,
  `ssd` int(11) NOT NULL,
  `psu` int(11) NOT NULL,
  `cpu` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pcpackage`
--

INSERT INTO `pcpackage` (`id`, `casing`, `mb`, `gpu`, `ram`, `ssd`, `psu`, `cpu`) VALUES
(11, 1, 14, 9, 5, 7, 8, 13),
(12, 1, 8, 10, 6, 8, 8, 2),
(13, 10, 15, 11, 7, 8, 9, 15),
(14, 1, 14, 12, 5, 7, 8, 13),
(15, 1, 21, 10, 6, 8, 10, 2),
(16, 10, 15, 13, 7, 8, 9, 15),
(17, 11, 21, 10, 6, 8, 10, 14),
(18, 12, 16, 15, 5, 7, 11, 7),
(19, 1, 21, 6, 4, 1, 8, 2),
(20, 10, 15, 6, 7, 8, 9, 15),
(21, 15, 17, 18, 2, 3, 15, 10),
(22, 9, 6, 18, 2, 3, 15, 6),
(23, 9, 13, 15, 6, 3, 6, 12),
(24, 12, 8, 3, 4, 8, 9, 9);

-- --------------------------------------------------------

--
-- Table structure for table `psu`
--

CREATE TABLE `psu` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `psu`
--

INSERT INTO `psu` (`id`, `name`, `brand`, `price`) VALUES
(1, 'INVASION CORE-650W 80+ BRONZE', 'INVASION', 229),
(2, 'SILVERSTONE DA 650W 80+ GOLD FULL MODULAR', 'SILVERSTONE', 389),
(3, 'FSP HYDRO K SERIES 500W 80+ BRONZE', 'FSP', 209),
(4, 'CORSAIR CV650 80+ Bronze', 'CORSAIR', 250),
(5, 'SILVERSTONE ST5OF-ES2500W 80+ WHITE', 'SILVERSTONE', 179),
(6, 'GIGABYTE P850GM 850W 80+ GOLD FULL MODULAR', 'GIGABYTE', 499),
(8, 'FSP HV PRO 650W 80+ BRONZE', 'FSP', 300),
(9, 'COUGAR XTC650 80+ WHITE', 'COUGAR', 185),
(10, 'FSP HV PRO 650W 80+ BRONZE', 'FSP', 229),
(11, 'SILVERSTONE DA 750W 80+ GOLD', 'SILVERSTONE', 579),
(12, 'GIGABYTE P850GM 850W 80+ GOLD FULL MODULAR', 'GIGABYTE', 455),
(13, 'GIGABYTE P650B 650W 80+ BRONZE', 'GIGABYTE', 309),
(14, 'SEGOTEP SG-950G 850W 80+ Gold Full Modular', 'SEGOTEP', 385),
(15, 'SILVERSTONE DA750W 80+ GOLD FULL MODULAR', 'SILVERSTONE', 630),
(16, 'FSP Dagger 650W Pro SFX 80+ Gold Full Modular', 'FSP', 558);

-- --------------------------------------------------------

--
-- Table structure for table `ram`
--

CREATE TABLE `ram` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ram`
--

INSERT INTO `ram` (`id`, `name`, `brand`, `price`) VALUES
(1, 'XPG D6OG 16GB (2x8) DDR4 3200MHZ', 'XPG', 409),
(2, 'GIGABYTE AORUS RGB 16GB (2x8) DDR4 3733MHZ', 'GIGABYTE', 579),
(3, 'KINGSTON HYPERX FURY RGB 8GB DDR4 3200MHZ', 'KINGSTON', 189),
(4, 'PNY 8GB DDR4 2666MHZ', 'PNY', 139),
(5, 'KLEVV CRAS X RGB 16GB (2x8) DDR4 3200MHZ', 'KLEVV', 335),
(6, 'XPG D50 WHITE 16GB (2x8) DDR4 3200MHZ', 'XPG', 353),
(7, 'ZADAK TWIST 16GB (2x8) 2666MHZ', 'ZADAK', 424),
(8, 'XPG D41 16GB (2X8) DDR4 3200MHZ', 'XPG', 438),
(9, 'COLORFUL CVN Guardian 16GB 3200mhz', 'COLORFUL', 225);

-- --------------------------------------------------------

--
-- Table structure for table `ssd`
--

CREATE TABLE `ssd` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ssd`
--

INSERT INTO `ssd` (`id`, `name`, `brand`, `price`) VALUES
(1, 'WD BLUE SN550 M.2 NVME 500GB', 'WD', 289),
(2, 'SAMSUNG EVO 860 SERIES 2.5\" 250GB', 'SAMSUNG', 199),
(3, 'XPG SX8200 PRO SSD M.2 NVME 1TB', 'XPG', 519),
(4, 'SANDISK SSD PLUS 2.5\" 480GB', 'SANDISK', 240),
(5, 'XPG SX8100 SSD M.2 NVME 256GB', 'XPG', 209),
(7, 'XPG SX8200 PRO SSD M.2 NVME 512GB', 'XPG', 295),
(8, 'PNY CS1030 SSD M.2 NVME 256GB', 'PNY', 249),
(9, 'XPG SX8200 PRO M.2 NVME 1TB', 'XPG', 529),
(10, 'KINGSTON NV1 M.2 NVME 500GB', 'KINGSTON', 195),
(11, 'ZADAK TWSG3 NVMe 512GB', 'ZADAK', 270);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `role`) VALUES
(8, 'arif@gmail.com', '123', 'customer'),
(9, 'admin@gmail.com', '12345', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`adminID`);

--
-- Indexes for table `casing`
--
ALTER TABLE `casing`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cpu`
--
ALTER TABLE `cpu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `custEmail` (`custEmail`);

--
-- Indexes for table `feedbacks`
--
ALTER TABLE `feedbacks`
  ADD PRIMARY KEY (`fbID`),
  ADD KEY `FK_custEmail` (`custEmail`);

--
-- Indexes for table `gpu`
--
ALTER TABLE `gpu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mb`
--
ALTER TABLE `mb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pcpackage`
--
ALTER TABLE `pcpackage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `casing` (`casing`),
  ADD KEY `mb` (`mb`),
  ADD KEY `gpu` (`gpu`),
  ADD KEY `ram` (`ram`),
  ADD KEY `ssd` (`ssd`),
  ADD KEY `cpu` (`cpu`),
  ADD KEY `psu` (`psu`);

--
-- Indexes for table `psu`
--
ALTER TABLE `psu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ram`
--
ALTER TABLE `ram`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ssd`
--
ALTER TABLE `ssd`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `adminID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `casing`
--
ALTER TABLE `casing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `cpu`
--
ALTER TABLE `cpu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `feedbacks`
--
ALTER TABLE `feedbacks`
  MODIFY `fbID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `gpu`
--
ALTER TABLE `gpu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `mb`
--
ALTER TABLE `mb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `pcpackage`
--
ALTER TABLE `pcpackage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `psu`
--
ALTER TABLE `psu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `ram`
--
ALTER TABLE `ram`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `ssd`
--
ALTER TABLE `ssd`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `feedbacks`
--
ALTER TABLE `feedbacks`
  ADD CONSTRAINT `FK_custEmail` FOREIGN KEY (`custEmail`) REFERENCES `customer` (`custEmail`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `pcpackage`
--
ALTER TABLE `pcpackage`
  ADD CONSTRAINT `pcpackage_ibfk_1` FOREIGN KEY (`casing`) REFERENCES `casing` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pcpackage_ibfk_2` FOREIGN KEY (`mb`) REFERENCES `mb` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pcpackage_ibfk_3` FOREIGN KEY (`gpu`) REFERENCES `gpu` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pcpackage_ibfk_4` FOREIGN KEY (`ram`) REFERENCES `ram` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pcpackage_ibfk_5` FOREIGN KEY (`ssd`) REFERENCES `ssd` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pcpackage_ibfk_6` FOREIGN KEY (`cpu`) REFERENCES `cpu` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pcpackage_ibfk_7` FOREIGN KEY (`psu`) REFERENCES `psu` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
