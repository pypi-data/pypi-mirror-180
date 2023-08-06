from multimetricprog.cls.calc.halstead import MetricBaseCalcHalstead
from multimetricprog.cls.calc.maintenance import MetricBaseCalcMaintenanceIndex
from multimetricprog.cls.calc.pylint import MetricBaseCalcPylint
from multimetricprog.cls.calc.tiobe import MetricBaseCalcTIOBE
from multimetricprog.cls.metric.comments import MetricBaseComments
from multimetricprog.cls.metric.cyclomatic import MetricBaseCyclomaticComplexity
from multimetricprog.cls.metric.fanout import MetricBaseFanout
from multimetricprog.cls.metric.loc import MetricBaseLOC
from multimetricprog.cls.metric.operands import MetricBaseOperands
from multimetricprog.cls.metric.operators import MetricBaseOperator
from multimetricprog.cls.stats.stats import MetricBaseStatsAverage


def get_modules_metrics(args, **kwargs):
    return [
        MetricBaseComments(args, **kwargs),
        MetricBaseCyclomaticComplexity(args, **kwargs),
        MetricBaseFanout(args, **kwargs),
        MetricBaseLOC(args, **kwargs),
        MetricBaseOperands(args, **kwargs),
        MetricBaseOperator(args, **kwargs),
    ]


def get_modules_calculated(args, **kwargs):
    return [
        MetricBaseCalcHalstead(args, **kwargs),
        MetricBaseCalcMaintenanceIndex(args, **kwargs),
        MetricBaseCalcTIOBE(args, **kwargs),
        MetricBaseCalcPylint(args, **kwargs)
    ]


def get_modules_stats(args, **kwargs):
    return [
        MetricBaseStatsAverage(args, **kwargs)
    ]


def get_additional_parser_args(parser):
    parser.add_argument("--bugpredict",
                        choices=MetricBaseCalcHalstead.BUGPRED_METHOD.keys(),
                        default=MetricBaseCalcHalstead.BUGPRED_DEFAULT,
                        help="Method how to calculate the bug prediction",
                        dest="halstead_bug_predict_method")
    parser.add_argument("--maintindex",
                        choices=MetricBaseCalcMaintenanceIndex.MI_METHOD.keys(),
                        default=MetricBaseCalcMaintenanceIndex.MI_DEFAULT,
                        help="Method how to calculate the maintainability index",
                        dest="maintenance_index_calc_method")
