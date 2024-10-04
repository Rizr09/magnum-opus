import numpy as np
import pandas as pd
import talib

def generate_technical_indicators(df):
    """
    Generate comprehensive technical indicators using TA-Lib.
    
    :param df: DataFrame with 'Open', 'High', 'Low', 'Close', 'Volume' columns
    :return: DataFrame with additional columns for indicators
    """
    # Ensure that the input columns are float type
    for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
        df[col] = df[col].astype(float)

    # Trend Indicators
    df['BBANDS_upper'], df['BBANDS_middle'], df['BBANDS_lower'] = talib.BBANDS(df['Close'])
    df['DEMA'] = talib.DEMA(df['Close'])
    df['EMA'] = talib.EMA(df['Close'])
    df['HT_TRENDLINE'] = talib.HT_TRENDLINE(df['Close'])
    df['KAMA'] = talib.KAMA(df['Close'])
    df['MA'] = talib.MA(df['Close'])
    
    df['MAMA'], df['FAMA'] = talib.MAMA(df['Close'])
    df['MAVP'] = talib.MAVP(df['Close'], df['Close'])  # Using Close as periods, adjust as needed
    df['MIDPOINT'] = talib.MIDPOINT(df['Close'])
    df['MIDPRICE'] = talib.MIDPRICE(df['High'], df['Low'])
    df['SAR'] = talib.SAR(df['High'], df['Low'])
    df['SAREXT'] = talib.SAREXT(df['High'], df['Low'])
    df['SMA'] = talib.SMA(df['Close'])
    df['T3'] = talib.T3(df['Close'])
    df['TEMA'] = talib.TEMA(df['Close'])
    df['TRIMA'] = talib.TRIMA(df['Close'])
    df['WMA'] = talib.WMA(df['Close'])

    # Momentum Indicators
    df['ADX'] = talib.ADX(df['High'], df['Low'], df['Close'])
    df['ADXR'] = talib.ADXR(df['High'], df['Low'], df['Close'])
    df['APO'] = talib.APO(df['Close'])
    df['AROON_down'], df['AROON_up'] = talib.AROON(df['High'], df['Low'])
    df['AROONOSC'] = talib.AROONOSC(df['High'], df['Low'])
    df['BOP'] = talib.BOP(df['Open'], df['High'], df['Low'], df['Close'])
    df['CCI'] = talib.CCI(df['High'], df['Low'], df['Close'])
    df['CMO'] = talib.CMO(df['Close'])
    df['DX'] = talib.DX(df['High'], df['Low'], df['Close'])
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'])
    df['MACDEXT'], df['MACDEXT_signal'], df['MACDEXT_hist'] = talib.MACDEXT(df['Close'])
    df['MACDFIX'], df['MACDFIX_signal'], df['MACDFIX_hist'] = talib.MACDFIX(df['Close'])
    df['MFI'] = talib.MFI(df['High'], df['Low'], df['Close'], df['Volume'])
    df['MINUS_DI'] = talib.MINUS_DI(df['High'], df['Low'], df['Close'])
    df['MINUS_DM'] = talib.MINUS_DM(df['High'], df['Low'])
    df['MOM'] = talib.MOM(df['Close'])
    df['PLUS_DI'] = talib.PLUS_DI(df['High'], df['Low'], df['Close'])
    df['PLUS_DM'] = talib.PLUS_DM(df['High'], df['Low'])
    df['PPO'] = talib.PPO(df['Close'])
    df['ROC'] = talib.ROC(df['Close'])
    df['ROCP'] = talib.ROCP(df['Close'])
    df['ROCR'] = talib.ROCR(df['Close'])
    df['ROCR100'] = talib.ROCR100(df['Close'])
    df['RSI'] = talib.RSI(df['Close'])
    df['STOCH_k'], df['STOCH_d'] = talib.STOCH(df['High'], df['Low'], df['Close'])
    df['STOCHF_k'], df['STOCHF_d'] = talib.STOCHF(df['High'], df['Low'], df['Close'])
    df['STOCHRSI_k'], df['STOCHRSI_d'] = talib.STOCHRSI(df['Close'])
    df['TRIX'] = talib.TRIX(df['Close'])
    df['ULTOSC'] = talib.ULTOSC(df['High'], df['Low'], df['Close'])
    df['WILLR'] = talib.WILLR(df['High'], df['Low'], df['Close'])

    # Volume Indicators
    df['AD'] = talib.AD(df['High'], df['Low'], df['Close'], df['Volume'])
    df['ADOSC'] = talib.ADOSC(df['High'], df['Low'], df['Close'], df['Volume'])
    df['OBV'] = talib.OBV(df['Close'], df['Volume'])

    # Cycle Indicators
    df['HT_DCPERIOD'] = talib.HT_DCPERIOD(df['Close'])
    df['HT_DCPHASE'] = talib.HT_DCPHASE(df['Close'])
    df['HT_PHASOR_inphase'], df['HT_PHASOR_quadrature'] = talib.HT_PHASOR(df['Close'])
    df['HT_SINE_sine'], df['HT_SINE_leadsine'] = talib.HT_SINE(df['Close'])
    df['HT_TRENDMODE'] = talib.HT_TRENDMODE(df['Close'])

    # Price Transform
    df['AVGPRICE'] = talib.AVGPRICE(df['Open'], df['High'], df['Low'], df['Close'])
    df['MEDPRICE'] = talib.MEDPRICE(df['High'], df['Low'])
    df['TYPPRICE'] = talib.TYPPRICE(df['High'], df['Low'], df['Close'])
    df['WCLPRICE'] = talib.WCLPRICE(df['High'], df['Low'], df['Close'])

    # Volatility Indicators
    df['ATR'] = talib.ATR(df['High'], df['Low'], df['Close'])
    df['NATR'] = talib.NATR(df['High'], df['Low'], df['Close'])
    df['TRANGE'] = talib.TRANGE(df['High'], df['Low'], df['Close'])

    # Pattern Recognition
    pattern_functions = [
        talib.CDL2CROWS, talib.CDL3BLACKCROWS, talib.CDL3INSIDE, talib.CDL3LINESTRIKE,
        talib.CDL3OUTSIDE, talib.CDL3STARSINSOUTH, talib.CDL3WHITESOLDIERS,
        talib.CDLABANDONEDBABY, talib.CDLADVANCEBLOCK, talib.CDLBELTHOLD,
        talib.CDLBREAKAWAY, talib.CDLCLOSINGMARUBOZU, talib.CDLCONCEALBABYSWALL,
        talib.CDLCOUNTERATTACK, talib.CDLDARKCLOUDCOVER, talib.CDLDOJI,
        talib.CDLDOJISTAR, talib.CDLDRAGONFLYDOJI, talib.CDLENGULFING,
        talib.CDLEVENINGDOJISTAR, talib.CDLEVENINGSTAR, talib.CDLGAPSIDESIDEWHITE,
        talib.CDLGRAVESTONEDOJI, talib.CDLHAMMER, talib.CDLHANGINGMAN,
        talib.CDLHARAMI, talib.CDLHARAMICROSS, talib.CDLHIGHWAVE, talib.CDLHIKKAKE,
        talib.CDLHIKKAKEMOD, talib.CDLHOMINGPIGEON, talib.CDLIDENTICAL3CROWS,
        talib.CDLINNECK, talib.CDLINVERTEDHAMMER, talib.CDLKICKING,
        talib.CDLKICKINGBYLENGTH, talib.CDLLADDERBOTTOM, talib.CDLLONGLEGGEDDOJI,
        talib.CDLLONGLINE, talib.CDLMARUBOZU, talib.CDLMATCHINGLOW, talib.CDLMATHOLD,
        talib.CDLMORNINGDOJISTAR, talib.CDLMORNINGSTAR, talib.CDLONNECK,
        talib.CDLPIERCING, talib.CDLRICKSHAWMAN, talib.CDLRISEFALL3METHODS,
        talib.CDLSEPARATINGLINES, talib.CDLSHOOTINGSTAR, talib.CDLSHORTLINE,
        talib.CDLSPINNINGTOP, talib.CDLSTALLEDPATTERN, talib.CDLSTICKSANDWICH,
        talib.CDLTAKURI, talib.CDLTASUKIGAP, talib.CDLTHRUSTING, talib.CDLTRISTAR,
        talib.CDLUNIQUE3RIVER, talib.CDLUPSIDEGAP2CROWS, talib.CDLXSIDEGAP3METHODS
    ]

    for func in pattern_functions:
        pattern_name = func.__name__[3:]  # Remove 'CDL' prefix
        df[f'PATTERN_{pattern_name}'] = func(df['Open'], df['High'], df['Low'], df['Close'])

    return df

# Example usage:
# Assume 'data' is your DataFrame with OHLCV data
# data = pd.read_csv('your_stock_data.csv')
# data_with_indicators = generate_technical_indicators(data)
# print(data_with_indicators.head())