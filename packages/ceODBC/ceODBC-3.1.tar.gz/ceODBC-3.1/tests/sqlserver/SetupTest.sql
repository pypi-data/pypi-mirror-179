/*-----------------------------------------------------------------------------
 * SetupTest.sql
 *   Creates the objects used for testing ceODBC with a SQL Server database.
 *---------------------------------------------------------------------------*/

create table TestDates (
    IntCol                              integer not null,
    DateCol                             date not null,
    TimestampCol                        timestamp not null,
    NullableDateCol                     date,
    NullableTimestampCol                timestamp
);

create table TestNumbers (
    IntCol              integer not null,
    BigIntCol           bigint,
    FloatCol            float,
    DoubleCol           double precision,
    DecimalCol          decimal(6, 2)
);

create table TestStrings (
    IntCol              integer not null,
    StringCol           varchar(20) not null,
    CharCol             char(5) not null,
    NullableCol         varchar(50)
);

create table TestBooleans (
    IntCol              integer not null,
    BooleanCol          bit
);

create table TestTempTable (
    IntCol              integer not null,
    StringCol           varchar(255)
);

alter table TestTempTable add constraint TestTempTable_pk
primary key (IntCol);

grant select on TestTempTable to public;

create procedure sp_Test (
    @a_InValue varchar(50),
    @a_InOutValue bigint
) as
begin
    noop1:
end;

create procedure sp_TestNoArgs as
begin
    nooop1:
end;

delete from TestNumbers;

insert into TestNumbers
values (1, 25, 5.2, 7.3, 125.25);

insert into TestNumbers
values (2, 1234567890123456, 25.1, 17.8, 245.37);

insert into TestNumbers
values (3, 9876543210, 37.8, 235.19, 25.99);

insert into TestNumbers
values (4, 98765432101234, 77.27, 922.78, 445.79);

delete from TestStrings;

insert into TestStrings
values (1, 'String 1', 'Fix01', null);

insert into TestStrings
values (2, 'String 2B', 'Fix02', 'Nullable One');

insert into TestStrings
values (3, 'String 3XX', 'Fix03', null);

insert into TestStrings
values (4, 'String 4YYY', 'Fix04', 'Nullable Two');

delete from TestDates;

insert into TestDates
values (1, '2020-02-08', '2019-12-20 18:35:25',
           '1969-07-29', '1988-01-25 08:24:13');

insert into TestDates
values (2, '1978-02-12', '2009-02-20 08:23:12', null, null);

insert into TestDates
values (3, '2000-06-18', '2007-01-28 06:22:11',
           '1988-06-30', '1998-04-29 11:35:24');

insert into TestDates
values (4, '1999-10-05', '2009-02-19 00:01:02', null, null);

insert into TestBooleans
values (1, 1);

insert into TestBooleans
values (2, 0);

insert into TestBooleans
values (3, 1);

insert into TestBooleans
values (4, 1);

insert into TestBooleans
values (5, null);

insert into TestBooleans
values (6, 0);
