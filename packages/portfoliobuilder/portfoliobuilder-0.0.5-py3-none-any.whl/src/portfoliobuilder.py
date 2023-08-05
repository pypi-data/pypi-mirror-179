import click

@click.group()
def portfoliobuilder():
    pass


###############################################
"""
CREATE GROUP
"""


@click.group(name='create')
def create_group():
      pass

@click.command(name='create_customized_portfolio',help="create a customized portfolio.")
def create_customized_portfolio():
      pass


##################################################
"""
FETCH GROUP
"""



@click.group(name='get')
def get_group():
      pass

@click.command(name='daily_model_portfolio',help="get daily model portfolio")
def get_daily_model_poretfolio():
      pass

@click.command(name='view_breached_stocks',help="list of stocks breached thier target limit.")
def get_breched_target_range_stocks():
      pass

@click.command(name="get_price")
def get_stock_price():
    """
    to get stock price
    :return:
    """
    pass



create_group.add_command(create_customized_portfolio)
get_group.add_command(get_daily_model_poretfolio)
get_group.add_command(get_stock_price)
portfoliobuilder.add_command(get_group)
portfoliobuilder.add_command(create_group)