import pickle 
import torch


pkl = "dataset/1ake.pkl"
fasta = "dataset/1ake.fasta"
pkl_data = pickle.load(open(pkl, "rb"))
# print(pkl_data)
if "representations" in pkl_data:
    pkl_data = pkl_data["representations"]
    single_repr = torch.from_numpy(pkl_data["single"]).float()
    # print(pkl_data['single'])
    # print(type(pkl_data['single']))
    print(pkl_data['single'].shape)
    # print(pkl_data['pair'])
    # print(type(pkl_data['pair']))
    print(pkl_data['pair'].shape) 

seq = open(fasta, "r").readlines()[1].strip()
print(seq)
assert len(seq) == single_repr.shape[0]