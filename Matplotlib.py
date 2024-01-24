import matplotlib.pyplot as plt

y = [99,70,97,66,23,44]
x = ["Part1","Part2","Part3","Part4","Part5","Part6"]
colors = ["red","green","orange","blue","yellow","red"]



# plt.bar(x,y,color = "orange")
# plt.bar(x,y,color = colors,)
plt.bar(x,y,color = colors,edgecolor="black")
plt.xlabel("Parts of Harry Potter ",fontsize = 18)
plt.ylabel("Popularity",fontsize = 18)
plt.title("Popularity of Harry Potter",fontsize = 18)
plt.show()