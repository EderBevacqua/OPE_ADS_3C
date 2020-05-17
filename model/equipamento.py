class Equipamento():
    def __init__(self, id, numeroEquipamento, marca, modelo, situacao):
        self.id = id
        self.numeroEquipamento = numeroEquipamento
        self.marca=marca
        self.modelo = modelo
        self.situacao = situacao

    def atualizar(self, dados):
        try:
            id = dados["id"]
            numeroEquipamento = dados["numeroEquipamento"]
            marca= dados["marca"]
            modelo = dados["modelo"]
            situacao = dados["situacao"]
            self.id, self.numeroEquipamento, self.marca, self.modelo, self.situacao = id, numeroEquipamento, marca, modelo, situacao
            return self
        except Exception as e:
            print("Problema ao criar novo equipamento!")
            print(e)

    def get_equip(self):
        return self.id, self.numeroEquipamento, self.marca, self.modelo, self.situacao
        #print("{}, {}, {}, {}, {}".format(self.id, self.numeroEquipamento, self.marca, self.modelo, self.situacao))

    def getDados(self):
        return self.id, self.numeroEquipamento, self.marca, self.modelo, self.situacao

    def dictEquipamento(self):
        d = dict()
        d["id"] = self.id
        d["numeroEquipamento"] = self.numeroEquipamento
        d["marca"] = self.marca
        d["modelo"] = self.modelo
        d["situacao"] = self.situacao
        return d

    @staticmethod
    def criar(dados):
        try:
            id = dados["id"]
            numeroEquipamento = dados["numeroEquipamento"]
            marca= dados["marca"]
            modelo = dados["modelo"]
            situacao = dados["situacao"]
            return Equipamento(id=id, numeroEquipamento=numeroEquipamento, marca=marca, modelo=modelo, situacao=situacao)
        except Exception as e:
            print("Problema ao criar novo Equipamento!")
            print(e)
