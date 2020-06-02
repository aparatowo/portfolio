import sqlite3


def initialize_db(cursor):
    query = """
        DROP TABLE IF EXISTS "backpack";
    
        CREATE TABLE "backpack"
        (
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "name" TEXT NOT NULL,
            "type" INTEGER CHECK ("type" IN ('equipment', 'food')),
            "quantity" INTEGER DEFAULT 1,
            "weight" FLOAT
        );
    """

    cursor.executescript(query)


def populate_with_sample_data(cursor):
    query = """
        INSERT INTO "backpack" VALUES (NULL, 'Szczoteczka do zębów', 'equipment', 1, 0.08);
        INSERT INTO "backpack" VALUES (NULL, 'Skarpety', 'equipment', 4, 0.06);
        INSERT INTO "backpack" VALUES (NULL, 'Wafelek czekoladowy', 'food', 6, 0.17);
        INSERT INTO "backpack" VALUES (NULL, 'Latarka czołowa', 'equipment', 1, 0.1);
    """

    cursor.executescript(query)


if __name__ == '__main__':
    db_location = 'zaddom08.db'
    conn = sqlite3.connect(db_location)
    cursor = conn.cursor()

    initialize_db(cursor)
    populate_with_sample_data(cursor)

    conn.commit()
    conn.close()
