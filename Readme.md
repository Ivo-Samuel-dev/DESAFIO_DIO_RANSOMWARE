Esse projeto, para toda sua funcionalidade, foi necessário dentro de um ambiente com python instalado, as bibliotecas cryptography e pynput instaladas, mantendo uma organização entre os testes a serem realizados, considerando a seguinte estrutura:

PASTA_PRINCIPAL:
    ---> Keylogger (pasta onde ficará armazenado os arquivos necessários para testar o Keylogger)
        --> logs (onde ficará armazenado o arquivo final com as entradas dos digitos do teclado)
        --> keylogger.py (arquivo responsável pela funcionalidade do Keylogger)
    ---> ransomware (pasta onde ficará armazenado os arquivos necessários para testar o ransomware)
        --> encrypt.py (arquivo responsável por simular o ataque de criptografia em arquivos / documentos)
        --> decrypt.py (arquivo responsável por reverte o ataque)
    ---> test_files (Pasta onde ficará os arquivos de teste para sofrer o ataque)
    
