from PIL import Image, ImageChops
import os # ファイルやフォルダ操作
import glob
import shutil
import datetime # 現在時刻を取得
import time

dir_name = "mikakou" # 画像が入っているフォルダ
new_dir_name = "new" # 画像を保存する先のフォルダ
used_dir_name ="used"

def crop_center(pil_img, crop_width, crop_height): # 画像の中心を切り出し
  img_width, img_height = pil_img.size
  return pil_img.crop(((img_width - crop_width) // 2,
                        (img_height - crop_height) // 2,
                        (img_width + crop_width) // 2,
                        (img_height + crop_height) // 2))

def func():
  # ディレクトリが存在しない場合は作成する
  if not os.path.exists(dir_name):
    os.mkdir(dir_name)

  # ディレクトリが存在しない場合は作成する
  if not os.path.exists(new_dir_name):
    os.mkdir(new_dir_name)

  # ディレクトリが存在しない場合は作成する
  if not os.path.exists(used_dir_name):
    os.mkdir(used_dir_name)

  def move_glob(dst_path, pathname, recursive=True): # glob.glob()で抽出された複数のファイルを一括で移動
    for p in glob.glob(pathname, recursive=recursive):
      shutil.move(p, dst_path)

  move_glob(dir_name, '*.png')
  move_glob(dir_name, '*.jpg')
  move_glob(dir_name, '*.jpeg')

  files = os.listdir(dir_name)

  i = 1

  for file in files: # ホーム画面用の処理
    im_original = Image.open(os.path.join(dir_name, file))
    name, ext = os.path.splitext(os.path.basename(file))
    width, height = im_original.size

    if height > width: # 縦長
      im = im_original
      im = crop_center(im, width, height - 208)
    else:
      im = im_original
      # im = crop_center(im, width - 50, height)

    # 背景色画像を生成
    im2 = im.convert("RGB")
    bg = Image.new("RGB", im2.size, im2.getpixel((0, 0)))

    # 背景色画像と元画像の差分画像を生成
    diff = ImageChops.difference(im2, bg)

    # 背景との境界を求めて画像を切り抜く
    croprange = diff.convert("RGB").getbbox()
    nim = im.crop(croprange)

    dt_now = datetime.datetime.now()
    # print(dt_now.strftime('%Y%m%d_%H%M%S'))
    name = str(dt_now.strftime('%Y%m%d_%H%M%S'))
    name += ".png"

    # 切り抜いた画像を保存
    nim.save(os.path.join(new_dir_name, name))

    print(str(i) + " done!")
    i += 1
    time.sleep(1)

  move_glob(used_dir_name, "./mikakou/*.PNG")
  move_glob(used_dir_name, "./mikakou/*.JPG")
  move_glob(used_dir_name, "./mikakou/*.JPEG")

  # 終了時に元の画像を削除
  # shutil.rmtree(dir_name)

  print("Exit a program")

if __name__ == "__main__":
  print("Execute a program")
  func()