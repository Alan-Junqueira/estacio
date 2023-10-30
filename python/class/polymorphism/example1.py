class Argentina:
    def capital(self):
        print("Buenos Aires is the capital of Argentina.")

    def language(self):
        print("Spanish is the primary language of Argentina.")


class Brasil:
    def capital(self):
        print("Brasília is the capital of Brazil.")

    def language(self):
        print("Portuguese is the primary language of Brazil.")


obj_arg = Argentina()
obj_bra = Brasil()

for country in (obj_arg, obj_bra):
    country.capital()
    country.language()
