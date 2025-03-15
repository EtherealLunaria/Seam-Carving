import sys
import imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

class Picture:
    def __init__(self, path):
        self.img = imageio.v3.imread(path)
        self.original_img = self.img.copy()
        self.height = self.img.shape[0]
        self.width = self.img.shape[1]
        self.backtrace_map = None
        self.energy_map = None
        self.min_seem = -1

    def calc_energy(self):
        filter_dx = np.array([
            [1.0, 2.0, 1.0],
            [0.0, 0.0, 0.0],
            [-1.0, -2.0, -1.0],
        ])
        filter_dx = np.stack([filter_dx] * 3, axis=2)

        filter_dy = np.array([
            [1.0, 0.0, -1.0],
            [2.0, 0.0, -2.0],
            [1.0, 0.0, -1.0],
        ])
        filter_dy = np.stack([filter_dy] * 3, axis=2)

        img=self.img.copy()
        img = img.astype('float32')
        convolved = np.absolute(convolve(img, filter_dx)) + np.absolute(convolve(img, filter_dy))

        self.energy_map = convolved.sum(axis=2)
        del img
        del convolved

    def search_min_seam(self):
        self.calc_energy()
        M = self.energy_map.copy()
        self.backtrack = np.zeros_like(M, dtype=np.int32)
        for i in range(1, self.height):
            for j in range(0, self.width):
                if j == 0:
                    idx = np.argmin(M[i-1, j:j + 2])
                    self.backtrack[i, j] = idx + j
                    min_energy = M[i-1, idx + j]
                elif j == self.width - 1:
                    idx = np.argmin(M[i-1, j-1:j + 1])
                    self.backtrack[i, j] = idx + j - 1
                    min_energy = M[i-1, idx + j - 1]
                else:
                    idx = np.argmin(M[i - 1, j - 1:j + 2])
                    self.backtrack[i, j] = idx + j - 1
                    min_energy = M[i - 1, idx + j - 1]
                M[i, j] += min_energy
        self.min_seem=np.argmin(M[-1])
        del M

    def remove_min_seam(self):
        self.search_min_seam()
        mask = np.ones((self.height, self.width), dtype=bool)
        j=self.min_seem
        for i in reversed(range(self.height)):
            mask[i, j] = False
            j = self.backtrack[i, j]

        mask = np.stack([mask] * 3, axis=2)
        self.img = self.img[mask].reshape((self.height, self.width - 1, 3))
        self.width -= 1

        del mask
        del j

    def crop_w(self, width):
        cropped_w = self.width - width
        for _ in range(cropped_w):
            self.remove_min_seam()

    def crop_h(self, height):
        cropped_h = self.height - height
        self.img = np.rot90(self.img, 1, (0, 1))
        self.height, self.width = self.width, self.height
        for _ in range(cropped_h):
            self.remove_min_seam()
        self.img = np.rot90(self.img, 3, (0, 1))
        self.height, self.width = self.width, self.height

    def show(self):
        plt.subplot(1, 2, 1)
        plt.imshow(self.original_img)
        plt.title('Original Image')
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(self.img)
        plt.title('Seam Carving')
        plt.axis('off')

        plt.show()

if __name__ == '__main__':
    pass