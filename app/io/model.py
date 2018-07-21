#!/usr/bin/env python3

import uuid
import os
from .. import app

from werkzeug.utils import secure_filename


class FileManager():
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

    @staticmethod
    def allowed_file(file_extension: str) -> bool:
        return '.' in file_extension and \
            file_extension.rsplit('.', 1)[1].lower(
            ) in FileManager.ALLOWED_EXTENSIONS

    @staticmethod
    def get_file_extension(filename: str) -> str:
        return '.' + filename.rsplit('.', 1)[1].lower()

    @staticmethod
    def get_secure_filename(filename: str) -> str:
        return secure_filename(filename)

    @staticmethod
    def get_profile_filename(email: str, file_extension: str) -> str:
        if FileManager.allowed_file(file_extension):
            base_name = email.rsplit('@', 1)[0].lower()
            print(base_name)
            filename = FileManager.get_secure_filename(
                '{0}{1}{2}'.format(
                    'profile_',
                    base_name,
                    file_extension))
            print(filename)
            return filename

        print('invalid' + filename)
        raise IOError('Invalid file extension.')

    @staticmethod
    def get_twit_filename(email: str, file_extension: str) -> str:
        if FileManager.allowed_file(file_extension):
            base_name = email.rsplit('@', 1)[0].lower()
            filename = FileManager.get_secure_filename(
                '{0}{1}{2}{3}'.format(
                    'twit_',
                    base_name,
                    str(uuid.uuid4().hex),
                    file_extension)
            )
            return filename

        print('invalid' + filename)
        raise IOError('Invalid filename.')

    @staticmethod
    def save_file(file, filename: str) -> None:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'])
        print(file_path)
        print(file_path + filename)
        file.save(file_path, filename)
