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

# 实盘模拟实现
# 1、设计一个线程对象，1秒钟执行一次，判断时间运行策略函数
# 2、主程序设计成一个命令行，可接受指令，输出实盘过程中的信息和数据分析


import threading
import os
import sys
import pandas as pd
from time import sleep
from qff.frame.context import context, strategy, RUNSTATUS, RUNTYPE, run_strategy_funcs
from qff.frame.backup import save_context
from qff.frame.order import order_broker
from qff.frame.settle import settle_by_day, profit_analyse
from qff.frame.cli import CLI
from qff.tools.date import is_trade_day
from qff.price.fetch import fetch_current_ticks
from qff.frame.interface import set_run_freq, set_init_cash, set_backtest_period, load_strategy_file
from qff.tools.logs import log


def sim_trade_run(strategy_file=None, resume=False):
    """
    实盘模拟框架运行函数,执行该函数将运行策略实盘模拟
    使用方法：一般在策略文件中的尾部
            if __name__ == '__main__':
                back_test_run(__file__)
    :param strategy_file 策略文件,策略文件中至少包含initialize()函数
    :param resume: 是否为恢复以前中断的策略，默认全新开始,该参数在__main__.py文件中使用
    :return: None
    """
    context.run_type = RUNTYPE.SIM_TRADE

    if context.status == RUNSTATUS.RUNNING:
        log.error('实盘模拟框架函数已运行！')
        return
    else:
        context.status = RUNSTATUS.RUNNING

    module = sys.argv[0] if strategy_file is None else strategy_file
    if not load_strategy_file(module):
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

    # 恢复运行时不能设置
    if context.bm_start is None:
        context.start_date = pd.Timestamp.now().strftime('%Y-%m-%d')
        context.bm_start = fetch_current_ticks(context.benchmark, market='index')['price']

    sim_thread = threading.Thread(target=_sim_trade_run)
    sim_thread.setDaemon(True)   # 主线程A一旦执行结束，不管子线程B是否执行完成，会全部被终止。
    sim_thread.start()
    # 运行命令行环境...
    cli = CLI()
    cli.cmdloop()
    # sim_thread.join()  # 主线程等待子线程执行完成
    log.warning("实盘模拟框架运行结束！")


def _sim_trade_run():
    while context.status == RUNSTATUS.RUNNING:
        _time = pd.Timestamp.now()
        stime = _time.strftime('%Y-%m-%d %H:%M:%S')
        if is_trade_day(stime[0:10]):
            # 固定时间点的策略函数
            # 移到此处（1）能够保证sleep后能够匹配到；（2）可以设置任意时间点运行的函数
            if stime[11:] in strategy.run_daily.keys():
                run_strategy_funcs(strategy.run_daily[stime[11:]])

            if stime[11:16] == '09:00':
                if strategy.before_trading_start is not None:
                    run_strategy_funcs(strategy.before_trading_start)
                sleep((_time.ceil(freq="1min") - pd.Timestamp.now()).total_seconds())
            elif '09:30' <= stime[11:16] <= '11:30' or '13:00' <= stime[11:16] <= '15:00':
                # # 固定时间点的策略函数
                # if stime[11:] in strategy.run_daily.keys():
                #     strategy.run_daily[stime[11:]]()
                # 按策略频率运行的策略函数
                if strategy.handle_data is not None:
                    run_strategy_funcs(strategy.handle_data)

                # 订单撮合 order_broker
                order_broker()

                _freq = "1min" if context.run_freq == 'min' else '3s'     # 3s是为了tick频率运行
                _t = pd.Timestamp.now()
                sleep((_t.ceil(freq=_freq) - _t).total_seconds())         # 考虑前面运行超过_freq，造成sleep负数
                # sleep((pd.Timestamp.now().ceil(freq='3s') - pd.Timestamp.now()).total_seconds())

            elif stime[11:16] == '15:30':
                if strategy.after_trading_end is not None:
                    run_strategy_funcs(strategy.after_trading_end)

                settle_by_day()
                profit_analyse()
                save_context()
                log.info("##################### 一天结束 ######################")
                log.info("")

                sleep((_time.ceil(freq="1min") - pd.Timestamp.now()).total_seconds())
            else:
                sleep((_time.ceil(freq="1min") - pd.Timestamp.now()).total_seconds())
        else:
            sleep(60)
    if context.status == RUNSTATUS.PAUSED:
        log.warning("回测运行暂停，保存过程数据...!")
        save_context()
    elif context.status == RUNSTATUS.CANCELED:
        log.warning("回测执行取消...!")
