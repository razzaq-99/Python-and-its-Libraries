import numpy as np

# l1 = [10,20,30]
# l2 = [40,50,60]

# print(l1+l2)


# arr1 = np.array([10,20,30])
# arr2 = np.array([40,50,60])


# print(arr1)
# print(arr2)
# print(arr1+arr2)
# print(arr1*arr2)

# arr3 = np.array([11,22,"33",44.0])
# print(arr3)

# arr4 = np.array([[1,2,3,4],[5,6,7,8]])

# print(arr4)

# arr5 = np.array([12,33,44,55,22])    #Slicing

# print(arr5[1:3])
# print(arr5[:2])
# print(arr5[0:])


# arr6 = np.array([[1,2,3,4],[5,6,7,8],[7,9,11,0]])
# arr7 = np.array([2])
# print(arr6[0:2,1:3])
# print(arr6[:4,:2])
# print(arr6[:4,:1])

# print(arr6[2,2])
# print(arr6[1,1])
# print(arr6[0,0])

# print(np.sum(arr6))
# print(np.shape(arr6))
# print(np.max(arr6))
# print(np.size(arr6))


# print(np.power(arr6,arr7))
# print(np.sqrt(arr6))




# arr8 = np.array([[11,22,33],[44,55,66]])
# arr9 = np.array([[12,23,31],[42,53,61]])

# print(np.concatenate([arr8,arr9]))              # Concatenate
# print(np.hstack([arr8,arr9]))                   # Horizontal Concatenate
# print(np.vstack([arr8,arr9]))                     # Vertical Concatenate



# arr = np.array([[12,34,55,66],[12,22,44,77]])

# print(np.array_split(arr,2))
# print(np.array_split(arr,3))
# print(np.array_split(arr,4))
# print(np.array_split(arr,5))
# print(np.array_split(arr,8))


# arr0 = np.array_split(arr,4)
# print(arr0[1])



# print(np.append(arr,0))                                # (array,value)
# print(np.append(arr,100))        
                      
# print(np.insert(arr,0,100,axis=1))                     # (array,index,value)
# print(np.insert(arr,0,[100,200],axis=1))                

# print(np.delete(arr,1))                                   # (array,index)
# print(np.delete(arr,0,axis=1))




# arr = np.array([20,40,60,80])

# print(np.sum(arr))
# print(np.cumsum(arr))                                   # Cumulative Sum
# print(np.size(arr))
# print(np.prod(arr))



# price = np.array([20,30,40])
# quantity = np.array([1,2,3])

# print(price,"\n",quantity)

# print()

# mul = np.cumprod([price,quantity],axis=0)                      # Cumulative Product
# print(mul)

# print()
# print(np.sum(mul))




# food_price = np.array([100,200,300,400,500,600,700,800,900])

# print(np.mean(food_price))
# print(np.median(food_price))
# print(np.std(food_price))


                                     # +1 is direct proportional relation
                                     # -1 is inversely proportional relation
                                     # 0 shows no relation
                                     
tabacco = np.array([10,30,50,40])
deaths = np.array([200,120,400,330])

print(np.corrcoef(tabacco,deaths))       
