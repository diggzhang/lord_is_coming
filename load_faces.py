#!/usr/bin/env python

import os
import sys
import glob
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
        # TODO 如果用户没有登记过，给登记一下
        pass

def load_file_list(file_lst):
    known_face_encodings = []
    known_face_names = []
    for file in file_lst:
        f = FileInfo(file)
        known_face_encodings.append(f.get_known_face_encodings())
        known_face_names.append(f.get_name())
    return {"names": known_face_names, "encoding": known_face_encodings}


def face_db():
    return load_file_list(
        glob.glob(os.getcwd() + "/images/*")
    )


if __name__ == '__main__':
    sys.exit(main())