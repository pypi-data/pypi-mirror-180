# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: bidofferv3.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .google import type


class BidOfferV3BidAskFlag(betterproto.Enum):
    UNDEFINED_FLAG = 0
    NORMAL = 1
    ATO = 2
    ATC = 3


@dataclass
class BidOfferV3(betterproto.Message):
    """
    Topic: proto/topic/bidofferv3/<symbol> Today's price and volume of top ten
    bids/offers
    """

    # Subscribed symbol
    symbol: str = betterproto.string_field(1)
    # Bid flag
    bid_flag: "BidOfferV3BidAskFlag" = betterproto.enum_field(22)
    # Offer flag
    ask_flag: "BidOfferV3BidAskFlag" = betterproto.enum_field(23)
    # 1st bid price Price equals to zero during ATO/ATC
    bid_price1: type.Money = betterproto.message_field(2)
    # 2nd bid price
    bid_price2: type.Money = betterproto.message_field(3)
    # 3rd bid price
    bid_price3: type.Money = betterproto.message_field(4)
    # 4th bid price
    bid_price4: type.Money = betterproto.message_field(5)
    # 5th bid price
    bid_price5: type.Money = betterproto.message_field(6)
    # 6th bid price
    bid_price6: type.Money = betterproto.message_field(24)
    # 7th bid price
    bid_price7: type.Money = betterproto.message_field(25)
    # 8th bid price
    bid_price8: type.Money = betterproto.message_field(26)
    # 9th bid price
    bid_price9: type.Money = betterproto.message_field(27)
    # 10th bid price
    bid_price10: type.Money = betterproto.message_field(28)
    # 1st ask price Price equals to zero during ATO/ATC
    ask_price1: type.Money = betterproto.message_field(7)
    # 2nd ask price
    ask_price2: type.Money = betterproto.message_field(8)
    # 3rd ask price
    ask_price3: type.Money = betterproto.message_field(9)
    # 4th ask price
    ask_price4: type.Money = betterproto.message_field(10)
    # 5th ask price
    ask_price5: type.Money = betterproto.message_field(11)
    # 6th ask price
    ask_price6: type.Money = betterproto.message_field(29)
    # 7th ask price
    ask_price7: type.Money = betterproto.message_field(30)
    # 8th ask price
    ask_price8: type.Money = betterproto.message_field(31)
    # 9th ask price
    ask_price9: type.Money = betterproto.message_field(32)
    # 10th ask price
    ask_price10: type.Money = betterproto.message_field(33)
    # 1st bid volume
    bid_volume1: int = betterproto.int64_field(12)
    # 2nd bid volume
    bid_volume2: int = betterproto.int64_field(13)
    # 3rd bid volume
    bid_volume3: int = betterproto.int64_field(14)
    # 4th bid volume
    bid_volume4: int = betterproto.int64_field(15)
    # 5th bid volume
    bid_volume5: int = betterproto.int64_field(16)
    # 6th bid volume
    bid_volume6: int = betterproto.int64_field(34)
    # 7th bid volume
    bid_volume7: int = betterproto.int64_field(35)
    # 8th bid volume
    bid_volume8: int = betterproto.int64_field(36)
    # 9th bid volume
    bid_volume9: int = betterproto.int64_field(37)
    # 10th bid volume
    bid_volume10: int = betterproto.int64_field(38)
    # 1st ask volume
    ask_volume1: int = betterproto.int64_field(17)
    # 2nd ask volume
    ask_volume2: int = betterproto.int64_field(18)
    # 3rd ask volume
    ask_volume3: int = betterproto.int64_field(19)
    # 4th ask volume
    ask_volume4: int = betterproto.int64_field(20)
    # 5th ask volume
    ask_volume5: int = betterproto.int64_field(21)
    # 6th ask volume
    ask_volume6: int = betterproto.int64_field(39)
    # 7th ask volume
    ask_volume7: int = betterproto.int64_field(40)
    # 8th ask volume
    ask_volume8: int = betterproto.int64_field(41)
    # 9th ask volume
    ask_volume9: int = betterproto.int64_field(42)
    # 10th ask volume
    ask_volume10: int = betterproto.int64_field(43)
