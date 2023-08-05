from ..utils import request
import json

class IESLabEvaluationModel(object):
    _baseUri = ''
    _kindNameMap = {}
    _financialParasDefaultValues={}

    def __init__(self, simulationId):
        self.simulationId = simulationId

    def _saveItemData(self, url, data): 
        r = request('POST', url, data=json.dumps(data))
        dataList = json.loads(r.text)
        return dataList

    def _fetchItemData(self, url, planID):
        '''
            获取planID对应的优化方案下财务评估模块的基础信息
            :param planID int类型，表示优化方案的ID，数值位于0~优化方案数量之间

            :return: dict 类型，为源数据的引用，代表方案对应的财务评价基础参数信息
        '''
        r = request('GET',
                    url,
                    params={
                        "simu_id": self.simulationId,
                        "planId": planID,
                    })
        data = json.loads(r.text) 
        return data

    def GetFinancialParas(self, planID):
        '''
            获取planID对应的优化方案下财务评估模块的基础信息
            :param planID int类型，表示优化方案的ID，数值位于0~优化方案数量之间

            :return: dict 类型，为源数据的引用，代表方案对应的财务评价基础参数信息
        '''
        dict_result = dict()
        for k,v in self._kindNameMap.items():
            kind = self._kindNameMap.get(k, k)
            url = self._baseUri + kind + '/'
            list = self._fetchItemData(url, planID) 
            if(len(list['results']) == 0):
                data = {
                    "simu": self.simulationId,
                    "planId": planID,
                }
                if(k in self._financialParasDefaultValues):
                    data.update(self._financialParasDefaultValues[k])
                    res = self._saveItemData(url, data)
                    dict_result[v] = res
                else:
                    pass
            else:
                dict_result[v] = list['results']
        return dict_result

class IESLabEvaluationModelType(IESLabEvaluationModel):
    _baseUri = 'api/ieslab-plan/rest/'
    _kindNameMap = {
        "投资组成": "investmentbanchandproportion",
        "资金来源": "capitalsource",
        "资产形式": "assetformation",
        "生产成本": "productioncost",
        "流动资金及财务费用": "workingcapitalandfinancialexpenses",
        "税率及附加": "projectcalculation",
    }
    pass

    # 财务评价基础参数接口默认值
    _financialParasDefaultValues = {
        "资产形式": {
            "fixedAssetsRatio": "95",
            "residualRrate": "5",
            "depreciationPeriod": "15",
            "reimbursementPeriod": "5"
        },
        "生产成本": {
            'annualSalary': "8",
            'capacity': "4",
            'insuranceRate': "0.25",
            'materialsExpenses': "5.0",
            'otherExpenses': "1.0",
            'welfareFactor': "0"
        },
        "流动资金及财务费用": {
            "annualAPCirculationTimes": "12",
            "annualARCirculationTimes": "12",
            "annualCashCirculationTimes": "12",
            "annualStockCirculationTimes": "12",
            "interestRateAndWorkingCapital": "4",
            "workingCapitalLoanRatio": "70"
        },
        "税率及附加": {
            "aleatoricAccumulationFundRate": "0",
            "basicDiscountRate": "8",
            "cityMaintenanceConstructionTaxTate": "5",
            "corporateIncomeTaxRate": "25",
            "educationFeePlus": "5",
            "electricityVATRate": "18",
            "fuelBoughtVATRate": "10",
            "hotColdVATRate": "12",
            "legalAccumulationFundRate": "10",
            "localEducationPlus": "2",
            "materialBoughtVATRate": "17",
            "steamSaleVATRate": "12"
        }
    }