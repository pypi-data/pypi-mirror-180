import cv2
import datetime
import ecdsa
import glob
import hashlib
import imutils
import numpy as np
import os
from os.path import exists
import pandas as pd
import random
import re
import skimage
import time
from ecdsa._compat import remove_whitespace
from ecdsa import ellipticcurve
from ecdsa.ecdsa import Public_key, Private_key
from random import randint, randrange
from skimage.feature import blob_log
import time

_p = int(remove_whitespace("""115792089210356248762697446949407573530086143415290314195533631308867097853951"""))
_r = int(remove_whitespace("""115792089210356248762697446949407573529996955224135760342422259061068512044369"""))
_b = int(remove_whitespace("""5AC635D8 AA3A93E7 B3EBBD55 769886BC 651D06B0 CC53B0F6 3BCE3C3E 27D2604B"""), 16)
_Gx = int(remove_whitespace("""6B17D1F2 E12C4247 F8BCE6E5 63A440F2 77037D81 2DEB33A0 F4A13945 D898C296"""), 16)
_Gy = int(remove_whitespace("""4FE342E2 FE1A7F9B 8EE7EB4A 7C0F9E16 2BCE3357 6B315ECE CBB64068 37BF51F5"""), 16)

curve_256 = ellipticcurve.CurveFp(_p, -3, _b, 1)
generator_256 = ellipticcurve.PointJacobi(curve_256, _Gx, _Gy, 1, _r, generator=True)

# generator
g = generator_256
n = g.order()

numbers = re.compile(r'(\d+)')


def short_names(images_path):
    list_images = sorted(glob.glob(images_path + '/*.jpg'), key=numerical_sort)
    short_names = []
    for img in list_images:
        short_names.append(img.replace(images_path + '/', '').replace('.jpg', ''))

    return short_names


def open_image(file_name):
    """
    :param file_name: path of the image
    :rtype: (image)
    """
    image = cv2.imread(file_name)
    return image


