import requests
import pandas as pd
import json
import re


def post_flows_to_database(dataset: pd.DataFrame, access_token: str, verbose: bool = True):
    """
    This function enables the posting of data to the database. The function firstly checks that the
    input arguments are of the correct type, followed by modifying the dataset to a list or dictionaries.
    The function then attempts to post the dictionaries to the API, recording the status code for each post
    request as a printed value, if verbose = True.

    :param dataset: data in the correct schema to be posted to the Forecast Flows DB. (pd.DataFrame)
    :param access_token: the access token of the user, must be an active access token. (str)
    :param verbose: determines if status is printed. Default=True. (bool)
    :return: failed_uploads: the information which failed to upload. (pd.DataFrame)
    """
    if not isinstance(dataset, pd.DataFrame):
        raise TypeError("The 'dataset' argument must be a Pandas DataFrame.")
    if not isinstance(access_token, str):
        raise TypeError("The 'access_token' argument must be a string type.")
    if not isinstance(verbose, bool):
        raise TypeError("The 'verbose' argument must be a boolean type.")
    failed_uploads = []
    dict_list = dataset.to_dict('records')
    url = "https://www.samsonrockapis.com/forecast_flows"
    header = {'Authorization': 'Bearer ' + access_token}
    for item in dict_list:
        response = requests.post(url, data=json.dumps(item), headers=header)
        if response.status_code in [200, 201]:
            if verbose:
                print("Status Code: {}, Uploaded.".format(response.status_code))
        else:
            failed_uploads.append(item)
            if verbose:
                print("Status Code: {}, {}.".format(response.status_code, response.text))
    return pd.DataFrame.from_records(failed_uploads)


def get_all_index_data_from_db(index: str, access_token: str, verbose: bool = True):
    """
    This function enables the user to collect all information held in the database relating to a specific index.
    The function firstly checks that the arguments are of the correct type, followed by attempting to collect the
    requested information from the database. If the information is available, it is returned as a Pandas DataFrame,
    otherwise, empty data shall be returned, with an appropriate status code printed if verbose=True.

    :param index: the index for which the user would like to return data. (str)
    :param access_token: the access token of the user, must be an active access token. (str)
    :param verbose: determines if status is printed. Default=True. (bool)
    :return: dataset: a Pandas DataFrame containing all data relating to the index argument. (pd.DataFrame)
    """
    if not all(isinstance(v, str) for v in [index, access_token]):
        raise TypeError("The 'index' and 'access_token' arguments must be string types.")
    if not isinstance(verbose, bool):
        raise TypeError("The 'verbose' argument must be a boolean type.")
    index_values = ['AEX', 'AMX', 'AMZ', 'AMZI', 'AS51', 'ASX', 'BEL20', 'CAC', 'CPQ', 'DAX', 'DJASD', 'DJCASD',
                    'DJDVY', 'DJEMDIV', 'DJEPCSD', 'DJINET', 'DJSHMB', 'DJSMDQT', 'DJUSDIVT', 'EPRA-EUROPE',
                    'FTSEMIB', 'FUDP', 'GDM', 'GDXJ', 'GEIS-AWCHINA', 'GEIS-AWDEVEUR', 'GEIS-AWEMEUR',
                    'GEIS-AWEXCHINA', 'GEIS-AWJAPAN', 'GEIS-AWLATAM', 'GEIS-AWMEA', 'GEIS-AWNAM',
                    'GEIS-GSCCHINA', 'GEIS-GSCDEVEUR', 'GEIS-GSCEMEUR', 'GEIS-GSCEXCHINA', 'GEIS-GSCJAPAN',
                    'GEIS-GSCLATAM', 'GEIS-GSCMEA', 'GEIS-GSCNAM', 'HSCEI', 'HUR', 'IBEX', 'KOSPI2', 'MCMOT',
                    'MCX', 'MDAX', 'MEXBOL', 'MOAT', 'MSCI-DM-SC-ASIAEXJAP', 'MSCI-DM-SC-CAN', 'MSCI-DM-SC-EMEA',
                    'MSCI-DM-SC-JAPAN', 'MSCI-DM-SC-USA', 'MSCI-DM-STD-ASIAEXJAP', 'MSCI-DM-STD-CAN',
                    'MSCI-DM-STD-EMEA', 'MSCI-DM-STD-JAPAN', 'MSCI-DM-STD-USA', 'MSCI-EM-SC-AMERICAS',
                    'MSCI-EM-SC-ASIA', 'MSCI-EM-SC-EMEA', 'MSCI-EM-STD-AMERICAS', 'MSCI-EM-STD-ASIA',
                    'MSCI-EM-STD-EMEA', 'MSCI-MINVOL-EUROPE', 'MSCI-MINVOL-USA', 'MSCI-MINVOL-EM',
                    'MSCI-SRI-ASIAEXJAP', 'MSCI-SRI-CANADA', 'MSCI-SRI-EMEA', 'MSCI-SRI-JAPAN', 'MSCI-SRI-USA',
                    'MSCI-ESG-ASIAEXJAP', 'MSCI-ESG-CANADA', 'MSCI-ESG-EMEA', 'MSCI-ESG-JAPAN', 'MSCI-ESG-USA',
                    'NBI', 'NDX', 'OMX', 'RIY', 'RTY', 'SD3E', 'SD3P', 'SDAX', 'SMI', 'SMIM', 'SPEUHDA',
                    'SPGTAQD', 'SPGTCED', 'SPGTIND', 'SPI', 'SPTSX', 'SPTSX60', 'SPTXDV', 'SX5E', 'SX5P',
                    'SXXP', 'TecDAX', 'TOP40', 'TW50', 'UKX', 'XIN9I', 'EPRA-ASIA', 'EPRA-NAM', 'IXAROBK',
                    'IXBRHLTK', 'MID', 'SML', 'SPX', 'STXTDSV', 'TWDP', 'NIKKEI', 'TOPIX', 'CRSP', 'TA-125',
                    'TA-35', 'HSI', 'KLCI', 'STI', 'MUNR', 'BLOSSOM', 'OMX30', 'FBLSSRTR', 'MDYF', 'FR10',
                    'FREM', 'MCVAT', 'ENDP']
    if index not in index_values:
        raise ValueError("The 'index' value must be one of {}".format(index_values))

    url = "https://www.samsonrockapis.com/forecast_flows&index={}".format(index)
    header = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        if verbose:
            print("Status Code: {}".format(response.status_code))
        return pd.read_json(response.text)
    elif response.status_code == 404:
        if verbose:
            print("Status Code: {}, cannot find data for this Index.".format(response.status_code))
        return pd.DataFrame()
    elif response.status_code == 401:
        if verbose:
            print("Status Code: {}, user not properly authenticated for endpoint.".format(response.status_code))
        return pd.DataFrame()
    else:
        if verbose:
            print("Status Code: {}, {}.".format(response.status_code, response.text))
        return pd.DataFrame()


