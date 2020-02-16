StampDuty = 0.001
Commission = 0.003
ChangeUser = 2 / 100000


def calc_trade_info(buy_price, now_price, hold_volume, add_volume):
    buy_cost = now_price * hold_volume * Commission
    if buy_cost < 5:
        buy_cost = 5
    history_cost = buy_price * hold_volume + buy_cost
    add_cost = add_volume * now_price * Commission
    if add_cost < 5:
        add_cost = 5
    added_volume_value = add_volume * now_price + history_cost + add_cost
    now_per_cost = added_volume_value / (add_volume + hold_volume)
    print("补仓股数：{}, 成本变为：{}".format(add_volume, now_per_cost))
    calc_sale_profit(buy_price, add_volume + hold_volume, now_per_cost)


def calc_sale_profit(sale_price, sale_volume, now_per_cost):
    hold_value = now_per_cost * sale_volume
    profit = sale_price * sale_volume
    sale_cost = profit * (StampDuty + Commission)
    if sale_cost < 5:
        sale_cost = 5
    net_profit = sale_price * sale_volume - hold_value - sale_cost
    if net_profit == 0:
        print("交易后：收支平衡")
    elif net_profit > 0:
        print("交易后：盈利")
    else:
        print("交易后：赔本")
    print("以：{}元/股, 卖出：{} 股, 收益：沪深A股：{}, 其他：{}".format(sale_price, sale_volume, net_profit - profit * ChangeUser,
                                                       net_profit))


if __name__ == '__main__':
    buy_price = 5
    now_price = 4
    hold_volume = 100
    add_volume = 100
    print("======加仓成本=========")
    calc_trade_info(buy_price=buy_price, now_price=now_price, hold_volume=hold_volume, add_volume=add_volume)
    expect_price = 4.6
    per_cost = 4.55
    short_sale = hold_volume + add_volume
    sale_volume = 90
    print("======沽空=========")
    calc_sale_profit(sale_price=expect_price, sale_volume=short_sale, now_per_cost=per_cost)
    print("======卖出一定量=========")
    calc_sale_profit(sale_price=expect_price, sale_volume=sale_volume, now_per_cost=per_cost)
