#코드 5-1
CREATE DATABASE IF NOT EXISTS firstDB;
USE firstDB;

#코드 5-2
CREATE TABLE 학생
(학번 CHAR(2) PRIMARY KEY,
이름 VARCHAR(20) NOT NULL,
주소 VARCHAR(50) NOT NULL UNIQUE,
전화번호 CHAR(13) NOT NULL DEFAULT '해당사항 없음',
생년월일 DATE NULL);

#코드 5-3
CREATE TABLE 과목
(과목번호 CHAR(2) PRIMARY KEY,
과목명 VARCHAR(20) NOT NULL,
강의실 VARCHAR(2) NOT NULL,
시간수 INT NOT NULL);

#코드 5-4
CREATE TABLE 수강
(학번 CHAR(2) NOT NULL,
과목번호 CHAR(2) NOT NULL,
학점 CHAR(1) NULL,
PRIMARY KEY(학번, 과목번호),
FOREIGN KEY(학번) REFERENCES 학생(학번),
FOREIGN KEY(과목번호) REFERENCES 과목(과목번호));

#코드 5-5
#학생 테이블 데이터 입력하기
INSERT INTO 학생 VALUES('s1', '홍길동', '경기 파주', '010-1111-1111', '2001-01-15');
INSERT INTO 학생 VALUES('s2', '강감찬', '경남 부산','010-2222-2222', '2002-12-25');
INSERT INTO 학생 VALUES('s3', '을지문덕', '서울 강남', '010-3333-3333', '2000-05-05');
INSERT INTO 학생 VALUES('s4', '이순신', '대전 유성', '010-4444-4444', '2002-07-17');
INSERT INTO 학생 VALUES('s5', '김유신', '강원 원주', DEFAULT, NULL);

#과목 테이블 데이터 입력하기
INSERT INTO 과목 VALUES('c1', '인공지능개론', 'r1', 3);
INSERT INTO 과목 VALUES('c2', '웃음치료', 'r2', 2);
INSERT INTO 과목 VALUES('c3', '경영학', 'r3', 3);

#수강 테이블 데이터 입력하기
INSERT INTO 수강 VALUES('s1', 'c1', 'A');
INSERT INTO 수강 VALUES('s1', 'c2', 'A');
INSERT INTO 수강 VALUES('s2', 'c2', 'B');
INSERT INTO 수강 VALUES('s2', 'c3', 'D');
INSERT INTO 수강 VALUES('s4', 'c1', 'C');
INSERT INTO 수강 VALUES('s4', 'c3', 'A');
INSERT INTO 수강 VALUES('s5', 'c1', 'B');

#코드 5-6
SELECT * FROM 학생;


#코드 5-7
SELECT 학번 FROM 수강;

#코드 5-8
SELECT DISTINCT 학번 FROM 수강;

#코드 5-9
SELECT 학번 FROM 수강 WHERE 과목번호 ='c1' AND 학점 ='A';

#코드 5-10
SELECT 이름 FROM 학생 WHERE 주소 LIKE '서울%' OR 주소 LIKE '대전%';

#코드 5-11
SELECT 과목번호, 과목명, 시간수 FROM 과목 WHERE 시간수 BETWEEN 1 AND 3;

#코드 5-12
SELECT 학번, COUNT(*) FROM 수강 GROUP BY 학번;
SELECT 학번, COUNT(*) AS "수강 과목의 개수" FROM 수강 GROUP BY 학번;
-- 항상 NULL이 아닌 고정값 → 행 개수 우연히 결과가 같음
SELECT 학번, COUNT('s1') AS "수강 과목의 개수" FROM 수강 GROUP BY 학번;

#코드 5-13
SELECT * FROM 학생 INNER JOIN 수강 ON 학생.학번 = 수강.학번;
SELECT * FROM 학생, 수강 where 학생.학번 = 수강.학번;

#코드 5-14
SELECT * FROM 학생 INNER JOIN 수강 ON 학생.학번 = 수강.학번;


#코드 5-15
SELECT * FROM 학생, 수강, 과목
  WHERE 학생.학번 = 수강.학번 AND 수강.과목번호 = 과목.과목번호;

#코드 5-16
SELECT 수강.학번, 이름, 전화번호, 과목번호, 학점
  FROM 학생 LEFT OUTER JOIN 수강 ON 학생.학번 = 수강.학번;


#코드 5-17
CREATE TABLE 학생_수강
  AS SELECT 수강.학번, 이름, 전화번호, 과목번호, 학점
  FROM 학생 LEFT OUTER JOIN 수강 ON 학생.학번 = 수강.학번;

#코드 5-18
SELECT 학번 FROM 학생 WHERE 생년월일 >= '2002-05-01';

#코드 5-19
SELECT 과목번호 FROM 수강 WHERE 학번 IN ('s2', 's4');

#코드 5-20
SELECT 과목번호 FROM 수강
  WHERE 학번 IN (SELECT 학번 FROM 학생 WHERE 생년월일 >= '2002-05-01');

#코드 5-21
SELECT * FROM 학생 WHERE 생년월일 IS NULL;


#코드 5-22
SELECT 과목번호 FROM 과목 UNION SELECT 과목번호 FROM 수강;

#코드 5-23
UPDATE 학생 SET 이름 = '홍길수' WHERE 학번 = 's1';


#코드 5-24
UPDATE 학생 SET 생년월일 = '2002-12-25', 주소 = '서울 관악' WHERE 이름 = '이순신';


#코드 5-25
DELETE FROM 수강 WHERE 학번 = 's5';


#코드 5-26
DELETE FROM 학생 WHERE 학번 = 's1'; -- 키가 수강table에 참조되어 삭제가 되지 않는다

#코드 5-27
DELETE FROM 수강 WHERE 학번 = 's1'; -- 수강 table에 학번을 삭제후
DELETE FROM 학생 WHERE 학번 = 's1';
