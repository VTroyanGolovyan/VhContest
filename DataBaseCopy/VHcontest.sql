-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 04, 2020 at 03:55 AM
-- Server version: 5.7.29-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `VHcontest`
--

-- --------------------------------------------------------

--
-- Table structure for table `sendings`
--

CREATE TABLE `sendings` (
  `id` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  `code` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `language` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `result` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `time` int(11) NOT NULL,
  `memory` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sendings`
--

INSERT INTO `sendings` (`id`, `type`, `user_id`, `task_id`, `code`, `language`, `result`, `time`, `memory`) VALUES
(1, 1, 1, 1, 'while True:\n    pass', 'python', 'TL', 1040, 8),
(2, 1, 1, 1, 'print(\'Hello, world!\')', 'python', 'OK', 0, 1),
(3, 1, 1, 1, 'уцацуа', 'python', 'RE', 90, 23),
(4, 1, 1, 1, 'print(\'ddd\')', 'python', 'WA', 0, 1),
(5, 1, 1, 1, 'a = []\nfor i in Range(100000000)\n    a.append(i)', 'python', 'RE', 90, 23),
(6, 1, 1, 1, 'print(\'dwd\')', 'python', 'WA', 0, 1),
(7, 1, 1, 1, '', 'python', 'P', 0, 0),
(8, 1, 1, 1, '', 'python', 'P', 0, 0),
(9, 1, 1, 1, '', 'python', 'WA', 0, 1),
(10, 1, 1, 1, 'wdwa', 'python', 'RE', 90, 21),
(11, 1, 1, 1, 'print(\'Hello, world!\')', 'python', 'OK', 0, 1),
(12, 1, 1, 1, '', 'python', 'WA', 0, 1),
(13, 1, 1, 1, 'print(\'krk\')', 'python', 'WA', 0, 1),
(14, 1, 1, 1, 'while True:\n    pass', 'python', 'TL', 1050, 9),
(15, 1, 1, 2, 'a = int(input())\nb = int(input())\nprint(a + b)', 'python', 'OK', 0, 1),
(16, 1, 1, 2, 'a = int(input())\nb = int(input())\nprint(a - b)', 'python', 'WA', 0, 1),
(17, 1, 1, 2, 'a = int(input())\nb = int(input())\nprint(a + b)', 'python', 'OK', 0, 1),
(18, 1, 1, 2, 'a = int(input())\nb = int(input())\nprint(a + b)', 'python', 'OK', 0, 1),
(19, 1, 1, 4, 'a = int(input())\nb = int(input())\nprint(a * b)', 'python', 'OK', 0, 1),
(20, 1, 1, 4, 'a = int(input())\nb = int(input())\nprint(a - b)', 'python', 'WA', 0, 1),
(21, 1, 1, 3, 'a = int(input())\nb = int(input())\nprint(a - b)', 'python', 'OK', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tasks`
--

CREATE TABLE `tasks` (
  `id` int(11) NOT NULL,
  `name` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `condition` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `time_limit` int(11) NOT NULL,
  `memory_limit` int(11) NOT NULL,
  `process_limit` int(11) NOT NULL,
  `test_generator` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `test_generator_language` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `checker` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `checker_language` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `author_solution` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `author_solution_language` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tasks`
--

INSERT INTO `tasks` (`id`, `name`, `condition`, `time_limit`, `memory_limit`, `process_limit`, `test_generator`, `test_generator_language`, `checker`, `checker_language`, `author_solution`, `author_solution_language`) VALUES
(1, 'Hello, world!', 'Вам нужно написать программу, которая выводит на экран текст Hello, world!', 1000, 64, 1, '', '', '', '', 'print(\'Hello, world!)', 'python'),
(2, 'A + B', 'Дано два числа, вывести их сумму', 1000, 64, 1, '', '', '', '', 'print(\'Hello, world!)', 'python'),
(3, 'A - B', 'Дано два числа, вывести их разность', 1000, 64, 1, '', '', '', '', 'print(\'Hello, world!)', 'python'),
(4, 'A * B', 'Дано два числа, вывести их произведение', 1000, 64, 1, '', '', '', '', 'print(\'Hello, world!)', 'python');

-- --------------------------------------------------------

--
-- Table structure for table `tests`
--

CREATE TABLE `tests` (
  `id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  `input` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `output` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tests`
--

INSERT INTO `tests` (`id`, `task_id`, `input`, `output`) VALUES
(1, 1, '', 'Hello, world!'),
(2, 1, '', 'Hello, world!'),
(3, 2, '5\r\n6', '11'),
(4, 2, '7\r\n9\r\n', '16'),
(5, 2, '167\r\n3', '170'),
(6, 2, '13\r\n24', '37'),
(7, 2, '54\r\n1', '55'),
(8, 4, '2\r\n3', '6'),
(9, 4, '20\r\n20', '400'),
(10, 4, '50\r\n50', '2500'),
(11, 3, '4\r\n4', '0'),
(12, 3, '6\r\n7', '-1'),
(13, 3, '45\r\n25', '20'),
(14, 3, '17\r\n11', '6');

-- --------------------------------------------------------

--
-- Table structure for table `tests_result`
--

CREATE TABLE `tests_result` (
  `id` int(11) NOT NULL,
  `sending_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  `result` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `patronymic` varchar(100) COLLATE utf8_bin NOT NULL,
  `email` varchar(200) COLLATE utf8_bin NOT NULL,
  `password` varchar(300) COLLATE utf8_bin NOT NULL,
  `salt` varchar(10) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sendings`
--
ALTER TABLE `sendings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tasks`
--
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tests`
--
ALTER TABLE `tests`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tests_result`
--
ALTER TABLE `tests_result`
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
-- AUTO_INCREMENT for table `sendings`
--
ALTER TABLE `sendings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
--
-- AUTO_INCREMENT for table `tasks`
--
ALTER TABLE `tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `tests`
--
ALTER TABLE `tests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `tests_result`
--
ALTER TABLE `tests_result`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
