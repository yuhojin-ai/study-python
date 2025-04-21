create database exampleDB;

use exampleDB;

create table exam_tbl (
	a_col varchar(10),
    b_col varchar(10)
);

drop database exampleDB;

drop table exam_tbl;

insert into exam_tbl values('s1', '유호진');

insert into exam_tbl(b_col, a_col) values('이순신', 's2');


-- **Safe Update Mode(안전 모드)**에서는 실수로 모든 데이터를 날리지 않도록,
-- DELETE나 UPDATE할 때 반드시 WHERE 절에 키(primary key 또는 index column)를 사용
delete from exam_tbl;

delete from exam_tbl where a_col = 's2';