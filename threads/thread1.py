# importação de biblioteca
import threading
import time
import math
# Estrutura da Thread
def estrutura(nome, inicio, fim):
    for i in range(inicio, fim +1):
        print(f"{nome} -> {i}")
    # pausa entre as durações de contagem
    time.sleep(4)

#criar thread
thread1 = threading.Thread(target=estrutura, args=("Thread-1", 1, 10))
thread2 = threading.Thread(target=estrutura, args=("Thread-2", 10, 20))

#rodar
thread1.start()
thread2.start()

#estado de espera
thread1.join()
thread2.join()




