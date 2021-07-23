class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		moltiplicazione_da_sinistra = [nums[0]]
		for i in range(1,len(nums)):
			nuovo = moltiplicazione_da_sinistra[-1] * nums[i] 
			moltiplicazione_da_sinistra.append(nuovo)
 
		moltiplicazione_da_destra = [nums[-1]]
		for i in range(len(nums)-2,-1,-1):
			nuovo = moltiplicazione_da_destra [-1] * nums[i] 
			moltiplicazione_da_destra.append(nuovo)
 
	
		print(moltiplicazione_da_sinistra)
		print(moltiplicazione_da_destra)
		res = []
 
		for i in range(len(nums)):
			moltiplicazione=1
			if i!=0:
				moltiplicazione*= moltiplicazione_da_sinistra[i-1]
			if i!=len(nums)-1:
				moltiplicazione*= moltiplicazione_da_destra[len(nums)-i-2]
			res.append(moltiplicazione)
		return res


