import pymysql

"""
一. 基本命令
    ○ 1. 启动服务:
        说明:以管理员身份运行cmd
        格式: net start 服务名称
        示例: net start mysql80

    ○ 2. 停止服务:    
        说明:以管理员身份运行cmd
        格式: net stop 服务名称
        示例: net stop mysql80    

    ○ 3. 连接数据库:  
        格式: mysql -u 用户名 -p
        示例: mysql -u root -p
              输入密码:（安装时设置）

    ○ 4. 退出登录（断开连接）:  
        格式: quit 或者 exit

    ○ 5. 查看版本（连接后执行）:  
        格式: select version();

    ○ 6. 显示当前时间（连接后执行）:  
        格式: select now();
        
    ○ 7. 远程连接:  
        格式: mysql -h ip地址 -u 用户名 -p
              输入对方mysql密码

              
二. 数据库操作
    
    ⊙ 1. 创建数据库
        格式: create database 数据库名 charset=utf8;
        示例: create database zzy charset=utf8;
    
    ⊙ 2. 删除数据库
        格式: drop database 数据库名 ;
        示例: drop database zzy ;
    
    ⊙ 3. 切换数据库
        格式: use 数据库名 ;
        示例: use  zzy ;
    
    ⊙ 4. 查看当前选择的数据库
        格式: select database();


三. 表操作

    ◇ 1. 查看当前数据库中所有表
        格式: show tables ;
    
    ◇ 2. 创建表
        格式: create table 表名(列及类型) ;
        示例: create table student(id int auto_increment primary key,name varchar(20) not null) ;
        说明: auto_increment 表明自增长
              primary key  主键
              not null  不为空
        
    ◇ 3. 删除表
        格式: drop table 表名 ;
        示例: drop table  car ;
    
    ◇ 4. 查看表结构
        格式: desc  表名 ;
        示例: desc student ;
        
    ◇ 5. 查看建表语句
        格式: show create table  表名 ;
        示例: show create table student ;

    ◇ 6. 重命名表名
        格式: rename table  原表名 to 新表名 ;
        示例: rename table  student to newstudent ;
        
    ◇ 7. 修改表结构
        格式:alter table  表名 add|change|drop 列名 类型 ;
        示例: alter table car add isDelecte bit default 0 ;


四. 数据操作
    
    ☆. 增
        ●· 全列插入 : 
            格式: insert into 表名 values(...);
            示例: insert into car values(0,"大众","黄色",150,0);
            说明: 主键列是自动增长，但是在全列插入时需要站位，通常使用0，插入成功后以实际数据为准。
                  插入的数据类型，要和创建表时的数据类型一致
                  
        ●· 缺省插入 :
            格式: insert into 表名(列1,列2,...) values(值1,值2,...);
            示例: insert into car(id,name,color,maxSpeed) values(1,"别克","灰色",200);
        
        
        ●· 同时插入多条数据 :
            格式: insert into 表名  values(...),(...),(...),...;
            示例: insert into car values(2,"丰田","白色",160,0),(3,"福特","黑色",180,0),(4,"马自达","银色",150,1);
        
        
    ☆. 删
        格式: delete from 表名 where 条件 ;
        示例: delete from car where id=4 ;
        说明: 没有条件是全部删除，慎用！
        
       
    ☆. 改
        格式: update 表名 set 列1=值1,列2=值2,...  where 条件;
        示例: update car set  color="红色" where id=3;
        说明: 没有条件是全部列都修改，慎用！
    
    ☆. 查
        
        ∽· 基本语法
            格式: select * from 表名;
            说明: 
                ·1: from 关键字后面是表名，表示数据来源于这张表
                ·2: select 后面写表中的列名，如果是*表示在结果集中显示表彰的所有列
                ·3: 在select后面的列名部分，可以使用as为列名起别名，这个别名显示在结果集中
                ·4: 如果要查询多个列，之间使用逗号分隔
            示例:
                select name,color from car;
                select name as a,color from car;
        
        ∽· 消除重复行
            在select后面列前面使用distinct可以消除重复的行
            示例:
                select maxSpeed from car;
                select distinct maxSpeed from car;
                
        
        ∽· 条件查询
        
            々· 语法
                select * from 表名 where 条件
            
            々· 比较运算符
                等于          =
                大于          >
                小于          <
                大于等于      >=
                小于等于      <=
                不等于        != 或 <>
                
                示例：查询id值大于3的所有数据
                    select * from car where id>2;
            
            々· 逻辑运算符
                and     并且
                or      或者
                not     非
                
                示例：查询id值大于7的女同学
                    select * from student where id>7 and gender=0;
            
            々· 模糊查询
                like
                %            表示任意多个任意字符
                _（下划线）  表示一个任意的字符
                
                示例：查询姓习的同学
                    select * from student where name like "习%";
                    select * from car where name like "别%";
                    select * from car where name like "别_";
            
            々· 范围查询
                in                  表示在一个非连续的范围内
                between...and...    表示在一个连续的范围内
                
                示例：查询编号（id）为8,10,12的学生
                    select * from student where id in (8,10,12);
                    
                      查询编号为6到8的学生
                    select * from car where id between 6 and 8;
                
            々· 空判断
                注意: null 与 " "是不同的
                判断空: is null
                判断非空: is not null
                
                示例：查询没有地址的学生
                    select * from student where address is null;
            
            々· 优先级
                优先级依次递减:
                    小括号·not·比较运算符·逻辑运算符
                    and 比 or 优先级高，如果同时出现并希望优先级 or 高，需要结合()使用
        
                
        ∽· 查询表中的全部数据
            
            格式: select * from 表名 ;
            示例: select * from car ;
             
        ∽· 聚合
            为了快速得到统计数据，提供了5个聚合函数:
            
            ♀· count(*) --------> 表示计算总行数，括号中可以写 * 和 列名
                
                需求: 查询学生总数
                示例: select count(*) from student;
            
            ♀· max(列)  --------> 表示求此列的最大值
                
                需求: 查询女生的编号最大值
                示例: select max(id) from student where gender=0;
            
            ♀· min(列) -------->   表示求此列的最小值
                
                需求: 查询女生的编号最小值
                示例: select min(id) from student where gender=0;
            
            ♀· sum(列) -------->    表示求此列的和
                
                需求: 查询所有学生的年龄和
                示例: select sum(age) from student;
            
            ♀· avg(列) -------->    表示求此列的平均值
                
                需求: 查询所有学生的年龄平均值
                示例: select avg(age) from student;
        
        ∽· 分组
        
            1.按照字段分组，表示此字段相同的数据会被放到一个集合中。
            2.分组后，只能查询相同的数据列，对于有差异的数据列，无法显示在结果集中。
            3.可以对分组后的数据进行统计，做聚合运算
            
            语法:
                select 列1,列2,聚合... from 表名 group by 列1,列2,列3,...;
                
            示例: 查询男女生总数
                select gender,count(*) from student group by gender;
                
            分组后的数据筛选: 
                 select 列1,列2,聚合... from 表名 group by 列1,列2,列3,... having 列1,列2,..., 聚合...;
            
            示例: 查询男女生总数中男生总数（不写条件，默认值）
                select gender,count(*) from student group by gender having gender;
                
                    查询男女生总数中女生总数
                select gender,count(*) from student group by gender having gender=0;
                
            where 和 having 的区别 :
                where: 是对from后面指定的表进行筛选，属于对原始数据的筛选。
                having: 是对 group by 的结果进行筛选。
                
        
        ∽· 排序
            语法: 
                select * from 表名 order by 列1 asc|desc,列2 asc|desc,...;
            说明:
                1. 将数据按照列1进行排序，如果某些列1的值相同，则按照列2进行排序，以此类推。
                2. 默认按照从小到大的顺序排序（升序）
                3. asc 降序
                4. desc 升序
                
            示例: 按年龄排序
                select * from student order by age;
                
                  将没有被删除的数据按年龄排序
                select * from student where isDelect=0 order by age;
        
        ∽· 分页
            格式:
            示例:
        
        ∽·




"""



