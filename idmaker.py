from threading import Lock


class IdMaker:
    _instacelock = Lock()
    _instace = None
    _id = -1

    def __new__(cls):
        raise ImportError("Instantition not allowed")

    @classmethod
    def get_instance(cls):
        with cls._instacelock:
            if cls._instace is None:
                cls._instace = super().__new__(cls)
            return cls._instace

    def get_id(self):
        self._id += 1
        return self._id

def test_id_maker():

    # IdMaker 是单例类，只允许有一个实例

    id1 = IdMaker.get_instance().get_id()

    id2 = IdMaker.get_instance().get_id()

    id3 = IdMaker.get_instance().get_id()

    print(id1, id2, id3)

if __name__ == '__main__':
    test_id_maker()