def numerical_sort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def mk_dir(folder_path):
    """
    :param folder_path: Folder path
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def string_blobs(omega: pd.DataFrame) -> str:
    """
    :param omega: dataframe
    :return: string
    """
    blobs_string = ''

    for row in omega.index:
        # if (omega.loc[row] != '0.0').all():
        bit_x0 = f"{int(omega['x'][row]):#0{6}x}"[2:]
        bit_y0 = f"{int(omega['y'][row]):#0{6}x}"[2:]
        blobs_string += (bit_x0 + bit_y0)

    return blobs_string


def head_txt_csr_file(file_name):
    with open(file_name, 'w') as f:
        f.write('csr' + '\t'
                + 'attempt' + '\t'
                + 'csr_name' + '\t'
                + 'image_length' + '\t'
                + 'detected_blobs' + '\t'
                + 'N' + '\t'
                + 'n' + '\t'
                + 'blobs_diameter' + '\t'
                + 'time_minutiae' + '\t'
                + 'time_grid'
                + '\n')


def resize_image(image_path: str, scale_percent: int = 80) -> np.array:
    """
    :param image_path: str
    :param scale_percent: int, value to be resized
    :rtype: (resized image)
    """
    image = open_image(image_path)
    height, width, _ = image.shape

    height_center, width_center = height // 2, width // 2
    center = min(height_center, width_center)

    h_0, h_1, w_0, w_1 = (height_center - center), (height_center + center), \
                         (width_center - center), (width_center + center)

    squared_image = image[h_0:h_1, w_0:w_1, :]
    image_size = int((center * 2 * scale_percent) / 100)
    dimension = (image_size, image_size)

    resized = cv2.resize(squared_image, dimension, interpolation=cv2.INTER_AREA)

    return resized


def image_generation(folder_path, image_path, std_start=0, std_stop=0.3, rot='OFF',
                     blur_in=1, blur_out=4, stage='Enrollment'):
    """
    :param folder_path:
    :param image_path:
    :param std_start:
    :param std_stop:
    :param rot:
    :param blur_in:
    :param blur_out:
    :param stage:
    :return:
    """
    n_attempts = 1 if 'Enrollment' in stage else 20
    str_position = [m.start() for m in re.finditer(r"/", image_path)][-1]

    resized_image = resize_image(image_path)
    h, w, d = resized_image.shape

    for i in range(1, n_attempts + 1):
        folder_name = folder_path + stage + '/' + image_path[str_position + 1:-4] + '/F_{0}'.format(i)

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        counter = 7

        if rot == 'OFF':
            rnd_vals = np.random.uniform(std_start, std_stop, 5)
            for val in rnd_vals:
                gauss_noise = np.random.normal(0, val, resized_image.size)
                gauss_noise = gauss_noise.reshape(h, w, d).astype('uint8')
                img_gauss = cv2.add(resized_image, gauss_noise)
                for blur in range(blur_in, blur_out):
                    counter -= 1
                    ksize = (blur, blur)
                    image_blurred = cv2.blur(img_gauss, ksize)
                    if counter < 0:
                        break
                    else:
                        cv2.imwrite(folder_name + '/'
                                    + image_path[str_position + 1:-4]
                                    + '_gauss_' + str(round(val, 4)).replace('.', '_')
                                    + '_blur_' + str(blur)
                                    + '.jpg', image_blurred)
        else:
            # Copy the reference image into each folder
            cv2.imwrite(folder_name + '/'
                        + image_path[str_position + 1:-4]
                        + '.jpg', resized_image)
            rot_start, rot_stop = 1, 6
            for angle in random.sample(range(rot_start, rot_stop), (rot_stop - rot_start)):
                val = random.uniform(std_start, std_stop)
                gauss_noise = np.random.normal(0, val, resized_image.size)
                gauss_noise = gauss_noise.reshape(h, w, d).astype('uint8')
                img_gauss = cv2.add(resized_image, gauss_noise)
                image_rotated = imutils.rotate(img_gauss, angle)
                for blur in range(blur_in, blur_out):
                    counter -= 1
                    ksize = (blur, blur)
                    image_blurred = cv2.blur(image_rotated, ksize)
                    resized = cv2.resize(image_blurred)
                    if counter < 0:
                        break
                    else:
                        cv2.imwrite(folder_name + '/'
                                    + image_path[str_position + 1:-4]
                                    + '_rot_' + str(angle)
                                    + '_gauss_' + str(round(val, 4)).replace('.', '_')
                                    + '_blur_' + str(blur)
                                    + '.jpg', resized)


def dataset_generation(reference_images_path, database_path):
    """
    :return: set of images
    """

    stages = ['Enrollment', 'Authentication']
    ref_images = sorted(glob.glob(reference_images_path + '*.jpg'), key=numerical_sort)
    for stage in stages[:]:
        for ref_image in ref_images[:]:
            image_generation(database_path, ref_image, stage=stage)


def find_centers(x_omega: int, y_omega: int, factor: int) -> np.array:
    """
    :param x_omega: x-position
    :param y_omega: y-position
    :param factor: K * a
    :return:  x- y-center
    """
    N = 6
    x_index_start, y_index_start = (x_omega // factor), (y_omega // factor)

    index = y_index_start * N + x_index_start
    center = np.array([int((x_index_start * factor) + factor // 2), int((y_index_start * factor) + factor // 2)])

    return index, center


def blob_movement(x_omega, y_omega, k, N, a=1):
    """
    :param x_omega: x_omega
    :param y_omega: y_omega
    :param k: average blob (grid) size
    :param N: number of grids on one dimension
    :param coin: 1 or 0
    :param a: secure factor
    :return: index, sketch
    """

    coin = random.randint(0, 1)
    factor = k * a
    k_center = factor // 2
    x_max: Union[int, Any] = N * factor

    if (x_omega % factor == 0) and (y_omega % factor == 0):
        x_new = ((x_omega + k_center) % x_max) if (coin == 1) else ((x_omega - k_center) % x_max)
        y_new = ((y_omega + k_center) % x_max) if (coin == 1) else ((y_omega - k_center) % x_max)
    elif (x_omega % factor == 0) and (y_omega % factor != 0):
        x_new, y_new = ((x_omega + k_center) % x_max) if (coin == 1) else (x_omega - k_center) % x_max, y_omega
    elif (x_omega % factor != 0) and (y_omega % factor == 0):
        x_new, y_new = x_omega, ((y_omega + k_center) % x_max) if (coin == 1) else ((y_omega - k_center) % x_max)
    else:
        x_new, y_new = x_omega, y_omega

    _, center = find_centers(x_new, y_new, factor)
    s = np.array([center[0] - x_omega, center[1] - y_omega])

    return s


def grid_positioning(image_height: int, blob_diameter: int, blobs_detected: pd.DataFrame, a=1):
    """
    :param image_height: in pixels
    :param blob_diameter: blob's average
    :param blobs_detected: dataframe [x,y] with the detected blobs
    :param a: security value
    :return: N, grid
    """
    factor = a * blob_diameter
    N = len(np.arange(0, image_height, factor))

    omega = pd.DataFrame(np.zeros((N ** 2, 2)).astype(str), columns=['x', 'y'])

    for i in blobs_detected.index:
        x, y = blobs_detected['x'][i], blobs_detected['y'][i]
        if x == image_height:
            index = ((y // factor) * N + (x // factor)) % (N * N) - N
        else:
            index = ((y // factor) * N + (x // factor)) % (N * N)

        omega.loc[index] = blobs_detected.loc[i]

    return N, omega


def feature_extraction(image_path: str, min_sigma: int, max_sigma: int, num_sigma: int):
    '''
    :param image_path: path of the image
    :param min_sigma: int
    :param max_sigma: int
    :param num_sigma: int
    :return:
    '''

    IMAGE_ = cv2.imread(image_path)

    image_height, _, _ = IMAGE_.shape
    gray_scale = cv2.cvtColor(IMAGE_, cv2.COLOR_BGR2GRAY)

    ts1 = time.time()
    # Blob's detection and extraction
    blobs_array = (blob_log(gray_scale,
                            min_sigma=min_sigma, max_sigma=max_sigma, num_sigma=num_sigma,
                            threshold=0.07, overlap=1, exclude_border=2)).astype(int)

    time_blobs_detection = f'{round(time.time() - ts1, 4)}'

    blobs_number, _ = blobs_array.shape
    # average blobs diameter
    blobs_diameter = int(blobs_array[:, 2].mean()) * 2
    blobs_detected = pd.DataFrame(blobs_array[:, :2], columns=["x", "y"]).sort_values(
        ["x", "y"], ascending=[True, True]).reset_index(drop=True)

    ts2 = time.time()
    N, omega = grid_positioning(image_height, blobs_diameter, blobs_detected)
    time_grid = f'{round(time.time() - ts2, 4)}'

    return image_height, blobs_number, blobs_diameter, N, omega, time_blobs_detection, time_grid


def blob_extraction(attempt: str, txt_file: str) -> (pd.DataFrame, int, int, int):
    """
    :param attempt: folder with the set of images
    :param txt_file:
    :return:
    """

    global image_height, blobs_diameter, N
    if 'Image_972' in attempt:
        min_sigma, max_sigma, num_sigma = 6, 12, 6
    elif 'Image_975' in attempt or 'Image_997' in attempt:
        min_sigma, max_sigma, num_sigma = 8, 18, 9
    # elif 'Image_997' in attempt:
    #     min_sigma, max_sigma, num_sigma = 10, 18, 10
    elif 'Image_1079' in attempt:
        min_sigma, max_sigma, num_sigma = 8, 20, 8
    elif 'Image_618' in attempt:
        min_sigma, max_sigma, num_sigma = 9, 14, 9
    elif 'Image_1104' in attempt or 'Image_2366' in attempt:
        min_sigma, max_sigma, num_sigma = 10, 16, 10
    elif 'Image_6' in attempt or 'Image_7' in attempt:
        min_sigma, max_sigma, num_sigma = 12, 16, 14
    elif 'tag9' in attempt or 'tag10' in attempt or 'tag11' in attempt or 'tag13' in attempt or 'tag14' in attempt \
            or 'tag15' in attempt or 'tag16' in attempt or 'tag17' in attempt:
        min_sigma, max_sigma, num_sigma = 4, 8, 6
    else:
        min_sigma, max_sigma, num_sigma = 6, 14, 12

    responses = sorted(glob.glob(attempt + '/*.jpg'), key=numerical_sort)
    omega_concat = []
    for response in responses:
        str0 = [m.start() for m in re.finditer(r"/", response)][-3]
        str1 = [m.start() for m in re.finditer(r"/", response)][-2]
        str2 = [m.start() for m in re.finditer(r"/", response)][-1]

        image_height, blobs_number, blobs_diameter, N, omega, time_blobs_detection, time_grid = \
            feature_extraction(response, min_sigma, max_sigma, num_sigma)

        omega_concat.append(omega)

        with open(txt_file, 'a') as file:
            file.write(response[str0 + 1:str1] + '\t'
                       + response[str1 + 1: str2] + '\t'
                       + response[str2 + 1:] + '\t'
                       + str(image_height) + '\t'
                       + str(blobs_number) + '\t'
                       + str(N) + '\t'
                       + str(N ** 2) + '\t'
                       + str(blobs_diameter) + '\t'
                       + time_blobs_detection + '\t'
                       + time_grid
                       + '\n')

    omega_concat = pd.concat(omega_concat, axis=1)

    return omega_concat, image_height, blobs_diameter, N


def robust_positions(omegas: pd.DataFrame, txt_file: str) -> pd.DataFrame:
    """
    :param omegas: dataframe with n number of images
    :param txt_file: str
    :return: dataframe with robust positions
    """
    # A dataframe is created with the same size as df, filled with string values.
    omega_robust = pd.DataFrame(np.zeros((len(omegas), 2)).astype(str), columns=['x', 'y'])

    # threshold: half of the images. Defined as the total number of columns divided by 2 (x,y).
    # Then, by 2 for obtaining half of the images.
    threshold = len(omegas.columns.values) // 2 // 2

    if 'case1' in txt_file:
        # Case 1: blob in all acquired images
        for i in range(len(omegas)):
            if (omegas.loc[i] != '0.0').all():
                x = np.round(np.mean(omegas.loc[i]["x"]))
                y = np.round(np.mean(omegas.loc[i]["y"]))
                omega_robust.loc[i] = x.astype(int), y.astype(int)
            else:
                continue
    else:
        # Case 2: blob in the majority of the images
        for i in range(len(omegas)):
            if ((omegas.loc[i] != '0.0').sum() // 2) > threshold:
                x = np.round(omegas.loc[i]['x'].replace('0.0', np.NaN).mean())
                y = np.round(omegas.loc[i]['y'].replace('0.0', np.NaN).mean())
                omega_robust.loc[i] = x.astype(int), y.astype(int)
            else:
                continue

    robust_blobs = omega_robust[omega_robust['x'].astype(str).str.isdigit()].reset_index(drop=True)

    return robust_blobs


def secure_sketch(omega: pd.DataFrame, k: int, N: int) -> pd.DataFrame:
    """
    :param omega: with positioned indices
    :param k: blob's diameter
    :param N: number of grids in 1D
    :param coin: random 1 or 0
    :return: dataframe sketch
    """
    sketch = pd.DataFrame(np.zeros((len(omega), 2)).astype(str), columns=['x', 'y'])

    for i in omega.index:
        # if (omega.loc[i] != '0.0').all():
        s = blob_movement(omega["x"][i], omega["y"][i], k, N)
        sketch.loc[i] = s

    return sketch


def robust_secure_sketch(omega: pd.DataFrame, sketch: pd.DataFrame) -> (str, str):
    """
    :param omega: dataframe
    :param sketch: dataframe
    :return: str, str
    """
    omega_str = string_blobs(omega).encode()
    sketch_str = string_blobs(sketch).encode()

    hash = "{0:d}".format(int(hashlib.sha256(omega_str + sketch_str).hexdigest(), 16))

    return hash, omega_str


def generation(omega: pd.DataFrame, sketch: pd.DataFrame) -> (list, str):
    """
    :param omega: robust omega
    :param sketch: sketch
    :return: P tuple, secret string
    """
    r = "{0:d}".format(random.randint(0, 2 ** 256)).encode()
    hash, omega_str = robust_secure_sketch(omega, sketch)
    P = (sketch, hash, r.decode())

    R = "{0:d}".format(int(hashlib.sha256(omega_str + r).hexdigest(), 16))

    return P, R


def reconstruction(omega_prime: pd.DataFrame, sketch: pd.DataFrame, k: int) -> pd.DataFrame:
    """
    :param omega_prime: robust omega prime
    :param sketch: sketch
    :param k: blob diameter
    :return: omega rec
    """
    v = pd.DataFrame(np.zeros((len(omega_prime), 2)).astype(int), columns=['x', 'y'])
    z = pd.DataFrame(np.zeros((len(omega_prime), 2)).astype(int), columns=['x', 'y'])
    factor = k * 1  # a = 1, a is a security parameter
    threshold = factor // 2

    for i in omega_prime.index:
        # if (omega_prime.loc[i] != '0.0').all():
        # Omega movement: v = omega_prime + s
        v.loc[i] = omega_prime.loc[i] + sketch.loc[i]
        # Find v's center
        _, center = find_centers(v.loc[i]['x'], v.loc[i]['y'], factor)
        # condition to reconstruct omega
        if ((center[0] - v.loc[i]['x']) < threshold) and ((center[1] - v.loc[i]['y']) < threshold):
            # Reconstruct omega: z = omega?
            z.loc[i] = center[0] - sketch.loc[i]['x'], center[1] - sketch.loc[i]['y']
        else:
            return '0'

    return z


def robust_reconstruction(omega_rec: pd.DataFrame, sketch: pd.DataFrame, h):
    """
    :param omega_rec:  robust omega prime
    :param sketch: sketch
    :param h: hash value
    :return:
    """
    # omega_rec = reconstruction(omega_prime, sketch, k)

    omega_rec_str = string_blobs(omega_rec).encode()
    sketch_str = string_blobs(sketch).encode()

    h_rec = "{0:d}".format(int(hashlib.sha256(omega_rec_str + sketch_str).hexdigest(), 16))

    if h == h_rec:
        # return omega_rec, omega_rec_str
        return omega_rec_str
    else:
        # return '0', '0'
        return '0'


def reproduction(omega_prime: pd.DataFrame, sketch: pd.DataFrame, h, r):
    """
    :param omega_prime:  robust omega prime
    :param sketch: sketch
    :param k: blobs diameter
    :param h: hash value
    :param r: 256-bits random number
    :return:
    """
    # omega_rec, omega_rec_str = robust_reconstruction(omega_prime, sketch, k, h)
    omega_rec_str = robust_reconstruction(omega_prime, sketch, h)

    if omega_rec_str != '0':
        R = "{0:d}".format(int(hashlib.sha256(omega_rec_str + r).hexdigest(), 16))
    else:
        R = "{0:d}".format(int(0.0))

    return R


def sign_key_gen(R):
    """
    :param R: secret value
    :return: pubkey, privkey
    """
    secret = int(R, 16)
    pubkey = Public_key(g, g * secret)
    privkey = Private_key(pubkey, secret)

    return pubkey, privkey


def digital_signature(privkey, nonces):
    """
    :param privkey: secret key
    :param nonces: 256-bits random number
    :return:
    """
    fresh = randrange(1, n)
    signature = privkey.sign(nonces, fresh)

    return signature


def verification(pubkey, signature, n_AS, n_AD):
    """
    :param pubkey: public key
    :param signature: digital signature
    :param n_AS: 256-bits random number
    :param n_AD: 256-bits random number
    :return:
    """
    return pubkey.verifies(int((n_AS + n_AD), 16), signature)
