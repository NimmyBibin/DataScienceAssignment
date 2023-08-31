create database userinfo;
use userinfo;
CREATE TABLE User_Activity1 (
    user_id INT NOT NULL,
    activity_date DATE NOT NULL,
    activity_type ENUM('login', 'click', 'purchase') NOT NULL,
    PRIMARY KEY (user_id, activity_date)
);
insert into User_Activity1  values(1, 11/10/2021,"login" ),
(2 , 10/10/2021,'click' );
SELECT
    activity_date,
    ROUND(
        (COUNT(DISTINCT CASE WHEN activity_type IS NOT NULL THEN user_id END) * 100.0) /
        COUNT(DISTINCT user_id), 
        2
    ) AS daily_engagement_rate
FROM
    User_Activity1
GROUP BY
    activity_date
ORDER BY
    activity_date;
select * from 