-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 06, 2020 at 10:00 PM
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
(21, 1, 1, 3, 'a = int(input())\nb = int(input())\nprint(a - b)', 'python', 'OK', 0, 1),
(22, 1, 1, 4, 'a = int(input())\nb = int(input())\nprint(a * b)', 'python', 'OK', 0, 1),
(23, 1, 1, 1, 'print(\'dw\')', 'python', 'WA', 0, 4),
(24, 1, 1, 1, 'print(\'Hello, world!\')', 'python', 'OK', 0, 1),
(25, 1, 1, 1, 'while True:\n    pass', 'python', 'TL', 1050, 8),
(26, 1, 1, 3, '', 'python', 'WA', 40, 9),
(27, 1, 1, 4, '', 'python', 'P', 0, 0),
(28, 1, 1, 1, 'print(\'lol\')', 'python', 'P', 0, 0),
(29, 1, 1, 1, 'print(\'lol\')', 'python', 'P', 0, 0),
(30, 1, 1, 1, 'print(\'lol\')', 'python', 'WA', 0, 1),
(31, 1, 1, 1, 'print(\'Hello, world\')', 'python', 'WA', 0, 1),
(32, 1, 1, 1, 'print(\'Hello, world!\')', 'python', 'OK', 0, 1),
(33, 1, 1, 1, 'print(\'Hello, world!\')', 'python', 'OK', 0, 1),
(34, 1, 1, 1, '', 'python', 'WA', 0, 1),
(35, 1, 1, 1, '', 'python', 'WA', 0, 1),
(36, 1, 1, 1, '', 'python', 'WA', 0, 1),
(37, 1, 1, 1, '', 'c++', 'WA', 0, 1),
(38, 1, 1, 1, '', 'c++', 'P', 0, 0),
(39, 1, 1, 1, '', 'c++', 'P', 0, 0),
(40, 1, 1, 1, '', 'c++', 'P', 0, 0),
(41, 1, 1, 1, '', 'c++', 'WA', 0, 1),
(42, 1, 1, 1, 'int wd', 'c++', 'TL', 50, 13),
(43, 1, 1, 1, 'int wd', 'c++', 'TL', 50, 11),
(44, 1, 1, 1, 'int wd', 'python', 'TL', 40, 10),
(45, 1, 1, 1, 'int wd', 'python', 'TL', 90, 23),
(46, 1, 1, 1, 'int wd', 'c++', 'TL', 50, 10),
(47, 1, 1, 1, 'int wd', 'c++', 'TL', 90, 14),
(48, 1, 1, 1, 'int wd', 'c++', 'C', 0, 0),
(49, 1, 1, 1, 'int main() {\n    \n}', 'python', 'TL', 50, 10),
(50, 1, 1, 1, 'int main() {\n    \n}', 'c++', 'C', 0, 0),
(51, 1, 1, 1, 'int main() {\n    \n}', 'c++', 'C', 0, 0),
(52, 1, 1, 1, 'int main() {\n    \n}', 'c++', 'E', 0, 0),
(53, 1, 1, 1, 'int main() {\n    \n}', 'c++', 'ML', 40, 15),
(54, 1, 1, 1, 'int main() {\n    \n}', 'c++', 'P', 0, 0),
(55, 1, 1, 1, 'int main() {\n    \n}', 'c++', 'TL', 90, 23),
(56, 1, 1, 1, 'int main() {\n    \n}', 'c++', 'TL', 90, 23),
(57, 1, 1, 1, 'int main() {\n    \n}', 'c++', 'E', 0, 0),
(58, 1, 1, 1, 'int main() {\n    \n}', 'c++', 'P', 0, 0),
(59, 1, 1, 1, 'int main() {\n    \n}', 'c++', 'P', 0, 0),
(60, 1, 1, 1, 'int main() {\n    \n}', 'c++', 'P', 0, 0),
(61, 1, 1, 1, 'int main() {\n    \n}', 'c++', 'TL', 50, 15),
(62, 1, 1, 1, '#include <iostream>\nint main() {\n    std::cout << \"Hi\";\n}', 'c++', 'TL', 100, 14),
(63, 1, 1, 1, '#include <iostream>\nint main() {\n    std::cout << \"Hi\";\n}', 'c++', 'TL', 90, 14),
(64, 1, 1, 1, '#include <iostream>\nint main() {\n    std::cout << \"Hi\";\n}', 'c++', 'TL', 90, 14),
(65, 1, 1, 1, '#include <iostream>\nint main() {\n    std::cout << \"Hi\";\n}', 'c++', 'TL', 90, 14),
(66, 1, 1, 1, '#include <iostream>\nint main() {\n    std::cout << \"Hi\";\n}', 'c++', 'RE', 90, 23),
(67, 1, 1, 1, '#include <iostream>\nint main() {\n    std::cout << \"Hi\";\n}', 'c++', 'RE', 90, 23),
(68, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hi\";\n}', 'c++', 'RE', 90, 23),
(69, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hi\";\n}', 'c++', 'P', 0, 0),
(70, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hi\";\n}', 'c++', 'RE', 90, 23),
(71, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 90, 23),
(72, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 90, 23),
(73, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 90, 23),
(74, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 80, 21),
(75, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 90, 23),
(76, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 90, 21),
(77, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 0, 1),
(78, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 0, 1),
(79, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 0, 1),
(80, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 0, 1),
(81, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 0, 1),
(82, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 0, 1),
(83, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 0, 1),
(84, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'TL', 0, 3),
(85, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'TL', 0, 3),
(86, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'TL', 0, 3),
(87, 1, 1, 1, 'print(\'lol\')', 'python', 'WA', 0, 1),
(88, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'TL', 0, 3),
(89, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 0, 1),
(90, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 0, 1),
(91, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hell\";\n}', 'c++', 'RE', 0, 1),
(92, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"lol\";\n}', 'c++', 'RE', 0, 1),
(93, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, world!\";\n}', 'c++', 'RE', 0, 1),
(94, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, world!\";\n}', 'c++', 'RE', 0, 1),
(95, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, world!\";\n}', 'c++', 'OK', 0, 1),
(96, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, worldd!\";\n}', 'c++', 'WA', 0, 1),
(97, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, worldd!\";\n     while(true);\n     \n}', 'c++', 'TL', 0, 3),
(98, 1, 1, 1, 'while True:\n    pass', 'python', 'TL', 1050, 8),
(99, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, worldd!\";\n     while(true);\n     \n}', 'c++', 'TL', 0, 3),
(100, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, worldd!\";\n     while(true);\n     \n}', 'c++', 'TL', 0, 3),
(101, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, worldd!\";\n     while(true);\n     \n}', 'c++', 'TL', 0, 3),
(102, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, worldd!\";\n     while(true);\n     \n}', 'c++', 'TL', 0, 3),
(103, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, worldd!\";\n}', 'c++', 'WA', 50, 3),
(104, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, worldd!\";\n     while(True):\n         pass\n}', 'c++', 'C', 0, 0),
(105, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, worldd!\";\n     while(true);\n}', 'c++', 'TL', 2000, 2),
(106, 1, 1, 1, '#include <iostream>\nint main() {\n     std::cout << \"Hello, worldd!\";\n     while(true);\n}', 'c++', 'RE', 1000, 3),
(107, 1, 1, 1, 'console.log(\'JJ\')', 'javascript', 'WA', 50, 0),
(108, 1, 1, 1, 'console.log(\'Hello, world!\')', 'javascript', 'OK', 50, 1),
(109, 1, 1, 1, '<?php \n  print(\'hih\'); \n?>', 'php', 'WA', 50, 1),
(110, 1, 1, 1, '<?php \n  print(\'Hello, world!\'); \n?>', 'php', 'OK', 50, 1),
(111, 1, 1, 1, 'import java.util.*\n\nclass Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'P', 0, 0),
(112, 1, 1, 1, 'import java.util.*\n\nclass Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'RE', 600, 3),
(113, 1, 1, 1, 'import java.util.*;\n\nclass Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'RE', 500, 3),
(114, 1, 1, 1, 'import java.util.*;\n\nclass Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'RE', 500, 3),
(115, 1, 1, 1, 'import java.util.*;\n\nclass Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'RE', 100, 3),
(116, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'RE', 100, 2),
(117, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'C', 0, 0),
(118, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'C', 0, 0),
(119, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'C', 0, 0),
(120, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'C', 0, 0),
(121, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'C', 0, 0),
(122, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'P', 0, 0),
(123, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'P', 0, 0),
(124, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'H\');\n    }\n}', 'java', 'WA', 50, 3),
(125, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'Hello, world!\');\n    }\n}', 'java', 'C', 0, 0),
(126, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'Hello, world!\');\n    }\n}', 'java', 'C', 0, 0),
(127, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'Hello, world!\');\n    }\n}', 'java', 'C', 0, 0),
(128, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\'Hello,\');\n    }\n}', 'java', 'C', 0, 0),
(129, 1, 1, 1, 'import java.util.*;\n\npublic class Main {\n    public static void main(String []args) {\n        System.out.print(\"Hello, world!\");\n    }\n}', 'java', 'WA', 50, 1),
(130, 1, 1, 1, '#include <iostream>\nint main() {\n    std::cout << \"Hello, world!\";\n}', 'java', 'C', 0, 0),
(131, 1, 1, 1, '#include <iostream>\nint main() {\n    std::cout << \"Hello, world!\";\n}', 'c++', 'OK', 50, 1),
(132, 1, 1, 1, '#include <iostream>\nint main() {\n    std::cout << \"Hello, worldwd!\";\n}', 'c++', 'WA', 50, 1),
(133, 1, 1, 1, 'console.log(\"Hello, world!\")', 'javascript', 'OK', 50, 1),
(134, 1, 1, 1, 'import java.util.*;\nclass Main {\n    public static void main(String []ar) {\n        System.out.print(\"Hello, world!\");\n    }\n}', 'java', 'OK', 50, 1),
(135, 1, 1, 1, 'print(\"Hello, world!\")', 'python', 'OK', 50, 1),
(136, 1, 1, 1, 'console.log(\"Hello, world!\")', 'javascript', 'OK', 50, 1),
(137, 1, 1, 1, '#include <iodtream>\nint main() {\n    std::cout << \"Hello, world!\";\n}', 'c++', 'C', 0, 0),
(138, 1, 1, 1, '<?php\n   print(\'Hello, world!\');\n?>', 'php', 'OK', 50, 1),
(139, 1, 1, 1, '#include <iostream>\nint main() {\n    std::cout << \"Hello, world!\";\n}', 'php', 'WA', 50, 1),
(140, 1, 1, 1, 'dqwq', 'python', 'P', 0, 0),
(141, 1, 1, 1, 'dqwq', 'python', 'P', 0, 0),
(142, 1, 1, 1, 'dqwq', 'python', 'RE', 90, 21),
(143, 1, 1, 1, 'print(\'Hello, world!\')', 'python', 'OK', 50, 1),
(144, 1, 1, 2, '#include <iostream>\nint main() {\n    int a, b;\n    std::cin >> a >> b;\n    std::cout << a + b;\n    return 0;\n}', 'c++', 'OK', 50, 1),
(145, 1, 1, 3, '#include <iostream>\nint main() {\n    int a, b;\n    std::cin >> a >> b;\n    std::cout << a - b;\n    return 0;\n}', 'python', 'RE', 90, 22),
(146, 1, 1, 3, '#include <iostream>\nint main() {\n    int a, b;\n    std::cin >> a >> b;\n    std::cout << a - b;\n    return 0;\n}', 'c++', 'OK', 50, 1),
(147, 1, 1, 1, 'fsf', 'python', 'RE', 90, 23),
(148, 1, 1, 1, 'fsf', 'python', 'RE', 90, 21),
(149, 1, 1, 1, 'print(\'Hello, world!\')', 'python', 'OK', 50, 1);

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `id` int(11) NOT NULL,
  `user` int(11) NOT NULL,
  `token` varchar(400) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `refresh_token` varchar(400) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sessions`
--

INSERT INTO `sessions` (`id`, `user`, `token`, `refresh_token`) VALUES
(1, 1, '0ab2a2a3db3decefec87a82dab831ae9f4369614dfdfc19f27797c0b294acacc5aa83415f613e3ad702cc890af12a0a084533a07ee7b47d15faec3b62773d4a1', 'd9e685ed92f8647b5297a25927bf766555e840f8a59b8834e48b6141eb79fb7935a99d9b2a2a74038e4c6ab0e004130bc30adf08ad66a1f859eecd2a968cab51'),
(2, 1, 'e2da7bd65bea4eee2ee4f076bf092209086a16eede577ed0b37c10353ec2fbbd0c57eca61dc954dc6b1ba00cd3bc2a3bb6574dd303831f1ca37362c8855b9b53', '2ae1a9a44eb62bc5c256893685be9f0c7362cfba360e1fde683f234fc9103fe63189f72ff0f1fc3aceb6d8370c12b74c0b0517d4379d5bde9143d9fa005739b9'),
(3, 1, '9764ba393cf57eed8d7c7db310a121c0c9983046fd8e2a79f8a736867807135c8bfffa8de9cb40c18ab8518bad838a9b545851a02fd45b0b68f2eb6559633cbf', '54adf18c630c95b65f68c540bd2fc81f78ad8d45b1f601f2b04457ffabb114327ebe4671c063b3affdc35147a953b4b76ee9e28684f22517178c06a4d881ccb1'),
(4, 1, 'f24455b64d744709d94fddfb59007218fd6ab75fea5da487ef210e98ff15a88642c2243082a000223b3ff0edd27f469a80d234bd30a9d9eb946b25c4744de63d', 'adb5633469c97d72956e12cfba9132b2e6735193f62f5727a0943c4deae98a50c24e7c239548724e49e9a4d2b1bdbffc3cbca1bb4d09ad455405c6d575c0ec21'),
(5, 1, '4a0256cddb75f64fdf5225f25f78591c7fe32351d0c13e7498052743ac7d3341c2fdf82e904645fcfe5ea222f0748e3756f18a2ddd422d4e1a6b14ae8307cbdf', '25ecf22cf463f82a840dff7b192c9774d6d2c4e3584f26d3dcae3b9dd662e5ccf637ca89ce6c0f0d8f0162f341346c100f55533629d410870a7741ae57e93fd6'),
(6, 1, '5961e33b0df5fb5145e039349e845c096ea39428ef7d085fda2349f8806a64867f499dd63edb34909af3295b1cb6fa0568be326363f8076b07f40fb56c533049', 'fe6ee0896a6a89aaaf846cd28cb27c8cbf3abe7e869ff4fbf0c4fe3a984dc5481e25011d832cd15dc314a61b1820df705e4f5b019bef0be1cf36b50e31beb37d');

-- --------------------------------------------------------

--
-- Table structure for table `tasks`
--

CREATE TABLE `tasks` (
  `id` int(11) NOT NULL,
  `name` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `condition` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `input_description` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `output_description` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `input_example` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `output_example` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
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

INSERT INTO `tasks` (`id`, `name`, `condition`, `input_description`, `output_description`, `input_example`, `output_example`, `time_limit`, `memory_limit`, `process_limit`, `test_generator`, `test_generator_language`, `checker`, `checker_language`, `author_solution`, `author_solution_language`) VALUES
(1, 'Hello, world!', 'Вам нужно написать программу, которая выводит на экран текст Hello, world!', 'Ввод отсутствует', 'Вывести текст', '', 'Hello, world!', 1000, 64, 1, '', '', '', '', 'print(\'Hello, world!)', 'python'),
(2, 'A + B', 'Дано два числа, вывести их сумму', 'Два числа типа int\r\nКаждое с новой строки', 'Вывести 1 число типа int', '5\r\n4', '9', 1000, 64, 1, '', '', '', '', 'print(\'Hello, world!)', 'python'),
(3, 'A - B', 'Дано два числа, вывести их разность', 'Два числа типа int\nКаждое с новой строки', 'Вывести 1 число типа int', '3\r\n1', '2', 1000, 64, 1, '', '', '', '', 'print(\'Hello, world!)', 'python'),
(4, 'A * B', 'Дано два числа, вывести их произведение', 'Два числа типа int\nКаждое с новой строки', 'Вывести 1 число типа int', '25\r\n25', '625', 1000, 64, 1, '', '', '', '', 'print(\'Hello, world!)', 'python'),
(5, 'Стримеры', 'Жили были два студента, и решили они вести канал на twich. Постепенно популярность их канала росла, появлялись донаты, они решили собрать статистику, и понять, в какие дни их стримы смотрят чаще. Для этого они собрали статистику за N дней, сколько было посетителей стримов. Они не могут сейчас написать программу, так как сейчас у них по плану стрим. Помогите им найти день, когда их стрим самый популярный (популярность оценивается средним арифметическим посещаемости по всем дням)', '', '', '', '', 1000, 1000, 1, '', '', '', '', '', '');

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
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `last_name`, `patronymic`, `email`, `password`, `salt`) VALUES
(1, 'Vladislav', 'Troyan-Golovyan', 'Dmitrievich', 'vladislavhacker111@gmail.com', '64c0d89d75e778586af80e265ebd5a841847ce1db4e08fe70e8af024377c14afc368f9797c2d4d52bd12b542bc22430490c63aefc8ca6f266ec3b3bf15e7eac6', 'JKHK');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sendings`
--
ALTER TABLE `sendings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=150;
--
-- AUTO_INCREMENT for table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `tasks`
--
ALTER TABLE `tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
