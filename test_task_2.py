import pytest
from tasks.task_2 import YandexDiskFolder, create_folder

class TestYandexDiskFolder:

    # Папка создана/ уже существует 
    @pytest.mark.parametrize( "x",
                            [
                            201, 409
                            ]
    )
    def test_crate_folder(self, x): 
        assert  create_folder().status_code == x
