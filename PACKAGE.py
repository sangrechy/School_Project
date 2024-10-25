##################################-IMPORTING MODULE AND PACKAGES-###########################
import mysql.connector as sql
import time

#######################################-CONNECTING TO MYSQL-################################
user='root'#{user_name}
password=''#{user_password}
def CONNECT():
    connection_object=sql.connect(host='localhost',user=user,passwd=password)
    return connection_object
connection_object=CONNECT()
if connection_object.is_connected():
    print('SUCCESSFULLY CONNECTED TO MYSQL..')
else:
    print('ERROR CONNECTING TO MYSQL, PLEASE TRY AGAIN')
    connection_object=CONNECT()
    if connection_object.is_connected():
        print('SUCCESSFULLY CONNECTED TO MYSQL..')
    else:
        print('ERROR CONNECTING TO MYSQL, PLEASE TRY LATER')
        time.sleep(20)
        exit()
cursor_object=connection_object.cursor()

#######################################-CREATING DATABASE AND TABLES-######################
#CREATING DATABASES AND ACCESSING IT
cursor_object.execute('CREATE DATABASE IF NOT EXISTS MOVIES;')
cursor_object.execute('USE MOVIES;')

tempvar2='DROP DATABASE MOVIES'
tempvar3=('CREATE DATABASE IF NOT EXISTS MOVIES;')
tempvar4=('USE MOVIES;')
tempvar5='''INSERT INTO MOVIE_INFO (MOVIE_CODE, MOVIE_NAME, YEAR_RELEASED, GENERE, ACTORS, DURATION, IMDB_RATING) VALUES
(1, 'Passenger', 2016, 'SCI_FI,ROMANCE', 'Jennifer Lawrence, Chris Pratt', '01:56:00', 7.0),
(2, 'Gifted', 2017, 'DRAMA,COMEDY', 'Chris Evans, Mckenna Grace', '01:41:00', 7.6),
(3, 'The Perks of Being a Wallflower', 2012, 'DRAMA,ROMANCE', 'Logan Lerman, Emma Watson', '01:43:00', 8.0),
(4, 'Interstellar', 2014, 'SCI_FI,DRAMA', 'Matthew McConaughey, Anne Hathaway', '02:49:00', 8.6),
(5, 'Avengers: Endgame', 2019, 'ACTION,SCI_FI', 'Robert Downey Jr., Chris Evans', '03:01:00', 8.4),
(6, 'Spider Man Across the Universe', 2007, 'ANIMATION,ACTION', 'Evan Rachel Wood, Jim Sturgess', '02:13:00', 7.4),
(7, 'How to Train Your Dragon', 2010, 'ANIMATION,FAMILY', 'Jay Baruchel, Gerard Butler', '01:38:00', 8.1),
(8, 'Annabelle', 2014, 'HORROR,THRILLER', 'Annabelle Wallis, Ward Horton', '01:39:00', 5.4),
(9, 'The Nun', 2018, 'HORROR,THRILLER', 'Taissa Farmiga, Demián Bichir', '01:36:00', 5.3),
(10, 'Free Guy', 2021, 'ACTION,COMEDY', 'Ryan Reynolds, Jodie Comer', '01:55:00', 7.4),
(11, 'Self/less', 2015, 'SCI_FI,THRILLER', 'Ryan Reynolds, Ben Kingsley', '01:57:00', 6.5),
(12, 'Inception', 2010,'ACTION,SCI_FI', 'Leonardo DiCaprio,Cillian Murphy', '02:28:00', 8.8),
(13, 'Star Wars: Episode IV - A New Hope', 1977, 'SCI_FI,FANTASY', 'Mark Hamill, Harrison Ford', '02:01:00', 8.6),
(14, 'WALL-E', 2008, 'ANIMATION,FAMILY', 'Ben Burtt, Elissa Knight', '01:38:00', 8.4),
(15, 'It', 2017, 'HORROR,THRILLER', 'Bill Skarsgård, Jaeden Martell', '02:15:00', 7.3),
(16, 'Harry Potter and the Sorcerers Stone', 2001, 'FANTASY,ADVENTURE', 'Daniel Radcliffe, Rupert Grint', '02:32:00', 7.6),
(17, 'Captain America: The First Avenger', 2011, 'ACTION,ADVENTURE', 'Chris Evans, Hugo Weaving', '02:04:00', 6.9),
(18, 'Iron Man', 2008, 'ACTION,SCI_FI', 'Robert Downey Jr., Gwyneth Paltrow', '02:06:00', 7.9),
(19, 'Thor', 2011, 'ACTION,FANTASY', 'Chris Hemsworth, Natalie Portman', '01:55:00', 7.0),
(20, 'Mission: Impossible', 1996, 'ACTION,THRILLER', 'Tom Cruise, Jon Voight', '01:50:00', 7.1),
(21, 'Pirates of the Caribbean: The Curse of the Black Pearl', 2003, 'ACTION,ADVENTURE', 'Johnny Depp, Geoffrey Rush', '02:23:00', 8.0),
(22, 'Pirates of the Caribbean: Dead Mans Chest', 2006, 'ACTION,ADVENTURE', 'Johnny Depp, Orlando Bloom', '02:31:00', 7.3),
(23, 'Pirates of the Caribbean: At Worlds End', 2007, 'ACTION,ADVENTURE', 'Johnny Depp, Keira Knightley', '02:49:00', 7.1),
(24, 'Pirates of the Caribbean: On Stranger Tides', 2011, 'ACTION,ADVENTURE', 'Johnny Depp, Penélope Cruz', '02:16:00', 6.6),
(25, 'Pirates of the Caribbean: Dead Men Tell No Tales', 2017, 'ACTION,ADVENTURE', 'Johnny Depp, Javier Bardem', '02:09:00', 6.5),
(26, 'Star Wars: Episode V - The Empire Strikes Back', 1980, 'SCI_FI,FANTASY', 'Mark Hamill, Harrison Ford', '02:04:00', 8.7),
(27, 'Star Wars: Episode VI - Return of the Jedi', 1983, 'SCI_FI,FANTASY', 'Mark Hamill, Harrison Ford', '02:11:00', 8.3),
(28, 'Star Wars: Episode I - The Phantom Menace', 1999, 'SCI_FI,FANTASY', 'Liam Neeson, Ewan McGregor', '02:16:00', 6.5),
(29, 'Star Wars: Episode II - Attack of the Clones', 2002, 'SCI_FI,ROMANCE', 'Hayden Christensen, Natalie Portman', '02:22:00', 6.5), 
(30, 'Star Wars: Episode III - Revenge of the Sith', 2005, 'SCI_FI,DRAMA', 'Hayden Christensen, Natalie Portman', '02:20:00', 7.5), 
(31, 'Star Wars: The Force Awakens', 2015, 'SCI_FI,ACTION', 'Daisy Ridley, John Boyega', '02:18:00', 7.8),
(32, 'Star Wars: The Last Jedi', 2017, 'SCI_FI,ACTION', 'Daisy Ridley, Mark Hamill', '02:31:00', 7.0),
(33, 'Star Wars: The Rise of Skywalker', 2019, 'SCI_FI,ACTION', 'Daisy Ridley, Adam Driver', '02:21:00', 6.5),
(34, 'The Avengers', 2012, 'ACTION,SCI_FI', 'Robert Downey Jr., Chris Evans', '02:23:00', 8.0),
(35, 'Avengers: Age of Ultron', 2015, 'ACTION,SCI_FI', 'Robert Downey Jr., Chris Evans', '02:21:00', 7.3),
(36, 'Avengers: Infinity War', 2018, 'ACTION,SCI_FI', 'Robert Downey Jr., Chris Evans', '02:29:00', 9.6);'''
tempvar1="UPDATE MOVIE_INFO  SET PRICE=IMDB_RATING*500 "
tempvar6='''INSERT INTO USER_INFO (USER_ID, USER_NAME, AGE, GENDER, FAVORITE_ACTOR) VALUES
(1, 'Emma Watson', 18, 'FEMALE', 'Tom Hanks'),
(2, 'Liam Hemsworth', 42, 'MALE', 'Meryl Streep'),
(3, 'Olivia Wilde', 33, 'FEMALE', 'Denzel Washington'),
(4, 'Noah Centineo', 55, 'MALE', 'Julia Roberts'),
(5, 'Sophia Vergara', 26, 'FEMALE', 'Brad Pitt'),
(6, 'Elijah Wood', 67, 'MALE', 'Angelina Jolie'),
(7, 'Ava Gardner', 12, 'FEMALE', 'Leonardo DiCaprio'),
(8, 'Jackson Smith', 40, 'MALE', 'Jennifer Lawrence'),
(9, 'Mia Johnson', 8, 'FEMALE', 'Will Smith'),
(10, 'William Smith', 70, 'MALE', 'Sandra Bullock'),
(11, 'Sophia Johnson', 71, 'FEMALE', 'George Clooney'),
(12, 'Michael Davis', 73, 'MALE', 'Meryl Streep'),
(13, 'Olivia Parker', 77, 'FEMALE', 'Tom Hanks'),
(14, 'James Lee', 82, 'MALE', 'Julia Roberts'),
(15, 'Lily Cooper', 85, 'FEMALE', 'Denzel Washington'),
(16, 'Noah Wilson', 88, 'MALE', 'Angelina Jolie'),
(17, 'Emily Carter', 90, 'FEMALE', 'Brad Pitt'),
(18, 'Liam Johnson', 92, 'MALE', 'Jennifer Lawrence'),
(19, 'Harper White', 95, 'FEMALE', 'Will Smith'),
(20, 'Jackson Martin', 99, 'MALE', 'Leonardo DiCaprio'),
(21, 'Aiden Davis', 47, 'MALE', 'Sandra Bullock'),
(22, 'Isabella Smith', 19, 'FEMALE', 'George Clooney'),
(23, 'Oliver Taylor', 52, 'MALE', 'Meryl Streep'),
(24, 'Charlotte Hall', 35, 'FEMALE', 'Tom Hanks'),
(25, 'Henry Martin', 58, 'MALE', 'Julia Roberts'),
(26, 'Grace Williams', 62, 'FEMALE', 'Denzel Washington'),
(27, 'William Harris', 65, 'MALE', 'Brad Pitt'),
(28, 'Sophia Thomas', 35, 'FEMALE', 'Angelina Jolie'),
(29, 'Michael Anderson', 52, 'MALE', 'Leonardo DiCaprio'),
(30, 'Mia Taylor', 60, 'FEMALE', 'Sandra Bullock'),
(31, 'Benjamin Brown', 29, 'MALE', 'George Clooney'),
(32, 'Olivia Adams', 39, 'FEMALE', 'Sandra Bullock'),
(33, 'Henry Mitchell', 48, 'MALE', 'Julia Roberts'),
(34, 'Aria Davis', 32, 'FEMALE', 'Denzel Washington'),
(35, 'James Smith', 22, 'MALE', 'Meryl Streep');'''

def p2():
    cursor_object.execute(tempvar2)
def p3():
    cursor_object.execute(tempvar3)
def p4():
    cursor_object.execute(tempvar4)
def p5():
    cursor_object.execute(tempvar5)
    connection_object.commit()
    cursor_object.execute(tempvar1)
    connection_object.commit()
def p6():
    cursor_object.execute(tempvar6)
    connection_object.commit()
def p1():
    p5()
    p6()

