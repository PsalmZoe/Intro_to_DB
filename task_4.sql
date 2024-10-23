-- Use the alx_book_store database
USE alx_book_store;

-- Select full description of the Books table
SELECT 
    COLUMN_NAME AS 'Column Name', 
    COLUMN_TYPE AS 'Data Type', 
    IS_NULLABLE AS 'Is Nullable', 
    COLUMN_DEFAULT AS 'Default Value', 
    COLUMN_KEY AS 'Key', 
    EXTRA AS 'Extra Info'
FROM 
    INFORMATION_SCHEMA.COLUMNS 
WHERE 
    TABLE_NAME = 'Books' AND 
    TABLE_SCHEMA = 'alx_book_store';
