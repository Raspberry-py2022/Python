Input = "Your_Hitomi"

class 느금마:
    def __init__(self,_Input):
        self.Input = _Input

    def 암호화(self):
        _work = 0
        for i in range(len(Input)):

            _work += ord(Input[i])* (len(Input) * 137)

        return _work


A = 느금마(Input)

print(A.암호화())
