from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class PlayerTrend:
    player_id: Optional[str]
    count: Optional[int]

    @staticmethod
    def from_dict(player_trend_dict: dict) -> PlayerTrend:
        return PlayerTrend(player_id=player_trend_dict.get("player_id", None),
                           count=player_trend_dict.get("count", None))

    @staticmethod
    def from_dict_list(player_trend_dict_list: dict) -> list[PlayerTrend]:
        player_trends = list()
        for player_trend_dict in player_trend_dict_list:
            player_trends.append(PlayerTrend.from_dict(player_trend_dict))
        return player_trends