def get_index_review_data_from_db(index: str, review_year: int, review_month: int, review_type: str,
                                  access_token: str, verbose: bool = True):
    """
    This function enables the user to collect all information held in the database relating to a specific index review.
    The function firstly checks that the arguments are of the correct type, followed by attempting to collect the
    requested information from the database. If the information is available, it is returned as a Pandas DataFrame,
    otherwise, empty data shall be returned, with an appropriate status code printed if verbose=True.

    :param index: the index for which the user would like to return data. (str)
    :param review_year: the year at which the review event took place. (int)
    :param review_month: the month at which the review took place. (int)
    :param review_type: the type of review. (str)
    :param access_token: the access token of the user, must be an active access token. (str)
    :param verbose: determines if status is printed. Default=True. (bool)
    :return: dataset: a Pandas DataFrame containing all data relating to the index argument. (pd.DataFrame)
    """
    if not all(isinstance(v, str) for v in [index, review_type, access_token]):
        raise TypeError("The 'index', 'review_type' and 'access_token' arguments must be string types.")
    if not all(isinstance(v, int) for v in [review_year, review_month]):
        raise TypeError("The 'review_year' and 'review_month' arguments must be integer types.")
    if not isinstance(verbose, bool):
        raise TypeError("The 'verbose' argument must be a boolean type.")
    index_values = ['AEX', 'AMX', 'AMZ', 'AMZI', 'AS51', 'ASX', 'BEL20', 'CAC', 'CPQ', 'DAX', 'DJASD', 'DJCASD',
                    'DJDVY', 'DJEMDIV', 'DJEPCSD', 'DJINET', 'DJSHMB', 'DJSMDQT', 'DJUSDIVT', 'EPRA-EUROPE',
                    'FTSEMIB', 'FUDP', 'GDM', 'GDXJ', 'GEIS-AWCHINA', 'GEIS-AWDEVEUR', 'GEIS-AWEMEUR',
                    'GEIS-AWEXCHINA', 'GEIS-AWJAPAN', 'GEIS-AWLATAM', 'GEIS-AWMEA', 'GEIS-AWNAM',
                    'GEIS-GSCCHINA', 'GEIS-GSCDEVEUR', 'GEIS-GSCEMEUR', 'GEIS-GSCEXCHINA', 'GEIS-GSCJAPAN',
                    'GEIS-GSCLATAM', 'GEIS-GSCMEA', 'GEIS-GSCNAM', 'HSCEI', 'HUR', 'IBEX', 'KOSPI2', 'MCMOT',
                    'MCX', 'MDAX', 'MEXBOL', 'MOAT', 'MSCI-DM-SC-ASIAEXJAP', 'MSCI-DM-SC-CAN', 'MSCI-DM-SC-EMEA',
                    'MSCI-DM-SC-JAPAN', 'MSCI-DM-SC-USA', 'MSCI-DM-STD-ASIAEXJAP', 'MSCI-DM-STD-CAN',
                    'MSCI-DM-STD-EMEA', 'MSCI-DM-STD-JAPAN', 'MSCI-DM-STD-USA', 'MSCI-EM-SC-AMERICAS',
                    'MSCI-EM-SC-ASIA', 'MSCI-EM-SC-EMEA', 'MSCI-EM-STD-AMERICAS', 'MSCI-EM-STD-ASIA',
                    'MSCI-EM-STD-EMEA', 'MSCI-MINVOL-EUROPE', 'MSCI-MINVOL-USA', 'MSCI-MINVOL-EM',
                    'MSCI-SRI-ASIAEXJAP', 'MSCI-SRI-CANADA', 'MSCI-SRI-EMEA', 'MSCI-SRI-JAPAN', 'MSCI-SRI-USA',
                    'MSCI-ESG-ASIAEXJAP', 'MSCI-ESG-CANADA', 'MSCI-ESG-EMEA', 'MSCI-ESG-JAPAN', 'MSCI-ESG-USA',
                    'NBI', 'NDX', 'OMX', 'RIY', 'RTY', 'SD3E', 'SD3P', 'SDAX', 'SMI', 'SMIM', 'SPEUHDA',
                    'SPGTAQD', 'SPGTCED', 'SPGTIND', 'SPI', 'SPTSX', 'SPTSX60', 'SPTXDV', 'SX5E', 'SX5P',
                    'SXXP', 'TecDAX', 'TOP40', 'TW50', 'UKX', 'XIN9I', 'EPRA-ASIA', 'EPRA-NAM', 'IXAROBK',
                    'IXBRHLTK', 'MID', 'SML', 'SPX', 'STXTDSV', 'TWDP', 'NIKKEI', 'TOPIX', 'CRSP', 'TA-125',
                    'TA-35', 'HSI', 'KLCI', 'STI', 'MUNR', 'BLOSSOM', 'OMX30', 'FBLSSRTR', 'MDYF', 'FR10',
                    'FREM', 'MCVAT', 'ENDP']
    review_types = ["QIR", "SAIR", "AIR", "IPO", "Recon", "CQIR"]
    if index not in index_values:
        raise ValueError("The 'index' value must be one of {}".format(index_values))
    if review_type not in review_types:
        raise ValueError("The 'review_type' argument must be one of {}".format(review_types))
    if not 2030 >= review_year > 1981:
        raise ValueError("The 'review_year' argument must be between 1981 and 2030.")
    if review_month not in range(1, 13):
        raise ValueError("The 'review_month' argument must be between 1-12 inclusive.")

    url = "https://www.samsonrockapis.com/forecast_flows&index={}&" \
          "review_year={}&review_month={}&review_name={}".format(index,
                                                                 review_year,
                                                                 review_month,
                                                                 review_type)
    header = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        if verbose:
            print("Status Code: {}".format(response.status_code))
        return pd.read_json(response.text)
    elif response.status_code == 404:
        if verbose:
            print("Status Code: {}, no data available for the {}{}{} review".format(response.status_code, index,
                                                                                    review_year, review_month,
                                                                                    review_type))
        return pd.DataFrame()
    elif response.status_code == 401:
        if verbose:
            print("Status Code: {}, user not properly authenticated for endpoint.".format(response.status_code))
        return pd.DataFrame()
    else:
        if verbose:
            print("Status Code: {}, {}.".format(response.status_code, response.text))
        return pd.DataFrame()


