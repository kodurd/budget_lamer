import pandas as pd
from typing import Tuple


def groups_df_api_dzen(dataset: pd.DataFrame, now_month: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Groups datasets received from the DZEN MONEY API.
    Returns two dataframes, the first one in the structure:
    {'index': name_category, 'outcome': value, 'income': value}
    the second in the structure:
    {'index': name_account, 'balance': value}
    """

    df_transaction = pd.DataFrame(dataset.get('transaction', {}))
    df_tag = pd.DataFrame(dataset.get('tag', {}))[['id', 'title']]
    df_account = pd.DataFrame(dataset.get('account', {}))[['id', 'title', 'balance']]

    # Фильтруем транзакции
    df_transaction['date'] = df_transaction['date'].astype('datetime64[ns]')
    df_transaction['year_month'] = df_transaction['date'].dt.to_period('M')
    df_transaction = df_transaction.loc[(df_transaction['year_month'] == now_month) & (df_transaction['deleted'] == 0)]
    df_transaction = df_transaction[['date', 'income', 'outcome', 'incomeAccount', 'outcomeAccount', 'tag']]
    df_transaction['tag'] = df_transaction['tag'].map(lambda x: x[0] if x is not None else x)

    # Объединим dataframes
    df_transaction = (df_transaction.merge(df_tag, left_on='tag', right_on='id', how='left')
                      .merge(df_account, left_on='incomeAccount', right_on='id', how='left')
                      .merge(df_account, left_on='outcomeAccount', right_on='id', how='left'))
    df_transaction.rename(columns={'title_x': 'category',
                                   'title_y': 'income_account',
                                   'title': 'outcome_account'}, inplace=True)
    df_transaction = df_transaction[['date', 'income', 'outcome', 'income_account', 'outcome_account', 'category']]

    df_budget = df_transaction.groupby(['category']).agg(outcome=('outcome', 'sum'),
                                                         income=('income', 'sum'))
    df_account = df_account[df_account['balance'] != 0][['title', 'balance']].set_index('title')

    return df_budget, df_account


def groups_df_api_moex(dataset: pd.DataFrame) -> pd.DataFrame:
    """The group responds to the MOEX API, which calculates the share price.
    the structure's datarem is called: {'index': ticker, 'price' : price_shares}"""

    dataset['price'] = dataset['value'] / dataset['volume']
    return dataset[dataset['market_title'] == 'Рынок акций'][['secid', 'price']].set_index('secid')
