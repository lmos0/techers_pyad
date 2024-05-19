from caps_lock import caixa_alta, concatenar_strings


def main():
    test_caixa_alta()
    test_concatenar_strings

def test_caixa_alta():
    assert caixa_alta("luis") == "Luis"
    assert caixa_alta("élton") == "Élton"
    assert caixa_alta("caio") == "Caio"

def test_concatenar_strings():
    assert concatenar_strings("tudo", 'bem') == "tudobem"
    assert concatenar_strings('2',"8") == "28"

if __name__ == "__main__":
    main()