# arquivo de configuração de autenticação na API do facebook

def get_credentials():
	credentials = type("", (object,), {})()	
	# id do aplicativo
	credentials.app_id = '*****'
	# chave secreta do aplicativo
	credentials.app_secret = '***************************'
	# token de acesso
	credentials.access_token='**********************************************'
	# id das contas de anuncios que serão extraidas as informações
	credentials.accounts_id = [
					# ID da Conta
					'*************', 
					# ID da campanha2
					'*********', 
					]
	# id das contas de anuncios que possuem formulário ativos				
	credentials.accounts_leads_form_active = [
					# Leads Account
					'*******'
					]
	
	return credentials;

