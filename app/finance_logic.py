# Finance and Plotting Libraries
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import io, urllib, base64

def getCompanyClose(co):
    # start = (dt.datetime.now() - dt.timedelta(days=1*365)).date()
    # end = dt.datetime.now().date()
    start, end = '2016-01-01', '2016-12-31'
    df = web.DataReader(co, 'quandl', start, end)
    close = df['Close']
    all_weekdays = pd.date_range(start=start, end=end, freq='B')
    close = close.reindex(all_weekdays)
    close = close.fillna(method='ffill')
    return close

def graphStockData(comp_A_close, comp_B_close):
    plt.plot(comp_A_close.index, comp_A_close, label='MSFT')
    plt.plot(comp_B_close.index, comp_B_close, label='FB')
    plt.xlabel("Date")
    plt.ylabel("Daily Closing Stock Price")
    plt.title("FB vs. MSFT Closing Stock Price")
    plt.legend()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_data = urllib.parse.quote(base64.b64encode(img.read()).decode())
    return plot_data


