import os
import pandas as pd  # type: ignore


def validar_estrutura(pasta: str, arquivo_modelo: str):

    # Lê o arquivo modelo
    nome_modelo, ext_modelo = os.path.splitext(arquivo_modelo)
    if ext_modelo.lower() == ".csv":
        df_modelo = pd.read_csv(arquivo_modelo, sep=None, engine="python")
    elif ext_modelo.lower() in [".xlsx", ".xls"]:
        df_modelo = pd.read_excel(arquivo_modelo)
    else:
        raise ValueError(
            "Formato de arquivo modelo não suportado. Use CSV ou XLSX.")

    colunas_referencia = list(df_modelo.columns)

    # Percorre os arquivos da pasta
    arquivos = os.listdir(pasta)
    estruturas = {}
    inconsistencias = {}
    erros = []

    for arquivo in arquivos:
        caminho = os.path.join(pasta, arquivo)
        nome, ext = os.path.splitext(arquivo)

        # pula o próprio arquivo modelo
        if caminho == arquivo_modelo:
            continue

        try:
            if ext.lower() == ".csv":
                df = pd.read_csv(caminho, sep=None, engine="python")
            elif ext.lower() in [".xlsx", ".xls"]:
                df = pd.read_excel(caminho)
            else:
                continue

            estruturas[arquivo] = list(df.columns)

            if list(df.columns) != colunas_referencia:
                inconsistencias[arquivo] = list(df.columns)

        except Exception as e:
            erros.append((arquivo, str(e)))

    return {
        "colunas_referencia": colunas_referencia,
        "estruturas": estruturas,
        "inconsistencias": inconsistencias,
        "erros": erros,
    }


# Exemplo de uso:
pasta = r"C:\proj_pessoal\VALIDADOR\TESTES"
arquivo_modelo = r"C:\proj_pessoal\VALIDADOR\TESTES\modelo.csv"
resultado = validar_estrutura(pasta, arquivo_modelo)

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
