StampDuty = 0.001
ChangeUser = 2 / 100000


def calc_trade_info(buy_price, now_price, hold_volume, add_volume):
    buy_cost = now_price * hold_volume * 0.003
    if buy_cost < 5:
        buy_cost = 5
    history_cost = buy_price * hold_volume + buy_cost
    add_cost = add_volume * now_price * 0.003
    if add_cost < 5:
        add_cost = 5
    now_per_cost = (add_volume * now_price + history_cost + add_cost) / (add_volume + hold_volume)
    print("补仓股数：{}, 成本变为：{}".format(add_volume, now_per_cost))
    calc_sale_profit(buy_price, add_volume + hold_volume)


def calc_sale_profit(sale_price, sale_volume):
    profit = sale_price * sale_volume
    sale_cost = profit * 0.003
    if sale_cost < 5:
        sale_cost = 5
    net_profit = sale_price * sale_volume - expect_price * sale_volume - sale_cost
    print("以：{} 每股, 卖出：{} 股, 收益：沪深A股：{}, 其他：{}".format(sale_price, sale_volume, net_profit - profit * ChangeUser,
                                                       net_profit))


if __name__ == '__main__':
    buy_price = 0
    now_price = 0
    hold_volume = 0
    add_volume = 100
    calc_trade_info(buy_price=buy_price, now_price=now_price, hold_volume=hold_volume, add_volume=add_volume)
    expect_price = 0
    sale_volume = hold_volume + add_volume
    calc_sale_profit(sale_price=expect_price, sale_volume=sale_volume)
