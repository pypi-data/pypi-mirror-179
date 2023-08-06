# found module but no type hints or library stubs
from typing import Any
from typing import Dict
from typing import Optional

import pandas as pd  # type:ignore

from pandas_estat.appid import get_appid
from pandas_estat.base import BaseReader


def read_statsdata(
    code: str,
    limit: Optional[int] = None,
    start_position: Optional[int] = None,
    lang: str = "J",
    appid: Optional[str] = None,
    version: str = "3.0",
    **kwargs
) -> pd.DataFrame:
    """統計データを取得します。

    Args:
        code (str): 統計表 ID です。
            統計表情報 (:func:`read_statslist`) から検索できます。
            e-Stat API の ``statsDataId`` に相当します。
        limit (int, optional): データの取得行数を指定して下さい。
            省略時は 10 万件です。
            データ件数が指定した limit 値より少ない場合、全件を取得します。
            データ件数が指定した limit 値より多い場合（継続データが存在する）は、
            受信したデータの ``<NEXT_KEY>`` タグに継続データの開始行が設定されます。
            e-Stat API の ``limit`` に対応します。
        start_position (int, optional): データの取得行数を指定して下さい。
            省略時は 10 万件です。
            データ件数が指定した limit 値より少ない場合、全件を取得します。
            データ件数が指定した limit 値より多い場合（継続データが存在する）は、
            受信したデータの ``<NEXT_KEY>`` タグに継続データの開始行が設定されます。
            e-Stat API の ``startPosition`` に対応します。
        lang ({"J", "E"}, default "J"): 取得するデータの言語です。
            ``"J"`` （日本語）または ``"E"`` （英語）で指定してください。
            e-Stat API の ``lang`` に対応します。
        appid (str, optional): アプリケーション ID です。
            指定しない場合、:func:`set_appid` で指定した値か、
            環境変数 ``ESTAT_APPID`` を用います。
            e-Stat API の ``appId`` に対応します。
        version (str, default "3.0"): API 仕様バージョンです。
            （参考: https://www.e-stat.go.jp/api/api-info/api-spec）
        **kwargs: e-Stat API から取得した CSV データをパースする
            :func:`pandas.read_csv` に与えるパラメータです。

    Returns:
        pandas.DataFrame
    """
    reader = StatsDataReader(
        code,
        limit=limit,
        start_position=start_position,
        lang=lang,
        appid=appid,
        version=version,
    )
    dataframe = reader.read(**kwargs)
    return dataframe


class StatsDataReader(BaseReader):
    """統計データを取得します。

    Args:
        code (str): 統計表 ID です。
            統計表情報 (:func:`read_statslist`) から検索できます。
            e-Stat API の ``statsDataId`` に相当します。
        limit (int, optional): データの取得行数を指定して下さい。
            省略時は 10 万件です。
            データ件数が指定した limit 値より少ない場合、全件を取得します。
            データ件数が指定した limit 値より多い場合（継続データが存在する）は、
            受信したデータの ``<NEXT_KEY>`` タグに継続データの開始行が設定されます。
            e-Stat API の ``limit`` に対応します。
        start_position (int, optional): データの取得行数を指定して下さい。
            省略時は 10 万件です。
            データ件数が指定した limit 値より少ない場合、全件を取得します。
            データ件数が指定した limit 値より多い場合（継続データが存在する）は、
            受信したデータの ``<NEXT_KEY>`` タグに継続データの開始行が設定されます。
            e-Stat API の ``startPosition`` に対応します。
        lang ({"J", "E"}, default "J"): 取得するデータの言語です。
            ``"J"`` （日本語）または ``"E"`` （英語）で指定してください。
            e-Stat API の ``lang`` に対応します。
        appid (str, optional): アプリケーション ID です。
            指定しない場合、:func:`set_appid` で指定した値か、
            環境変数 ``ESTAT_APPID`` を用います。
            e-Stat API の ``appId`` に対応します。
        version (str, default "3.0"): API 仕様バージョンです。
            （参考: https://www.e-stat.go.jp/api/api-info/api-spec）
    """

    QUERY = "getSimpleStatsData"
    TABLE_TAG = "VALUE"

    def __init__(
        self,
        code: str,
        limit: Optional[int] = None,
        start_position: Optional[int] = None,
        lang: str = "J",
        appid: Optional[str] = None,
        version: str = "3.0",
    ) -> None:
        self.code = code
        self.limit = limit
        self.start_position = start_position
        self.lang = lang
        self.appid = get_appid(appid)
        self.version = version

        if self.appid is None:
            raise ValueError("アプリケーション ID が指定されていません。")
        if not isinstance(code, str):
            raise ValueError("統計表 ID は str 型で指定してください。")

        if lang == "E":
            raise NotImplementedError
        if lang not in ("J", "E"):
            raise ValueError('言語 lang は "J" か "E" で指定してください。')

    @property
    def params(self) -> dict:
        """e-Stat API のパラメータ群を `dict` 形式で返します。
        参照: e-Stat API v3.0 仕様 2.3 API の利用方法 - 統計データ取得
        参照: e-Stat API v3.0 仕様 3.4 API パラメータ - 統計データ取得

        Returns:
            dict
        """
        params: Dict[str, Any] = {"appId": self.appid, "statsDataId": self.code}

        if self.limit is not None:
            params["limit"] = self.limit
        if self.start_position is not None:
            params["startPosition"] = self.start_position
        if self.lang is not None:
            params["lang"] = self.lang

        return params
