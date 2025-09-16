import os
import pandas as pd  # type: ignore


def validar_estrutura(pasta: str):
    arquivos = os.listdir(pasta)
    estruturas = {}
    erros = []

    for arquivo in arquivos:
        caminho = os.path.join(pasta, arquivo)
        nome, ext = os.path.splitext(arquivo)

        try:
            if ext.lower() == ".csv" or ext.lower() == ".txt":
                # detecta separador automaticamente
                df = pd.read_csv(caminho, sep=None, engine="python")
            elif ext.lower() in [".xlsx", ".xls"]:
                df = pd.read_excel(caminho)
            else:
                continue  # ignora outros formatos

            estruturas[arquivo] = list(df.columns)
        except Exception as e:
            erros.append((arquivo, str(e)))

    # Verificar consistência das colunas
    colunas_referencia = None
    inconsistencias = {}

    for arq, cols in estruturas.items():
        if colunas_referencia is None:
            colunas_referencia = cols
        elif cols != colunas_referencia:
            inconsistencias[arq] = cols

    return {
        "colunas_referencia": colunas_referencia,
        "estruturas": estruturas,
        "inconsistencias": inconsistencias,
        "erros": erros,
    }


# Exemplo de uso:
pasta = r"C:\proj_pessoal\VALIDADOR\TESTES"
resultado = validar_estrutura(pasta)

print("Colunas de referência:", resultado["colunas_referencia"])
print("\nEstruturas identificadas:")
for arq, cols in resultado["estruturas"].items():
    print(f"{arq}: {cols}")

print("\nInconsistências:")
for arq, cols in resultado["inconsistencias"].items():
    print(f"{arq}: {cols}")

if resultado["erros"]:
    print("\nErros ao ler arquivos:")
    for arq, erro in resultado["erros"]:
        print(f"{arq}: {erro}")
