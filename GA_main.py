# -*- coding: utf-8 -*-
# Script baseado nos códigos de exemplos da API do google adwords #

# importa as libs que serão utilizadas
import accounts_config
import accounts
import reports
import argparse
from googleads import adwords

# define os argumentos que serão passados para o script
parser = argparse.ArgumentParser()
parser.add_argument('--report_name', default=None)
# deixa como default para pegar os últimos 30 dias se não for passado o periodo para o script
parser.add_argument('--during', default='LAST_30_DAYS')

def download_campaign_perfomance_report(client, during):

        # busca todos os ids das contas
        accounts_ids = accounts.get_ids(client)

        # cria query do report
        report_query = (adwords.ReportQueryBuilder().Select('AccountDescriptiveName', 'Date', 'CampaignName', 'Device', 'AdNetworkType1',
                                                'Impressions', 'Clicks', 'Cost', 'SearchImpressionShare', 'ContentImpressionShare',
                                                'SearchBudgetLostImpressionShare', 'ContentBudgetLostImpressionShare', 'Ctr')
                                        .From('CAMPAIGN_PERFORMANCE_REPORT')
                                        .During(during)
                                        .Build())

        # realiza o download do report para cada conta
        for id in accounts_ids:
                client.SetClientCustomerId(id)
                reports.download_report(client, report_query, 'campaign_performance_report_'+str(id)+'.csv')

# inicio do script
if __name__ == '__main__':
        args = parser.parse_args()

        # inicializa o client e busca todos os ids das contas
        client_adwords = adwords.AdWordsClient.LoadFromStorage('//AdWordsPerformanceCampanha//googleads.yaml')

        # verifica se foi passado o nome do report para chamar a função que realiza o download
        if args.report_name == 'campaign_perfomance_report':
                download_campaign_perfomance_report(client_adwords, args.during)
        else:
                print('Favor informar o nome do relatorio para realizar o download!')
