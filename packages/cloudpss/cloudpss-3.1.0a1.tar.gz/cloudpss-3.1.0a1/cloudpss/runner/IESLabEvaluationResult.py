
import json
from ..utils.httprequests import request

class IESLabEvaluationResult(object):
    _baseUri=""
    _kindNameMap={}

    def __init__(self,simulationId) -> None:
        self.simulationId=simulationId

    def _fetchItemData(self, url, planID):
        '''
            获取planID对应的优化方案下resultType财务评估结果

            :param planID int 类型，表示优化方案的ID，数值位于0~优化方案数量之间
            :param resultType enum 类型，表示财务评价结果表格的类型

            :return: dict 类型，为源数据的引用，代表方案对应的财务评价基础参数信息
        '''
        r = request('GET',
                    url,
                    params={
                        "simu_id": self.simulationId,
                        "planId": planID,
                        "time": 0
                    })
        data = json.loads(r.text)
        return data

    def GetFinancialResult(self, planID, resultType):
        '''
            获取planID对应的优化方案下resultType财务评估结果

            :param planID int 类型，表示优化方案的ID，数值位于0~优化方案数量之间
            :param resultType enum 类型，表示财务评价结果表格的类型

            :return: dict 类型，为源数据的引用，代表方案对应的财务评价基础参数信息

        '''
        assert (resultType in self._kindNameMap), "数据类型不存在"
        kind = self._kindNameMap.get(resultType, resultType)
        url = self._baseUri + kind
        list = self._fetchItemData(url, planID)
        dict_result = dict()
        for val in list['results']:
            for k,v in val.items():
                dict_result[k]=v
        return dict_result


class IESLabEvaluationResultType(IESLabEvaluationResult):
    _baseUri = 'api/ieslab-plan/taskmanager/'
    _kindNameMap = {
        "利润与利润分配": "getEconomyResult",
        "财务计划现金": "getFinancialPlanCashFlowResult",
        "资产负债": "getLiabilityAssetsResult",
        "投资使用计划与资金筹措": "getInvestPlanDataResult",
        "借款还本付息计划": "getLoanRepaymentPlanResult",
        "流动资金估算": "getFlowCashEvaluteResult",
        "资产折旧与摊销估算": "getFlowCashEvaluteResult",
        "总成本费用估算表": "getSumCostResult",
        "项目总投资现金流量": "getSumInvestFlowCashResult",
        "项目资本金现金流量": "getProjectCashFlowResult",
        "营业收入、税金、附加和增值税估算": "getIncomeTaxResult",
    }
    pass