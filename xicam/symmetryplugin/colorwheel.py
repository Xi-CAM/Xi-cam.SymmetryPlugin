import colorsys
import math
from pathlib import Path

import numpy as np
from PIL import Image

from .utils import get_test_data_file


def build_color_wheel(nx, ny, sym):
    im = Image.new("RGB", (nx, ny))
    radius = min(im.size) / 2.0
    centre = im.size[0] / 2, im.size[1] / 2
    pix = im.load()
    for x in range(im.width):
        for y in range(im.height):
            rx = x - centre[0]
            ry = y - centre[1]
            s = 1
            if s <= 1.0:
                h = ((math.atan2(ry, rx) / math.pi) + 1.0) / 2.0
                h = h * sym  # symmetry
                rgb = colorsys.hsv_to_rgb(h, s, 1.0)
                pix[x, y] = tuple([int(round(c * 255.0)) for c in rgb])
    imnp = np.array(im)
    return imnp


def color_range(whl, p1, p2):
    x2 = round(whl.shape[0] / 2)
    y2 = round(whl.shape[0] / 2)
    x = np.arange(-x2, x2, 1)
    y = np.arange(-y2, y2, 1)
    xx, yy = np.meshgrid(x, y, sparse=True)
    z1 = xx ** 2 + yy ** 2 < p1 ** 2
    z2 = xx ** 2 + yy ** 2 > p2 ** 2
    z = z1 * z2
    whl[:, :, 0] = whl[:, :, 0] * z
    whl[:, :, 1] = whl[:, :, 1] * z
    whl[:, :, 2] = whl[:, :, 2] * z
    return whl


def create_sym(img_all, order):
    (nz, nx, ny) = img_all.shape
    print(nx, ny, nz)
    rgb = np.zeros((nz, nx, ny, 3))
    for n in range(nz):
        img = img_all[n, :, :]
        (nx, ny) = img.shape
        whl = build_color_wheel(ny, nx, order)
        # whl = colorrange(whl,180, 50)
        imnp = np.array(img)
        fimg = np.fft.fft2(imnp)
        whl = np.fft.fftshift(whl)
        proimg = np.zeros((nx, ny, 3))
        comb = np.zeros((nx, ny, 3), dtype=complex)
        magnitude = np.abs(fimg)
        phase = np.angle(fimg)
        for n in range(3):
            proimg[:, :, n] = whl[:, :, n] * magnitude
            comb[:, :, n] = np.multiply(proimg[:, :, n], np.exp(1j * phase))
            proimg[:, :, n] = np.real(np.fft.ifft2(comb[:, :, n]))
            proimg[:, :, n] = proimg[:, :, n] - np.min(proimg[:, :, n])
            proimg[:, :, n] = proimg[:, :, n] / np.max(proimg[:, :, n])
        iim = np.zeros((nx, ny, 3))
        iim[:, :, 0] = img
        iim[:, :, 1] = img
        iim[:, :, 2] = img
        rgb2 = iim * proimg / 255
        rgb[n, :, :, :] = rgb2
        print(rgb2.shape)
    return np.fft.fftshift(whl), rgb2


def fake_create_sym(img_all, order):
    # TODO: remove hard code path
    img = np.array(Image.open(Path(get_test_data_file("seo.tif"))))
    (nx, ny) = img.shape
    whl = build_color_wheel(ny, nx, order)
    # whl = colorrange(whl,180, 50)
    imnp = np.array(img)
    fimg = np.fft.fft2(imnp)
    whl = np.fft.fftshift(whl)
    proimg = np.zeros((nx, ny, 3))
    comb = np.zeros((nx, ny, 3), dtype=complex)
    magnitude = np.abs(fimg)
    phase = np.angle(fimg)
    for n in range(3):
        proimg[:, :, n] = whl[:, :, n] * magnitude
        comb[:, :, n] = np.multiply(proimg[:, :, n], np.exp(1j * phase))
        proimg[:, :, n] = np.real(np.fft.ifft2(comb[:, :, n]))
        proimg[:, :, n] = proimg[:, :, n] - np.min(proimg[:, :, n])
        proimg[:, :, n] = proimg[:, :, n] / np.max(proimg[:, :, n])
    iim = np.zeros((nx, ny, 3))
    iim[:, :, 0] = img
    iim[:, :, 1] = img
    iim[:, :, 2] = img
    rgb2 = iim * proimg / 255
    return np.fft.fftshift(whl), rgb2


""" im = Image.open('tau.png')
order = 2

whl, rgb2 = create_sym(im, order)
plt.imshow(whl)
plt.show()

plt.imshow(rgb2)
plt.show()

imageio.imwrite('pic2.jpg', rgb2) """
