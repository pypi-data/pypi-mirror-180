# -*- ecoding: utf-8 -*-
# @ModuleName: pandas.py
# @Author: jason
# @Email: jasonforjob@qq.com
# @Time: 2022/08/01
# @Desc: pandas 常用操作封装



import numpy as np
import pandas as pd
import re



def fill_cols(df, cols=None, cols_dict=None,fill_str=''):
    """
    接受一个数据帧，并用默认值填充数据帧中的任何缺失列。cols参数是需要添加到数据帧的列名列表，
    cols_dict参数是将列名映射到其默认值的字典。如果未指定cols参数，函数将添加cols_dict中的所有列。如果指定了fill_str参数，
    它将用作添加到数据帧的任何列的默认值。
    :param df: dataframe数据集
    :param cols: 要补充的字段，补充默认为空字符,传入的为list
    :param cols_dict: 要补充字段的对应的值的字典,传入为dict
    :param str: 需要填充的值,默认是空字符串
    :return: df

    # 创建一个示例数据帧
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    # 向数据帧添加两列
    cols = ['C', 'D']
    cols_dict = {'C': 7, 'D': 8}

    # 填充数据帧中的缺失列
    df = fill_cols(df, cols=cols, cols_dict=cols_dict)

    # 最终的数据帧应该有四列：A、B、C和D
    print(df)
    这段代码的输出应该是：

       A  B  C  D
    0  1  4  7  8
    1  2  5  7  8
    2  3  6  7  8
    """
    df = df.copy()
    if cols:
        for col in cols:
            if col not in df.columns:
                df[col] = fill_str
    if cols_dict:
        for col in cols_dict.keys():
            df[col] = cols_dict[col]
    return df



def replace_nan(df, rep_str=''):
    """
    none替换成空字符串
    :param df:
    :param rep_str:
    :return:
    """
    df = df.copy()
    return df.replace([np.nan, None], [rep_str, rep_str])


def replace_str_to_nan(df, rep_str=''):
    """
    空字符串替换none
    :param df:
    :param rep_str:
    :return:
    """
    df = df.copy()
    return df.replace([rep_str], [np.nan])

def split_df_into_batches(df, num=10):
    """
    dataframe 分块,返回迭代器
    :param df:
    :param num: 分块数
    :return: 迭代器

    # 创建一个数据框
    df = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [10, 20, 30, 40, 50]})

    # 将数据框分块
    for batch in split_df_by_batch(df, num=3):
        print(batch)
    运行上面的代码会得到下面的输出：

       a   b
    0  1  10
    1  2  20

       a   b
    2  3  30
    3  4  40

       a   b
    4  5  50
    """
    split_num = len(df) // num
    for i in range(0, len(df), split_num):
        yield df.iloc[i:i + split_num]



def count_non_empty_values(df):
    '''
    统计每个字段列不为空的数量
    :param origin_df:
    :return:
    '''
    df = df.copy()

    for col in df.columns:
        # 如果存在空字符串，则计算非空值的数量时应该将空字符串的值也算在内
        t = len(df) - df[col].isnull().sum() - df[col].eq('').sum()
        percent = str(round(t / len(df) * 100, 2)) + '%'
        print(col, t,percent)



def drop_cols(df, pct=0.8, retain_cols=None):
    """
    删除列中数据为空的行的比例超过一定比例的列，如果传入retain_cols，则保留指定的列
    :param df: 需要删除列的 DataFrame (DataFrame)
    :param pct: 数据为空的行的比例（float, default=0.8）
    :param retain_cols: 保留的列 (list, default=None)
    :return: 删除列后的 DataFrame (DataFrame)

       A     B     C  D
    0  1     1  None  0
    1  2     0   NaN  0
    2  3           0  0
    3  4  None        0

    df = drop_cols(df, pct=0.8, retain_cols=['A'])
    删除-> ['B', 'C']
       A  D
    0  1  0
    1  2  0
    2  3  0
    3  4  0


    """
    df = df.copy()

    if retain_cols is None:
        retain_cols = []

    cols = []
    for col in df.columns:
        # 如果存在空字符串，则计算非空值的数量时应该将空字符串的值也算在内
        t = len(df) - df[col].isnull().sum() - df[col].eq('').sum()

        # 如果满足条件，且不在保留的列中，则将该列添加到待删除的列中
        if t / len(df) <= pct and col not in retain_cols:
            cols.append(col)
    print('删除->',cols)
    df = df.drop(cols,axis=1)
    return df

