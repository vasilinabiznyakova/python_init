# class MyContextManager:
#     def __enter__(self):
#         # Ініціалізація ресурсу
#         print("Enter the block")
#         return self  # Може повертати об'єкт

#     def __exit__(self, exc_type, exc_value, traceback):
#         # Звільнення ресурсу
#         print("Exit the block")
#         if exc_type:
#             print(f"Error detected: {exc_value}")
#         # Повернення False передає виключення далі, True - поглинає виключення.
#         return False


# # Використання власного менеджера контексту
# with MyContextManager() as my_resource:
#     print("Inside the block")
#     raise Exception("Something went wrong")


# from contextlib import contextmanager


# @contextmanager
# def my_context_manager():
#     # Ініціалізація ресурсу
#     print("Enter the block")
#     try:
#         yield  # Місце виконання блоку `with`
#     except Exception as e:
#         # Обробка виключень
#         print(f"Error detected: {e}")
#         # Можна ре-підняти виключення або вирішити його тут
#         raise
#     finally:
#         # Звільнення ресурсу
#         print("Exit the block")


# # Використання
# with my_context_manager():
#     print("Inside the block")
#     raise Exception("Something went wrong")




