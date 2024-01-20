DROP TABLE IF EXISTS PUBLISHER;
CREATE TABLE PUBLISHER (
  Publisher_Name    VARCHAR(255)    NOT NULL    PRIMARY KEY,
  Phone             VARCHAR(20)     NOT NULL,
  Address           VARCHAR(255)    NOT NULL
);

DROP TABLE IF EXISTS LIBRARY_BRANCH;
CREATE TABLE LIBRARY_BRANCH (
  Branch_Id         INTEGER         NOT NULL    PRIMARY KEY,
  Branch_Name       VARCHAR(255)    NOT NULL    UNIQUE,
  Branch_Address    VARCHAR(255)    NOT NULL
);

DROP TABLE IF EXISTS BORROWER;
CREATE TABLE BORROWER (
  Card_No           INTEGER         NOT NULL    PRIMARY KEY,
  Name              VARCHAR(255)    NOT NULL,
  Address           VARCHAR(255)    NOT NULL,
  Phone             VARCHAR(20)     NOT NULL
);

DROP TABLE IF EXISTS BOOK;
CREATE TABLE BOOK (
  Book_Id           INTEGER         NOT NULL    PRIMARY KEY,
  Title             VARCHAR(255)    NOT NULL,
  Book_Publisher    VARCHAR(255)    NOT NULL
);

DROP TABLE IF EXISTS BOOK_LOANS;
CREATE TABLE BOOK_LOANS (
  Book_Id           INTEGER         NOT NULL,
  Branch_Id         INTEGER         NOT NULL,
  Card_No           INTEGER         NOT NULL,
  Date_Out          DATE            NOT NULL,
  Due_Date          DATE            NOT NULL,
  Returned_Date     DATE,
  PRIMARY KEY (Book_Id, Branch_Id, Card_No),
  FOREIGN KEY (Book_Id) REFERENCES BOOK(Book_Id),
  FOREIGN KEY (Branch_Id) REFERENCES LIBRARY_BRANCH(Branch_Id),
  FOREIGN KEY (Card_No) REFERENCES BORROWER(Card_No)
);

DROP TABLE IF EXISTS BOOK_COPIES;
CREATE TABLE BOOK_COPIES (
  Book_Id           INTEGER         NOT NULL,
  Branch_Id         INTEGER         NOT NULL,
  No_Of_Copies      INTEGER         NOT NULL,
  PRIMARY KEY (Book_Id, Branch_Id),
  FOREIGN KEY (Book_Id) REFERENCES BOOK(Book_Id),
  FOREIGN KEY (Branch_Id) REFERENCES LIBRARY_BRANCH(Branch_Id)
);

DROP TABLE IF EXISTS BOOK_AUTHORS;
CREATE TABLE BOOK_AUTHORS (
  Book_Id           INTEGER         NOT NULL,
  Author_Name       VARCHAR(255)    NOT NULL,
  PRIMARY KEY (Book_Id, Author_Name),
  FOREIGN KEY (Book_Id) REFERENCES BOOK(Book_Id)
);