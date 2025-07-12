use segment ;
SELECT * from customers ;
SELECT * from transactions ;

##########################
# total number of category to know where porple investing more 
SELECT
category , 
count(*) as count_category
from transactions 
group by category 
ORDER BY count_category desc;

#####################33
SELECT * from transactions ;
# total spend category  txn_tyope
SELECT
category , 
sum(txn_amount) as total_amount
from transactions
group by category
ORDER BY category desc  ;

#################################
SELECT * from transactions ;
# which comapny using most 
SELECT
merchant_name , 
count(*) as total_customer
from transactions
GROUP BY merchant_name
ORDER BY total_customer desc ;

# paytm is somethings most of people is using make be for payment and bills , movies and etc 

SELECT * from transactions ;

SELECT
category  ,
sum(txn_amount) over() as amounts 
from transactions 
ORDER BY amounts ;
#####################
SELECT * from customers ;
SELECT
distinct city , 
 occupation ,
sum(income) over(PARTITION BY occcupation) as total_sums 
from customers
ORDER BY total_sums DESC;

##########################A
# number of employee in sector vs gneder 


SELECT 
distinct occupation ,
gender ,
count(gender) over(PARTITION BY occupation) as count_gender 
from customers ;

##############################ALTER
SELECT
occupation ,
round(avg(age) ,2) as average_age 
from customers
GROUP BY occupation 
ORDER BY average_age desc  ;