def split_col_data(df,split_col,split_str,reset_index=True):
    """
    在origin_df中切分split_col字段中的split_str字符，一行切分成多行
    例如:
       a    b  c
    0  1  a,b  2
    1  2  c,c  3
    2  3    d  5
    3  4    e  7

    split_data(origin_df,b,',') ->

       a  c  b
    0  1  2  a
    0  1  2  b
    1  2  3  c
    1  2  3  c
    2  3  5  d
    3  4  7  e


    :param origin_df: 需要切分的df
    :param split_col: 需要切分的列
    :param split_str: 需要切分的字符串
    :return: 切分后的数据集
    """
    df = df.copy()

    df[split_col] = df[split_col].str.split(split_str)
    df = df.explode('year')
    if reset_index:
        df = df.reset_index(drop=True)
    return df


def strip_data(df):
    """
     删除dataframe中所有字符串值的两端的空格和换行符。

     df: pandas DataFrame, 待处理的dataframe。
     return: pandas DataFrame，经过处理的dataframe。

     示例：
     >>> df = pd.DataFrame({'A': ['   abc   ', 'def  '], 'B': ['ghi', '   jkl']})
     >>> strip_data(df)
       A    B
     0 abc  ghi
     1 def  jkl
     """
    df = df.copy()
    # 过滤出dataframe中的字符串类型的列
    str_cols = df.select_dtypes(include=['object']).columns
    # 对字符串类型的列进行strip操作
    df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())
    return df


def stack_df_by_index(df,index_col=['index'],split_cols=['a', 'b'],rename='split'):
    """
    这段代码实现了对数据框（df）的处理，将其中的某些列的内容按照指定的索引（index）列拆分成多行，并将拆分后的列重新命名为rename。
    具体实现方法是通过将拆分的列（cols）堆叠成一个Series，并用DataFrame的stack方法将该Series的内容拆分成多行，最后使用reset_index方法重置行索引，
    并通过rename方法重命名拆分后的列

    df:数据
    index_col:index列
    split_cols:需要拆分的列
    rename:拆分后的列明

    index a b
    1   A  B
    2   A1 B2
    ->
    index rename
    1 A
    1 B
    2 A1
    2 B2
    """
    df = df.copy()
    df = pd.merge(df[index_col], pd.DataFrame(df[split_cols].stack().droplevel(
        1)), left_index=True, right_index=True).reset_index(drop=True).rename(columns={0: rename})
    return  df


def stack_df(df, axis=1):
    """
    将 DataFrame 降维。

    参数:
        df: DataFrame, 输入的数据
        axis: int, 降维的方向。1 表示按列降维，0 表示按行降维，默认为 1。

    返回:
        DataFrame，降维后的数据。

    降维的方式分为按行降维和按列降维，默认情况下采用按列降维。

    下面是一个例子，假设有以下 DataFrame：

       a  b
    a  2  1
    b  3  1
    如果采用按列降维，结果将会是这样：

      key1 key2  value
    0    a    a      2
    1    a    b      3
    2    b    a      1
    3    b    b      1
    如果采用按行降维，结果将会是这样：

      key1 key2  value
    0    a    a      2
    1    b    a      3
    2    a    b      1
    3    b    b      1
    """
    df = df.copy()
    if axis:
        df2 = df.unstack().reset_index()
    else:
        df2 = df.stack().reset_index()
    df2.columns = ['key1', 'key2', 'value']
    return df2

