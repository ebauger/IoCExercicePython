from Interfaces import List, File, FileListService
import sqlite3
# Assuming we have a SQLite database named "files.db" with a table "files"
DB_NAME = "files.db"

""" 
CREATE TABLE files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    content BLOB NOT NULL
); 

-- Inserting first dummy file
INSERT INTO files (name, content) VALUES ('file1.txt', 'This is the content of file1.');

-- Inserting second dummy file
INSERT INTO files (name, content) VALUES ('file2.txt', 'Content for file2 goes here.');

-- Inserting third dummy file
INSERT INTO files (name, content) VALUES ('file3.txt', 'And this is for file3.');

"""


class SQLiteFileListService(FileListService):
    def fetch_files(self) -> List[File]:
        files: List[File] = []
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            for row in cursor.execute("SELECT name, content FROM files"):
                name, content = row
                files.append({"name": name, "content": content})
        return files
