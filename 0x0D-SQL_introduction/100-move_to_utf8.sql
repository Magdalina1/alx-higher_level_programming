-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
-- need to convert Database hbtn_0c_0, Table first_table, Field name in first_table to UTF8

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4, collate utf8mb4_unicode_ci;
ALTER first_table CONVERT TO CHARACTER SET utf8mb4, collate utf8mb4_unicode_ci;
