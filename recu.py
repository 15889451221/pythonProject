
class IdMaker:
    _instance = None
    __id = -1

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_id(self):
        self.__id += 1
        return self.__id

def test_id_maker():
    id1 = IdMaker().get_id()
    id2 = IdMaker().get_id()
    id3 = IdMaker().get_id()
    print(id1,id2,id3)

if __name__ == "__main__":
    test_id_maker()