def split_col_range_data(df,col,split_str='-',reset_index=True):
    """将连续的数据拆成多行
    df:Dataframe
    col:要拆分的字段
    split_str:连接符，类似2000-2002中的'-'

    make    model    year
    0    Chevrolet    Classic    2004-2005
    1    Chevrolet    Malibu    1999-2003
    2    Chevrolet    Malibu    1998

    ->
    make    model    year
    0    Chevrolet    Classic    2004
    0    Chevrolet    Classic    2005
    1    Chevrolet    Malibu    1999
    1    Chevrolet    Malibu    2000
    1    Chevrolet    Malibu    2001
    1    Chevrolet    Malibu    2002
    1    Chevrolet    Malibu    2003
    2    Chevrolet    Malibu    1998

    """
    new=[]
    df = df.copy()
    def process(row):

        if split_str in row[col]:
            start,end = row[col].split(split_str)
            for i in range(int(start),int(end)+1): # 遍历 start 到 end 的所有年份，依次添加到 new 中
                item = row.copy()
                item[col] = i
                new.append(item)

        else:
            item=row.copy()
            new.append(item)
        return row

    # 将数据分成需要分割和不需要分割
    df_split = df[df[col].str.contains(split_str)]
    df_no_split = df[~df[col].str.contains(split_str)]

    df_split.apply(process,axis=1)

    res = pd.DataFrame(new).append(df_no_split)

    if reset_index:
        res = res.reset_index(drop=True)

    return res

def check_duplicate_cols(df):
    """
    该函数接收一个 DataFrame 作为输入，并返回 DataFrame 中重复列名的列表。

    df：Dataframe

        a	a
    0	1	2
    1	2	3

    ->

    ['a']

    """

    return df.columns[df.columns.duplicated()].tolist()




def split_df_by_groups(df, col, drop_col=False):
    """
    这个函数用于根据指定字段将数据集拆分成多个数据子集。
    df: 要拆分的数据集，是一个 pandas DataFrame
    col: 拆分数据集的依据，是一个字段名
    drop_col: 是否删除字段 col，默认为 False
    return: 拆分后的多个数据子集，是一个 DataFrame 的列表

    例子
    A B group
    a v 1
    b c 2
    c c 2
    ->
    [
    A B group
    a v 1
    ,
    A B group
    b c 2
    c c 2
    ]
    这两个数据子集分别包含值为 1 和 2 的行。如果 drop_col 设为 True，则拆分后的数据子集中将不再包含 group 字段。
    """
    # 定义返回列表
    new = []
    # 对于数据集中的每一个不同的字段值
    for i in df[col].unique():
        # 复制一份数据子集，包含值为 i 的行
        df2 = df[df[col] == i].copy()
        # 如果 drop_col 为 True，则删除字段 col
        if drop_col:
            df2.drop(col, axis=1, inplace=True)
        # 将数据子集加入返回列表
        new.append(df2)
    # 返回列表
    return new



def values_to_binary(df, cols=None):
    """
    将传入的df的空值转成''，然后将空值赋为0，非空赋为1
    df: 要转换的数据集，是一个 pandas DataFrame
    cols: 需要转化的字段，默认为数据集的所有列
    return: 转换后的数据集，是一个 pandas DataFrame

    下面是一个使用 values2binary 函数的例子：

    假设我们有一个数据集：

    A B C
    a v 1
    b c
    c c 2
    我们可以使用 values2binary 函数将其转换为二进制值：

    # 使用 values2binary 函数
    df_binary = values2binary(df)

    输出结果为：

    A B C
    1 1 1
    1 1 0
    1 1 1
    所有非空值都被赋值为 1，空值被赋值为 0。
    """
    # 如果 cols 没有指定，则默认为数据集的所有列
    if cols is None:
        cols = df.columns
    # 将数据集中的空值转换为 ''
    df = replace_nan(df)
    # 将空值赋为 0，非空值赋为 1
    return (df[cols] != '') * 1

