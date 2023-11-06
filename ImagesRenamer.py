import os
import glob
from tkinter import filedialog

directory_path = filedialog.askdirectory()

image_files = glob.glob(os.path.join(directory_path, '*.jpg')) + glob.glob(os.path.join(directory_path, '*.jpeg')) + glob.glob(os.path.join(directory_path, '*.png')) + glob.glob(os.path.join(directory_path, '*.gif'))


for i, image_file in enumerate(image_files, start=1):

  base = os.path.basename(image_file)
  name, ext = os.path.splitext(base)

  new_image_file = os.path.join(directory_path, 'Screenshot ' + str(i) + ext)
  os.rename(image_file, new_image_file)