def get_index_review_data_single_day(index: str, review_year: int, review_month: int, review_type: str, date: str,
                                     access_token: str, verbose: bool = True):
    """
    This function enables the user to collect all information held in the database relating to a specific index review
    on a given day. The function firstly checks that the arguments are of the correct type, followed by attempting to
    collect the requested information from the database. If the information is available, it is returned as a Pandas
    DataFrame, otherwise, empty data shall be returned, with an appropriate status code printed if verbose=True.

    :param index: the index for which the user would like to return data. (str)
    :param review_year: the year at which the review event took place. (int)
    :param review_month: the month at which the review took place. (int)
    :param review_type: the type of review. (str)
    :param date: the date for which the forecast flows should be retrieved, format "YYYY-MM-DD". (str)
    :param access_token: the access token of the user, must be an active access token. (str)
    :param verbose: determines if status is printed. Default=True. (bool)
    :return: dataset: a Pandas DataFrame containing all data relating to the index argument. (pd.DataFrame)
    """
    if not all(isinstance(v, str) for v in [index, review_type, date, access_token]):
        raise TypeError("The 'index', 'review_type', 'date' and 'access_token' arguments must be string types.")
    if not all(isinstance(v, int) for v in [review_year, review_month]):
        raise TypeError("The 'review_year' and 'review_month' arguments must be integer types.")
    if not isinstance(verbose, bool):
        raise TypeError("The 'verbose' argument must be a boolean type.")
    if not re.match("([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))", date):
        raise ValueError("The 'date' argument must be passed in the format 'YYYY-MM-DD'.")
    index_values = ['AEX', 'AMX', 'AMZ', 'AMZI', 'AS51', 'ASX', 'BEL20', 'CAC', 'CPQ', 'DAX', 'DJASD', 'DJCASD',
                    'DJDVY', 'DJEMDIV', 'DJEPCSD', 'DJINET', 'DJSHMB', 'DJSMDQT', 'DJUSDIVT', 'EPRA-EUROPE',
                    'FTSEMIB', 'FUDP', 'GDM', 'GDXJ', 'GEIS-AWCHINA', 'GEIS-AWDEVEUR', 'GEIS-AWEMEUR',
                    'GEIS-AWEXCHINA', 'GEIS-AWJAPAN', 'GEIS-AWLATAM', 'GEIS-AWMEA', 'GEIS-AWNAM',
                    'GEIS-GSCCHINA', 'GEIS-GSCDEVEUR', 'GEIS-GSCEMEUR', 'GEIS-GSCEXCHINA', 'GEIS-GSCJAPAN',
                    'GEIS-GSCLATAM', 'GEIS-GSCMEA', 'GEIS-GSCNAM', 'HSCEI', 'HUR', 'IBEX', 'KOSPI2', 'MCMOT',
                    'MCX', 'MDAX', 'MEXBOL', 'MOAT', 'MSCI-DM-SC-ASIAEXJAP', 'MSCI-DM-SC-CAN', 'MSCI-DM-SC-EMEA',
                    'MSCI-DM-SC-JAPAN', 'MSCI-DM-SC-USA', 'MSCI-DM-STD-ASIAEXJAP', 'MSCI-DM-STD-CAN',
                    'MSCI-DM-STD-EMEA', 'MSCI-DM-STD-JAPAN', 'MSCI-DM-STD-USA', 'MSCI-EM-SC-AMERICAS',
                    'MSCI-EM-SC-ASIA', 'MSCI-EM-SC-EMEA', 'MSCI-EM-STD-AMERICAS', 'MSCI-EM-STD-ASIA',
                    'MSCI-EM-STD-EMEA', 'MSCI-MINVOL-EUROPE', 'MSCI-MINVOL-USA', 'MSCI-MINVOL-EM',
                    'MSCI-SRI-ASIAEXJAP', 'MSCI-SRI-CANADA', 'MSCI-SRI-EMEA', 'MSCI-SRI-JAPAN', 'MSCI-SRI-USA',
                    'MSCI-ESG-ASIAEXJAP', 'MSCI-ESG-CANADA', 'MSCI-ESG-EMEA', 'MSCI-ESG-JAPAN', 'MSCI-ESG-USA',
                    'NBI', 'NDX', 'OMX', 'RIY', 'RTY', 'SD3E', 'SD3P', 'SDAX', 'SMI', 'SMIM', 'SPEUHDA',
                    'SPGTAQD', 'SPGTCED', 'SPGTIND', 'SPI', 'SPTSX', 'SPTSX60', 'SPTXDV', 'SX5E', 'SX5P',
                    'SXXP', 'TecDAX', 'TOP40', 'TW50', 'UKX', 'XIN9I', 'EPRA-ASIA', 'EPRA-NAM', 'IXAROBK',
                    'IXBRHLTK', 'MID', 'SML', 'SPX', 'STXTDSV', 'TWDP', 'NIKKEI', 'TOPIX', 'CRSP', 'TA-125',
                    'TA-35', 'HSI', 'KLCI', 'STI', 'MUNR', 'BLOSSOM', 'OMX30', 'FBLSSRTR', 'MDYF', 'FR10',
                    'FREM', 'MCVAT', 'ENDP']
    review_types = ["QIR", "SAIR", "AIR", "IPO", "Recon", "CQIR"]
    if index not in index_values:
        raise ValueError("The 'index' value must be one of {}".format(index_values))
    if review_type not in review_types:
        raise ValueError("The 'review_type' argument must be one of {}".format(review_types))
    if not 2030 >= review_year > 1981:
        raise ValueError("The 'review_year' argument must be between 1981 and 2030.")
    if review_month not in range(1, 13):
        raise ValueError("The 'review_month' argument must be between 1-12 inclusive.")

    url = "https://www.samsonrockapis.com/forecast_flows&index={}" \
          "&review_year={}&review_month={}&review_name={}&date={}".format(index, review_year, review_month,
                                                                          review_type, date)
    header = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        if verbose:
            print("Status Code: {}".format(response.status_code))
        return pd.read_json(response.text)
    elif response.status_code == 404:
        if verbose:
            print("Status Code: {}, no data available for the {}{}{} review".format(response.status_code, index,
                                                                                    review_year, review_month,
                                                                                    review_type))
        return pd.DataFrame()
    elif response.status_code == 401:
        if verbose:
            print("Status Code: {}, user not properly authenticated for endpoint.".format(response.status_code))
        return pd.DataFrame()
    else:
        if verbose:
            print("Status Code: {}, {}.".format(response.status_code, response.text))
        return pd.DataFrame()


