__author__ = 'zeno'

from AVCommon.logger import logging
import time

from AVCommon import command

def execute(vm, protocol, vms):
    """ client side, returns (bool,*) """

    logging.debug("    VM %s" % str(vms))

    assert vm, "null vm"
    assert command.context is not None

    assert isinstance(vms, list), "VM expects a list"

    command.context["VM"] = vms

    logging.debug("items: %s" % (command.context))
    return True, vms