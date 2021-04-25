from src.freeos import iterations

class FreeDao(object):
    def __init__(self):
        self.iterations=iterations.Iterations()
    def __repr__(self):
        return "I am FreeDAO object"

if __name__=="__main__":
    freedao = FreeDao()
    print(repr(freedao))
    freedao.iterations.admin_passwords()