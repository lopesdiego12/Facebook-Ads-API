# script com funções uteis que podem ser utilizadas por qualquer metódo

# importa as libs que serão utilizadas
import csv

def download_csv(list, file_path, encode=None):
	# busca o cabeçalho do relatório
	header = list[0].keys()
	
	# cria o arquivo .csv do relatório
	with open(file_path, 'w', newline='', encoding=encode) as output_file:
		dict_writer = csv.DictWriter(output_file, header)
		dict_writer.writeheader()
		dict_writer.writerows(list)