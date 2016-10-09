-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 21, 2016 at 06:41 AM
-- Server version: 5.5.50-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `co_dbbase`
--

-- --------------------------------------------------------

--
-- Table structure for table `co_movie`
--

CREATE TABLE IF NOT EXISTS `co_movie` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `url_id` int(20) unsigned NOT NULL,
  `title` varchar(1024) COLLATE utf8_unicode_ci DEFAULT NULL,
  `xflink` text COLLATE utf8_unicode_ci,
  `divcontent` text COLLATE utf8_unicode_ci NOT NULL,
  `topimg` text COLLATE utf8_unicode_ci,
  `kind` int(11) NOT NULL,
  `create_time` bigint(30) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=257 ;

-- --------------------------------------------------------

--
-- Table structure for table `co_pics`
--

CREATE TABLE IF NOT EXISTS `co_pics` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `url_id` int(20) unsigned NOT NULL,
  `title` varchar(1024) COLLATE utf8_unicode_ci DEFAULT NULL,
  `divcontent` text COLLATE utf8_unicode_ci NOT NULL,
  `kind` int(11) NOT NULL,
  `create_time` bigint(30) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1119 ;

-- --------------------------------------------------------

--
-- Table structure for table `co_txts`
--

CREATE TABLE IF NOT EXISTS `co_txts` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `url_id` int(20) unsigned NOT NULL,
  `title` varchar(1024) COLLATE utf8_unicode_ci DEFAULT NULL,
  `divcontent` longtext COLLATE utf8_unicode_ci NOT NULL,
  `kind` int(11) NOT NULL,
  `create_time` bigint(30) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1117 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
