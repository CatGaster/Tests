import pytest
from tasks.task_1 import task_1_1, task_1_2, task_1_3

class TestTask_1:

    # проверка типа
    @pytest.mark.parametrize("x", 
                             [
                                str, list, int
                              ]
                              )
    def test_task_str(self, x):
        assert type((task_1_1())) == x

    # проверка совпадений
    @pytest.mark.parametrize("x",
                             [
                              "Адилет", "Азамат", "Владимир", "Денис", "Дмитрий",
                                "Евгений", "Елена",  "Олег", "Павел", "Ринат", "Филипп", "Эдгар", "Юрий"
                             ] 
                            ) 
    def test_task_count_unique(self, x):
        assert task_1_1().count(x,) == 1
    
class TestTask_2:

    # проверка типа
    @pytest.mark.parametrize("x",
                             [
                                str, list, int
                             ]
    )
    def test_task_str(self, x):
        assert type(task_1_2()) == x
   
    #не больше 3-х имён
    def test_task_count(self):
        assert task_1_2().count(':') == 3

class TestTask_3:

    # проверка типа
    @pytest.mark.parametrize("x",
                             [
                                str, list, int
                             ]
    )
    def test_task_str(self):
        assert type(task_1_3()) == str

    # сравнение
    def test_task_compare(self):
        count = ""
        numbers =[]
        task = task_1_3()
        for i in task:
            if i.isdigit():
                count += i
            else:
                if count.isdigit():
                    numbers.append(int(count))
                    count = ""
        assert numbers[0] > numbers[1]








    
    
