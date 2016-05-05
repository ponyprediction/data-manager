-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 05, 2016 at 10:20 AM
-- Server version: 5.5.49-0+deb8u1
-- PHP Version: 5.6.20-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: 'ponyprediction'
--
CREATE DATABASE IF NOT EXISTS ponyprediction DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE ponyprediction;

-- --------------------------------------------------------

--
-- Table structure for table 'arrivals'
--

DROP TABLE IF EXISTS arrivals;
CREATE TABLE IF NOT EXISTS arrivals (
id int(11) NOT NULL,
  place varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  win tinyint(1) NOT NULL,
  winMoney double NOT NULL,
  placed tinyint(1) NOT NULL,
  placedMoney double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'days'
--

DROP TABLE IF EXISTS days;
CREATE TABLE IF NOT EXISTS days (
  `date` date NOT NULL,
  reunionCount int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'horses'
--

DROP TABLE IF EXISTS horses;
CREATE TABLE IF NOT EXISTS horses (
id int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  gender char(1) COLLATE utf8_unicode_ci NOT NULL,
  age int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'jockeys'
--

DROP TABLE IF EXISTS jockeys;
CREATE TABLE IF NOT EXISTS jockeys (
id int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'races'
--

DROP TABLE IF EXISTS races;
CREATE TABLE IF NOT EXISTS races (
id int(11) NOT NULL,
  textId varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `date` date NOT NULL,
  teamCount int(11) NOT NULL,
  length int(11) NOT NULL,
  `type` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'racesInReunions'
--

DROP TABLE IF EXISTS racesInReunions;
CREATE TABLE IF NOT EXISTS racesInReunions (
id int(11) NOT NULL,
  race int(11) NOT NULL,
  reunion int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'reunions'
--

DROP TABLE IF EXISTS reunions;
CREATE TABLE IF NOT EXISTS reunions (
id int(11) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'reunionsInDays'
--

DROP TABLE IF EXISTS reunionsInDays;
CREATE TABLE IF NOT EXISTS reunionsInDays (
id int(11) NOT NULL,
  reunion int(11) NOT NULL,
  `day` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'starts'
--

DROP TABLE IF EXISTS starts;
CREATE TABLE IF NOT EXISTS `starts` (
id int(11) NOT NULL,
  oddsPlaced double NOT NULL,
  oddsWin double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'teams'
--

DROP TABLE IF EXISTS teams;
CREATE TABLE IF NOT EXISTS teams (
id int(11) NOT NULL,
  raceId varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  horseId int(11) NOT NULL,
  jockeyId int(11) NOT NULL,
  trainerId int(11) NOT NULL,
  `start` int(11) NOT NULL,
  prediction int(11) NOT NULL,
  arrival int(11) NOT NULL,
  odds1 double NOT NULL,
  odds2 double NOT NULL,
  odds3 double NOT NULL,
  firstMoney double NOT NULL,
  secondMoney double NOT NULL,
  fourthMoney double NOT NULL,
  showMoney double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'teamsInRaces'
--

DROP TABLE IF EXISTS teamsInRaces;
CREATE TABLE IF NOT EXISTS teamsInRaces (
id int(11) NOT NULL,
  teamId int(11) NOT NULL,
  raceId int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'trainers'
--

DROP TABLE IF EXISTS trainers;
CREATE TABLE IF NOT EXISTS trainers (
id int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table arrivals
--
ALTER TABLE arrivals
 ADD PRIMARY KEY (id);

--
-- Indexes for table days
--
ALTER TABLE days
 ADD PRIMARY KEY (`date`);

--
-- Indexes for table horses
--
ALTER TABLE horses
 ADD PRIMARY KEY (id), ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table jockeys
--
ALTER TABLE jockeys
 ADD PRIMARY KEY (id), ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table races
--
ALTER TABLE races
 ADD PRIMARY KEY (id), ADD KEY `date` (`date`);

--
-- Indexes for table racesInReunions
--
ALTER TABLE racesInReunions
 ADD PRIMARY KEY (id);

--
-- Indexes for table reunions
--
ALTER TABLE reunions
 ADD PRIMARY KEY (id);

--
-- Indexes for table reunionsInDays
--
ALTER TABLE reunionsInDays
 ADD PRIMARY KEY (id);

--
-- Indexes for table starts
--
ALTER TABLE starts
 ADD PRIMARY KEY (id);

--
-- Indexes for table teams
--
ALTER TABLE teams
 ADD PRIMARY KEY (id), ADD UNIQUE KEY ids_index (raceId,horseId,jockeyId,trainerId), ADD KEY trainerId (trainerId), ADD KEY jockeyId (jockeyId), ADD KEY horseId (horseId);

--
-- Indexes for table teamsInRaces
--
ALTER TABLE teamsInRaces
 ADD PRIMARY KEY (id), ADD UNIQUE KEY indexTeamRace (teamId,raceId), ADD KEY raceId (raceId);

--
-- Indexes for table trainers
--
ALTER TABLE trainers
 ADD PRIMARY KEY (id), ADD UNIQUE KEY `name` (`name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table arrivals
--
ALTER TABLE arrivals
MODIFY id int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table horses
--
ALTER TABLE horses
MODIFY id int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table jockeys
--
ALTER TABLE jockeys
MODIFY id int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table races
--
ALTER TABLE races
MODIFY id int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table racesInReunions
--
ALTER TABLE racesInReunions
MODIFY id int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table reunions
--
ALTER TABLE reunions
MODIFY id int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table reunionsInDays
--
ALTER TABLE reunionsInDays
MODIFY id int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table starts
--
ALTER TABLE starts
MODIFY id int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table teams
--
ALTER TABLE teams
MODIFY id int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table teamsInRaces
--
ALTER TABLE teamsInRaces
MODIFY id int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table trainers
--
ALTER TABLE trainers
MODIFY id int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table teams
--
ALTER TABLE teams
ADD CONSTRAINT teams_ibfk_1 FOREIGN KEY (trainerId) REFERENCES trainers (id),
ADD CONSTRAINT teams_ibfk_2 FOREIGN KEY (jockeyId) REFERENCES jockeys (id),
ADD CONSTRAINT teams_ibfk_3 FOREIGN KEY (horseId) REFERENCES horses (id);

--
-- Constraints for table teamsInRaces
--
ALTER TABLE teamsInRaces
ADD CONSTRAINT teamsInRaces_ibfk_1 FOREIGN KEY (raceId) REFERENCES races (id),
ADD CONSTRAINT teamsInRaces_ibfk_2 FOREIGN KEY (teamId) REFERENCES teams (id);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
