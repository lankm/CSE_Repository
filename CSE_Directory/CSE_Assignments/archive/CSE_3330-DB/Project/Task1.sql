-- 1: [5]

ALTER TABLE BOOK_LOANS
  ADD Late INTEGER;

UPDATE BOOK_LOANS
  SET Late = 
    CASE WHEN Returned_Date > Due_Date
      THEN 1 
      ELSE 0 
    END;


-- 2: [5]

ALTER TABLE LIBRARY_BRANCH
  ADD LateFee DECIMAL(3,2) NOT NULL DEFAULT 1.00;

UPDATE LIBRARY_BRANCH
  SET LateFee = CAST((Branch_Id+2) AS DECIMAL(3,2))/4.00;


-- 2: [10]
CREATE VIEW IF NOT EXISTS vBookLoanInfo AS
  SELECT Card_no, 
         Name AS "Borrower Name", 
         Date_Out, 
         Due_Date, 
         Returned_date, 
         (JULIANDAY(Returned_Date) - JULIANDAY(Date_Out)) AS TotalDays, 
         Title AS "Book Title", 
         (max(0, JULIANDAY(Returned_Date) - JULIANDAY(Due_Date))) AS DaysLate, 
         Branch_Id, 
         (LateFee * (max(0, JULIANDAY(Returned_Date) - JULIANDAY(Due_Date)))) AS LateFeeBalance
  FROM BORROWER NATURAL JOIN BOOK_LOANS NATURAL JOIN LIBRARY_BRANCH NATURAL JOIN BOOK;

SELECT * FROM vBookLoanInfo;
