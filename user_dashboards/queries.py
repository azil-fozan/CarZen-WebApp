RECEIPTS_MAIN_TABLE = '''
SELECT `receipt`.`id`,
       `customer`.`name`,
       `receipt`.`active_date`,
       `receipt`.`paid_amount`,
       `receipt`.`expiry_date`,
       `receipt`.`status`,
       sum(`product`.`price`*`bill`.`quantity`)
FROM `receipt`
    left JOIN `customer` ON (`receipt`.`customer` = `customer`.`id`)
    LEFT OUTER JOIN `bill` ON (`receipt`.`id` = `bill`.`receipt_id`)
    LEFT OUTER JOIN `product` ON (`bill`.`product_id` = `product`.`id`)
WHERE `receipt`.`created_by` = {} -- user id
group by receipt_id
order by `receipt`.`expiry_date`;'''

RECEIPTS_TOTAL_AMOUNTS = '''
select r.id, sum(p.price*b.quantity)
from bill b
    left join product p on b.product_id = p.id
    left join receipt r on b.receipt_id = r.id
where r.id in ({})
group by r.id;'''

