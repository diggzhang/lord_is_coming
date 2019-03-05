#!/usr/bin/env python

import os
import sys
import glob
import sqlite3
import face_recognition


class FileInfo:
    def __init__(self, file_abs_path):
        self.file = file_abs_path

    def get_name(self):
        this_file = str(self.file)
        return this_file.split('.')[0].split('/')[-1]

    def get_known_face_encodings(self):
        this_file = str(self.file)
        load_image = face_recognition.load_image_file(this_file)
        return face_recognition.face_encodings(load_image)[0]

    def sign_in_db(self):
        conn = sqlite3.connect('sign-in.db')
        c = conn.cursor()
        # Just be sure any changes have been committed or they will be lost.
        sql_str = """
            SELECT COUNT(1) FROM members WHERE NAME = '{name}'
        """.format(name=self.get_name())
        if c.execute(sql_str).fetchone()[0] == 0:
            insert_str = """
            INSERT INTO members VALUES ('{name}', 1000);
            """.format(name=self.get_name())
            c.execute(insert_str)
        c.close()
        conn.commit()
        conn.close()


def load_file_list(file_lst):
    known_face_encodings = []
    known_face_names = []
    for file in file_lst:
        f = FileInfo(file)
        f.sign_in_db()
        known_face_encodings.append(f.get_known_face_encodings())
        known_face_names.append(f.get_name())
    return {"names": known_face_names, "encoding": known_face_encodings}


def face_db():
    return load_file_list(
        glob.glob(os.getcwd() + "/images/*")
    )


def main():
    # print(
    face_db()
    # )


if __name__ == '__main__':
    sys.exit(main())