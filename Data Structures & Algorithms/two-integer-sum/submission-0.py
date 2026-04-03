class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numeros_vistos = {}
        
        for indice, numero_actual in enumerate(nums):
            complemento = target - numero_actual
            
            if complemento in numeros_vistos:
                return [numeros_vistos[complemento], indice]
                
            numeros_vistos[numero_actual] = indice
            
        return []