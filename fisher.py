
#########add this at line 82!!!!######################
train_a_labels=np.array(train_a_labels)
train_a_labels0 = np.where(train_a_labels>0) 
train_a_labels1 = np.where(train_a_labels<1) 
###########
train_a_labels0=np.array(train_a_labels0)
############
Fisher=[]
train_data0 = np.delete(train_data, train_a_labels0, axis=0)
train_data1= np.delete(train_data, train_a_labels1, axis=0)

mean_train_data0=np.mean(train_data0,axis=0)
mean_train_data1=np.mean(train_data1,axis=0)

std_train_data0=np.std(train_data0)
std_train_data1=np.std(train_data1)
std_sum=(std_train_data1)*(std_train_data1)+std_train_data0*std_train_data0


Fisher=(mean_train_data0-mean_train_data1)/std_sum
Fisher=np.array(Fisher)
print(Fisher.shape)

#sort the fisher from small to large

feature_idx=np.arange(212)
Fisher_sorted = np.array(Fisher).argsort()
#####################################################
sorted_feature_idx = feature_idx[Fisher_sorted[::-1]]
#####################################################
