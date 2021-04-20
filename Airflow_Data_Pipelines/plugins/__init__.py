from __future__ import division, absolute_import, print_function

from airflow.plugins_manager import AirflowPlugin

import operators
import helpers

# define the plugin case
class Plugin(AirflowPlugin):
    name = "plugin"
    operators = [
                    operators.CreateTableOperator,
                    operators.StageToRedShiftOperator,
                    operators.LoadFactOperator,
                    operators.LoadDimensionOperator,
                    operators.DataQualityOperator
    ]
    helpers = [
                helpers.SqlQueries
    ]