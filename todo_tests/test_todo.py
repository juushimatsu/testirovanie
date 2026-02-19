import unittest
import os
import tempfile
import shutil
import json
from unittest.mock import patch
import main  

class TestTaskManager(unittest.TestCase):
    def setUp(self): # создание temp файла и подмена TASK_FILE
        self.temp_dir = tempfile.mkdtemp()
        self.temp_file = os.path.join(self.temp_dir, "tasks.json")
        self.original_task_file = main.TASK_FILE
        main.TASK_FILE = self.temp_file

    def tearDown(self): # удаление temp файла
        shutil.rmtree(self.temp_dir)
        main.TASK_FILE = self.original_task_file

    def test_load_tasks_no_file(self): # тест при отсутствии файла 
        tasks = main.load_tasks()
        self.assertEqual(tasks, [])

    def test_save_and_load_tasks(self): # сохранение и загрузка задачи
        test_tasks = [{"id": 1, "description": "Test task", "completed": False}]
        main.save_tasks(test_tasks)
        loaded = main.load_tasks()
        self.assertEqual(loaded, test_tasks)

    @patch('builtins.input', return_value="Купить молоко")
    def test_add_task(self, mock_input): # добавление задачи
        tasks = []
        main.add_task(tasks) 
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Купить молоко")
        self.assertFalse(tasks[0]["completed"])
        loaded = main.load_tasks() 
        self.assertEqual(loaded, tasks)
        # проверка добавления и сохранения

    @patch('builtins.input', side_effect=["1", "Новое описание"])
    def test_edit_task(self, mock_input): # тест редактирования
        tasks = [{"id": 1, "description": "Старое описание", "completed": False}]
        main.edit_task(tasks)
        self.assertEqual(tasks[0]["description"], "Новое описание")
        loaded = main.load_tasks()
        self.assertEqual(loaded[0]["description"], "Новое описание")

    @patch('builtins.input', return_value="1")
    def test_complete_task(self, mock_input): # тест смены статуса
        tasks = [{"id": 1, "description": "Сделать зарядку", "completed": False}]
        main.complete_task(tasks)
        self.assertTrue(tasks[0]["completed"])
        main.complete_task(tasks)
        self.assertFalse(tasks[0]["completed"])
        loaded = main.load_tasks()
        self.assertEqual(loaded[0]["completed"], False)
        # повторная проверка и проверка сохранения 

if __name__ == "__main__":
    unittest.main()