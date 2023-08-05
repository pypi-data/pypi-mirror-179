import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import pkg_resources
#import get_data
stream = pkg_resources.resource_stream(__name__,'data/symbol_recommendation.csv')
symbol= pd.read_csv(stream)
#symbol=pd.read_csv('symbol_recommendation.csv')
#symbol=get_dataset()
def list_stocks():
    return symbol.filter(['isin','name','full_name','symbol'],axis=1)
class company:
    def __init__(self,stock):
        self.stock=stock
        self.mysymbol=symbol.filter(symbol.index[(symbol['symbol']==self.stock)],axis=0)['isin'].to_numpy()[0]
        link='https://www.afc.com.tn/entreprise?isin='+self.mysymbol+'#content'
        page = requests.get(link)
        self.soup = BeautifulSoup(page.content,"html.parser")
    def income_statement_indicators(self):
        ''' in this income_statement_indicators you can find the Return on equity ROE ratio,gearing ratio,EBIT and 
        EBITDA and others for the last 4 years  '''
        ratio_resultat=self.soup.find('div', attrs={'class':'mod_ind_res'}).find('table')
        output_rows2=[]
        for table_row in ratio_resultat.findAll('tr'):
            columns2 = table_row.findAll('td')
            output_row2 = []
            for column in columns2:
                output_row2.append(column.text)
            output_row2.extend([symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]])
            output_rows2.append(output_row2)
        df_ratio_resultat = pd.DataFrame(output_rows2,columns=['ratios','2019','2020','2021','2022','Stock'])[1:]
        df_ratio_resultat['2019']=pd.to_numeric(df_ratio_resultat['2019'],errors = 'coerce')
        df_ratio_resultat['2020']=pd.to_numeric(df_ratio_resultat['2020'],errors = 'coerce')
        df_ratio_resultat['2021']=pd.to_numeric(df_ratio_resultat['2021'],errors = 'coerce')
        df_ratio_resultat['2022']=pd.to_numeric(df_ratio_resultat['2022'],errors = 'coerce')
        df_ratio_resultat1=df_ratio_resultat.T
        df_ratio_resultat1.columns=df_ratio_resultat['ratios']
        df_ratio_resultat1=df_ratio_resultat1[1:-1]
        df_ratio_resultat1['Stock']=symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]
        return df_ratio_resultat1
    def balance_sheet_indicators(self):
        ratio_bilan=self.soup.find('div', attrs={'class':'mod_ind_bilan'}).find('table')
        output_rows1=[]
        for table_row in ratio_bilan.findAll('tr'):
            columns1 = table_row.findAll('td')
            output_row1 = []
            for column in columns1:
                output_row1.append(column.text)
            output_row1.extend([symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]])
            output_rows1.append(output_row1)
        df_ratio_bilan = pd.DataFrame(output_rows1)
        df_ratio_bilan=df_ratio_bilan[1:]
        df_ratio_bilan.columns=['ratios','2019','2020','2021','2022','Stock']
        df_ratio_bilan['2019']=df_ratio_bilan['2019'].str.replace(',','.')
        df_ratio_bilan['2019']=pd.to_numeric(df_ratio_bilan['2019'],errors = 'coerce')
        df_ratio_bilan['2020']=df_ratio_bilan['2020'].str.replace(',','.')
        df_ratio_bilan['2020']=pd.to_numeric(df_ratio_bilan['2020'],errors = 'coerce')
        df_ratio_bilan['2021']=df_ratio_bilan['2021'].str.replace(',','.')
        df_ratio_bilan['2021']=pd.to_numeric(df_ratio_bilan['2021'],errors = 'coerce')
        df_ratio_bilan['2022']=df_ratio_bilan['2022'].str.replace(',','.')
        df_ratio_bilan['2022']=pd.to_numeric(df_ratio_bilan['2022'],errors = 'coerce')
        df_ratio_bilan1=df_ratio_bilan.T
        df_ratio_bilan1.columns=df_ratio_bilan['ratios']
        df_ratio_bilan1=df_ratio_bilan1[1:-1]
        df_ratio_bilan1['Stock']=symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]
        return df_ratio_bilan1
        #Indicateurs boursiers
    def stock_market_indicators(self):
        ind_bourse=self.soup.find('div', attrs={'class':'mod_ind_bourse'}).find('table')
        output_rows = []
        for table_row in ind_bourse.findAll('tr'):
            columns = table_row.findAll('td')
            output_row = []
            for column in columns:
                output_row.append(column.text)
            output_row.extend([symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]])
            output_rows.append(output_row)
        df_ind_bourse = pd.DataFrame(output_rows)
        df_ind_bourse=df_ind_bourse[1:].drop(columns=1)
        df_ind_bourse.drop(df_ind_bourse.index[(df_ind_bourse[0]=='Secteur')],axis=0,inplace=True)
        df_ind_bourse.drop(df_ind_bourse.index[(df_ind_bourse[0]=='Marché')],axis=0,inplace=True)
        df_ind_bourse.columns=['ratios','2019','2020','2021','2022','Stock']
        df_ind_bourse['2019']=df_ind_bourse['2019'].apply(replace_x)
        df_ind_bourse['2019']=pd.to_numeric(df_ind_bourse['2019'],errors = 'coerce')
        df_ind_bourse['2020']=df_ind_bourse['2020'].apply(replace_x)
        df_ind_bourse['2020']=pd.to_numeric(df_ind_bourse['2020'],errors = 'coerce')
        df_ind_bourse['2021']=df_ind_bourse['2021'].apply(replace_x)
        df_ind_bourse['2021']=pd.to_numeric(df_ind_bourse['2021'],errors = 'coerce')
        df_ind_bourse['2022']=df_ind_bourse['2022'].apply(replace_x)
        df_ind_bourse['2022']=pd.to_numeric(df_ind_bourse['2022'],errors = 'coerce')
        df_ind_bourse1=df_ind_bourse.T
        df_ind_bourse1.columns=df_ind_bourse['ratios']
        df_ind_bourse1=df_ind_bourse1[1:-1]
        df_ind_bourse1['Stock']=symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]
        return df_ind_bourse1
    def shareholders(self):
        actionnaire=self.soup.find('div', attrs={'class':'mod_act_ent'}).find('table')
        output_rows = []
        for table_row in actionnaire.findAll('tr'):
            columns = table_row.findAll('td')
            output_row = []
            for column in columns:
                output_row.append(column.text)
            output_row.extend([symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]])
            output_rows.append(output_row)
        df_actionnaire = pd.DataFrame(output_rows)[1:]
        df_actionnaire.columns=['Actionnaire','Type','Pourcentage','Stock']
        return df_actionnaire
    def Dividende(self):
        ind_divend=self.soup.find('div', attrs={'class':'mod_div_ent'}).find('table')
        output_rows = []
        for table_row in ind_divend.findAll('tr'):
            columns = table_row.findAll('td')
            output_row = []
            for column in columns:
                output_row.append(column.text)
            output_row.extend([symbol.filter(symbol.index[(symbol['isin']==self.mysymbol)],axis=0)['symbol'].to_numpy()[0]])
            output_rows.append(output_row)
        Dividende = pd.DataFrame(output_rows[1:],columns=['Dividende par action','Actions concernées','Montant total','Exercice','Date de distribution','Stock'])
        Dividende['Actions concernées']=Dividende['Actions concernées'].str.replace(' ','')
        Dividende['Montant total']=Dividende['Montant total'].str.replace(' ','')
        Dividende['Montant total']=Dividende['Montant total'].str.replace('DT','')
        Dividende['Dividende par action']=Dividende['Dividende par action'].str.replace(' ','')
        Dividende['Dividende par action']=Dividende['Dividende par action'].str.replace('DT','')
        Dividende['Dividende par action']=pd.to_numeric(Dividende['Dividende par action'],errors = 'coerce')
        Dividende['Actions concernées']=pd.to_numeric(Dividende['Actions concernées'],errors = 'coerce')
        Dividende['Montant total']=pd.to_numeric(Dividende['Montant total'],errors = 'coerce')
        Dividende['Date']=pd.to_datetime(Dividende['Date de distribution'], format='%d/%m/%Y')
        return Dividende
