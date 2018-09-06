from pyramid_restful.viewsets import APIViewSet
from ..models.stock import Stock
from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import IntegrityError, DataError
import numpy as np
import pandas as pd
import requests
import bokeh.plotting as bk
from bokeh.models import HoverTool, Label, BoxZoomTool, PanTool, ZoomInTool, ZoomOutTool, ResetTool
import json


API_URL = 'https://api.iextrading.com/1.0/'
STOCK_SYMBOL = 'MSFT'

class VisualAPIViewset(APIViewSet):
    """A class that handles request from a visual endpoint. """

    def list(self, id=None):
        res = requests.get(f'{API_URL}stock/{SYMBOL}/company')
        data = res.json()
        company_name = data['companyName']

        data = res.json()
        df = pd.DataFrame(data)
        df.shape
        seqs = np.arange(df.shape[0])
        df['seqs'] = pd.Series(seqs)

        df['changePercent'] = df['changePercent'].apply(lambda x: float(x) + '%')
        df.sample(20)

        df['mid'] = df.apply(lambda x: (x['open'] + x['close']) / 2, axis=1)

        df['height'] = df.apply(
            lambda x: x['close'] - x['open'] if x['close'] != x['open'] else 0.000, axis=1)

        inc = df.close > df.open
        dec = df.close < df.open
        w = .3

        sourceInc = bk.ColumnDataSource(df.loc[inc])
        sourceDec = bk.ColumnDataSource(df.loc[dec])

        hover = HoverTool(
            tooltips=[
                ('date', '@date'),
                ('low', '@low'),
                ('high', '@high'),
                ('open', '@open'),
                ('close', '@close'),
                ('percent', '@changePercent'),
            ]
        )

        TOOLS = [hover, BoxZoomTool(), PanTool(), ZoomInTool(), ZoomOutTool(), ResetTool()]

        p = bk.figure(plot_width=1000, plot_height=800, tools=TOOLS, title=f'{company_name}', toolbar_location='above')

        p.xaxis.major_label_orientation = np.pi / 4
        p.grid.grid_line_alpha = w

        descriptor = Label(x=70, y=70, text='')
        p.add_layout(descriptor)

        p.segment(df.seqs[inc], df.high[inc], df.seqs[inc], df.low[inc], color='green')

        p.segment(df.seqs[dec], df.high[dec], df.seqs[dec], df.low[dec], color='red')

        p.rect(x='seqs', y='mid', width=w, height='height', fill_color='green', line_color='green', source=sourceInc)

        p.rect(x='seqs', y='mid', width=w, height='height', fill_color='red', line_color='red', source=sourceDec)

        bk.save(p, f'../static/{company_name}_candle_stick.html', title=f'{company_name}_5yr_candlestick')

        return Response(json='Graph Visuals', status=200)
