# sage, midage, endage
def y_value(df, choose_age):
    # raw df
    df_mean = df.groupby('age.1').mean()
    y = df_mean.loc[choose_age, 'two']
    return y

def slope_diff(df, sage, midage, endage):
    # raw df
    slope1 = abs((y_value(df, midage)-y_value(df, sage)) / (midage - sage))
    slope2 = abs((y_value(df, endage)-y_value(df, midage)) / (endage - sage))
    diff = abs(slope1-slope2)
    return diff

def max_slope(df, sage, endage):
    df_new = df.groupby('age.1').mean()
    slope = {}
    for index, row in df_new.iterrows():
        if index == sage:
            continue
        if index == endage:
            continue
        else:
            slope[index] = slope_diff(df, sage, index, endage)
    max_value = max(slope.values())
    age_set = {key for key, value in slope.items() if value == max_value}
    return age_set


def per_child_max(df, name):
    df_new = df.loc[df['corpus'] == name].groupby('age.1').mean()
    slope = {}
    index_sort = sorted(df_new.index.tolist())
    sage = index_sort[0]
    endage = index_sort[-1]
    for index, row in df_new.iterrows():
        if index == sage:
            continue
        if index == endage:
            continue
        else:
            slope[index] = slope_diff(df, sage, index, endage)
    max_value = max(slope.values())
    age_set = {key for key, value in slope.items() if value == max_value}
    return age_set

