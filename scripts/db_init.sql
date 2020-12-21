START TRANSACTION;
CREATE DATABASE video_uploader DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON video_uploader.* TO 'django'@'localhost';
FLUSH PRIVILEGES;
COMMIT;