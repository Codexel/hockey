def categorize_players_by_skill(metric, new_column, lower_percentile, upper_percentile, reverse = False):
    """Assigns players to a category (low, medium, top) depending on their score in a given metric
    
    Parameters:
    metric (str): the metric used for categorizing players
    new_column (str): the name of the new column that will hold the category value (low/medium/top)
    lower_percentile (float): players below this percentile will be categorized as low
    upper_percentile (float): players above this percentile will be categorized as top
    reverse (bool): used for reversing the percentiles when applying the function to a defensive metric
    where a lower score is better 

    Returns:
    Nothing. The function automatically manipulates the players dataset. 
    """

    if reverse:
        lower_percentile = 1 - lower_percentile
        upper_percentile = 1 - upper_percentile

    # finding the values that correspond to the selected percentiles
    percentile_values = players.loc[:,metric].describe(percentiles=[lower_percentile, upper_percentile])
    cutoff_value_low = percentile_values[4] # players with a lower score than this will be labeled as low
    cutoff_value_top = percentile_values[6] # players with a higher score than this will be labeled as top

    # labeling the players
    players[new_column] = medium

    if reverse:
        players.loc[players.loc[:,metric] > cutoff_value_top, new_column] = low
        players.loc[players.loc[:,metric] < cutoff_value_low, new_column] = top

    else:
        players.loc[players.loc[:,metric] > cutoff_value_top, new_column] = top
        players.loc[players.loc[:,metric] < cutoff_value_low, new_column] = low