def split_df_by_unique_cols(df):
    """
    这个函数用于将数据框中相同有值的字段数据块拆分成多个数据子集。

    df: 要拆分的数据集，是一个 pandas DataFrame
    return: 一个包含有效字段、无效字段和数据子集的元组的列表，每个元组代表一个数据子集

    例如
      A  B  C
    0  a  v  1
    1  b  c
    2  c  c  2

    调用函数，传入这个数据框作为参数，将会返回一个包含两个元组的列表，每个元组代表一个数据子集
    ->
    [    (['A', 'B', 'C'], [],
            A  B  C
         0  a  v  1
         2  c  c  2),
        (['A', 'B', 'C'], [],
            A  B  C
         1  b  c)
    ]

    这两个元组分别对应了两个数据子集，每个元组包含三个列表，分别表示该数据子集中的有效字段、无效字段和数据子集本身。

    数据子集有效字段表示这个数据子集中的每一列都包含至少一个非空值。例如，上面的例子中，两个数据子集中都只包含列 A、B 和 C，因此这些列都被视为有效字段。

    数据子集无效字段表示这个数据子集中的每一列
    """
    # 将数据集重置索引
    df = df.reset_index(drop=True)
    # 获取数据集的所有列名
    cols = df.columns.tolist()
    # 转换数据集中的值为二进制值
    df_binary = values_to_binary(df)
    # 去除重复行
    df_binary_unique = df_binary.drop_duplicates().copy()
    # 为每一行分配一个组号
    df_binary_unique['group'] = list(range(df_binary_unique.shape[0]))
    # 将组号合并到原数据集中
    df_res = pd.merge(df_binary_unique, df_binary, on=cols, how='right')
    df = pd.merge(df_res[['group']], df, left_index=True, right_index=True)
    # 根据组号将数据集拆分为多个数据子集
    dfs = []
    for df in split_df_by_groups(df, 'group', drop_col=True):
        # 检测哪些列包含空值
        valid_field, invalid_field = get_empty_columns(df)
        # 将有效字段、无效字段和数据子集放入元组中，并将元组加入列表中
        dfs.append([valid_field, invalid_field, df])
    # 返回结果列表
    return dfs

def get_empty_columns(df):
    '''
    该函数用于接受一个包含多列的数据框（DataFrame）作为输入，并返回两个列表，分别包含非空列和全为空的列的列名。
    :param df: pandas.DataFrame，包含多列数据
    :return: list，包含非空列和全为空的列的列名
    例如，假设我们有以下数据框：
           col1  col2  col3
        0     1     2     3
        1     4     5     6
        2     7     8     9
        那么调用 getNaCols 函数，传入这个数据框作为参数，将会返回如下两个列表：

        ['col1', 'col2', 'col3']
        []
    '''
    invalid_field=[]
    df = replace_nan(df)  # 用空字符串替换空值
    for col in df.columns:
        try:
            if sum(df[col] != '') == 0:  # 计算列中非空字符串的数量
                invalid_field.append(col)  # 如果数量为零，将列名添加到列表中
        except Exception as e:
            print(col,'有异常')
            raise e
    valid_field = list(np.setdiff1d(df.columns,invalid_field))  # 计算非空列
    return [valid_field,invalid_field]  # 返回两个列表

def split_column_into_multiple_columns(df, col, new_cols):
    """
    将数据框中的一列，拆分成多列

    参数:
    df: pandas DataFrame. 要拆分的数据框
    col: str. 包含元组或列表的列名
    new_cols: list of str. 新列的名字

    返回:
    pandas DataFrame. 拆分后的数据框


    例子:
    # 假设这是您的原始数据框，包含了一个包含元组的列
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'new_col': [(1, 2, 3), (4, 5, 6), (7, 8, 9)]})

    # 使用join_data_to_columns函数，拆分new_col列
    df = join_data_to_columns(df, 'new_col', ['new_col1', 'new_col2', 'new_col3'])

    # 现在，您应该会看到新的列，它们包含了每行的结果
    print(df)
    """
    # 复制原始数据框
    df = df.copy()

    # 使用join方法，拆分col列
    df = df.join(pd.DataFrame(df[col].tolist(), columns=new_cols))

    return df



