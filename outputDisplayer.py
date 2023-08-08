import win32console
import multiprocessing

def subprocess(queue):
    win32console.FreeConsole() #Frees subprocess from using main console
    win32console.AllocConsole() #Creates new console and all input and output of subprocess goes to this new console
    while True:
        print(queue.get())


class OutputDisplayer:
    def __init__(self):
        self.queue = multiprocessing.Queue()
        multiprocessing.Process(target=subprocess, args=[self.queue]).start()


    def sub_print(self, text):
        self.queue.put(text)

#NOTE!!! a check is required a check is required -> if __name__ == '__main__':
# if __name__ == '__main__':
#     con1 =OutputDisplayer()
#     con2 =OutputDisplayer()

#     print('This is main console')
#     print('main:')

#     con1.sub_print('This is console1')
#     con1.sub_print('con1:')

#     con2.sub_print('This is console2')
#     con2.sub_print('con2:')
