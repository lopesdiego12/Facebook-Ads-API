# -*- coding: utf-8 -*-
# Script baseado nos códigos de exemplos da API do google adwords #

# importa as libs que serão utilizadas
import os

def download_report(client, report_query, file_name):	
	# inicializa o servico de relatorios
	report_downloader = client.GetReportDownloader(version='v201809')
	
	# faz o download do report em string
	content = report_downloader.DownloadReportAsStringWithAwql(report_query, 'CSV', skip_report_header=True,
		skip_column_header=False, skip_report_summary=True, include_zero_impressions=False)
	
	# cria os arquivos csv com o relatório da campanha
	csv = open(os.path.join('//files//AdWords//input',file_name), "w") 
	csv.write(content)