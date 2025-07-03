# decorator is attached by @, exception handlers, time measurements, logger 
import random
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except ValueError:
            print("Value is wrong")
        except FileNotFoundError:
            print("Please create file first")
        except KeyboardInterrupt:
            print("Did you hit escape btn?")
        except:
            pass
    return wrapper


@exception_handler
def find_max_vowels():
    match random.randint(1, 3):
        case 1:
            raise ValueError
        case 2: 
            raise FileNotFoundError
        case 3: 
            raise KeyboardInterrupt
        

find_max_vowels()


