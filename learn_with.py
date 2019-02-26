class WithLearning:
    def __init__(self):
        print("init")
    def __enter__(self):
        print("enter....")
        #return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
    def __del__(self):
        print("del")

    def test(self):
        print("test")

with WithLearning() as wl:
    print("in with")
    print(wl)