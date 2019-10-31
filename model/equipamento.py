class Equipamento():
    def __init__(self, numeroEquipamento, marca, modelo, status):
        self.numeroEquipamento = numeroEquipamento
        self.marca=marca
        self.modelo = modelo
        self.status = status

    def atualizar(self, dados):
        try:
            numeroEquipamento = dados["numeroEquipamento"]
            marca= dados["marca"]
            modelo = dados["modelo"]
            status = dados["status"]
            self.numeroEquipamento, self.marca, self.modelo, self.status = numeroEquipamento, marca, modelo, status
            return self
        except Exception as e:
            print("Problema ao criar novo equipamento!")
            print(e)

    def __dict__(self):
        d = dict()
        d["numeroEquipamento"]=self.numeroEquipamento
        d["marca"]= self.marca
        d["modelo"]= self.modelo
        d["status"]= self.status
        return d

    @staticmethod
    def criar(dados):
        try:
            numeroEquipamento = dados["numeroEquipamento"]
            marca= dados["marca"]
            modelo = dados["modelo"]
            status = dados["status"]
            return Equipamento(numeroEquipamento=numeroEquipamento, marca=marca, modelo=modelo, status=status)
        except Exception as e:
            print("Problema ao criar novo equipamento!")
            print(e)