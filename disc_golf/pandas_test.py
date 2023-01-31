import re

import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
from unicodedata import normalize
from bs4 import BeautifulSoup

pattern = re.compile('.MPO-round.')


# url = 'https://www.pdga.com/tour/event/48172'
# url = r'C:\Users\benhartd\PycharmProjects\Fun\disc_golf\Dynamic Discs Open - National Tour Professional Disc Golf Association.htm'
url = r'Dynamic Discs Open - National Tour Professional Disc Golf Association.htm'

source = open(url, encoding='utf8')

ddo = pd.read_html(url)
df = ddo[1]
# print(df.head())
cols = df.columns
# print(cols)
rounds = 0
for col in cols:
    if 'Rd' in col:
        rounds += 1
    if 'Final' in col:
        rounds += 1


soup = BeautifulSoup(source, 'html.parser')
spans = soup.find_all('span', attrs={'id': pattern})
pars = []
for span in spans:
    par = span.text.split(';')[2].split()[1]
    pars.append(int(par))

print(pars)

if rounds >= 2:
    round_2_lead = df.nsmallest(4, columns=['Rd1', 'PDGA#'])
    if rounds >= 3:
        df['rd_2_total'] = df.loc[:, ['Rd1', 'Rd2']].sum(1)
        round_2_lead_score = round_2_lead['Rd2'].sum()
        r2_under_par = pars[1] * 4 - round_2_lead_score
        round_3_lead = df.nsmallest(4, columns=['rd_2_total', 'PDGA#'])
        print('round 2')
        print(round_2_lead[['Name', 'Rd1', 'Rd2']])
        print(r2_under_par)
        # TODO check whether it is always true that Round 3 is never listed as Finals
        df['rd_3_total'] = df.loc[:, ['Rd1', 'Rd2', 'Rd3']].sum(1)
        round_3_lead_score = round_3_lead['Rd3'].sum()
        r3_under_par = pars[2] * 4 - round_3_lead_score
        print('round 3')
        print(round_3_lead[['Name', 'Rd1', 'Rd2', 'Rd3']])
        print(r3_under_par)
        if rounds == 4:
            # df['rd_3_total'] = df.loc[:, ['Rd1', 'Rd2', 'Rd3']].sum(1)
            # round_3_lead_score = round_3_lead['Rd3'].sum()
            # print('round 3')
            # print(round_3_lead[['Name', 'Rd1', 'Rd2', 'Rd3']])
            # print(round_3_lead_score)
            round_4_lead = df.nsmallest(4, columns=['rd_3_total', 'PDGA#'])
            round_4_lead_score = round_4_lead['Finals'].sum()
            r4_under_par = pars[3] * 4 - round_4_lead_score
            print('round 4')
            print(round_4_lead[['Name', 'Rd1', 'Rd2', 'Rd3', 'Finals']])
            print(r4_under_par)
        # else:
        #     round_3_lead_score = round_3_lead['Finals'].sum()
        #     print('round 3')
        #     print(round_3_lead[['Name', 'Rd1', 'Rd2', 'Finals']])
        #     print(round_3_lead_score)
    else:
        round_2_lead_score = round_2_lead['Finals'].sum()
        print('round 2')
        print(round_2_lead[['Name', 'Rd1', 'Finals']])
        print(round_2_lead_score)
