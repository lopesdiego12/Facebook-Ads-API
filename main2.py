# Script baseado nos códigos de exemplos do SDK do facebook_business #

# importa as libs que serão utilizadas
import argparse
import datetime
import credentials_config
import report_adinsights
import util
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights

# define os argumentos que serão passados para o script
parser = argparse.ArgumentParser()
parser.add_argument('--report_name', default=None)
parser.add_argument('--date_start', default=None)

def download_ad_insights_report(accounts_id):
	
	for account_id in accounts_id:
		# define a conta de anuncios que será utilizada
		account = AdAccount('act_' + str(account_id))
		
		# seta o filtro e os campos para realizar o download do relatório
		params = {
			'date_preset': 'last_7d',
			'fields': [
                  AdsInsights.Field.account_id,
                  AdsInsights.Field.account_name,
                  AdsInsights.Field.campaign_id,				
                  AdsInsights.Field.campaign_name,
                  AdsInsights.Field.impressions,
                  AdsInsights.Field.inline_link_clicks,
                  AdsInsights.Field.adset_id,
                  AdsInsights.Field.adset_name,
                  AdsInsights.Field.ad_id,
                  AdsInsights.Field.ad_name,
			  ],
			'breakdowns': [
				AdsInsights.Breakdowns.impression_device
			],
			'level': 'campaign',
			'time_increment': 1
			}
		
		print(params)
		
		
		file_path = 'C:\\Users\\diegols\\Desktop\\Facebook\\Python\\Downloads\\AdInsights\\ad' + str(account_id) + '.csv'
		
		# realiza o download do relatório
		report_adinsights.download_report(account, params, file_path)

# inicio do script
if __name__ == '__main__':
	args = parser.parse_args()
	
	# inicializa o client
	credentials = credentials_config.get_credentials()
	FacebookAdsApi.init(credentials.app_id, credentials.app_secret, credentials.access_token, api_version='v3.3')
	
	# verifica se foi passado o nome do report, o periodo  e o id da conta para chamar a função que realiza o download
	if args.report_name == 'ad_insights':
		download_ad_insights_report(credentials.accounts_id)
	elif args.report_name == 'leads_form' and args.date_start is not None:
		download_leadsform(credentials.accounts_leads_form_active, args.date_start)
	else:
		print('Favor informar o nome do relatorio para realizar o download!')