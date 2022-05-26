from datetime import datetime

import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt


class Finance:
    def __init__(self):
        # 판다스 데이터리더 라이브러리를 이용하기 위한 함수
        yf.pdr_override()


    def get_all_tickers_in_us_market(self):
        print('')



    def test_sshn(self):
        stocks = ['005930.KS', '000660.KS', '005380.KS', '035420.KS']
        df = pd.DataFrame()
        for stock in stocks:
            result = pdr.get_data_yahoo(stock, '2000-01-01')['Close']
            df[stock] = result

        daily_ret = df.pct_change()  # 시총 상위 4 종목의 수익률을 비교하려면 일간 변동률로 비교를 해야하기 때문.
        annual_ret = daily_ret.mean() * 252  # 평균 개장일 252일.
        daily_cov = daily_ret.cov()
        annual_cov = daily_cov * 252

        plt.figure(figsize=(10, 12))

        plt.subplot(811)
        plt.plot(daily_ret['005930.KS'])
        plt.subplot(812)
        plt.plot(daily_cov['005930.KS'], 'r--')

        plt.subplot(813)
        plt.plot(daily_ret['000660.KS'])
        plt.subplot(814)
        plt.plot(daily_cov['000660.KS'], 'r--')

        plt.subplot(815)
        plt.plot(daily_ret['005380.KS'])
        plt.subplot(816)
        plt.plot(daily_cov['005380.KS'], 'r--')

        plt.subplot(817)
        plt.plot(daily_ret['035420.KS'])
        plt.subplot(818)
        plt.plot(daily_cov['035420.KS'], 'r--')

        plt.show()

        print(daily_ret)
        print(daily_cov)


    def test_samsung(self):
        target_date = datetime(1990, 1, 1)
        df = pdr.get_data_yahoo('005930.KS', target_date)

        plt.figure(figsize=(9, 6))
        plt.subplot(2, 1, 1)
        plt.title('samsung yfinance')
        plt.plot(df.index, df['Close'], 'c', label='Close')
        plt.plot(df.index, df['Adj Close'], 'b--', label='Adj Close')
        plt.legend(loc='best')
        plt.subplot(2, 1, 2)
        plt.bar(df.index, df['Volume'], color='g', label='Volume')
        plt.legend(loc='best')
        plt.show()
