import requests
import os.path as path
import config

class YaUploader:
    def __init__(self, token: str):
        self.HOST = 'https://cloud-api.yandex.net:443'
        self.headers = {'Accept': 'application/json', 'Authorization': token}
        self.upload_uri = '/v1/disk/resources/upload'

    def upload(self, file_path: str):
        url = self.HOST + self.upload_uri
        file_ = path.basename(file_path)
        params = {'path': file_, 'overwrite': 'true'}
        response = requests.get(url, headers=self.headers, params=params)
        upload_resp = requests.put(response.json()['href'], headers=self.headers, data=open(file_, 'rb'))
        if upload_resp.status_code == 200 or 201:
            print('Всё получилось.')
        else:
            print('Что-то пошло не так.')

if __name__ == '__main__':
    path_to_file = 'test.txt' #input('Введите путь к файлу: ')
    token = config.TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)