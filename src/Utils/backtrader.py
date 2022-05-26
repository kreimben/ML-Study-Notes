import backtrader as bt
import datetime

import yfinance as yf


class BasicStrategy(bt.Strategy):
    def __init(self):
        self.rsi = bt.indicators.RSI(self.data.close)

    # RSI가 30 미만이면 과매도 구간으로 판단, 매수 시점으로 해석
    # RSI가 70 초과이면 과매수 구간으로 판단, 매도 시점으로 해석
    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.order = self.buy()
        else:
            if self.rsi > 70:
                self.order = self.sell()


def run_backtrader():
    cerebro = bt.Cerebro()
    cerebro.addstrategy(BasicStrategy)  # 위의 기본 전략을 추가.
    data = bt.feeds.YahooFinanceData(datename='036570.KS', fromdate=datetime(2017, 1, 1), todate=datetime(2019, 12, 1))  # 종목과 시점, 종점을 설정
    cerebro.adddata(data)  # 데이터를 받아온 것을 객체에 추가
    cerebro.broker.setcash(1_0000_0000)  # 총알을 설정.
    cerebro.addsizer(bt.sizers.SizerFix, stake=1)  # 주식의 매매 단위를 1주로 설정.

    print(f'초기 자금: {cerebro.broker.getvalue():,.0f} KRW')
    cerebro.run()
    print(f'최종 자금: {cerebro.broker.getvalue():,.0f} KRW')
    cerebro.plot()