def get_index_review_data_daterange(index: str, review_year: int, review_month: int, review_type: str,
                                    start_date: str, end_date: str, access_token: str, verbose: bool = True):
    """
    This function enables the user to collect all information held in the database relating to a specific index review
    for a given date range. The function firstly checks that the arguments are of the correct type, followed by
    attempting to collect the requested information from the database. If the information is available, it is returned
    as a Pandas DataFrame, otherwise, empty data shall be returned, with an appropriate status code printed if
    verbose=True.

    :param index: the index for which the user would like to return data. (str)
    :param review_year: the year at which the review event took place. (int)
    :param review_month: the month at which the review took place. (int)
    :param review_type: the type of review. (str)
    :param start_date: the date for which the forecast flows should be retrieved, format "YYYY-MM-DD". (str)
    :param end_date: the date for which the forecast flows should be retrieved, format "YYYY-MM-DD". (str)
    :param access_token: the access token of the user, must be an active access token. (str)
    :param verbose: determines if status is printed. Default=True. (bool)
    :return: dataset: a Pandas DataFrame containing all data relating to the index argument. (pd.DataFrame)
    """
    if not all(isinstance(v, str) for v in [index, review_type, start_date, end_date, access_token]):
        raise TypeError("The 'index', 'review_type', 'start_date', 'end_date' and 'access_token' "
                        "arguments must be string types.")
    if not all(isinstance(v, int) for v in [review_year, review_month]):
        raise TypeError("The 'review_year' and 'review_month' arguments must be integer types.")
    if not isinstance(verbose, bool):
        raise TypeError("The 'verbose' argument must be a boolean type.")
    index_values = ['AEX', 'AMX', 'AMZ', 'AMZI', 'AS51', 'ASX', 'BEL20', 'CAC', 'CPQ', 'DAX', 'DJASD', 'DJCASD',
                    'DJDVY', 'DJEMDIV', 'DJEPCSD', 'DJINET', 'DJSHMB', 'DJSMDQT', 'DJUSDIVT', 'EPRA-EUROPE',
                    'FTSEMIB', 'FUDP', 'GDM', 'GDXJ', 'GEIS-AWCHINA', 'GEIS-AWDEVEUR', 'GEIS-AWEMEUR',
                    'GEIS-AWEXCHINA', 'GEIS-AWJAPAN', 'GEIS-AWLATAM', 'GEIS-AWMEA', 'GEIS-AWNAM',
                    'GEIS-GSCCHINA', 'GEIS-GSCDEVEUR', 'GEIS-GSCEMEUR', 'GEIS-GSCEXCHINA', 'GEIS-GSCJAPAN',
                    'GEIS-GSCLATAM', 'GEIS-GSCMEA', 'GEIS-GSCNAM', 'HSCEI', 'HUR', 'IBEX', 'KOSPI2', 'MCMOT',
                    'MCX', 'MDAX', 'MEXBOL', 'MOAT', 'MSCI-DM-SC-ASIAEXJAP', 'MSCI-DM-SC-CAN', 'MSCI-DM-SC-EMEA',
                    'MSCI-DM-SC-JAPAN', 'MSCI-DM-SC-USA', 'MSCI-DM-STD-ASIAEXJAP', 'MSCI-DM-STD-CAN',
                    'MSCI-DM-STD-EMEA', 'MSCI-DM-STD-JAPAN', 'MSCI-DM-STD-USA', 'MSCI-EM-SC-AMERICAS',
                    'MSCI-EM-SC-ASIA', 'MSCI-EM-SC-EMEA', 'MSCI-EM-STD-AMERICAS', 'MSCI-EM-STD-ASIA',
                    'MSCI-EM-STD-EMEA', 'MSCI-MINVOL-EUROPE', 'MSCI-MINVOL-USA', 'MSCI-MINVOL-EM',
                    'MSCI-SRI-ASIAEXJAP', 'MSCI-SRI-CANADA', 'MSCI-SRI-EMEA', 'MSCI-SRI-JAPAN', 'MSCI-SRI-USA',
                    'MSCI-ESG-ASIAEXJAP', 'MSCI-ESG-CANADA', 'MSCI-ESG-EMEA', 'MSCI-ESG-JAPAN', 'MSCI-ESG-USA',
                    'NBI', 'NDX', 'OMX', 'RIY', 'RTY', 'SD3E', 'SD3P', 'SDAX', 'SMI', 'SMIM', 'SPEUHDA',
                    'SPGTAQD', 'SPGTCED', 'SPGTIND', 'SPI', 'SPTSX', 'SPTSX60', 'SPTXDV', 'SX5E', 'SX5P',
                    'SXXP', 'TecDAX', 'TOP40', 'TW50', 'UKX', 'XIN9I', 'EPRA-ASIA', 'EPRA-NAM', 'IXAROBK',
                    'IXBRHLTK', 'MID', 'SML', 'SPX', 'STXTDSV', 'TWDP', 'NIKKEI', 'TOPIX', 'CRSP', 'TA-125',
                    'TA-35', 'HSI', 'KLCI', 'STI', 'MUNR', 'BLOSSOM', 'OMX30', 'FBLSSRTR', 'MDYF', 'FR10',
                    'FREM', 'MCVAT', 'ENDP']
    review_types = ["QIR", "SAIR", "AIR", "IPO", "Recon", "CQIR"]
    if index not in index_values:
        raise ValueError("The 'index' value must be one of {}".format(index_values))
    if review_type not in review_types:
        raise ValueError("The 'review_type' argument must be one of {}".format(review_types))
    if not 2030 >= review_year > 1981:
        raise ValueError("The 'review_year' argument must be between 1981 and 2030.")
    if review_month not in range(1, 13):
        raise ValueError("The 'review_month' argument must be between 1-12 inclusive.")
    if not all(re.match("([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))", v) for v in [start_date, end_date]):
        raise ValueError("The 'start_date' and 'end_date' arguments must be passed in the format 'YYYY-MM-DD'.")

    url = "https://www.samsonrockapis.com/forecast_flows&index={}&review_year={}" \
          "&review_month={}&review_name={}&start_date={}&end_date={}".format(index, review_year, review_month,
                                                                             review_type, start_date, end_date)
    header = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        if verbose:
            print("Status Code: {}".format(response.status_code))
        return pd.read_json(response.text)
    elif response.status_code == 404:
        if verbose:
            print("Status Code: {}, no data available for the {}{}{} review".format(response.status_code, index,
                                                                                    review_year, review_month,
                                                                                    review_type))
        return pd.DataFrame()
    elif response.status_code == 401:
        if verbose:
            print("Status Code: {}, user not properly authenticated for endpoint.".format(response.status_code))
        return pd.DataFrame()
    else:
        if verbose:
            print("Status Code: {}, {}.".format(response.status_code, response.text))
        return pd.DataFrame()
