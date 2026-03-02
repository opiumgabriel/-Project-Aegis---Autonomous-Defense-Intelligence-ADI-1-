import hashlib
import os
import time

# Configurações do Protocolo Aegis
DIRETORIO_SENSIVEL = "./documentos_estrategicos"

def gerar_hash(caminho_arquivo):
    """Gera hash SHA-256 para verificar integridade."""
    sha256 = hashlib.sha256()
    with open(caminho_arquivo, "rb") as f:
        for bloco in iter(lambda: f.read(4096), b""):
            sha256.update(bloco)
    return sha256.hexdigest()

def monitorar():
    print(f"--- [🛡️ PROJECT AEGIS: MONITORAMENTO ATIVO] ---")
    if not os.path.exists(DIRETORIO_SENSIVEL):
        os.makedirs(DIRETORIO_SENSIVEL)
        with open(f"{DIRETORIO_SENSIVEL}/alerta.txt", "w") as f:
            f.write("Dados de Defesa Nacional.")

    # Mapeamento inicial (Baseline)
    hashes_originais = {arq: gerar_hash(os.path.join(DIRETORIO_SENSIVEL, arq)) 
                       for arq in os.listdir(DIRETORIO_SENSIVEL)}

    try:
        while True:
            time.sleep(5)
            for arq in os.listdir(DIRETORIO_SENSIVEL):
                caminho = os.path.join(DIRETORIO_SENSIVEL, arq)
                hash_atual = gerar_hash(caminho)
                
                if hash_atual != hashes_originais.get(arq):
                    print(f"\n[⚠️ ALERTA DE INTRUSÃO DETECTADO em {arq}]")
                    print(f"[!] Alteração de integridade suspeita (Possível Ransomware).")
                    print(f"[AÇÃO]: Bloqueando acesso ao arquivo e gerando log de defesa.")
                    hashes_originais[arq] = hash_atual
    except KeyboardInterrupt:
        print("\n[INFO] Monitoramento Aegis encerrado pelo operador.")

if __name__ == "__main__":
    monitorar()
