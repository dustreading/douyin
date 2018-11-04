from multiprocess import *
from multiprocess.action import start
from multiprocessing import Process

if __name__ == "__main__":
    process_list = [
        Process(target=start, args=("http://localhost:4723/wd/hub", CAP_F, "Pang17171717")),
        Process(target=start, args=("http://localhost:4725/wd/hub", CAP_S, "77618724"))]
    for p in process_list:
        p.start()
    for p in process_list:
        p.join()
