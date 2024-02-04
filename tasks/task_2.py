import requests

class YandexDiskFolder:
    def __init__(self, y_token):
            self.y_token = y_token

    def get_headers(self):
        return {
            "Authorization": self.y_token
        }

    def name_folder(self):
        return {
            "path": "test_folder"
        }

    def param(self, params):
          self.params = params

    def create_folder(self):
        return requests.put("https://cloud-api.yandex.net/v1/disk/resources", 
                            headers = self.get_headers(), params = self.name_folder())
    
    def refresh(self):
        return requests.get("https://cloud-api.yandex.net/v1/disk/resources", 
                            headers = self.get_headers(), params = self.param(self.params))

def create_folder():
    yandex_disk = YandexDiskFolder(input("Введите Яндекс OAuth токен: "))
    response = yandex_disk.create_folder()
    return response

if __name__ == "__main__":
    create_folder()

        
        

