from ..utils import request, fileLoad
import json
from enum import IntEnum, unique

class IESLabPlanModel(object):
    _baseUri = 'api/ieslab-plan/taskmanager/getSimuLastTasks'

    def __init__(self, simulationId):
        self.simulationId = simulationId

    def _fetchItemData(self, url):
        '''
            获取当前算例的优化目标设置信息

            :return: enum 类型，代表经济性优化和环保性优化的类型
        '''
        r = request('GET',
                    url,
                    params={
                        "simuid": self.simulationId
                    })
        data = json.loads(r.text) 
        return data

    def GetOptimizationInfo(self):
        '''
            获取当前算例的优化目标设置信息

            :return: enum 类型，代表经济性优化和环保性优化的类型
        '''
        try:
            data = self._fetchItemData(self._baseUri)
            for e in OptimizationMode:
                if(e.value == data['data']['optimizationpara']['OptimizationMode']):
                    return e
                else:
                    pass
        except:
            return OptimizationMode['经济性']
        


    def SetOptimizationInfo(self, optType):
        '''
            设置当前算例的优化目标

            :param optType: enum 类型，代表经济性优化和环保性优化的类型
            :return: bool 类型，代表参数设置是否成功
        '''


@unique
class OptimizationMode(IntEnum):
    经济性  = 0
    环保性 = 1