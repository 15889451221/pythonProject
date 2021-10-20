
class demo:
    def load(self,rule):
        parse = None
        if "xml" == rule:
            parse = xmlparse()
        elif "json" == rule:
            parse = JsonParseRuleFactory().create_parse()
        elif "excel" == rule:
            parse = excelparse()
        elif "csv" ==rule:
            parse =csvparse()
        else:
            parse =otherparse()
        parse.parse()



class IParseRuleFactory:
    def create_parse(self):
        raise ValueError()

class JsonParseRuleFactory(IParseRuleFactory):
    def create_parse(self):
        return jsonparse()

# class factory:
#     def create_parse(self,rule):
#         parse = factory().create_parse(rule)
#         parse.parse()

class Iparse:
    def parse(self):
        raise ValueError()

class xmlparse(Iparse):
    def parse(self):
        print("xmlparse")
class jsonparse(Iparse):
    def parse(self):
        print("jsonparse")
class excelparse(Iparse):
    def parse(self):
        print("excelparse")
class csvparse(Iparse):
    def parse(self):
        print("csvparse")
class otherparse(Iparse):
    def parse(self):
        print("otherparse")

if __name__ == '__main__':
    demo().load("json")