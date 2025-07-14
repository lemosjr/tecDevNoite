# 6. Um técnico em TI precisa organizar os arquivos recentes por nome. 
# Dada a lista ["relatorio.docx", "atendimento.pdf", "planilha.xlsx", "resumo.txt"],
# faça um programa que filtre apenas os arquivos com final .pdf ou .docx.

arquivos = ["relatorio.docx", "atendimento.pdf", "planilha.xlsx", "resumo.txt"]
arquivos_filtrados = [arq for arq in arquivos if arq.endswith((".pdf", ".docx"))]
print(arquivos_filtrados)
