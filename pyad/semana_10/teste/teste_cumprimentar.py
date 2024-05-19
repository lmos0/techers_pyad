from cumprimentar import ola

def test_ola():
    for nome in ["Élton", "Caio", "Luís"]:
        assert ola(nome) == f"Bom dia, {nome}"


test_ola()