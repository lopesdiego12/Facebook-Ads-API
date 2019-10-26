# Script baseado nos códigos de exemplos do SDK do facebook_business #

# importa as libs que serão utilizadas
import time
import csv
import util

def download_report(account, params, file_path):
	# chama a função assincrona para buscar as informações do relatório
	async_job = account.get_insights_async(params=params)
	
	status = async_job.remote_read()
	
	# enquanto não recuperar todas as informações a variavel async_job continua lendo os resultados
	while status['async_percent_completion'] < 100:
	  time.sleep(1)
	  status = async_job.remote_read()
	  
	# resultado do report
	result = async_job.get_result()
	
	# convertendo os resultados para lista de dicionários
	list = []
	for ad in result:
		dict = {}
		for prop in ad:
			dict[prop] = ad[prop]
		list.append(dict)
	
	# verifica se não foram encontrados registros para os filtros que foram passados
	if len(list) == 0:
		print ('Não foram encontrados registros com o filtro que foi passado.')
		return
	
	# download do relatório
	util.download_csv(list, file_path)