from src.config import WINDOW_SIZE
from src.data.loader import load_raw_data
from src.data.datapreprocessing import reshape_protein, extract_pssm, extract_labels, create_windows
from src.data.datapreprocessing import preprocess_dataset
import os




data = load_raw_data("cullpdb+profile_5926_filtered.npy")


###print("Full shape:", data.shape)
##print("One protein shape:", data[0].shape)
#print("One residue shape:", data[0][0].shape)

#protein = data[0].reshape(700, 57)

#print(protein.shape)
#print(protein[0])



# check slices
#print("AA part:", protein[0][:21])
#print("PSSM part:", protein[0][21:42])
#print("Label part:", protein[0][49:57])

protein = data[0]

p2d = reshape_protein(protein)
pssm = extract_pssm(p2d)
labels = extract_labels(p2d)

windows = create_windows(pssm)

print("PSSM shape:", pssm.shape)
print("Windows shape:", windows.shape)
print("Labels shape:", labels.shape)

X, Y = preprocess_dataset(data)

print("Final X:", X.shape)
print("Final Y:", Y.shape)






