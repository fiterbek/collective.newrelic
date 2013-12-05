__import__('pkg_resources').declare_namespace(__name__)

import newrelic.agent

#Patch newrelic_application to work with a threading.local for early (own thread!) lock checking
# import newrelic_application
import newrelic_transaction

# This is one is required: it creates the 'webtransaction'
import zserverpublisher

# Enable/disable as you like
import zpublisher_mapply

import transformchains

import zope_event

import catalog_tool

import talinterpreter

import cron4plone

import Globals

import os

from collective.newrelic.utils import logger 


try:
# if the environment var was set, use this instead of the default (local) newrelic ini file
    config_file = os.environ.get('NEW_RELIC_CONFIG_FILE')
    if config_file is None:
        config_file = 'newrelic.ini'     

    if Globals.DevelopmentMode:
        newrelic.agent.initialize(config_file, 'development')
    else:
        newrelic.agent.initialize(config_file, 'staging')
    logger.info('New Relic Python Agent configuration set from %s.' % config_file)
except:
    pass
