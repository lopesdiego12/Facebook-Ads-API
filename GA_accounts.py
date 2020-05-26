# -*- coding: utf-8 -*-
# Script baseado nos códigos de exemplos da API do google adwords #

# importa as libs que serão utilizadas
import sys
import accounts_config

# busca todos os ids das contas do adwords, exceto das contas de administrador
def get_ids(client):
	# configuracoes para conexao
	PAGE_SIZE = 500

	# inicializa o servico para buscar contas
	managed_customer_service = client.GetService('ManagedCustomerService', version='v201809')

	# seletor para buscar todas as contas
	offset = 0
	selector = {
		'fields': ['CustomerId', 'Name'],
		'paging': {
			'startIndex': str(offset),
			'numberResults': str(PAGE_SIZE)
		}
	}

	more_pages = True
	parent_links = {}
	customerIDs = []

	while more_pages:
		# servico de contas
		page = managed_customer_service.get(selector)
		if 'entries' in page and page['entries']:
			# insere o id da conta de administrador no objeto parent_links
			if 'links' in page:
				for link in page['links']:
					if link['clientCustomerId'] not in parent_links:
						parent_links[link['clientCustomerId']] = []
						parent_links[link['clientCustomerId']].append(link)
			# insere todos os ids de conta no array customerIDs
			for account in page['entries']:
				customerIDs.append(account['customerId'])
		# logica para continuar o loop até buscar todas as contas
		offset += PAGE_SIZE
		selector['paging']['startIndex'] = str(offset)
		more_pages = offset < int(page['totalNumEntries'])

	# localiza o id da conta de administrador para remove-lo da listagem
	for id in customerIDs:
		if id not in parent_links:
			customerIDs.remove(id)
	
	# busca os ids das contas que não estão vinculadas a MCC
	accounts = accounts_config.get_accounts()
	
	# adiciona os ids das contas que não estão vinculadas a MCC no array com os ids de todas as contas
	for id in accounts.account_id:
		customerIDs.append(id)
		
	return customerIDs