def get_top_n_groups_by_count(df,groupby=[],top_col='',n=5):
    """
    该函数的作用是，对数据进行分组，然后在每组内计算每个值出现的次数，并返回每组排序后的前n个最大值。
    这个函数接收三个参数：
    df：要处理的DataFrame
    groupby：分组的列名，分组时可以是多个列，默认为空
    top_col：计算每组最大值的列名
    n：取前n个最大值，默认为5
    return:DataFrame
    示例：

    # 假设df是以下数据
       city  color
    0     A     red
    1     A     red
    2     B     red
    3     B     blue
    4     B     green
    5     C     green
    6     C     green
    7     C     blue
    8     D     blue
    9     D     blue

    # 调用函数
    get_top_n_groups_by_count(df,groupby=['city'],top_col='color',n=2)

    # 返回值
      city  color_count
    0    B            2
    1    C            2
    上述代码表示，对数据按城市分组，并在每组内计算每个颜色出现的次数，最后返回每组排序后的前2个颜色。
    """
    data_agg = df.groupby(groupby)[top_col].count()
    g = data_agg.groupby(level=0, group_keys=False)
    g = g.nlargest(n).reset_index().rename(columns={top_col:f'{top_col}_count'})
    return g

def split_col_by_delimiter(origin_df, col, split_str=' '):
    """
    根据指定字符分列

    origin_df: 要拆分的数据集，是一个 pandas DataFrame
    col: 要拆分的字段，是一个字段名
    split_str: 分隔符，默认为空格
    return: 拆分后的数据集，是一个 pandas DataFrame

    下面是一个使用 split_col_by_delimiter 函数的例子：

    假设我们有一个数据集：

    A
    ACDelco 41-101 rockauto 1SPP0200
    我们可以使用 split_col_by_delimiter 函数将字段 A 按照空格分列：

    # 创建一个数据框
    origin_df = pd.DataFrame({
        'A': ['ACDelco 41-101 rockauto 1SPP0200']
    })

    # 使用 split_col_by_delimiter 函数
    df = split_col_by_delimiter(origin_df, 'A')

    输出结果为：

       0         1        2           3
    0 ACDelco  41-101   rockauto     1SPP0200

    """
    df = origin_df.copy()
    df[col].str.split(split_str, expand=True)
    df = strip_data(df)
    return df


def compare_dfs(df1, df2, by=[]):
    '''
    这个函数计算两个数据框的差集。它返回一个布尔值，表示两个数据框是否有不同的行。

    参数：

    df1：第一个数据框。
    df2：第二个数据框。
    by：一个字符串列表，表示用来比较的列名。如果为空，则默认使用两个数据框的交集作为比较的列。
    举个例子，假设有两个数据框 df1 和 df2，它们的内容如下：

    df1 = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })

    df2 = pd.DataFrame({
        'A': [3, 2, 1],
        'B': [6, 5, 4]
    })
    调用 setdiff1d 函数来比较这两个数据框，可以这样：

    setdiff1d(df1, df2, by=['A', 'B'])
    这个函数会返回 False，表示两个数据框没有不同的行。
    '''

    # 如果没有指定比较的列，则默认使用df1和df2的交集
    if len(by) == 0:
        by = np.intersect1d(df1.columns, df2.columns)
    else:
        # 检查比较的列是否存在，如果不存在，则抛出异常
        for col in by:
            if col not in df1.columns:
                raise KeyError(f'{col}列不存在！')

    # 拷贝df1，防止修改原数据框
    df1 = df1.copy()

    # 使用 Pandas 的 isin 函数来计算差集
    return df1[~df1[by].isin(df2[by])].shape[0] > 0


