create database if not exists libraryDB;

use libraryDB;

create table 회원(
	회원번호 varchar(5),
    이름 varchar(5),
    등번호 varchar(3)
);

create table 대출(
	회원번호 varchar(5),
    대출일 date,
    도서명 varchar(20),
    반납여부 varchar(2)
);

insert into 회원 values('m1', '배충성', '101');
insert into 회원 values('m2', '이소망', '102');
insert into 회원 values('m3', '오믿음', '107');
insert into 회원 values('m4', '최사랑', '111');

insert into 대출 values('m1', '2025-04-02', '성과를 향한 도전', 'O');
insert into 대출 values('m1', '2025-04-02', '취업의 비밀', 'O');
insert into 대출 values('m3', '2025-04-03', '부의 추월차선', 'O');
insert into 대출 values('m3', '2025-04-03', '면접 평범이 스펙이다', 'X');
insert into 대출 values('m4', '2025-04-04', '부의 추월차선', 'X');
insert into 대출 values('m2', '2025-04-05', '설득의 심리학', 'O');
insert into 대출 values('m3', '2025-04-13', '청소부 밥', 'X');

delete from 회원 where 회원번호='m1';

select distinct 이름 as '도서관 이용 명단' from 회원, 대출 where 회원.회원번호=대출.회원번호; -- 도서관 이용 명단

select 이름, 대출일 from 회원, 대출 where 대출.도서명='부의 추월차선' and 반납여부='X' and 회원.회원번호=대출.회원번호