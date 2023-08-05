# coding :utf-8
#
# The MIT License (MIT)
#
# Copyright (c) 2021-2029 XuHaiJiang/QFF
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
    策略回测环境实现模块
"""

import threading
import os
import sys

from qff.frame.interface import set_run_freq, set_init_cash, set_backtest_period, load_strategy_file
from qff.frame.settle import settle_by_day, profit_analyse
from qff.frame.order import order_broker
from qff.frame.context import context, strategy, RUNSTATUS, RUNTYPE, run_strategy_funcs
from qff.frame.backup import save_context
from qff.frame.cli import CLI
from qff.tools.date import get_trade_days, get_trade_min_list, get_pre_trade_day
from qff.price.query import get_price
from qff.tools.logs import log


def back_test_run(strategy_file, resume=False):
    """
    回测框架运行函数,执行该函数将运行回测过程
    Parameters
    ----------
    strategy_file:策略文件,策略文件中至少包含initialize()函数
    resume:是否为恢复以前中断的策略，默认全新开始,该参数在__main__.py文件中使用

    Returns
    -------
    无返回值

    Examples
    --------
    一般在策略文件的尾部使用以下语句，已启动策略的回测。

    if __name__ == '__main__':
        back_test_run(__file__)

    """

    context.run_type = RUNTYPE.BACK_TEST

    if context.status == RUNSTATUS.RUNNING:
        log.error('回测函数已运行！')
        return
    else:
        context.status = RUNSTATUS.RUNNING

    # module = sys.argv[0] if strategy_file is None else strategy_file
    if not load_strategy_file(strategy_file):
        log.error("策略文件载入失败或缺少初始化函数initialize！***")
        return

    if resume:
        if strategy.process_initialize is not None:
            strategy.process_initialize()
    else:
        strategy.initialize()

    if context.strategy_name is None:
        context.strategy_name = os.path.basename(sys.argv[0]).split('.')[0]
    if context.run_freq is None:
        set_run_freq()
    if context.start_date is None or context.end_date is None:
        set_backtest_period()
    if context.portfolio is None:
        set_init_cash()
    if context.run_freq == 'tick':
        log.error("回测模式不支持tick运行频率!")
        return

    context.bm_data = get_price(context.benchmark,
                                start=get_pre_trade_day(context.start_date),
                                end=context.end_date,
                                market='index')
    context.bm_start = context.bm_data.iloc[0].close
    sim_thread = threading.Thread(target=_back_test_run)
    sim_thread.setDaemon(True)
    # 运行命令行环境...
    cli = CLI()
    sim_thread.start()
    cli.cmdloop()
    log.warning("命令行交互环境退出...")
    sim_thread.join()
    log.warning("回测框架运行结束！")


def _back_test_run():
    days = get_trade_days(context.current_dt[0:10], context.end_date)  # 回测中断恢复时可继续运行
    for day in days:
        if context.status != RUNSTATUS.RUNNING:
            break
        if strategy.before_trading_start is not None:
            context.current_dt = day + " 09:00:00"
            run_strategy_funcs(strategy.before_trading_start)

        # 判断是否跳过当天
        if context.pass_today:
            context.pass_today = False
        else:
            if context.run_freq == 'day':
                # 执行每日策略函数
                if strategy.handle_data is not None:
                    context.current_dt = day + " 09:31:00"  # 分钟第一条数据时间
                    run_strategy_funcs(strategy.handle_data)

                if len(strategy.run_daily) > 0:
                    run_times = list(strategy.run_daily.keys())
                    run_times.sort()
                    for rt in run_times:                    # 目前还不支持非交易时间的函数
                        context.current_dt = day + " " + rt
                        run_strategy_funcs(strategy.run_daily[rt])

            elif context.run_freq == "min":
                # 生成交易时间分钟列表
                min_list = get_trade_min_list(day)
                for context.current_dt in min_list:
                    # 执行分钟策略函数
                    if strategy.handle_data is not None:
                        run_strategy_funcs(strategy.handle_data)
                    # 查找是否有定时执行的策略
                    if str(context.current_dt)[11:] in strategy.run_daily.keys():
                        run_strategy_funcs(strategy.run_daily[str(context.current_dt)[11:]])

                    # 订单撮合 order_broker
                    order_broker()

                    # 跳过当天
                    if context.pass_today:
                        context.pass_today = False
                        break

        if strategy.after_trading_end is not None:
            context.current_dt = day + " 15:30:00"
            run_strategy_funcs(strategy.after_trading_end)

        # 每日收盘处理函数
        context.current_dt = day + " 16:00:00"
        settle_by_day()
        log.info("##################### 一天结束 ######################")
        log.info("")

    if context.status == RUNSTATUS.PAUSED:
        log.warning("_back_test_run回测运行暂停，保存过程数据...!")
        save_context()
    elif context.status == RUNSTATUS.CANCELED:
        log.warning("_back_test_run回测执行取消...!")
    else:
        context.status = RUNSTATUS.DONE
        if strategy.on_strategy_end is not None:
            strategy.on_strategy_end()
        if context.status == RUNSTATUS.DONE:
            profit_analyse()
        # log.error("回测运行完成!，执行quit退出交互环境后进行回测数据分析")
        log.info("_back_test_run回测线程运行完成!")
