import numpy as np
import matplotlib.pyplot as plt

def plot_loss_epochs():

    mean_train_losses = [0.18647934, 0.30446067, 0.38610134, 0.43844506, 0.47100553, 0.5210056, 0.5476563, 0.5790953, 0.603125, 0.6251638, 0.6412298, 0.65821576, 0.6654486, 0.67144656, 0.6840474, 0.6918095, 0.7045237, 0.70267135, 0.7111895, 0.71762854, 0.71633065, 0.7282006, 0.73233366, 0.7297883, 0.73857105, 0.7405494, 0.73937756, 0.74609375, 0.7497732, 0.75287294, 0.7641885, 0.77139616, 0.7722404, 0.7753276, 0.77705395, 0.78345513, 0.7839088, 0.7870086, 0.787248, 0.7840978, 0.7899068, 0.78455144, 0.78647935, 0.7875756, 0.78658015, 0.79154485, 0.78721017, 0.79259074, 0.78775203, 0.7902848, 0.7918599, 0.7931704, 0.79334676, 0.7969128, 0.7937374, 0.79682463, 0.7987399, 0.7967238, 0.7977193, 0.80530494, 0.7995086, 0.79987395, 0.8061492, 0.80122226, 0.7983619, 0.7962197, 0.80036545, 0.7993448, 0.8020917, 0.79952115, 0.80530494, 0.797631, 0.79550153, 0.80220515, 0.79987395, 0.80220515, 0.80254537, 0.8055065, 0.8056703, 0.806376, 0.7986391, 0.7983367, 0.7982989, 0.8010585, 0.8015877, 0.80056703, 0.8038055, 0.80078125, 0.8017263, 0.8048387, 0.79992443, 0.8087071, 0.80059224, 0.8034778, 0.8033014, 0.8056956, 0.8022177, 0.7997228, 0.8020287, 0.8042213]

    mean_val_losses = [0.33121142, 0.47109696, 0.5235018, 0.6352559, 0.66253537, 0.66825813, 0.7269644, 0.7264982, 0.7636638, 0.7908629, 0.7840953, 0.7890143, 0.8089635, 0.79298484, 0.83294755, 0.80516976, 0.84937626, 0.8226756, 0.8312596, 0.8278678, 0.8556777, 0.85308963, 0.8244117, 0.82916987, 0.8716082, 0.8269193, 0.8378826, 0.82793206, 0.874373, 0.88615614, 0.8940168, 0.89634776, 0.9074878, 0.9070698, 0.9054302, 0.90523726, 0.90518904, 0.9158147, 0.9112011, 0.9163773, 0.91544497, 0.91880465, 0.9187725, 0.91856354, 0.9131141, 0.91616833, 0.92010677, 0.9177598, 0.920171, 0.92946243, 0.92222863, 0.9218268, 0.9252347, 0.92337, 0.9225341, 0.9189332, 0.92734057, 0.9229842, 0.9264725, 0.92023534, 0.91941553, 0.92406124, 0.9292856, 0.9274048, 0.9279835, 0.92293596, 0.92436665, 0.9250257, 0.92631173, 0.9245274, 0.92491317, 0.9270351, 0.9230324, 0.92865866, 0.9247203, 0.9256687, 0.92652076, 0.92726016, 0.92746913, 0.931086, 0.93160045, 0.9308128, 0.92486495, 0.9269065, 0.9244792, 0.9241577, 0.92833716, 0.92290384, 0.9292856, 0.9272441, 0.9238362, 0.9320506, 0.92660105, 0.93203443, 0.930009, 0.9259581, 0.9271316, 0.93044305, 0.9251061, 0.92457557]

    mean_train_losses = 1 - np.array(mean_train_losses)
    mean_val_losses = 1 - np.array(mean_val_losses)

    num_epochs = np.array([i for i in range(100)])

    plt.ylim([0, 1])
    plt.plot(num_epochs, mean_train_losses)
    plt.plot(num_epochs, mean_val_losses)

    plt.title('Train and validation loss vs number of epochs')
    plt.xlabel('Number of epochs trained')
    plt.ylabel('Loss')
    plt.show()

plot_loss_epochs()