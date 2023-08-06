#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import time

from decentra_network.blockchain.block.block_main import Block
from decentra_network.lib.log import get_logger

logger = get_logger("CONSENSUS_FIRST_ROUND")


def time_difference_check(block: Block, return_result=False) -> bool:

    the_time = block.start_time + block.round_1_time
    current_time = int(time.time())
    logger.info("Round 1 time control started")
    logger.debug(f"current_time: {current_time}")
    logger.debug(f"the_time: {the_time}")
    if current_time >= the_time:
        logger.info("Time is true")
        return True
    else:
        logger.info("Time is not true")
        return False if return_result is False else the_time
