"""
A python module for process tables.

@author: Rui Zhu  
@creation time: 2022-11-29
"""
import pandas as pd
from astropy.table import Table
from astropy.coordinates import SkyCoord
import astropy.units as u


def fits2df(path_fits):
    """
    读取fits中的table, 并转换成pandas的DataFrame
    """
    tbl = Table.read(path_fits, character_as_bytes=False)
    df = tbl.to_pandas()
    return df

def matching(cat1, cat2, coord_name1=('ra', 'dec'), coord_name2=('ra', 'dec'), sep=1):
    """
    Matching two catalogs.

    Parameter
    ---------
    cat1: DataFrame
        待交叉的catalog1
    cat2: DataFrame
        待交叉的catalog2
    coord_name1: tuple (optional)
        catalog1中ra, dec使用的名称
    coord_name2: tuple (optional)
        catalog2中ra, dec使用的名称
    sep: 1 (默认)
        match阈值, 单位arcsec

    Return
    ------
    matched_cat: DataFrame
        交叉后的catalog
    """
    # * ------ 阈值 -----
    max_sep = sep*u.arcsec
    # * ----------------

    # ^ ----- step1: 检查与规范
    # Dataframe检查
    cat1.reset_index(inplace=True, drop=True)
    cat2.reset_index(inplace=True, drop=True)

    # 坐标列名调成('ra', 'dec')
    normal_coord_name = ('ra', 'dec')
    if coord_name1 != normal_coord_name:
        cat1.rename(columns={
            coord_name1[0]: normal_coord_name[0], 
            coord_name1[1]: normal_coord_name[1]
            }, inplace=True)
    if coord_name2 != normal_coord_name:
        cat2.rename(columns={
            coord_name2[0]: normal_coord_name[0], 
            coord_name2[1]: normal_coord_name[1]
            }, inplace=True)
    
    # ^ ----- step2: 构建坐标列
    # 创建坐标列
    ra1 = list(cat1['ra'])
    dec1 = list(cat1['dec'])

    ra2 = list(cat2['ra'])
    dec2 = list(cat2['dec'])

    coord1 = SkyCoord(ra=ra1*u.degree, dec=dec1*u.degree)
    coord2 = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)

    # ^ ----- step3: match
    # 遍历coord1, 找到coord2中距离coord1中每个源最近的源的索引idx等信息
    idx, d2d, d3d = coord1.match_to_catalog_sky(coord2)
    sep_constraint = d2d < max_sep  # 条件满足则为True

    # 向cat1添加match信息
    cat1['idx'] = idx
    cat1['sep_constraint'] = sep_constraint
    cat1['d2d'] = d2d.to('arcsec').value  # 单位: 角秒

    # 设置cat2的索引列为id，用于merge
    cat2['idx'] = cat2.index

    # 合并两表(左边是cat1, 右边是match到的cat2)
    df_merge = pd.merge(left=cat1, right=cat2, on='idx')

    # 留下满足阈值条件的行
    matched_cat = df_merge.query("sep_constraint==True")

    # ^ ----- step4: 整理表格
    matched_cat.reset_index(inplace=True, drop=True)
    # 删除辅助列
    del matched_cat['idx']
    del matched_cat['sep_constraint']
    # 将距离d2d(unit: arcsec)移动到第1列
    ls_d2d = matched_cat['d2d']
    del matched_cat['d2d']
    matched_cat.insert(0, 'd2d', ls_d2d)

    return matched_cat