def diff_dfs(df1, df2, by=[]):
    '''
    此函数用于求出df1对df2的差集，即df1中有而df2中没有的数据。
    根据df1与df2的共同字段，求df1对df2的差集

    Parameters
    ----------
    df1 : pandas.DataFrame
        需要求差集的第一个DataFrame
    df2 : pandas.DataFrame
        需要求差集的第二个DataFrame
    by : list
        需要求差集的字段列表，默认为df1和df2的交集

    Returns
    -------
    diff_df : pandas.DataFrame
        df1对df2的差集

    举例说明:

    假设有两个DataFrame df1和df2，其中df1中有字段A和B，df2中有字段A和C，如下所示：

    df1:

    A	B
    0	1	2
    1	3	4
    df2:

    A	C
    0	1	5
    1	6	7
    调用diff_dfs(df1, df2, by=["A"])，返回值为df1中A字段和df2中A字段不同的数据，即：

    A	B
    1	3	4
    '''
    # 如果没有指定by参数，则默认为df1和df2的交集
    if len(by) == 0:
        common_fields = np.intersect1d(df1.columns, df2.columns)
    else:
        common_fields = by

    # 将df1和df2的数据去重
    df1 = df1.copy().drop_duplicates()
    df2 = df2[common_fields].copy().drop_duplicates()

    # 为df1和df2分别添加id字段，并进行合并
    df1_id, df2_id = 'df1_id1', 'df2_id1'
    df1[df1_id] = np.uint32(range(df1.shape[0]))
    df2[df2_id] = np.uint32(range(df2.shape[0]))
    merge_df = pd.merge(df1, df2, on=common_fields, how='left')

    # 求出差集的id列表
    diff_ids = merge_df.loc[merge_df[df2_id].isna()][df1_id]

    # 返回df1中在差集id列表中的数据
    return df1.loc[df1[df1_id].isin(diff_ids)].drop(columns=[df1_id])


def concat_cols(df,origin_cols,concat_cols):
    """
    从数据框（DataFrame） df 中选取两组列（origin_cols 和 concat_cols），
    将这两组列分别复制到两个新的数据框（df1 和 df2）中，并将 df2 中的列名修改为 origin_cols 中的列名。
    最后，将 df1 和 df2 按行拼接起来，返回新的数据框。

    df:dataframe
    origin_cols:保留的原始列
    concat_cols:将要合并到原始origin_cols的列
    return:dataframe

    例子：
        a        b		a1      b1
    0	000-004	NaN	    300-312	2
    1	010-041	5	    317-319	2
    2	042-049	6	    320-326	3

        a	    b
    0	000-004	NaN
    1	010-041	5
    2	042-049	6
    3   300-312	2
    4   317-319	2
    5   320-326	3
    """

    df1 = df[origin_cols].copy()
    df2 = df[concat_cols].copy()
    df2.columns=origin_cols
    df1.append(df2)
    return df1


def remove_upprintable_chars(df):
    """
    移除数据框中所有字符串类型的列中的不可见字符。并将这些字符串中的多个连续的空白字符替换为单个空格。
    参数:
        df: 要进行操作的数据框。
    返回值:
        一个包含更新后的数据的数据框。

    举个例子，假设有以下数据框：

    df = pd.DataFrame({
        'col1': ['hello\tworld', '\nfoo\nbar\t'],
        'col2': ['\rfoobar', '\vbarbaz']
    })
    调用 remove_upprintable_chars 函数：

    df_updated = remove_upprintable_chars(df)
    此时 df_updated 的值为：

    df_updated = pd.DataFrame({
        'col1': ['hello world', 'foo bar'],
        'col2': ['foobar', 'barbaz']
    })
    """
    for col in df.columns:
        try:
            if str(df[col].dtype)=='object': # 对于每一列，如果它的数据类型是字符串类型，则对它进行处理
                # 对于每一个字符串，只保留可打印的字符，并用一个空格替换多个连续的空白字符
                df[col] = df[col].apply(lambda s:re.sub(r'\s+', ' ', ''.join(x for x in s if x.isprintable())))
        except:
            print(col,'字段移除不可见字符失败')
            continue
    return df




